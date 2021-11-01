<template>
	<div id="socios" class="myTable">
		<!--HEAD DE LA PAGINA -->
		<vue-headful title="Socios - Federación Tucumana de Mutuales"></vue-headful>

		<h2>Listado de Socios</h2>

		<b-button @click="testFetch" class="mb-4" title="Recargar" variant="light">
			<v-icon dark style="color: black">mdi-cached</v-icon>
			Actualizar
		</b-button>

		<b-button
			@click="testFetch2"
			class="mb-4"
			style="margin-left: 0.5em"
			title="Mostrar"
			variant="success"
		>
			<v-icon dark style="color: black">mdi-check</v-icon>
			Mostrar Cuotas
		</b-button>

		<!-- ================ALTA SOCIO======================== -->
		<b-button
			class="mb-4 ml-2"
			v-b-modal.modal-alta
			@click="altaSocio()"
			title="Nuevo Socio"
			style="color: white"
		>
			<v-icon dark> mdi-plus </v-icon>
			Nuevo Socio
		</b-button>
		<b-modal id="modal-alta" hide-footer>
			<template #modal-title>
				<h5 class="modal-title">Alta</h5>
			</template>
			<socios-alta />
		</b-modal>

		<!-- ================ PAGO DE AFILIACION ======================== -->
		<b-button
			@click="GenerarPagoAfiliacion()"
			class="mb-4 ml-2"
			id="btn_Pago_afiliacion"
			title="Pago Afiliacion"
			>Pago de Afiliacion</b-button
		>
		<!-- ============================================================ -->
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
					@click="delete_all_Socios()"
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

		<div v-if="rows > 0">
			<div v-if="selected.length > 0">
				<pre>
					Cantidad de registros: {{ rows }} | 
					Filas seleccionadas: {{ selected.length }}
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
		<b-overlay
			:show="show"
			@shown="onShown"
			@hidden="onHidden"
			variant="dark"
			opacity="0.51"
		>
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
					:items="tabla_socios"
					show-empty
					:per-page="perPage"
					:current-page="currentPage"
					ref="tablaregistros"
					id="tablaregistros"
					selectable
					select-mode="multi"
					@row-selected="seleccionar_una"
					:filter="filter"
					@filtered="onFiltered"
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

					<template slot="cell(numero_socio)" slot-scope="data">
						<b>{{ data.value }}</b>
					</template>

					<template slot="cell(apellido)" slot-scope="data">
						{{ data.value.toUpperCase() }}
					</template>

					<template slot="cell(nombre)" slot-scope="data">
						{{ data.value.toUpperCase() }}
					</template>

					<template slot="cell(fecha_nacimiento)" slot-scope="data">
						{{ data.value.split("-")[2] }}/{{ data.value.split("-")[1] }}/{{
							data.value.split("-")[0]
						}}
					</template>

					<template slot="cell(carencia)" slot-scope="data">
						{{ data.value.split("-")[2] }}/{{ data.value.split("-")[1] }}/{{
							data.value.split("-")[0]
						}}
					</template>

					<template slot="cell(departamento)" slot-scope="data">
						{{ data.value.toUpperCase() }}
					</template>

					<template slot="cell(action)" slot-scope="row">
						<div class="mt-3">
							<b-button-group>
								<b-button
									variant="info"
									id="button-1"
									title="Mostrar Info"
									@click="
										row.toggleDetails();
										getFamiliar();
									"
									:disabled="btn_mostrar"
								>
									{{ row.detailsShowing ? "Ocultar" : "Mostrar" }} Detalles
								</b-button>

								<b-button
									variant="warning"
									id="button-2"
									title="Editar este registro"
									v-b-modal.modal-editar
									@click="editarSocio(row.item, row.index)"
									:disabled="btn_editar"
								>
									<!-- :disabled="btn_editar" -->
									<v-icon class="mr-2"> mdi-pencil </v-icon>
									Editar
								</b-button>

								<b-button
									variant="success"
									id="button-2"
									@click="showModalinfo1(row.item, row.index)"
									:disabled="btn_pagado"
								>
									<!-- isabled="btn_editar" -->
									<v-icon class="mr-2"> mdi-cash </v-icon>
									¿Pagado?
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

								<!-- ================ELIMINAR SOCIO======================== -->
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
											{{ infoEliminar.socio.apellido }},
											{{ infoEliminar.socio.nombre }} ?
										</h3>
									</div>
									<b-button
										class="mt-2"
										block
										@click="hideModal"
										title="Volver Atras"
										>Volver Atras</b-button
									>
									<b-button
										class="mt-3"
										variant="danger"
										block
										@click="deleteSocio(infoEliminar.socio.numero_socio)"
										title="Eliminar"
									>
										Eliminar
									</b-button>
								</b-modal>
								<b-modal
									id="modal_pagado"
									ref="my-modalpagado"
									hide-footer
									title="Pagado?"
									ok-only
								>
									<div class="d-block text-center">
										<h3>
											El socio
											{{ infopagado.socio.apellido }},
											{{ infopagado.socio.nombre }} pago hace
											{{ infopagado.dias }} dias por lo que
											{{ infopagado.mensaje }}
										</h3>
									</div>
									<b-button
										class="mt-2"
										block
										@click="hideModal"
										title="Volver Atras"
										>Volver Atras</b-button
									>
									<b-button
										class="mt-3"
										variant="success"
										block
										href="/cuotas/"
										title="Pagar"
									>
										Pagar
									</b-button>
								</b-modal>
								<!-- ==================================================== -->
							</b-button-group>
						</div>
					</template>

					<template #row-details="row">
						<b-card title="Datos del titular: ">
							<div>
								<b-list-group horizontal>
									<b-list-group>
										<b-list-group-item
											><b>Nombre Completo:</b>
											{{ row.item.apellido.toUpperCase() }},
											{{ row.item.nombre.toUpperCase() }}</b-list-group-item
										>
										<b-list-group-item
											><b>DNI:</b> {{ row.item.dni }}</b-list-group-item
										>
										<b-list-group-item
											><b>Fecha de Nacimiento:</b>
											{{ row.item.fecha_nacimiento }}</b-list-group-item
										>
										<b-list-group-item
											><b>Edad:</b> {{ row.item.edad }}</b-list-group-item
										>
									</b-list-group>
									&nbsp;
									<b-list-group>
										<b-list-group-item
											><b>Domicilio:</b> {{ row.item.calle.toUpperCase() }} -
											{{ row.item.localidad.toUpperCase() }}
										</b-list-group-item>
										<b-list-group-item
											><b>Departamento:</b>
											{{
												row.item.departamento.toUpperCase()
											}}</b-list-group-item
										>
										<b-list-group-item
											><b>Codigo Postal:</b>
											{{ row.item.cod_postal }}</b-list-group-item
										>
										<b-list-group-item
											><b>Correo:</b> {{ row.item.email }}
										</b-list-group-item>
									</b-list-group>
									&nbsp;
									<b-list-group>
										<b-list-group-item
											><b>Telefono Fijo:</b>
											{{ row.item.tel_fijo }}</b-list-group-item
										>
										<b-list-group-item
											><b>Celular:</b>
											{{ row.item.tel_celular }}</b-list-group-item
										>
										<b-list-group-item
											><b>Carencia:</b> {{ row.item.carencia }}
										</b-list-group-item>
									</b-list-group>
								</b-list-group>
							</div>
						</b-card>

						<b-card title="Adherentes: ">
							<div>
								<b-list-group horizontal>
									<div v-for="adherente in data" :key="adherente.dni_familiar">
										<div
											v-if="
												adherente.numero_socio.split('/')[4] ==
												row.item.numero_socio
											"
										>
											<b-list-group>
												<b-list-group-item
													><b>DNI:</b>
													{{ adherente.dni_familiar }}</b-list-group-item
												>
												<b-list-group-item
													><b>Nombre Completo:</b>
													{{ adherente.apellido.toUpperCase() }},
													{{
														adherente.nombre.toUpperCase()
													}}</b-list-group-item
												>
												<b-list-group-item
													><b>Fecha de Nacimiento:</b>
													{{ adherente.fecha_nacimiento }} | <b>Edad:</b>
													{{ adherente.edad }}</b-list-group-item
												>
												<b-list-group-item
													><b>Carencia:</b> {{ adherente.carencia }}
												</b-list-group-item>
											</b-list-group>
											&nbsp;
										</div>
									</div>
								</b-list-group>
							</div>

							<b-button
								@click="generarCarnet(row.item)"
								id="btn_down_pdf"
								class="mb-0 ml-2"
								title="Generar PDF"
								variant="info"
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
							</b-button>
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
											AL DIA
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
												id="input-group-4"
												v-slot="{ ariaDescribedby }"
											>
												<b-form-checkbox-group
													v-model="filter"
													id="socio_al_dia"
													:aria-describedby="ariaDescribedby"
													style="color: black"
												>
													<b-form-checkbox value="❌">NO❌</b-form-checkbox>
													<b-form-checkbox value="✔">SI✔️</b-form-checkbox>
												</b-form-checkbox-group>
											</b-form-group>
										</b-card-body>
									</b-collapse>

									<b-card-header header-tag="header" class="p-2" role="tab">
										<b-button block v-b-toggle.accordion-2 variant="info">
											DEPARTAMENTO
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
												<b-form-select
													id="departamento"
													v-model="filter"
													type="text"
													:options="options_deptos"
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
			<template #overlay>
				<div class="text-center">
					<v-icon>fas fa-circle-notch fa-spin</v-icon>
					<p id="cancel-label">Espere un momento...</p>
				</div>
			</template>
		</b-overlay>
		<b-modal id="modal-editar" hide-footer>
			<template #modal-title><h5 class="modal-title">Editar</h5></template>
			<socios-update :socio="editar" />
		</b-modal>

		<!-- ==================================CREAR CARNET================================== -->
		<vue-html2pdf
			:show-layout="false"
			:float-layout="true"
			:enable-download="false"
			:preview-modal="true"
			:paginate-elements-by-height="1400"
			filename="DetalleOrden"
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
					<b-card-group deck>
						<b-card
							img-src="../assets/logo.jpg"
							img-alt="Logo Federación"
							img-left
							class="mb-3"
							img-width="90"
							img-height="90"
						>
							<b-card-text>
								<h6>Federación Tucumana de Mutuales</h6>
								<div>
									<b-list-group horizontal="md" style="font-size: 70%">
										<b-list-group-item>
											<b>N°: {{ carnetAPDF.numero_socio }}</b> |
											<b>Afiliado:</b> {{ carnetAPDF.afiliado }} | <b>DNI:</b>
											{{ carnetAPDF.dni }}
											{{ carnetAPDF.adherentes }}
										</b-list-group-item>
									</b-list-group>
									<b-list-group>
										&nbsp;
										<h6>Adherentes</h6>

										<b-list-group-item
											v-for="adh in carnetAPDF.adhrentes"
											:key="adh.dni"
											style="font-size: 70%"
										>
											<b>{{ adh.dni }}</b> - {{ adh.adherente }}
										</b-list-group-item>
									</b-list-group>
								</div>
							</b-card-text>
						</b-card>
					</b-card-group>
				</section>
			</section>
		</vue-html2pdf>
	</div>
</template>

<script>
	let api = new URL("http://localhost");
	api.pathname = "socios";
	//api.port = 8000; //Cambien uds los puertos
	api.port = 8081;

	import VueAwesomplete from "vue-awesomplete";
	import SociosAlta from "./SociosAlta.vue";
	import SociosUpdate from "./SociosUpdate.vue";
	import VueHtml2pdf from "vue-html2pdf";

	import axios from "axios";
	import { APIControler } from "../store/APIControler";

	export default {
		components: {
			SociosAlta,
			SociosUpdate,
			VueAwesomplete,
			VueHtml2pdf,
		},
		data() {
			return {
				tabla_socios: [],
				fields: [
					{ key: "selected", label: "Seleccionar", sortable: true },
					{ key: "numero_socio", label: "N° Socio", sortable: true },
					{ key: "apellido", label: "Apellido/s", sortable: true },
					{ key: "nombre", label: "Nombre/s", sortable: true },
					{ key: "dni", label: "DNI", sortable: true },
					{
						key: "fecha_nacimiento",
						label: "Fecha de Nacimiento",
						sortable: true,
					},
					//{key: 'calle' ,label: 'Direccion', sortable: true,},
					//{key:'localidad' ,label: 'Localidad', sortable: true,},
					{ key: "departamento", label: "Departamento", sortable: true },
					//{key:'cod_postal' ,label: 'Codigo Postal', sortable: true,},
					//{key: 'email' ,label: 'Mail', sortable: true,},
					//{key: 'tel_fijo',label: 'Telefono Fijo', sortable: true,},
					//{key:'tel_celular' ,label: 'Telefono Celular', sortable: true,},
					{ key: "carencia", label: "Carencia", sortable: true },
					{ key: "aldia", label: "Al Día", sortable: true },
					{ key: "action", label: "Acciones", variant: "secondary" },
				],
				filter: null,
				totalRows: 1, //Total de filas
				currentPage: 1, //Pagina actual
				perPage: 10, // Datos en la tabla por pagina
				pageOptions: [10, 20, 40, 100, { value: 10000, text: "Todos" }],
				list_familiares: {},
				datos_familiar: {},
				data: {},
				editar: {},
				buscar: "",
				selected: [],
				infoEliminar: {
					id: "modal_eliminar",
					socio: -1,
				},
				infopagado: {
					id: "modal_pagado",
					socio: -1,
					dias: -1,
					mensaje: "no esta al dia ❌",
				},
				socioAldia: [],
				btn_down_pdf: true, //Desabilito los botones, hasta que muestre los datos
				btn_del_full: true,
				msj_tabla: " Presione 'Mostrar' para ver los regitros ",
				btn_mostrar: false,
				btn_editar: false,
				btn_pagado: false,
				btn_eliminar: false,
				btn_select: false,
				btn_limpiar: true,

				carnetAPDF: {
					numero_socio: null,
					afiliado: null,
					dni: 0,
					adhrentes: [],
				},
				show: false,

				options_deptos: [
					{ value: null, text: "Elija un departamento" },
					{ value: "Burruyacú", text: "1- Burruyacú" },
					{ value: "Capital", text: "2- Capital" },
					{ value: "Chicligasta", text: "3- Chicligasta" },
					{ value: "Cruz Alta", text: "4- Cruz Alta" },
					{ value: "Famaillá", text: "5- Famaillá" },
					{ value: "Graneros", text: "6- Graneros" },
					{ value: "Juan Bautista Alberdi", text: "7- Juan Bautista Alberdi" },
					{ value: "La Cocha", text: "8- La Cocha" },
					{ value: "Leales", text: "9- Leales" },
					{ value: "Lules", text: "10- Lules" },
					{ value: "Monteros", text: "11- Monteros" },
					{ value: "Río Chico", text: "12- Río Chico" },
					{ value: "Simoca", text: "13- Simoca" },
					{ value: "Tafí del Valle", text: "14- Tafí del Valle" },
					{ value: "Tafí Viejo", text: "15- Tafí Viejo" },
					{ value: "Trancas", text: "16- Trancas" },
					{ value: "Yerba Buena", text: "17- Yerba Buena" },
				],
			};
		},

		computed: {
			rows() {
				return (this.totalRows = this.tabla_socios.length);
			},
			id() {
				return this.tabla_socios.numero_socio;
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

		mounted: function () {},

		methods: {
			async getAldia(numero_socio) {
				let diaAPI = new APIControler();
				diaAPI.apiUrl.pathname = "aldia/" + numero_socio + "/aldia/";
				let response = await fetch(diaAPI.apiUrl);
				let data = await response.json();
				console.log(data);
				return data;
			},
			async testFetch() {
				try {
					const res = await fetch(api);
					const data = await res.json();
					var lista_socios = data.results;

					this.tabla_socios = lista_socios;
					this.btn_down_pdf = false; //Habilito los botones

					if (this.tabla_socios.length == 0) {
						this.msj_tabla = " No se encuentran regitros en esta tabla ";
					}
				} catch (error) {
					console.log(error);
				}
			},
			async testFetch2() {
				try {
					this.show = true;

					const res = await fetch(api);
					const data = await res.json();
					var lista_socios = data.results;

					for (var i = 0; i < lista_socios.length; i++) {
						var numerillo = await this.getAldia(lista_socios[i].numero_socio);
						if (numerillo < 30 && numerillo >= 0) {
							lista_socios[i].aldia = "✔";
						} else {
							lista_socios[i].aldia = "❌";
						}
					}
					//console.log(lista_socios[0].aldia);

					this.tabla_socios = lista_socios;
					this.btn_down_pdf = false; //Habilito los botones

					if (this.tabla_socios.length == 0) {
						this.msj_tabla = " No se encuentran regitros en esta tabla ";
					}
				} catch (error) {
					console.log(error);
				} finally {
					this.show = false;
				}
			},
			async getFamiliar() {
				let familiarAPI = new APIControler();
				familiarAPI.apiUrl.pathname = "familiar/";
				this.data = await familiarAPI.getData(this.list_familiares);
				this.data.forEach((element) => {
					console.log(element);
				});
			},
			editarSocio(item, index) {
				this.editar = item;
			},

			// Funcion para mostrar el modal
			showModal() {
				this.$refs["my-modal"].show();
			},

			showModalinfo(item, index) {
				this.infoEliminar.socio = item;
				this.showModal();
			},
			async showModalinfo1(item, index) {
				this.infopagado.socio = item;
				this.infopagado.dias = await this.getAldia(item.numero_socio);
				if (this.infopagado.dias < 31 && this.infopagado.dias >= 0) {
					this.infopagado.mensaje = "si esta al dia ✔️";
				} else {
					this.infopagado.mensaje = "no esta al dia ❌";
				}
				this.showModal1();
			},
			showModal1() {
				this.$refs["my-modalpagado"].show();
			},

			//Funcion para esconder el modal
			hideModal() {
				this.$refs["my-modal"].hide();
			},

			info(numero_socio) {
				alert("id: " + numero_socio);
			},

			showModalinfo(item, index) {
				this.infoEliminar.socio = item;
				this.showModal();
			},

			altaSocio() {},

			async deleteSocio(numero_socio) {
				axios
					.delete("http://localhost:8081/socios/" + numero_socio + "/")
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

			//Funcion para eliminar todos los socios seleccionados
			async delete_all_Socios() {
				var cantidad = this.selected.length;

				try {
					for (var i = 0; i < cantidad; i++) {
						axios.delete(
							"http://localhost:8081/socios/" +
								this.selected[i].numero_socio +
								"/"
						);
						if (this.selected.length == 0) {
							console.log("Eliminacion Exitosa");
							break;
						}
					}
					this.hideModal();
					swal("Eliminacion Exitosa", " ", "success");
					this.testFetch();
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
						this.btn_pagado = true;
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
					this.btn_pagado = false;
				}
			},
			//Selecciona todas
			seleccionar_todas() {
				this.$refs.tablaregistros.selectAllRows();
				this.btn_del_full = false;
				this.btn_mostrar = true;
				this.btn_editar = true;
				this.btn_eliminar = true;
				this.btn_pagado = true;

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
				this.btn_pagado = false;

				this.btn_select = false;
				this.btn_limpiar = true;
			},

			GenerarPagoAfiliacion() {},

			//Funcion para crear el PDF
			async generarCarnet(item) {
				let data_socio = {};
				data_socio.numero_socio = item.numero_socio;
				data_socio.afiliado = item.apellido + ", " + item.nombre;
				data_socio.dni = item.dni;
				data_socio.adhrentes = [];
				for (var i = 0; i < this.data.length; i++) {
					if (
						this.data[i].numero_socio.split("/")[4] == data_socio.numero_socio
					) {
						let data_fam = {};
						data_fam.dni = this.data[i].dni_familiar;
						data_fam.adherente =
							this.data[i].apellido + ", " + this.data[i].nombre;
						data_socio.adhrentes.push(data_fam);
					}
				}
				this.carnetAPDF = data_socio;
				this.$refs.html2Pdf.generatePdf();
			},

			onFiltered(filteredItems) {
				// Trigger pagination to update the number of buttons/pages due to filtering
				this.totalRows = filteredItems.length;
				this.currentPage = 1;
			},
			onShown() {
				// Focus the cancel button when the overlay is showing
				this.$refs.cancel.focus();
			},
			onHidden() {
				// Focus the show button when the overlay is removed
				this.$refs.show.focus();
			},
		},
		beforeMount() {
			//this.show = true;
			this.testFetch();
			//this.testFetch2();
			//this.searchAlDia();
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
