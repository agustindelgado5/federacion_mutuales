<template>
	<v-app id="app">
		<div id="estudios" class="myTable">
			<!--HEAD DE LA PAGINA -->
			<vue-headful
				title="Estudios - Federación Tucumana de Mutuales"
			></vue-headful>

			<h2>Listado de Estudios</h2>
			<b-button
				@click="testFetch"
				class="mb-4"
				title="Recargar"
				variant="light"
			>
				<v-icon dark style="color: black">mdi-cached</v-icon>
				Actualizar
			</b-button>

			<!-- ================ALTA ESTUDIOS======================== -->
			<b-button
				class="mb-4 ml-2"
				v-b-modal.modal-alta
				@click="altaEstudio()"
				title="Nuevo Estudio"
				style="color: white"
			>
				<v-icon dark> mdi-plus </v-icon>
				Nuevo Estudio
			</b-button>
			<b-modal id="modal-alta" hide-footer>
				<template #modal-title><h5 class="modal-title">Alta</h5></template>
				<estudios-alta :updateTable="testFetch" />
			</b-modal>

			<!-- ================================================================ -->
			<b-button
				class="mb-4 ml-2"
				variant="info"
				id="btn_del_prov"
				@click="VerProveedores()"
				title="Ver Proveedores"
				style="color: white"
			>
				<v-icon dark>mdi-format-list-bulleted-square</v-icon>
				Proveedores
			</b-button>
			<!-- ================================================================ -->

			<!-- ================ELIMINAR VARIOS ESTUDIOS======================== -->
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
						@click="delete_all_Estudios()"
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
					hover
					:items="
						tabla_estudios | Tipo(filter_tipo) | Proveedor(filter_proveedor)
					"
					show-empty
					:per-page="perPage"
					:current-page="currentPage"
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

					<template slot="cell(id_estudio)" slot-scope="data">
						<b>{{ data.value }}</b>
					</template>

					<template slot="cell(id_proveedor)" slot-scope="data">
						{{ data.value.split("/")[4] }}
					</template>

					<template slot="cell(precio_socio)" slot-scope="data">
						${{ data.value }}
					</template>

					<template slot="cell(precio_federacion)" slot-scope="data">
						${{ data.value }}
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
								<!-- ==================================CREAR PDF================================== -->
								<!-- Generar PDF -->
								<b-button
									@click="generarPDF(row.item)"
									id="btn_down_pdf"
									class="mb-0 ml-2"
									title="Generar PDF"
									variant="info"
									style="color: white"
									:disabled="btn_down_pdf"
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
									Generar
									<!-- ============================================================================== -->
								</b-button>
								<b-button
									variant="warning"
									id="button-2"
									title="Editar este registro"
									v-b-modal.modal-editar
									@click="editarEstudio(row.item, row.index)"
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
				</b-table>
				<b-container fluid>
					<b-col class="my-1">
						<b-pagination
							v-model="currentPage"
							align="center"
							pills
							:total-rows="totalRows"
							:per-page="perPage"
							aria-controls="table_estudios"
						>
						</b-pagination>
					</b-col>
				</b-container>
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
											v-b-toggle.accordion-filter-1
											variant="info"
											style="font-size: 0.82em"
										>
											TIPO
										</b-button>
									</b-card-header>
									<b-collapse
										id="accordion-filter-1"
										visible
										accordion="my-accordion"
										role="tabpanel"
									>
										<b-card-body>
											<b-form-group id="input-group-4">
												<v-autocomplete
													id="tipo"
													v-model="filter_tipo"
													:items="options_tipo"
													type="text"
													solo
													filled
												></v-autocomplete>
												<div v-show="filter_tipo != null">
													<b-button @click="filter_tipo = null" title="Limpiar">
														Limpiar
													</b-button>
												</div>
											</b-form-group>
										</b-card-body>
									</b-collapse>

									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button
											block
											v-b-toggle.accordion-filter-2
											variant="info"
											style="font-size: 0.82em"
										>
											PROVEEDOR
										</b-button>
									</b-card-header>
									<b-collapse
										id="accordion-filter-2"
										visible
										accordion="my-accordion"
										role="tabpanel"
									>
										<b-card-body>
											<b-form-group id="input-group-4">
												<v-autocomplete
													id="proveedor"
													v-model="filter_proveedor"
													:items="options_proveedor"
													type="text"
													solo
													filled
												></v-autocomplete>
												<div v-show="filter_proveedor != null">
													<b-button
														@click="filter_proveedor = null"
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
			<!-- ================ELIMINAR ESTUDIO======================== -->

			<b-modal
				id="modal_eliminar"
				ref="my-modal"
				hide-footer
				title="Eliminar"
				ok-only
			>
				<div class="d-block text-center">
					<h3>
						¿Esta seguro de eliminar los datos del estudio
						{{ infoEliminar.estudio.cod_estudio }}?
					</h3>
				</div>
				<b-button class="mt-2" block @click="hideModal" title="Volver Atras"
					>Volver Atras</b-button
				>
				<b-button
					class="mt-3"
					variant="danger"
					block
					@click="deleteEstudio(infoEliminar.estudio.id_estudio)"
					title="Eliminar"
				>
					Eliminar
				</b-button>
			</b-modal>

			<b-modal id="modal-editar" hide-footer>
				<template #modal-title><h5 class="modal-title">Editar</h5></template>
				<estudios-update :estudio="editar" :updateTable="testFetch" />
			</b-modal>

			<!-- ==================================CREAR PDF================================== -->
			<vue-html2pdf
				:show-layout="false"
				:float-layout="true"
				:enable-download="false"
				:preview-modal="true"
				:paginate-elements-by-height="1400"
				filename="DetalleEstudio"
				:pdf-quality="2"
				:manual-pagination="false"
				pdf-format="a4"
				pdf-orientation="portrait"
				pdf-content-width="80%"
				@progress="onProgress($event)"
				@startPagination="startPagination()"
				@hasPaginated="hasPaginated()"
				@beforeDownload="beforeDownload($event)"
				@hasDownloaded="hasDownloaded($event)"
				ref="html2Pdf"
			>
				<section slot="pdf-content">
					<!-- PDF Content Here -->
					<section class="pdf-item">
						<h3>Federación Tucumana de Mutuales</h3>
						<img
							src="@/assets/logo.jpg"
							alt="Logo Federación"
							srcset=""
							id="Logo_fed"
						/>
					</section>
					<section class="pdf-item">
						<h3>Estudio</h3>

						<b-list-group>
							<b-list-group-item
								v-for="value in fields.slice(0, -1)"
								:key="value.key"
								>{{ value.label }}:
								{{ estudioAPDF[value.key] }}</b-list-group-item
							>
						</b-list-group>
					</section>
				</section>
			</vue-html2pdf>
			<!-- ============================================================================== -->
		</div>
	</v-app>
</template>

<script>
	let api = new URL("http://localhost");
	api.pathname = "estudios";
	//api.port = 8000;
	api.port = 8081;
	import { APIControler } from "@/store/APIControler";
	import EstudiosAlta from "./EstudiosAlta.vue";
	import EstudiosUpdate from "./EstudiosUpdate.vue";
	import VueHtml2pdf from "vue-html2pdf";

	import axios from "axios";

	export default {
		components: { EstudiosAlta, EstudiosUpdate, VueHtml2pdf },
		data() {
			return {
				tabla_estudios: [],
				fields: [
					{ key: "selected", label: "Seleccionar", sortable: true },
					{ key: "id_estudio", label: "ID", sortable: true },
					{ key: "tipo", label: "Tipo", sortable: true },
					{ key: "abreviatura", label: "Abreviatura", sortable: true },
					{ key: "ub", label: "U.B.", sortable: true },
					{ key: "descripcion", label: "Descripción", sortable: true },
					{ key: "denominación", label: "Denominación", sortable: true },
					{ key: "proveedor", label: "Proveedor", sortable: true },
					{ key: "precio_socio", label: "Precio al socio", sortable: true },
					{
						key: "precio_federacion",
						label: "Precio a la federacion",
						sortable: true,
					},
					{ key: "action", label: "Acciones", variant: "secondary" },
				],
				totalRows: 1, //Total de filas
				currentPage: 1, //Pagina actual
				perPage: 10, // Datos en la tabla por pagina
				pageOptions: [10, 20, 40, 100, { value: 10000, text: "Todos" }],
				filter: null,

				selected: [],

				estudioAPDF: {},

				//Botones
				btn_down_pdf: false, //Desabilito los botones, hasta que muestre los datos
				btn_del_full: true,
				btn_limpiar: true,
				msj_tabla: " Presione 'Mostrar' para ver los regitros ",
				btn_mostrar: false,
				btn_editar: false,
				btn_ordenes: false,
				btn_eliminar: false,
				btn_select: false,
				editar: {},
				infoEliminar: {
					id: "modal_eliminar",
					estudio: -1,
				},

				//Campos a filtrar
				filter_tipo: null,
				filter_proveedor: null,

				//Opciones de filtro
				options_tipo: [{ value: null, text: "Elija un tipo", selected: true }],
				options_proveedor: [
					{ value: null, text: "Elija un proveedor", selected: true },
				],
			};
		},
		computed: {
			rows() {
				return (this.totalRows = this.tabla_estudios.length);
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

					var lista_estudios = data.results;

					console.log(lista_estudios);
					//this.getProveedor(lista_estudios);

					//this.tabla_estudios = lista_estudios;
					this.tabla_estudios = await this.getProveedor(lista_estudios);

					this.tabla_estudios.forEach((element) => {
						let opcionTipo = {};
						let opcionProv = {};
						opcionTipo.value = opcionTipo.text = element.tipo;
						//opcionTipo.text = element.laboratorio;
						opcionProv.value = opcionProv.text = element.proveedor;
						//opcionProv.text = element.cod_farmacia.split("/")[4];
						if (this.options_tipo.find((x) => x.value == opcionTipo.value)) {
							console.log(opcionTipo, " ya se encuentra en el listado");
						} else {
							this.options_tipo.push(opcionTipo);
						}
						if (
							this.options_proveedor.find((x) => x.value == opcionProv.value)
						) {
							console.log(opcionProv, " ya se encuentra en el listado");
						} else {
							this.options_proveedor.push(opcionProv);
						}
					});
				} catch (error) {
					console.log(error);
				}
			},

			async getProveedor(lista_estudios) {
				let listado = {};
				let DataReturn = [];
				let proveedorAPI = new APIControler();
				proveedorAPI.apiUrl.pathname = "proveedor_estudios/";
				let proveedor = await proveedorAPI.getData(listado);
				console.log("DATA LOS PROVEEDORES: ", proveedor);

				proveedor.forEach((element) => {
					var idProv =
						"http://localhost:8081/proveedor_estudios/" +
						element.id_proveedor +
						"/";
					lista_estudios.forEach((estudio) => {
						if (idProv == estudio.id_proveedor) {
							let datos = {};
							datos.id_estudio = estudio.id_estudio;
							datos.tipo = estudio.tipo;
							datos.abreviatura = estudio.abreviatura;
							datos.ub = estudio.ub;
							datos.descripcion = estudio.descripcion;
							datos.denominación = estudio.denominación;
							datos.proveedor = element.id_proveedor + "- " + element.nombre;
							datos.precio_socio = estudio.precio_socio;
							datos.precio_federacion = estudio.precio_federacion;
							DataReturn.push(datos);
						}
					});
				});
				return DataReturn;
			},

			editarEstudio(item, index) {
				this.editar = item;
			},
			//Funcion para mostrar el modal
			showModal() {
				this.$refs["my-modal"].show();
			},
			showModalinfo(item, index) {
				this.infoEliminar.estudio = item;
				this.showModal();
			},
			//Funcion para esconder el modal
			hideModal() {
				this.$refs["my-modal"].hide();
			},
			altaEstudio() {},

			async deleteEstudio(id_estudio) {
				axios
					.delete("http://localhost:8081/estudios/" + id_estudio + "/")
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

			//Funcion para eliminar todos los profesionales
			async delete_all_Estudios() {
				var cantidad = this.selected.length;

				try {
					for (var i = 0; i < cantidad; i++) {
						axios.delete(
							"http://localhost:8081/estudios/" +
								this.selected[i].id_estudio +
								"/"
						);
						if (this.selected.length == 0) {
							console.log("Eliminacion Exitosa");
							break;
						}
					}
					//this.testFetch();
					this.hideModal();

					swal("Eliminacion Exitosa", " ", "success");
				} catch (error) {
					this.hideModal();
					swal("¡ERROR!", "Se ha detectado un problema ", "error");
					console.log(error);
				} finally {
					location.reload();
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
			async generarPDF(item) {
				this.estudioAPDF = { ...item };
				this.$refs.html2Pdf.generatePdf();
			},

			VerProveedores() {
				this.$router.push("proveedor_estudios");
			},
		},
		beforeMount() {
			this.testFetch();
			//this.getProveedor();
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
