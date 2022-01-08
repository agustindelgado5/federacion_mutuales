<template>
	<div id="recetas" class="myTable">
		<!--HEAD DE LA PAGINA -->
		<vue-headful
			title="Recetas - Federación Tucumana de Mutuales"
		></vue-headful>

		<h2>Listado de Recetas</h2>
		<b-button @click="testFetch" class="mb-4" title="Recargar" variant="light">
			<v-icon dark style="color: black">mdi-cached</v-icon>
			Actualizar
		</b-button>

		<!-- ================ALTA RECETAS======================== -->
		<b-button
			class="mb-4 ml-2"
			v-b-modal.modal-alta
			@click="altaReceta()"
			title="Nueva Receta"
			style="color: white"
		>
			<v-icon dark> mdi-plus </v-icon>
			Nueva Receta
		</b-button>
		<b-modal id="modal-alta" hide-footer>
			<template #modal-title><h5 class="modal-title">Alta</h5></template>
			<recetas-alta />
		</b-modal>

		<!-- ================ELIMINAR VARIAS ORDENES======================== -->
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
					@click="delete_all_Recetas()"
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
			v-show="rows > 0"
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
					Cantidad de registros: {{ rows }} | Filas seleccionadas: {{ selected.length }}
				</pre
				>
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
		<!-- ======== Tabla con los registros ======= -->
		<section id="container">
			<b-table
				:fields="fields"
				striped
				sortable
				responsive
				hover
				:items="tabla_recetas"
				show-empty
				:per-page="perPage"
				:current-page="currentPage"
				:no-border-collapse="true"
				:sticky-header="true"
				ref="tablaregistros"
				id="tablaregistros"
				:filter="filter"
				@filtered="onFiltered"
				@row-selected="seleccionar_una"
				selectable
				select-mode="multi"
			>
				<!-- :sticky-header="true" -->
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
				<template slot="cell(numero_socio)" slot-scope="data">
					{{ data.value.split("/")[4] }}
				</template>
				<template slot="cell(paciente)" slot-scope="data">
					{{ data.value.split("/")[4] }}
				</template>
				<template slot="cell(id_medicamento)" slot-scope="data">
					{{ data.value.split("/")[4] }}
				</template>
				<template slot="cell(cod_farmacia)" slot-scope="data">
					{{ data.value.split("/")[4] }}
				</template>
				<template slot="cell(fecha)" slot-scope="data">
					{{ data.value.split("-")[2] }}/{{ data.value.split("-")[1] }}/{{
						data.value.split("-")[0]
					}}
				</template>
				<template slot="cell(carencia)" slot-scope="data">
					{{ data.value.split("-")[2] }}/{{ data.value.split("-")[1] }}/{{
						data.value.split("-")[0]
					}}
				</template>

				<template slot="cell(action)" slot-scope="row">
					<div class="mt-3">
						<b-button-group>
							<b-button
								variant="warning"
								id="button-2"
								title="Editar este registro"
								v-b-modal.modal-editar
								:disabled="btn_editar"
								@click="editarReceta(row.item, row.index)"
							>
								<v-icon class="mr-2"> mdi-pencil </v-icon>
								Editar
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
			</b-table>
			<b-container fluid>
				<b-col class="my-1">
					<b-pagination
						v-model="currentPage"
						align="center"
						pills
						:total-rows="totalRows"
						:per-page="perPage"
						aria-controls="table_receta"
					>
					</b-pagination>
				</b-col>
			</b-container>
      <!-- ================ELIMINAR RECETA======================== -->

		<b-modal
			id="modal_eliminar"
			ref="my-modal"
			hide-footer
			title="Eliminar"
			ok-only
		>
			<div class="d-block text-center">
				<h3>
					¿Esta seguro de eliminar los datos de la receta
					{{ infoEliminar.receta.id_receta }}?
				</h3>
			</div>
			<b-button class="mt-2" block @click="hideModal" title="Volver Atras"
				>Volver Atras</b-button
			>
			<b-button
				class="mt-3"
				variant="danger"
				block
				@click="deleteReceta(infoEliminar.receta.id_receta)"
				title="Eliminar"
			>
				Eliminar
			</b-button>
		</b-modal>
		<!-- ================EDITAR RECETA======================== -->
		<b-modal id="modal-editar" hide-footer>
			<template #modal-title><h5 class="modal-title">Editar</h5></template>
			<recetas-update :receta="editar" />
		</b-modal>
		</section>
		<aside v-show="rows > 0">
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
		</aside>

		
	</div>
</template>

<script>
	let api = new URL("http://localhost");
	api.pathname = "recetas";
	//api.port = 8000;
	api.port = 8081;

	import RecetasAlta from "./RecetasAlta.vue";
	import RecetasUpdate from "./RecetasUpdate.vue";
	import axios from "axios";

	export default {
		components: { RecetasAlta, RecetasUpdate },
		data() {
			return {
				tabla_recetas: [],
				fields: [
					{ key: "selected", label: "Seleccionar", sortable: true },
					{ key: "id_receta", label: "N° Receta", sortable: true },
					{ key: "numero_socio", label: "N° Socio", sortable: true },
					{ key: "paciente", label: "Paciente", sortable: true },
					{ key: "diagnostico", label: "Diagnostico", sortable: true },
					{ key: "id_medicamento", label: "Id Medicamento", sortable: true },
					{ key: "cod_farmacia", label: "Id Farmacia", sortable: true },
					{ key: "fecha", label: "Fecha", sortable: true },
					{ key: "carencia", label: "Carencia", sortable: true },
					{ key: "action", label: "Acciones", variant: "secondary" },
				],
				filter: null,
				pageOptions: [10, 20, 40, 100, { value: 10000, text: "Todos" }],
				totalRows: 1, //Total de filas
				currentPage: 1, //Pagina actual
				perPage: 10, // Datos en la tabla por pagina
				buscar: "",
				editar: {},
				infoEliminar: {
					receta: -1,
				},
				selected: [],

				//Botones
				btn_down_pdf: true, //Desabilito los botones, hasta que muestre los datos
				btn_del_full: true,
        		btn_limpiar:true,
				msj_tabla: " Presione 'Mostrar' para ver los regitros ",
				btn_mostrar: false,
				btn_editar: false,
				btn_ordenes: false,
				btn_eliminar: false,
				btn_select: false,
			};
		},
		computed: {
			rows() {
				return (this.totalRows = this.tabla_recetas.length);
			},
			id() {
				return this.tabla_recetas.id_receta;
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

					var lista_recetas = data.results;

					console.log(lista_recetas);

					this.tabla_recetas = lista_recetas;
				} catch (error) {
					console.log(error);
				}
			},
			editarReceta(item, index) {
				this.editar = item;
			},
			//Muestra el modal de eliminar
			showModalinfo(item, index) {
				this.infoEliminar.receta = item;
				this.showModal();
			},
			//Funcion para mostrar el modal
			showModal() {
				this.$refs["my-modal"].show();
			},
			//Funcion para esconder el modal
			hideModal() {
				this.$refs["my-modal"].hide();
			},
			altaReceta() {},

			//Funcion para eliminar una receta
			async deleteReceta(nro_receta) {
				axios
					.delete("http://localhost:8081/recetas/" + nro_receta + "/")
					.then((datos) => {
						swal("Operación Exitosa", " ", "success");
						console.log(datos);
						this.hideModal();
					})
					.catch((error) => {
						swal("¡ERROR!", "Se ha detectado un problema ", "error");
						console.log(error);
						this.hideModal();
					})
					.finally(() => this.testFetch());
			},

			//Funcion para eliminar todos las recetas
			async delete_all_Recetas() {
				var cantidad = this.selected.length;

				try {
					for (var i = 0; i < cantidad; i++) {
						axios.delete(
							"http://localhost:8081/recetas/" +
								this.selected[i].id_receta +
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
					this.btn_limpiar = true;
				}
			},
			//Selecciona todas
			seleccionar_todas() {
				this.$refs.tablaregistros.selectAllRows();
				this.btn_del_full = false;
				this.btn_mostrar = true;
				this.btn_editar = true;
				this.btn_eliminar = true;

				this.btn_select = true;
				this.btn_limpiar = false;
			},
			//Limpia todas las selecciones
			limpiar_seleccion() {
				this.$refs.tablaregistros.clearSelected();
				this.btn_del_full = true;
				this.btn_mostrar = false;
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
