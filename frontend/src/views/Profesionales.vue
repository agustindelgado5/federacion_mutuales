<template>
	<div id="profesionales" class="myTable">
		<vue-headful
			title="Profesionales - Federación Tucumana de Mutuales"
		></vue-headful>

		<h2>Listado de Profesionales</h2>
		<b-button @click="testFetch" class="mb-4" title="Recargar" variant="light">
			<v-icon dark style="color: black">mdi-cached</v-icon>
			Actualizar
		</b-button>

		<!-- ================ALTA PROFESIONAL======================== -->
		<b-button
			class="mb-4 ml-2"
			v-b-modal.modal-alta
			@click="altaProfesional()"
			title="Nuevo Profesional"
			style="color: white"
		>
			<v-icon dark> mdi-plus </v-icon>
			Nuevo Profesional
		</b-button>
		<b-modal id="modal-alta" hide-footer>
			<template #modal-title><h5 class="modal-title">Alta</h5></template>
			<profesionales-alta />
		</b-modal>

		<!-- ================ELIMINAR VARIOS PROFESIONALES======================== -->
		<b-button
			class="mb-4 ml-2"
			variant="danger"
			id="btn_del_full"
			title="Eliminar todos los registros"
			style="color: white"
			:disabled="btn_del_full"
			v-b-modal.modal-eliminarTodo
		>
			<v-icon class="mr-2" style="color: white"> mdi-delete </v-icon>
			Eliminar 
		</b-button>
    
    <div>
			<b-modal
				ref="my-modal"
				id="modal-eliminarTodo"
				hide-footer
				title="Eliminar"
				ok-only
			>
				<div class="d-block text-center" v-if="selected.length === rows">
					<h3>¿Esta seguro de eliminar todos los registros ?</h3>
				</div>
				<div class="d-block text-center" v-else>
					<h3>¿Esta seguro de eliminar {{ selected.length }} registros ?</h3>
				</div>

				<b-button class="mt-2" block @click="hideModal" title="Volver Atras">
					Volver Atras
				</b-button>

				<b-button
					class="mt-3"
					variant="danger"
					block
					title="Eliminar"
					@click="delete_all_Profesionales()"
				>
					Eliminar
				</b-button>
			</b-modal>
		</div>

		<!-- ======== Formulario de Busqueda ======== -->
		<b-form-group
			label-for="filter-input"
			label-align-sm="right"
			label-size="sm"
			class="mb-0"
			style="width: 100%; padding-bottom: 1em"
		>
			<b-input-group size="sm">
				<b-form-input
					id="filter-input"
					v-model="filter"
					type="search"
					placeholder="Buscar registros"
				></b-form-input>

				<b-input-group-append>
					<b-button :disabled="!filter" @click="filter = ''">Limpiar</b-button>
				</b-input-group-append>
			</b-input-group>
		</b-form-group>
		<!-- ======================================== -->

		<!-- ======================================== -->
		
		<div v-if="rows > 0">
			<div v-if="selected.length > 0">
				<pre>
					Cantidad de registros: {{ rows }} | Filas seleccionadas: {{selected.length}}
				</pre>
			</div>
			<div v-else>
				<pre>Cantidad de registros: {{ rows }}</pre>
			</div>
			<b-button
				class="mb-4 ml-2"
				size="sm"
				style="color: white"
				title="Seleccionar Todo"
				@click="seleccionar_todas"
				:disabled="btn_select"
			>
				Seleccionar Todo
			</b-button>
			<b-button
				class="mb-4 ml-2"
				size="sm"
				style="color: white"
				title="Limpiar Seleccion"
				@click="limpiar_seleccion"
				:disabled="btn_limpiar"
			>
				Limpiar Seleccion
			</b-button>
		</div>
		<div v-else>
			<pre>Cantidad de registros: {{ rows }}</pre>
		</div>


		<section class="container">
			<b-table
				:fields="fields"
				striped
				sortable
				responsive
				hover
				:items="tabla_profesionales"
				show-empty
				:per-page="perPage"
				:current-page="currentPage"
				:sticky-header="true"
				:no-border-collapse="false"
				ref="tablaregistros"
				id="tablaregistros"
				:filter="filter"
				@filtered="onFiltered"
				@row-selected="seleccionar_una"
				selectable
				select-mode="multi"
			>
				<template #empty="">
					<b>No hay registros para mostrar</b>
				</template>

				<template #cell(selected)="{ rowSelected }">
					<template v-if="rowSelected">
						<span aria-hidden="true">&check;</span>
						<span class="sr-only">Selected</span>
					</template>
					<template v-else>
						<span aria-hidden="true">&nbsp;</span>
						<span class="sr-only">Not selected</span>
					</template>
				</template>


				<template slot="cell(id_medico)" slot-scope="data">
					<b>{{ data.value }}</b>
				</template>

				<template slot="cell(apellido)" slot-scope="data">
					{{ data.value.toUpperCase() }}
				</template>

				<template slot="cell(nombre)" slot-scope="data">
					{{ data.value.toUpperCase() }}
				</template>

				<template slot="cell(action)" slot-scope="row">
					<div class="mt-3">
						<b-button-group>
							<b-button
								variant="info"
								id="button-1"
								title="Mostrar Info"
								@click="row.toggleDetails"
								:disabled="btn_mostrar"
							>
								{{ row.detailsShowing ? "Ocultar" : "Mostrar" }} detalles
							</b-button>

							<b-button
								variant="warning"
								id="button-2"
								title="Editar este registro"
								v-b-modal.modal-editar
								@click="editarProfesional(row.item, row.index)"
								:disabled="btn_editar"
							>
								<!-- :disabled="btn_editar" -->
								<v-icon class="mr-2"> mdi-pencil </v-icon>
								Editar
							</b-button>

							<b-button
								:to="{
									name: 'ordenesProf',
									params: { prof: row.item },
									query: { id: row.item.id_medico },
								}"
								variant="primary"
								id="button-3"
								title="Ver ordenes asociadas"
								:disabled="btn_ordenes"
							>
								<!-- @click="ordenesProfesional(row.item)" -->
								<v-icon dark style="color: black"
									>mdi-format-list-bulleted-square</v-icon
								>
								Ordenes
							</b-button>

							<b-button
								variant="danger"
								id="button-3"
								@click="showModalinfo(row.item, row.index)"
								title="Eliminar este registro"
								:disabled="btn_eliminar"
							>
								<v-icon class="mr-2"> mdi-delete </v-icon>
								Eliminar
							</b-button>
						</b-button-group>
					</div>
				</template>
				<template #row-details="row">
					<b-card title="Datos del Profesional: ">
						<div>
							<b-list-group horizontal>
								<b-list-group class="col-3">
									<b-list-group-item
										><b>Fecha de ingreso:</b>
										{{ row.item.fecha_ingreso }}</b-list-group-item
									>
									<b-list-group-item
										><b>Matricula:</b>
										{{ row.item.matricula }}</b-list-group-item
									>
									<b-list-group-item
										><b>CUIT:</b> {{ row.item.cuit }}</b-list-group-item
									>
								</b-list-group>
								&nbsp;
								<b-list-group class="col-5">
									<b-list-group-item
										><b>Provincia:</b>
										{{ row.item.provincia }}</b-list-group-item
									>
									<b-list-group-item
										><b>Localidad:</b>
										{{ row.item.localidad }}</b-list-group-item
									>
									<b-list-group-item
										><b>Correo:</b> {{ row.item.email }}
									</b-list-group-item>
								</b-list-group>
								&nbsp;
								<b-list-group class="col-4">
									<b-list-group-item
										><b>Telefono Fijo:</b>
										{{ row.item.tel_fijo }}</b-list-group-item
									>
									<b-list-group-item
										><b>Celular:</b>
										{{ row.item.tel_celular }}</b-list-group-item
									>
									<b-list-group-item
										><b>Calle:</b> {{ row.item.domicilio }}
									</b-list-group-item>
								</b-list-group>
							</b-list-group>
						</div>
					</b-card>
				</template>
			</b-table>

			<b-modal id="modal-editar" hide-footer>
				<template #modal-title>
					<h5 class="modal-title">Editar</h5>
				</template>
				<!-- {{ editar }} -->
				<profesionales-update :item_prof="editar" />
			</b-modal>

			<b-modal
				id="modal_eliminar"
				ref="my-modal"
				hide-footer
				title="Eliminar"
				ok-only
			>
				<div class="d-block text-center">
					<h3>
						¿Esta seguro de eliminar los datos de
						{{ infoEliminar.profesional.apellido }},
						{{ infoEliminar.profesional.nombre }} ?
					</h3>
				</div>
				<b-button class="mt-2" block @click="hideModal" title="Volver Atras"
					>Volver Atras</b-button
				>
				<b-button
					class="mt-3"
					variant="danger"
					block
					title="Eliminar"
					@click="deleteProfesional(infoEliminar.profesional.id_medico)"
					>Eliminar</b-button
				>
			</b-modal>

			<b-container fluid>
				<b-col class="my-1">
					<b-pagination
						v-model="currentPage"
						align="center"
						pills
						:total-rows="totalRows"
						:per-page="perPage"
						aria-controls="tabla_profesionales"
					>
					</b-pagination>
				</b-col>
			</b-container>
		</section>
		<aside>
			<div>
				<b-card-group deck>
					<b-card
						bg-variant="primary"
						text-variant="white"
						header="REGISTROS POR PAGINA"
						class="text-center"
					>
						<b-form-group label-for="per-page-select" class="mb-0">
							<b-form-select
								id="per-page-select"
								v-model="perPage"
								:options="pageOptions"
								size="sm"
							></b-form-select>
						</b-form-group>
					</b-card>
				</b-card-group>
			</div>

			<br />
			<div>
				<b-card-group deck>
					<b-card
						bg-variant="primary"
						text-variant="white"
						header="FILTRAR POR"
						class="text-center"
					>
						<div class="accordion" role="tablist">
							<b-card no-body>
								<b-card-header header-tag="header" class="p-1" role="tab">
									<b-button block v-b-toggle.accordion-1 variant="info">
										ESPECIALIDAD
									</b-button>
								</b-card-header>
								<b-collapse
									id="accordion-1"
									visible
									accordion="my-accordion"
									role="tabpanel"
								>
									<b-card-body>
										<b-form-group id="input-group-4">
											<b-form-select
												id="especialidad"
												v-model="filter"
												type="text"
												:options="options_especialidad"
											>
											</b-form-select>
										</b-form-group>
									</b-card-body>
								</b-collapse>
							</b-card>
						</div>
					</b-card>
				</b-card-group>
			</div>
		</aside>
	</div>
</template>

<script>
	let api = new URL("http://localhost");
	api.pathname = "profesionales";
	//api.port = 8000;
	api.port = 8081;

	import ProfesionalesAlta from "./ProfesionalesAlta.vue";
	import ProfesionalesUpdate from "./ProfesionalesUpdate.vue";
	import axios from "axios";

	export default {
		components: { ProfesionalesAlta, ProfesionalesUpdate },
		data() {
			return {
				tabla_profesionales: [],
				fields: [
					{ key: "selected", label: "Seleccionar", sortable: true },
					{
						key: "id_medico",
						label: "ID",
						sortable: true,
					},
					{
						key: "apellido",
						sortable: true,
					},
					{
						key: "nombre",
						sortable: true,
					},
					{
						key: "dni",
						label: "DNI",
						sortable: true,
					},
					{
						key: "especialidad",
						sortable: true,
					},
					{ key: "action", label: "Acciones", variant: "secondary" },
				],
				buscar: "",
				editar: {},
				filter: null,
				totalRows: 1, //Total de filas
				currentPage: 1, //Pagina actual
				perPage: 10, // Datos en la tabla por pagina
				pageOptions: [10, 20, 40, 100, { value: 10000, text: "Todos" }],
				selected: [],
				btn_down_pdf: true, //Desabilito los botones, hasta que muestre los datos
				btn_del_full: true,
				msj_tabla: " Presione 'Mostrar' para ver los regitros ",
				btn_mostrar: false,
				btn_editar: false,
				btn_ordenes: false,
				btn_eliminar: false,
				btn_select: false,
				btn_limpiar: true,
				infoEliminar: {
					id: "modal_eliminar",
					profesional: -1,
				},
				options_especialidad: [{ value: null, text: "Elija una especialidad" }],
			};
		},

		computed: {
			rows() {
				return (this.totalRows = this.tabla_profesionales.length);
			},
			id() {
				return this.tabla_profesionales.id_medico;
			},
			sortOptions() {
				// Create an options list from our fields
				return this.fields
					.filter((f) => f.sortable)
					.map((f) => {
						return { text: f.label, value: f.key };
					});
			},
		},

		methods: {
			async testFetch() {
				try {
					const res = await fetch(api);
					const data = await res.json();

					var lista_profesioales = data.results;

					console.log(lista_profesioales);

					this.tabla_profesionales = lista_profesioales;

					this.tabla_profesionales.forEach((element) => {
						let opcion = {};
						opcion.value = element.especialidad;
						opcion.text = element.especialidad;
						if (
							this.options_especialidad.find((x) => x.value == opcion.value)
						) {
							//this.options_especialidad.push(opcion);
							console.log(opcion, " ya se encuentra en el listado");
						} else {
							this.options_especialidad.push(opcion);
						}
					});
				} catch (error) {
					console.log(error);
				}
			},
			altaProfesional() {},
			//Funcion para mostrar el modal
			showModal() {
				this.$refs["my-modal"].show();
			},
			showModalinfo(item, index) {
				this.infoEliminar.profesional = item;
				this.showModal();
			},
			//Funcion para esconder el modal
			hideModal() {
				this.$refs["my-modal"].hide();
			},

			//Funcion para eliminar un profesional
			async deleteProfesional(id_medico) {
				axios
					.delete("http://localhost:8081/profesionales/" + id_medico + "/")
					.then((datos) => {
						swal("Operación Exitosa", " ", "success");
						console.log(datos);
					})
					.catch((error) => {
						swal("¡ERROR!", "Se ha detectado un problema ", "error");
						console.log(error);
					})
					.finally(() => this.testFetch());
			},

			//Funcion para eliminar todos los profesionales
			async delete_all_Profesionales() {
				var cantidad = this.selected.length;

				try {
					for (var i = 0; i < cantidad; i++) {
						axios.delete(
							"http://localhost:8081/profesionales/" +
								this.selected[i].id_medico +
								"/"
						);
						if (this.selected.length == 0) {
							console.log("Eliminacion Exitosa");
							break;
						}
					}
					this.hideModal();
					swal("Eliminacion Exitosa", " ", "success");
				} catch (error) {
					this.hideModal();
					swal("¡ERROR!", "Se ha detectado un problema ", "error");
					console.log(error);
				} finally {
					this.testFetch();
				}
			},

			editarProfesional(item, index) {
				this.editar = item;
			},
			ordenesProfesional(item) {
				this.editar = item;
			},

			//Selecciona una a una
			seleccionar_una(items) {
				this.selected = items;
				if (this.selected.length > 0) {
					this.btn_del_full = false;
					this.btn_limpiar = false;
					if (this.selected.length > 1) {
						this.btn_mostrar = true;
						this.btn_editar = true;
						this.btn_eliminar = true;
						this.btn_ordenes=true;
					}
					if (this.selected.length == this.rows) {
						this.btn_select = true;
					} else {
						this.btn_select = false;
					}
				} else {
					this.btn_del_full = true;
					this.btn_mostrar = false;
					this.btn_editar = false;
					this.btn_eliminar = false;
					this.btn_ordenes=false;
					this.btn_limpiar = true;
				}
			},
			//Selecciona todas
			seleccionar_todas() {
				this.$refs.tablaregistros.selectAllRows();
				this.btn_del_full = false;
				this.btn_mostrar = true;
				this.btn_editar = true;
				this.btn_ordenes=true;
				this.btn_eliminar = true;

				this.btn_select = true;
				this.btn_limpiar = false;
			},
			//Limpia todas las selecciones
			limpiar_seleccion() {
				this.$refs.tablaregistros.clearSelected();
				this.btn_del_full = true;
				this.btn_mostrar = false;
				this.btn_ordenes=false;
				this.btn_editar = false;
				this.btn_eliminar = false;

				this.btn_select = false;
				this.btn_limpiar = true;
			},


			//Funcion de busqueda
			onFiltered(filteredItems) {
				// Trigger pagination to update the number of buttons/pages due to filtering
				this.totalRows = filteredItems.length;
				this.currentPage = 1;
			},
		},
		beforeMount() {
			this.testFetch();
		},
	};
</script>

<style scoped>
	.myTable {
		position: absolute;
		left: 0;
		padding: 1.5em;
		margin-top: 4rem;
		overflow: auto;
		transition: 0.5s;
		width: 100%;
	}

	.container {
		float: left;
		width: 80%;
	}
	aside {
		float: right;
		width: 20%;
	}
</style>
