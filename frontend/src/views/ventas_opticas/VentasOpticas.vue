<template>
	<v-app id="app">
		<div id="ventasOpticas" class="myTable">
			<!--HEAD DE LA PAGINA -->
			<vue-headful
				title="Ventas Opticas - Federación Tucumana de Mutuales"
			></vue-headful>

			<h2>Listado de Ventas Opticas</h2>
			<b-button
				@click="testFetch"
				class="mb-4"
				title="Recargar"
				variant="light"
			>
				<v-icon dark style="color: black">mdi-cached</v-icon>
				Actualizar
			</b-button>

			<!-- ================ALTA VENTAS OPTICAS======================== -->
			<b-button
				class="mb-4 ml-2"
				v-b-modal.modal-alta
				@click="altaVentaOptica()"
				title="Nueva Venta Optica"
				style="color: white"
			>
				<v-icon dark> mdi-plus </v-icon>
				Nueva Venta Optica
			</b-button>
			<b-modal id="modal-alta" hide-footer>
				<template #modal-title><h5 class="modal-title">Alta</h5></template>
				<ventasOpticas-alta :updateTable="testFetch" />
			</b-modal>

			<!-- ================ELIMINAR VARIAS VENTAS OPTICAS======================== -->
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
						<h3>¿Esta seguro de eliminar todos los registros?</h3>
					</div>
					<div class="d-block text-center" v-else>
						<h3>¿Esta seguro de eliminar {{ selected.length }} registros?</h3>
					</div>

					<b-button class="mt-2" block @click="hideModal" title="Volver Atras">
						Volver Atras
					</b-button>

					<b-button
						class="mt-3"
						variant="danger"
						block
						title="Eliminar"
						@click="delete_all_VentasOpticas()"
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
						tabla_ventasOpticas
							| FechaVentaRange(
								filter_fechaVenta.desde,
								filter_fechaVenta.hasta
							)
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

					<template slot="cell(socio)" slot-scope="data">
						{{ data.value.toUpperCase() }}
					</template>
					<template slot="cell(fecha_venta)" slot-scope="data">
						{{ data.value | Date }}
					</template>

					<template slot="cell(action)" slot-scope="row">
						<div class="mt-3">
							<b-button-group>
								<!-- ==================================CREAR PDF================================== -->
								<b-button
									variant="info"
									id="button-1"
									title="Mostrar Info"
									@click="row.toggleDetails"
									:disabled="btn_mostrar"
								>
									{{ row.detailsShowing ? "Ocultar" : "Mostrar" }} detalles
								</b-button>
								<!-- Generar PDF -->
								<b-button
									@click="generarPDF(row.item)"
									id="btn_down_pdf"
									class="mb-0"
									title="Generar PDF"
									variant="secondary"
									style="color: white"
									:disabled="btn_down_pdf"
								>
									<!-- :disabled="btn_down_pdf" -->
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
									PDF
									<!-- ============================================================================== -->
								</b-button>
								<b-button
									variant="warning"
									id="button-2"
									title="Editar este registro"
									v-b-modal.modal-editar
									@click="editarVentaOptica(row.item, row.index)"
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
						<b-card title="Datos de la venta: ">
							<div>
								<b-list-group horizontal>
									<b-list-group class="col-6">
										<b-list-group-item
											><b>N° Venta:</b>
											{{ row.item.id_venta }}</b-list-group-item
										>
										<b-list-group-item
											><b>N° Socio:</b>
											{{ row.item.socio.toUpperCase() }}</b-list-group-item
										>
										<b-list-group-item
											><b>Lente:</b>
											{{ row.item.lente.split("/")[4] }}</b-list-group-item
										>
										<b-list-group-item
											><b>Fecha Receta:</b>
											{{ row.item.fecha_receta }}</b-list-group-item
										>
									</b-list-group>
									&nbsp;
									<b-list-group class="col-6">
										<b-list-group-item
											><b>Cristal Derecho:</b>
											{{
												row.item.cristal_derecho.split("/")[4]
											}}</b-list-group-item
										>
										<b-list-group-item
											><b>Cristal Izquierdo:</b>
											{{ row.item.cristal_izquierdo.split("/")[4] }}
										</b-list-group-item>
										<b-list-group-item
											><b>Fecha Venta:</b>
											{{ row.item.fecha_venta }}
										</b-list-group-item>
									</b-list-group>
								</b-list-group>
							</div>
						</b-card>
					</template>
				</b-table>
				<!-- ================ELIMINAR VENTA OPTICA======================== -->

				<b-modal
					id="modal_eliminar"
					ref="my-modal"
					hide-footer
					title="Eliminar"
					ok-only
				>
					<div class="d-block text-center">
						<h3>
							¿Esta seguro de eliminar los datos de la venta optica
							{{ infoEliminar.ventaOptica.id_venta }}?
						</h3>
					</div>
					<b-button class="mt-2" block @click="hideModal" title="Volver Atras"
						>Volver Atras</b-button
					>
					<b-button
						class="mt-3"
						variant="danger"
						block
						@click="deleteVentaOptica(infoEliminar.ventaOptica.id_venta)"
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
							aria-controls="table_ventasOpticas"
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
											v-b-toggle.accordion-1
											variant="info"
											style="font-size: 0.82em"
										>
											FECHA VENTA
										</b-button>
									</b-card-header>
									<b-collapse
										id="accordion-1"
										visible
										accordion="my-accordion"
										role="tabpanel"
										style="color: black"
									>
										<b-card-body>
											<b-form-group id="input-group-4">
												<b-form-group label="Desde" label-for="fecha_desde">
													<b-form-input
														id="fecha_desde"
														v-model="filter_fechaVenta.desde"
														type="date"
													></b-form-input>
												</b-form-group>
												<b-form-group label="Hasta" label-for="fecha_hasta">
													<b-form-input
														id="fecha_inicio_hasta"
														v-model="filter_fechaVenta.hasta"
														type="date"
													></b-form-input>
												</b-form-group>

												<div style="color: black">
													{{ filter_fechaVenta.desde }} <br />
													{{ filter_fechaVenta.hasta }} <br />
												</div>
												<div
													v-show="
														filter_fechaVenta.desde != null &&
														filter_fechaVenta.hasta != null
													"
												>
													<b-button
														@click="limpiar_filtro_fecha()"
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
				<ventasOpticas-update :ventaOptica="editar" :updateTable="testFetch" />
			</b-modal>

			<!-- ==================================CREAR PDF================================== -->
			<vue-html2pdf
				:show-layout="false"
				:float-layout="true"
				:enable-download="false"
				:preview-modal="true"
				:paginate-elements-by-height="1400"
				filename="DetalleVentaOptica"
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
						<h3>Venta Optica</h3>

						<b-list-group>
							<b-list-group-item
								v-for="value in fields.slice(0, -1)"
								:key="value.key"
								>{{ value.label }}:
								{{ ventaOpticaAPDF[value.key] }}</b-list-group-item
							>
							<b-list-group-item
								><b>N° Venta:</b>
								{{ ventaOpticaAPDF.id_venta }}</b-list-group-item
							>
							<b-list-group-item
								><b>N° Socio:</b>
								{{ ventaOpticaAPDF.numero_socio }}</b-list-group-item
							>
							<b-list-group-item
								><b>Lente:</b>
								{{ ventaOpticaAPDF.lente | Split }}</b-list-group-item
							>
							<b-list-group-item
								><b>Fecha Receta:</b>
								{{ ventaOpticaAPDF.fecha_receta }}</b-list-group-item
							>
							<b-list-group-item
								><b>Cristal Derecho:</b>
								{{ ventaOpticaAPDF.cristal_derecho | Split }}</b-list-group-item
							>
							<b-list-group-item
								><b>Cristal Izquierdo:</b>
								{{ ventaOpticaAPDF.cristal_izquierdo | Split }}
							</b-list-group-item>
							<b-list-group-item
								><b>Fecha Venta:</b>
								{{ ventaOpticaAPDF.fecha_venta }}
							</b-list-group-item>
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
	api.pathname = "ventasOpticas/";
	//api.port = 8000;
	api.port = 8081;
	import { APIControler } from "@/store/APIControler";
	import VentasOpticasAlta from "./VentasOpticasAlta.vue";
	import VentasOpticasUpdate from "./VentasOpticasUpdate.vue";
	import VueHtml2pdf from "vue-html2pdf";

	import axios from "axios";

	export default {
		components: { VentasOpticasAlta, VentasOpticasUpdate, VueHtml2pdf },
		data() {
			return {
				tabla_ventasOpticas: [],
				fields: [
					{ key: "id_venta", label: "N° venta", sortable: true },
					{ key: "socio", label: "Número Socio", sortable: true },
					{ key: "fecha_venta", label: "Fecha de venta", sortable: true },
					{ key: "action", label: "Acciones", variant: "secondary" },
				],
				filter: null,
				totalRows: 1, //Total de filas
				currentPage: 1, //Pagina actual
				perPage: 10, // Datos en la tabla por pagina
				pageOptions: [10, 20, 40, 100, { value: 10000, text: "Todos" }],
				buscar: "",
				editar: {},
				infoEliminar: {
					id: "modal_eliminar",
					ventaOptica: -1,
				},
				selected: [],
				//Botones
				btn_down_pdf: false, //Deshabilito los botones, hasta que muestre los datos
				btn_del_full: true,
				btn_limpiar: true,
				msj_tabla: " Presione 'Mostrar' para ver los regitros ",
				btn_mostrar: false,
				btn_editar: false,
				btn_ventasOpticas: false,
				btn_eliminar: false,
				btn_select: false,

				//Campos a filtrar
				filter_fechaVenta: {
					desde: null,
					hasta: null,
				},

				ventaOpticaAPDF: {}, //Se carga cuando se hace clic en exportar a pdf, con la venta a exportar
			};
		},
		computed: {
			rows() {
				return (this.totalRows = this.tabla_ventasOpticas.length);
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

					var lista_ventasOpticas = data.results;

					//this.tabla_ventasOpticas = lista_ventasOpticas;
					this.tabla_ventasOpticas = await this.getSocio(lista_ventasOpticas);
					
					
					
				} catch (error) {
					console.log(error);
				}
			},

			async getSocio(lista_ventasOptica) {
				let listado = {};
				let DataReturn = [];
				let socioAPI = new APIControler();
				socioAPI.apiUrl.pathname = "socios/";
				let socios = await socioAPI.getData(listado);
				console.log("DATA LOS SOCIOS: ", socios);
				
				socios.forEach((element) => {
					var IdSocio =
						"http://localhost:8081/socios/" + element.numero_socio + "/";
					lista_ventasOptica.forEach((venta) => {
						if (IdSocio == venta.numero_socio) {
							let datos = {};
							datos.id_venta = venta.id_venta;
							datos.socio =
								element.numero_socio +
								"- " +
								element.apellido +
								", " +
								element.nombre;

							datos.cristal_derecho = venta.cristal_derecho;
							datos.cristal_izquierdo = venta.cristal_izquierdo;
							datos.fecha_receta = venta.fecha_receta;
							datos.fecha_venta = venta.fecha_venta;
							datos.lente = venta.lente;

							DataReturn.push(datos);
						}
					});
				});
				console.log("DATOS! :", DataReturn);
				return DataReturn;
			},
			editarVentaOptica(item, index) {
				this.editar = item;
			},
			//Funcion para mostrar el modal
			showModal() {
				this.$refs["my-modal"].show();
			},
			showModalinfo(item, index) {
				this.infoEliminar.ventaOptica = item;
				this.showModal();
			},
			//Funcion para esconder el modal
			hideModal() {
				this.$refs["my-modal"].hide();
			},
			altaVentaOptica() {},

			//Elimino una venta Optica
			async deleteVentaOptica(id_venta) {
				axios
					.delete("http://localhost:8081/ventasOpticas/" + id_venta + "/")
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
			async delete_all_VentasOpticas() {
				var cantidad = this.selected.length;

				try {
					for (var i = 0; i < cantidad; i++) {
						axios.delete(
							"http://localhost:8081/ventasOpticas/" +
								this.selected[i].id_venta +
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
						this.btn_down_pdf = true;
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
					this.btn_down_pdf = false;
				}
			},
			//Selecciona todas
			seleccionar_todas() {
				this.$refs.tablaregistros.selectAllRows();
				this.btn_del_full = false;
				this.btn_mostrar = true;
				this.btn_editar = true;
				this.btn_eliminar = true;
				this.btn_down_pdf = true;

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
				this.btn_down_pdf = false;

				this.btn_select = false;
				this.btn_limpiar = true;
			},
			//Funcion de busqueda
			onFiltered(filteredItems) {
				// Trigger pagination to update the number of buttons/pages due to filtering
				this.totalRows = filteredItems.length;
				this.currentPage = 1;
			},
			//Funcion para crear el PDF
			async generarPDF(item) {
				//let resultSocio = (await axios.get(item.numero_socio)).data;
				let resultVenta = (
					await axios.get(
						"http://localhost:8081/ventasOpticas/" + item.id_venta
					)
				).data;
				this.ventaOpticaAPDF = { ...resultVenta };
				// this.ventaOpticaAPDF = { ...item };

				this.ventaOpticaAPDF.numero_socio = item.socio;

				this.$refs.html2Pdf.generatePdf();
			},
			limpiar_filtro_fecha() {
				this.filter_fechaVenta.desde = null;
				this.filter_fechaVenta.hasta = null;
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
