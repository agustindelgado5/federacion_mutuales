<template>
	<v-app id="app">
		<div id="farmacias" class="myTable">
			<!--HEAD DE LA PAGINA -->
			<vue-headful
				title="Farmacias - Federación Tucumana de Mutuales"
			></vue-headful>

			<h2>Listado de Farmacias</h2>
			<b-button
				@click="testFetch"
				class="mb-4"
				title="Recargar"
				variant="light"
			>
				<v-icon dark style="color: black">mdi-cached</v-icon>
				Actualizar
			</b-button>

			<!-- ================ALTA FARMACIA======================== -->
			<b-button
				class="mb-4 ml-2"
				v-b-modal.modal-alta
				@click="altaFarmacia()"
				title="Nueva Farmacia"
				style="color: white"
			>
				<v-icon dark> mdi-plus </v-icon>
				Nueva Farmacia
			</b-button>
			<b-modal id="modal-alta" hide-footer>
				<template #modal-title><h5 class="modal-title">Alta</h5></template>
				<farmacias-alta :updateTable="testFetch" />
			</b-modal>

			<!-- ==================================CREAR PDF================================== -->
			<b-button
				@click="generarPDF()"
				id="btn_down_pdf"
				class="mb-4 ml-2"
				title="Generar PDF"
				variant="danger"
				style="color: white"
				
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					width="16"
					height="16"
					fill="currentColor"
					class="bi bi-file-pdf-fill"
					viewBox="0 0 16 16"
				>
					<path
						d="M5.523 10.424c.14-.082.293-.162.459-.238a7.878 7.878 0 0 1-.45.606c-.28.337-.498.516-.635.572a.266.266 0 0 1-.035.012.282.282 0 0 1-.026-.044c-.056-.11-.054-.216.04-.36.106-.165.319-.354.647-.548zm2.455-1.647c-.119.025-.237.05-.356.078a21.035 21.035 0 0 0 .5-1.05 11.96 11.96 0 0 0 .51.858c-.217.032-.436.07-.654.114zm2.525.939a3.888 3.888 0 0 1-.435-.41c.228.005.434.022.612.054.317.057.466.147.518.209a.095.095 0 0 1 .026.064.436.436 0 0 1-.06.2.307.307 0 0 1-.094.124.107.107 0 0 1-.069.015c-.09-.003-.258-.066-.498-.256zM8.278 4.97c-.04.244-.108.524-.2.829a4.86 4.86 0 0 1-.089-.346c-.076-.353-.087-.63-.046-.822.038-.177.11-.248.196-.283a.517.517 0 0 1 .145-.04c.013.03.028.092.032.198.005.122-.007.277-.038.465z"
					/>
					<path
						fill-rule="evenodd"
						d="M4 0h8a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2zm.165 11.668c.09.18.23.343.438.419.207.075.412.04.58-.03.318-.13.635-.436.926-.786.333-.401.683-.927 1.021-1.51a11.64 11.64 0 0 1 1.997-.406c.3.383.61.713.91.95.28.22.603.403.934.417a.856.856 0 0 0 .51-.138c.155-.101.27-.247.354-.416.09-.181.145-.37.138-.563a.844.844 0 0 0-.2-.518c-.226-.27-.596-.4-.96-.465a5.76 5.76 0 0 0-1.335-.05 10.954 10.954 0 0 1-.98-1.686c.25-.66.437-1.284.52-1.794.036-.218.055-.426.048-.614a1.238 1.238 0 0 0-.127-.538.7.7 0 0 0-.477-.365c-.202-.043-.41 0-.601.077-.377.15-.576.47-.651.823-.073.34-.04.736.046 1.136.088.406.238.848.43 1.295a19.707 19.707 0 0 1-1.062 2.227 7.662 7.662 0 0 0-1.482.645c-.37.22-.699.48-.897.787-.21.326-.275.714-.08 1.103z"
					/>
				</svg>
				Generar PDF
			</b-button>
			<!-- ============================================================================== -->

			<!-- ================ELIMINAR VARIAS FARMACIAS======================== -->
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
						@click="delete_all_Farmacias()"
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
						<b-button :disabled="!filter" @click="filter = ''"
							>Limpiar</b-button
						>
					</b-input-group-append>
				</b-input-group>
			</b-form-group>

			<!-- ======================================== -->

			<div v-if="rows > 0">
				<div v-if="selected.length > 0">
					<div v-if="rows != rowsFilter">
						<pre>
Registros Fitrados: {{ rowsFilter }} | Filas seleccionadas: {{
								selected.length
							}}</pre
						>
					</div>
					<div v-else>
						<pre>
Cantidad de registros: {{ rows }} | Filas seleccionadas: {{
								selected.length
							}}</pre
						>
					</div>
				</div>
				<div v-else>
					<div v-if="rows != rowsFilter">
						<pre>Registros Fitrados: {{ rowsFilter }} </pre>
					</div>
					<div v-else>
						<pre>Cantidad de registros: {{ rows }}</pre>
					</div>
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
				<!-- ======== Tabla con los registros ======= -->
				<b-table
					:fields="fields"
					striped
					sortable
					responsive
					:sticky-header="true"
					:no-border-collapse="false"
					hover
					:items="
						tabla_farmacias
							| Representante(filter_representante)
							| Correo(filter_correo)
					"
					show-empty
					:per-page="perPage"
					:current-page="currentPage"
					:filter="filter"
					@filtered="onFiltered"
					ref="tablaregistros"
					id="tablaregistros"
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
									@click="editarFarmacia(row.item, row.index)"
									:disabled="btn_editar"
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

					<template #row-details="row">
						<b-card title="Datos de la farmacia: ">
							<div>
								<b-list-group horizontal>
									<b-list-group class="col-3">
										<b-list-group-item
											><b>Codigo:</b>
											{{ row.item.cod_farmacia }}</b-list-group-item
										>
										<b-list-group-item
											><b>Matricula:</b>
											{{ row.item.matricula_farm }}</b-list-group-item
										>
										<b-list-group-item
											><b>CUIT:</b> {{ row.item.cuit }}</b-list-group-item
										>
									</b-list-group>
									&nbsp;
									<b-list-group class="col-5">
										<b-list-group-item
											><b>Farmacia:</b>
											{{ row.item.farmacia }}</b-list-group-item
										>
										<b-list-group-item
											><b>Sucursal:</b>
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
											><b>Representante:</b> {{ row.item.representante }}
										</b-list-group-item>
									</b-list-group>
								</b-list-group>
							</div>
						</b-card>
					</template>
				</b-table>
				<!-- ================ELIMINAR FARMACIA======================== -->

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
							{{ infoEliminar.farmacia.farmacia }}?
						</h3>
					</div>
					<b-button class="mt-2" block @click="hideModal" title="Volver Atras"
						>Volver Atras</b-button
					>
					<b-button
						class="mt-3"
						variant="danger"
						block
						@click="deleteFarmacia(infoEliminar.farmacia.cod_farmacia)"
						title="Eliminar"
					>
						Eliminar
					</b-button>
				</b-modal>
				<b-container fluid>
					<b-col class="my-1">
						<b-pagination
							v-model="currentPage"
							align="center"
							pills
							:total-rows="totalRows"
							:per-page="perPage"
							aria-controls="tabla_farmacias"
						>
						</b-pagination>
					</b-col>
				</b-container>
			</section>
			<aside v-show="rows > 0">
				<!--
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
      -->
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
										<b-button
											block
											v-b-toggle.accordion-1
											variant="info"
											style="font-size: 0.82em"
										>
											CORREO
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
												<v-autocomplete
													id="correo"
													v-model="filter_correo"
													:items="options_correo"
													type="text"
													solo
													filled
												></v-autocomplete>
												<div v-show="filter_correo != null">
													<b-button
														@click="filter_correo = null"
														title="Limpiar"
													>
														Limpiar
													</b-button>
												</div>
											</b-form-group>
										</b-card-body>
									</b-collapse>
									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button
											block
											v-b-toggle.accordion-2
											variant="info"
											style="font-size: 0.82em"
										>
											REPRESENTANTE
										</b-button>
									</b-card-header>
									<b-collapse
										id="accordion-2"
										visible
										accordion="my-accordion"
										role="tabpanel"
									>
										<b-card-body>
											<b-form-group id="input-group-4">
												<v-autocomplete
													id="representante"
													v-model="filter_representante"
													:items="options_representante"
													type="text"
													solo
													filled
												></v-autocomplete>
												<div v-show="filter_representante != null">
													<b-button
														@click="filter_representante = null"
														title="Limpiar"
													>
														Limpiar
													</b-button>
												</div>
											</b-form-group>
										</b-card-body>
									</b-collapse>
								</b-card>
							</div>
						</b-card>
					</b-card-group>
				</div>
			</aside>
			<b-modal id="modal-editar" hide-footer>
				<template #modal-title><h5 class="modal-title">Editar</h5></template>
				<farmacias-update :farmacia="editar" :updateTable="testFetch"/>
			</b-modal>

			<!-- ==================================CREAR PDF================================== -->
			<b-modal
				size="xl"
				ref="modal-pdfFarmacia"
				id="modal-pdfFarmacia"
				hide-footer
			>
				<template #modal-title
					><h5 class="modal-title">Vista Previa</h5></template
				>
				<farmacias-listadopdf :PDFfarmacia=farmaciasAPdf></farmacias-listadopdf>
			</b-modal>
			<!-- ==============================================================================-->
		</div>
	</v-app>
</template>

<script>
	let api = new URL("http://localhost");
	api.pathname = "farmacias/";
	//api.port = 8000;
	api.port = 8081;
	import FarmaciasAlta from "./FarmaciasAlta.vue";
	import FarmaciasUpdate from "./FarmaciasUpdate.vue";
	import FarmaciasListadopdf from "./FarmaciasListadopdf.vue"

	import axios from "axios";

	export default {
		components: { FarmaciasAlta, FarmaciasUpdate, FarmaciasListadopdf  },
		data() {
			return {
				tabla_farmacias: [],
				fields: [
					{ key: "selected", label: "Seleccionar", sortable: true },
					{ key: "cod_farmacia", label: "Codigo", sortable: true },
					{ key: "matricula_farm", label: "Matricula", sortable: true },
					{ key: "cuit", label: "CUIT", sortable: true },
					{ key: "farmacia", label: "Farmacia", sortable: true },
					{ key: "localidad", label: "Sucursal", sortable: true },
					{ key: "email", label: "Correo", sortable: true },
					{ key: "tel_fijo", label: "Telefono Fijo", sortable: true },
					{ key: "tel_celular", label: "Celular", sortable: true },
					{ key: "representante", label: "Representante", sortable: true },
					{ key: "action", label: "Acciones", variant: "secondary" },
				],
				totalRows: 1, //Total de filas
				currentPage: 1, //Pagina actual
				perPage: 10, // Datos en la tabla por pagina
				//buscar: '',
				filter: null,
				editar: {},
				infoEliminar: {
					id: "modal_eliminar",
					farmacia: -1,
				},

				farmaciasAPdf :{},

				//Opciones de filtro
				options_correo: [
					{ value: null, text: "Elija un correo", selected: true },
				],
				options_representante: [
					{ value: null, text: "Elija un representante", selected: true },
				],
				selected: [],

				//Botones
				btn_down_pdf: true, //Desabilito los botones, hasta que muestre los datos
				btn_del_full: true,
				btn_limpiar: true,
				msj_tabla: " Presione 'Mostrar' para ver los regitros ",
				btn_mostrar: false,
				btn_editar: false,
				btn_ordenes: false,
				btn_eliminar: false,
				btn_select: false,

				//Campos a filtrar
				filter_correo : null,
				filter_representante: null,
			};
		},
		computed: {
			rows() {
				return (this.totalRows = this.tabla_farmacias.length);
			},
			id() {
				return this.tabla_farmacias.cod_farmacia;
			},
			rowsFilter() {
				return this.totalRows;
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

					var lista_farmacias = data.results;

					console.log(lista_farmacias);

					this.tabla_farmacias = lista_farmacias;

					this.tabla_farmacias.forEach((element) => {
						let opcionCorreo = {};
						let opcionRepre = {};
						opcionCorreo.value = element.email;
						opcionCorreo.text = element.email;
						opcionRepre.value = element.representante;
						opcionRepre.text = element.representante;
						if (
							this.options_correo.find((x) => x.value == opcionCorreo.value)
						) {
							console.log(opcionCorreo, " ya se encuentra en el listado");
						} else {
							this.options_correo.push(opcionCorreo);
						}

						if (
							this.options_representante.find(
								(x) => x.value == opcionRepre.value
							)
						) {
							console.log(opcionRepre, " ya se encuentra en el listado");
						} else {
							this.options_representante.push(opcionRepre);
						}
					});
				} catch (error) {
					console.log(error);
				}
			},
			editarFarmacia(item, index) {
				this.editar = item;
			},
			//Funcion para mostrar el modal
			showModal() {
				this.$refs["my-modal"].show();
			},
			showModalinfo(item, index) {
				this.infoEliminar.farmacia = item;
				this.showModal();
			},
			//Funcion para esconder el modal
			hideModal() {
				this.$refs["my-modal"].hide();
			},
			altaFarmacia() {},
			//Elimina una farmacia
			async deleteFarmacia(cod_Farmacia) {
				axios
					.delete("http://localhost:8081/farmacias/" + cod_Farmacia + "/")
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

			//Elimino todas las farmacias
			//Funcion para eliminar todos los profesionales
			async delete_all_Farmacias() {
				var cantidad = this.selected.length;

				try {
					for (var i = 0; i < cantidad; i++) {
						axios.delete(
							"http://localhost:8081/farmacias/" +
								this.selected[i].cod_farmacia +
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

			onFiltered(filteredItems) {
				// Trigger pagination to update the number of buttons/pages due to filtering
				this.totalRows = filteredItems.length;
				this.currentPage = 1;
			},

			//Funcion para crear el PDF
			async generarPDF(){
				if (this.tabla_farmacias.length != 0) {
					//this.btn_down_pdf=false;
					this.farmaciasAPdf = this.tabla_farmacias;
					this.$refs["modal-pdfFarmacia"].show();
				} else {
					//this.btn_down_pdf=true;
					swal("Debe tener al menos 1 registro");
				}
				
				//console.log("Profesional: ", this.profesionalAPdf);
				//this.$refs["modal-pdfFarmacia"].show();
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
