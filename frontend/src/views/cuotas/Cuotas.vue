<template>
	<v-app id="app">
		<div id="cuotas" class="myTable">
			<!--HEAD DE LA PAGINA -->
			<vue-headful
				title="Cuotas - Federación Tucumana de Mutuales"
			></vue-headful>

			<h2>Listado de Cuotas</h2>

			<b-button @click="testFetch" class="mb-4" title="Recargar" variant="light">
				<v-icon dark style="color: black">mdi-cached</v-icon>
				Actualizar
			</b-button>
			<!-- ================ALTA CUOTAS======================== -->
			<b-button
				class="mb-4 ml-2"
				v-b-modal.modal-alta
				@click="altaCuota()"
				title="Nuevo Pago de Cuota"
				style="color: white"
			>
				<v-icon dark> mdi-plus </v-icon>
				Nuevo Pago de Cuota
			</b-button>
			<b-modal id="modal-alta" hide-footer>
				<template #modal-title>
					<h5 class="modal-title">Alta</h5>
				</template>
				<cuotas-alta :updateTable="testFetch" />
			</b-modal>
			<!-- =========================================================== -->
			<!-- ==================================CREAR PDF================================== -->
			<b-button
				@click="generarPDF()"
				id="btn_down_pdf"
				class="mb-4 ml-2"
				title="Generar PDF"
				variant="danger"
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
				Generar PDF
			</b-button>
			<!-- ============================================================================== -->

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

			<!-- ================ELIMINAR VARIAS CUOTAS======================== -->
			<div>
				<b-modal
					ref="my-modal"
					id="modal-eliminarTodo"
					hide-footer
					title="Eliminar"
					ok-only
				>
					<div class="d-block text-center" v-if="selected.length === rows">
						<h3>¿Está seguro de eliminar todos los registros?</h3>
					</div>
					<div class="d-block text-center" v-else>
						<h3 v-if="selected.length>1">¿Está seguro de eliminar {{ selected.length }} registros?</h3>
						<h3 v-else>¿Está seguro de eliminar un registro?</h3>
					</div>

					<b-button class="mt-2" block @click="hideModal" title="Volver Atras">
						Volver Atras
					</b-button>

					<b-button
						class="mt-3"
						variant="danger"
						block
						title="Eliminar"
						@click="delete_all_Cuotas()"
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
					<pre>
Cantidad de registros: {{ rows }} | Filas seleccionadas: {{
							selected.length
						}}</pre
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

			<section class="container">
				<b-table
					:fields="fields"
					striped
					sortable
					responsive
					hover
					:items="tabla_cuot | FechaPagoRange(dateDesde, dateHasta)"
					show-empty
					:sticky-header="true"
					:no-border-collapse="false"
					:per-page="perPage"
					:current-page="currentPage"
					ref="tablaregistros"
					id="tablaregistros"
					selectable
					select-mode="multi"
					@row-selected="seleccionar_una"
					empty-text="No hay registros cargados"
					empty-filtered-text="No hemos encontrado registros que coincidan con lo que está buscando"
					:filter="filter"
					@filtered="onFiltered"
				>
					

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

					<template slot="cell(id_cuota)" slot-scope="data">
						<b>{{ data.value }}</b>
					</template>
					<template slot="cell(periodo)" slot-scope="data">
						{{ data.value | Date | mmyy }}
					</template>

					<template slot="cell(monto)" slot-scope="data">
						${{ data.value }}
					</template>

					<template slot="cell(pagado)" slot-scope="data">
						<div v-if="data.value === true">
							<svg
								xmlns="http://www.w3.org/2000/svg"
								width="16"
								height="16"
								fill="currentColor"
								class="bi bi-check-circle-fill"
								viewBox="0 0 16 16"
								style="color: green"
							>
								<path
									d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"
								/>
							</svg>
							SI
						</div>
						<div v-else>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								width="16"
								height="16"
								fill="currentColor"
								class="bi bi-x-circle-fill"
								viewBox="0 0 16 16"
								style="color: red"
							>
								<path
									d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM5.354 4.646a.5.5 0 1 0-.708.708L7.293 8l-2.647 2.646a.5.5 0 0 0 .708.708L8 8.707l2.646 2.647a.5.5 0 0 0 .708-.708L8.707 8l2.647-2.646a.5.5 0 0 0-.708-.708L8 7.293 5.354 4.646z"
								/>
							</svg>
							NO
						</div>
					</template>

					<template slot="cell(action)" slot-scope="row">
						<div class="mt-3">
							<b-button-group>
								<b-button
									variant="info"
									id="button-1"
									title="Mostrar Información adicional"
									:disabled="btn_mostrar"
									@click="row.toggleDetails"
								>
									{{ row.detailsShowing ? "Ocultar" : "Mostrar" }} Detalles
								</b-button>

								<b-button
									variant="warning"
									id="button-2"
									title="Editar este registro"
									v-b-modal.modal_editar
									@click="editarCuota(row.item, row.index)"
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
						<b-card>
							<b-list-group horizontal>
								<b-list-group>
									<b-list-group-item
										><b>Persona que pagó :</b>
										{{ row.item.personapago.toUpperCase() }}</b-list-group-item
									>
									<b-list-group-item
										><b>Nombre del socio:</b>
										{{ row.item.socio }}</b-list-group-item
									>
									<b-list-group-item
										><b>Monto:</b> ${{ row.item.monto }}</b-list-group-item
									>
									<b-list-group-item
										><b>Fecha:</b>
										{{
											row.item.fecharealizacion | Date
										}}</b-list-group-item
									>
								</b-list-group>
								&nbsp;
							</b-list-group>
						</b-card>
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
							aria-controls="table_socios"
						>
						</b-pagination>
					</b-col>
				</b-container>

				<b-modal
					id="modal_editar"
					ref="my-modaledit"
					hide-footer
					title="Editar"
					ok-only
				>
					<cuotas-update :item_cuot="editar" :updateTable="testFetch" />
				</b-modal>
				<!-- ================ELIMINAR UN MEDICAMENTO======================== -->
				<b-modal
					id="modal_eliminar"
					ref="my-modal"
					hide-footer
					title="Eliminar"
					ok-only
				>
					<div class="d-block text-center">
						<h3>
							¿Esta seguro de eliminar los datos del pago de '{{
								infoEliminar.cuota.nombre
							}}, {{ infoEliminar.cuota.apellido }}'?
						</h3>
					</div>
					<b-button class="mt-2" block @click="hideModal" title="Volver Atras">
						Volver Atras
					</b-button>

					<b-button
						class="mt-3"
						variant="danger"
						block
						title="Eliminar"
						@click="deleteCuota(infoEliminar.cuota.id_cuota)"
					>
						Eliminar
					</b-button>
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
				<div>
					<b-card-group deck>
						<b-card
							style="width: 100%"
							bg-variant="primary"
							text-variant="white"
							header="FILTRAR POR"
							class="text-center"
						>
							<div class="accordion" role="tablist" style="width: 100%">
								<b-card no-body>
									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button
											block
											v-b-toggle.accordion-1
											variant="info"
											style="font-size: 0.82em"
										>
											FECHA DE PAGO
										</b-button>
									</b-card-header>

									<b-collapse
										id="accordion-1"
										visible
										accordion="my-accordion"
										role="tabpanel"
									>
										<b-card-body>
											<b-form-group
												style="color: black"
												label="Desde"
												label-for="fechaDesde"
												@submit.stop.prevent="handleSubmit"
											>
												<b-form-input
													id="fechaDesde"
													v-model="dateDesde"
													type="date"
													aria-label="Desde"
													placeholder="Ingrese una Fecha"
													invalid-feedback="Complete este campo"
													required
												>
												</b-form-input>
												{{ dateDesde }}
											</b-form-group>

											<b-form-group
												style="color: black"
												label="Hasta"
												label-for="fechaHasta"
												@submit.stop.prevent="handleSubmit"
											>
												<b-form-input
													id="fechaHasta"
													v-model="dateHasta"
													type="date"
													placeholder="Ingrese una Fecha"
													required
												>
												</b-form-input>
												{{ dateHasta }}
											</b-form-group>
											<div v-show="dateDesde != null && dateHasta != null">
												<b-button
													@click="limpiar_filtro_fecha()"
													title="Limpiar"
												>
													Limpiar
												</b-button>
											</div>
										</b-card-body>
									</b-collapse>
								</b-card>
							</div>
						</b-card>
					</b-card-group>
				</div>
			</aside>

			<!-- ==================================CREAR PDF================================== -->
			<vue-html2pdf
				:show-layout="false"
				:float-layout="true"
				:enable-download="false"
				:preview-modal="true"
				:paginate-elements-by-height="1400"
				filename="Listado de Cuotas"
				:pdf-quality="2"
				:manual-pagination="false"
				pdf-format="a4"
				pdf-orientation="portrait"
				pdf-content-width="100%"
				ref="html2Pdf"
			>
				<section class="container-fluid pt-5" slot="pdf-content">
					<!-- PDF Content Here -->
					<section class="pdf-item">
						<h3 class="text-center">Federación Tucumana de Mutuales</h3>
						<img
							src="@/assets/logo.jpg"
							alt="Logo Federación"
							srcset=""
							id="Logo_fed"
						/>
					</section>
					<section class="pdf-item">
						<h3 class="text-center mb-3">Listado de Cuotas</h3>
						
						<b-table
							:fields="fields.slice(1,-1).map(x=>{x.sortable=false;return x})"
							:items="tabla_cuot"
							:no-border-collapse="false"
							small
							bordered
							head-variant="light"
						>
							<template slot="cell(fecharealizacion)" slot-scope="data">
								{{ data.value | Date }}
							</template>
						</b-table>
					
							
					</section>
				</section>
			</vue-html2pdf>
			<!-- ============================================================================== -->
		</div>
	</v-app>
</template>

<script>
	let api = new URL("http://localhost");
	api.pathname = "cuotas";
	//api.port = 8000;
	api.port = 8081;

	import CuotasAlta from "./CuotasAlta.vue";
	import CuotasUpdate from "./CuotasUpdate.vue";
	import axios from "axios";
	import VueHtml2pdf from "vue-html2pdf";

	import { APIControler } from "@/store/APIControler";
	import swal from "sweetalert";

	export default {
		components: { CuotasAlta, CuotasUpdate, VueHtml2pdf },
		data() {
			return {
				tabla_cuot: [],
				fields: [
					{ key: "selected", label: ""},
					{ key: "id_cuota", label: "ID", sortable: true },
					{ key: "monto", label: "Monto", sortable: true },
					{ key: "periodo", label: "Mes",sortable: true},
					{ key: "socio", label: "Socio", sortable: true },
					{ key: "dni_socio", label: "DNI Socio", sortable: true },
					{ key: "pagado", label: "Pagada",sortable: true},
					{ key: "action", label: "Acciones", variant: "secondary" },
				],
				modal: false,

				dateDesde: null,
				dateHasta: null,

				editar: {},
				filter: null,
				totalRows: 1, //Total de filas
				currentPage: 1, //Pagina actual
				perPage: 10, // Datos en la tabla por pagina
				pageOptions: [10, 20, 40, 100, { value: 10000, text: "Todos" }],
				selected: [],
				infoEliminar: {
					id: "modal_eliminar",
					cuota: -1,
				},
				btn_down_pdf: true, //Desabilito los botones, hasta que muestre los datos
				btn_del_full: true,
				btn_mostrar: false,
				btn_editar: false,
				btn_eliminar: false,
				btn_select: false,
				btn_limpiar: true,
			};
		},
		computed: {
			rows() {
				return (this.totalRows = this.tabla_cuot.length);
			},
			sortOptions() {
				// Funcion para filtrar
				return this.fields
					.filter((f) => f.sortable)
					.map((f) => {
						return { text: f.label, value: f.key };
					});
			},
		},

		methods: {
			//Funcion para mostrar todos los medicamentos
			async getSocio(numero_socio) {
				let socioAPI = new APIControler();
				socioAPI.apiUrl.pathname = "socios/" + numero_socio+'/';
				let response = await fetch(socioAPI.apiUrl);
				let data = await response.json();
				return data;
			},
			async testFetch() {
				try {
					const res = await fetch(api);
					const data = await res.json();

					var lista_cuot = data.results;

					for (var i = 0; i < lista_cuot.length; i++) {
						var socio1 = await this.getSocio(
							lista_cuot[i].numero_socio.split("/")[4]
						);
						lista_cuot[i].socio = socio1.apellido + ", " + socio1.nombre;
						lista_cuot[i].dni_socio = socio1.dni;
					}
					console.log(lista_cuot);

					this.tabla_cuot = lista_cuot;

					this.btn_down_pdf = false; //Habilito los botones

				} catch (error) {
					console.log(error);
				}
			},
			//Funcion para mostrar el modal
			showModal() {
				this.$refs["my-modal"].show();
			},
			//Funcion para esconder el modal
			hideModal() {
				this.$refs["my-modal"].hide();
			},

			info(id) {
				alert("id: " + id);
			},

			showModalinfo(item, index) {
				this.infoEliminar.cuota = item;
				this.showModal();
			},

			//-----Funciones de seleccion
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

			//Funcion para crear el PDF
			generarPDF() {
				if (this.tabla_cuot.length != 0) {
					this.$refs.html2Pdf.generatePdf();
				} else {
					swal("Debe tener al menos 1 registro");
				}
			},

			//Alta de medicamento
			altaCuota() {},

			//Editar medicamento
			editarCuota(item, index) {
				this.editar = item;
			},

			//Funcion para eliminar el medicamento
			async deleteCuota(id) {
				axios
					.delete("http://localhost:8081/cuotas/" + id + "/")
					.then((datos) => {
						swal("Eliminacion Exitosa", " ", "success");
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

			//Funcion para eliminar todos los medicamentos seleccionados
			async delete_all_Cuotas() {
				var cantidad = this.selected.length;

				try {
					for (var i = 0; i < cantidad; i++) {
						axios.delete(
							"http://localhost:8081/cuotas/" + this.selected[i].id_cuota + "/"
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

			limpiar_filtro_fecha() {
				this.dateDesde = null;
				this.dateHasta = null;
			},

			onFiltered(filteredItems) {
				// Trigger pagination to update the number of buttons/pages due to filtering
				this.totalRows = filteredItems.length;
				this.currentPage = 1;
			},

			//Edicion del pdf antes de descargar
			async beforeDownload({ html2pdf, options, pdfContent }) {
				await html2pdf()
					.set(options)
					.from(pdfContent)
					.toPdf()
					.get("pdf")
					.then((pdf) => {
						const totalPages = pdf.internal.getNumberOfPages();
						for (let i = 1; i <= totalPages; i++) {
							pdf.setPage(i);
							pdf.setFontSize(10);
							pdf.setTextColor(150);
							pdf.text(
								"Página " + i + " of " + totalPages,
								pdf.internal.pageSize.getWidth() * 0.88,
								pdf.internal.pageSize.getHeight() - 0.3
							);
						}
					})
					.save();
			},
		},
		filters: {mmyy(dia){
			const [day,mes,año]=dia.split('/')
			return mes+"/"+año
		}
		},

		beforeMount() {
			this.testFetch();
			//this.seachPorFecha();
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
