<template>
	<v-app id="app">
		<div id="vendedores" class="myTable">
			<!--HEAD DE LA PAGINA -->
			<vue-headful
				title="Vendedores - Federación Tucumana de Mutuales"
			></vue-headful>

			<h2>Listado de Vendedores</h2>
			<b-button
				@click="testFetch"
				class="mb-4"
				title="Recargar"
				variant="light"
			>
				<v-icon dark style="color: black">mdi-cached</v-icon>
				Actualizar
			</b-button>

			<!-- ================ALTA COBRADORES======================== -->
			<b-button
				class="mb-4 ml-2"
				v-b-modal.modal-alta
				@click="altaVendedor()"
				title="Nuevo Vendedor"
				style="color: white"
			>
				<v-icon dark> mdi-plus </v-icon>
				Nuevo Vendedor
			</b-button>
			<b-modal id="modal-alta" hide-footer>
				<template #modal-title><h5 class="modal-title">Alta</h5></template>
				<vendedores-alta :updateTable="testFetch" />
			</b-modal>

			<!-- ================ELIMINAR VARIAS COBRADORES======================== -->
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
						@click="delete_all_Vendedores()"
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
					:items="
						tabla_vendedores
							| Localidad(filter_localidad)
							| Departamento(filter_departamento)
					"
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
					<template #empty="">
						<b>No hay registros para mostrar</b>
					</template>

					<template slot="cell(apellido)" slot-scope="data">
						{{ data.value.toUpperCase() }}
					</template>

					<template slot="cell(nombre)" slot-scope="data">
						{{ data.value.toUpperCase() }}
					</template>

					<template slot="cell(id_vendedor)" slot-scope="data">
						<b>{{ data.value }}</b>
					</template>

					<template slot="cell(fecha_nacimiento)" slot-scope="data">
						{{ data.value | Date }}
					</template>

					<template #cell(selected)="{ rowSelected }">
						<template v-if="rowSelected">
							<span aria-hidden="true">&check;</span>
							<span class="sr-only">Selected</span>
						</template>
						<!--
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
					-->
					</template>

					<template slot="cell(action)" slot-scope="row">
						<div class="mt-3">
							<b-button-group>
								<b-button
									variant="info"
									id="button-1"
									title="Mostrar Info"
									@click="row.toggleDetails"
								>
									{{ row.detailsShowing ? "Ocultar" : "Mostrar" }} detalles
								</b-button>
								<b-button
									:to="{
										name: 'vendedor',
										params: { id: row.item },
										query: { id: row.item.id_vendedor },
									}"
									variant="primary"
									id="button-4"
									title="Ver socios del vendedor"
									style="color: white"
								>
									<v-icon dark>mdi-format-list-bulleted-square</v-icon>
									Socios
								</b-button>
								<b-button
									variant="warning"
									id="button-2"
									title="Editar este registro"
									v-b-modal.modal-editar
									@click="editarVendedor(row.item, row.index)"
								>
									<v-icon class="mr-2"> mdi-pencil </v-icon>
									Editar
								</b-button>

								<b-button
									variant="danger"
									id="button-3"
									@click="showModalinfo(row.item, row.index)"
									title="Eliminar este registro"
								>
									<v-icon class="mr-2"> mdi-delete </v-icon>
									Eliminar
								</b-button>
							</b-button-group>
						</div>
					</template>
					<template #row-details="row">
						<b-card title="Datos del vendedor: ">
							<div>
								<b-list-group horizontal>
									<b-list-group class="col-3">
										<b-list-group-item
											><b>ID:</b> {{ row.item.id_vendedor }}</b-list-group-item
										>
										<b-list-group-item
											><b>DNI:</b> {{ row.item.dni }}
										</b-list-group-item>
									</b-list-group>
									&nbsp;
									<b-list-group class="col-5">
										<b-list-group-item
											><b>Apellido:</b>
											{{ row.item.apellido }}</b-list-group-item
										>
										<b-list-group-item
											><b>Nombre:</b> {{ row.item.nombre }}</b-list-group-item
										>
									</b-list-group>
								</b-list-group>
							</div>
						</b-card>
					</template>
				</b-table>
				<!-- ================ELIMINAR COBRADOR======================== -->

				<b-modal
					id="modal_eliminar"
					ref="my-modal"
					hide-footer
					title="Eliminar"
					ok-only
				>
					<div class="d-block text-center">
						<h3>
							¿Esta seguro de eliminar los datos del vendedor
							{{ infoEliminar.vendedor.id_vendedor }}?
						</h3>
					</div>
					<b-button class="mt-2" block @click="hideModal" title="Volver Atras"
						>Volver Atras</b-button
					>
					<b-button
						class="mt-3"
						variant="danger"
						block
						@click="deleteVendedor(infoEliminar.vendedor.id_vendedor)"
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
							aria-controls="table_vendedores"
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
											DEPARTAMENTO
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
													id="departamento"
													v-model="filter_departamento"
													:items="options_deptos"
													type="text"
													solo
													filled
												></v-autocomplete>
												<div v-show="filter_departamento != null">
													<b-button
														@click="filter_departamento = null"
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
											v-b-toggle.accordion-filter-2
											variant="info"
											style="font-size: 0.82em"
										>
											LOCALIDAD
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
													id="localidad"
													v-model="filter_localidad"
													:items="op_localidad"
													type="text"
													solo
													filled
												></v-autocomplete>
												<div v-show="filter_localidad != null">
													<b-button
														@click="filter_localidad = null"
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
				<vendedores-update :vendedor="editar" :updateTable="testFetch" />
			</b-modal>

			<!-- ==================================CREAR PDF================================== -->
			<vue-html2pdf
				:show-layout="false"
				:float-layout="true"
				:enable-download="false"
				:preview-modal="true"
				:paginate-elements-by-height="1400"
				filename="DetalleVendedor"
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
						<h3>Vendedor</h3>

						<b-list-group>
							<b-list-group-item
								v-for="value in fields.slice(0, -1)"
								:key="value.key"
								>{{ value.label }}:
								{{ vendedorAPDF[value.key] }}</b-list-group-item
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
	api.pathname = "vendedores/";
	//api.port = 8000;
	api.port = 8081;

	import VendedoresAlta from "../vendedores/VendedoresAlta.vue";
	import VendedoresUpdate from "../vendedores/VendedoresUpdate.vue";
	import VueHtml2pdf from "vue-html2pdf";
	import axios from "axios";

	export default {
		components: { VendedoresAlta, VendedoresUpdate, VueHtml2pdf },
		data() {
			return {
				tabla_vendedores: [],
				fields: [
					{ key: "selected", label: "Seleccionar", sortable: true },
					{ key: "id_vendedor", label: "ID Vendedor", sortable: true },
					{ key: "apellido", label: "Apellido", sortable: true },
					{ key: "nombre", label: "Nombre", sortable: true },
					{ key: "dni", label: "DNI", sortable: true },
					{
						key: "fecha_nacimiento",
						label: "Fecha Nacimiento",
						sortable: true,
					},
					{ key: "calle", label: "Calle", sortable: true },
					{ key: "localidad", label: "Localidad", sortable: true },
					{ key: "departamento", label: "Departamento", sortable: true },
					{ key: "cod_postal", label: "Codigo Postal", sortable: true },
					{ key: "tel_fijo", label: "Telefono Fijo", sortable: true },
					{ key: "tel_celular", label: "Telefono Celular", sortable: true },
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
					vendedor: -1,
				},
				selected: [],
				//Botones
				btn_down_pdf: false, //Desabilito los botones, hasta que muestre los datos
				btn_del_full: true,
				btn_limpiar: true,
				msj_tabla: " Presione 'Mostrar' para ver los regitros ",
				btn_mostrar: false,
				btn_editar: false,
				btn_vendedores: false,
				btn_eliminar: false,
				btn_select: false,
				//Campos a filtrar
				filter_localidad: null,
				filter_departamento: null,

				//Opciones de filtrado
				options_deptos: [
					{
						value: null,
						text: "Elija un departamento",
						selected: true,
					},
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
				op_localidad: [
					{ value: null, text: "Elija una localidad" },
					{ value: "Acheral", text: " 1 - Acheral " },
					{
						value: "Agua Dulce y La Soledad",
						text: "2 - Agua Dulce y La Soledad",
					},
					{ value: "Aguilares", text: " 3 - Aguilares " },
					{ value: "Alderetes", text: " 4 - Alderetes " },
					{
						value: "Alpachiri y El Molino",
						text: " 5 - Alpachiri y El Molino ",
					},
					{
						value: "Alto Verde y Los Gucheas",
						text: " 6 - Alto Verde y Los Gucheas ",
					},
					{ value: "Amaichá del Valle", text: " 7 - Amaichá del Valle " },
					{ value: "Amberes", text: " 8 - Amberes " },
					{ value: "Anca Juli", text: " 9 - Anca Juli " },
					{ value: "Arcadia", text: " 10 - Arcadia " },
					{ value: "Atahona", text: " 11 - Atahona " },
					{ value: "Banda del Río Salí", text: " 12 - Banda del Río Salí " },
					{ value: "Bella Vista", text: " 13 - Bella Vista " },
					{ value: "Buena Vista", text: " 14 - Buena Vista " },
					{ value: "Burruyacú", text: " 15 - Burruyacú " },
					{ value: "Capitán Cáceres", text: " 16 - Capitán Cáceres " },
					{ value: "Cevil Redondo", text: " 17 - Cevil Redondo " },
					{ value: "Choromoro", text: " 18 - Choromoro " },
					{ value: "Ciudacita", text: " 19 - Ciudacita " },
					{ value: "Colalao del Valle", text: " 20 - Colalao del Valle " },
					{ value: "Colombres", text: " 21 - Colombres " },
					{ value: "Concepción", text: " 22 - Concepción " },
					{
						value: "Delfín Gallo (Ex Ingenio Esperanza)",
						text: " 23 - Delfín Gallo (Ex Ingenio Esperanza) ",
					},
					{
						value: "El Bracho y El Cevilar",
						text: " 24 - El Bracho y El Cevilar ",
					},
					{ value: "El Cadillal", text: " 25 - El Cadillal " },
					{ value: "El Cercado", text: " 26 - El Cercado " },
					{ value: "El Chañar", text: " 27 - El Chañar " },
					{ value: "El Manantial", text: " 28 - El Manantial " },
					{ value: "El Mojón", text: " 29 - El Mojón " },
					{ value: "El Mollar", text: " 30 - El Mollar " },
					{ value: "El Naranjito", text: " 31 - El Naranjito " },
					{
						value: "El Naranjo y El Sunchal",
						text: " 32 - El Naranjo y El Sunchal ",
					},
					{ value: "El Polear", text: " 33 - El Polear " },
					{ value: "El Puestito", text: " 34 - El Puestito " },
					{ value: "El Sacrificio", text: " 35 - El Sacrificio " },
					{ value: "El Timbó", text: " 36 - El Timbó " },
					{ value: "Escaba", text: " 37 - Escaba " },
					{ value: "Esquina y Mancopa", text: " 38 - Esquina y Mancopa " },
					{
						value: "Estación Araox y Tacanas",
						text: " 39 - Estación Araox y Tacanas ",
					},
					{ value: "Famaillá", text: " 40 - Famaillá " },
					{ value: "Gastona y Belicha", text: " 41 - Gastona y Belicha " },
					{
						value: "Gobernador Garmendia",
						text: " 42 - Gobernador Garmendia ",
					},
					{
						value: "Gobernador Piedrabuena",
						text: " 43 - Gobernador Piedrabuena ",
					},
					{ value: "Graneros", text: " 44 - Graneros " },
					{ value: "Huasa Pampa", text: " 45 - Huasa Pampa " },
					{
						value: "Juan Bautista Alberdi",
						text: " 46 - Juan Bautista Alberdi ",
					},
					{ value: "La Cocha", text: " 47 - La Cocha " },
					{ value: "La Esperanza", text: " 48 - La Esperanza " },
					{
						value: "La Florida y Luisiana",
						text: " 49 - La Florida y Luisiana ",
					},
					{
						value: "La Ramada y La Cruz",
						text: " 50 - La Ramada y La Cruz ",
					},
					{ value: "La Trinidad", text: " 51 - La Trinidad " },
					{ value: "Lamadrid", text: " 52 - Lamadrid " },
					{ value: "Las Cejas", text: " 53 - Las Cejas " },
					{ value: "Las Talas", text: " 54 - Las Talas " },
					{ value: "Las Talitas", text: " 55 - Las Talitas " },
					{
						value: "Los Bulacio y Los Villagra",
						text: " 56 - Los Bulacio y Los Villagra ",
					},
					{ value: "Los Gómez", text: " 57 - Los Gómez " },
					{ value: "Los Nogales", text: " 58 - Los Nogales " },
					{ value: "Los Pereyra", text: " 59 - Los Pereyra " },
					{ value: "Los Puestos", text: " 60 - Los Puestos " },
					{ value: "Los Pérez", text: " 61 - Los Pérez " },
					{ value: "Los Ralos", text: " 62 - Los Ralos " },
					{
						value: "Los Sarmientos y La Tipa",
						text: " 63 - Los Sarmientos y La Tipa ",
					},
					{ value: "Los Sosas", text: " 64 - Los Sosas " },
					{ value: "Lules", text: " 65 - Lules " },
					{
						value: "Manuel García Fernández",
						text: " 66 - Manuel García Fernández ",
					},
					{ value: "Manuela Pedraza", text: " 67 - Manuela Pedraza " },
					{ value: "Medinas", text: " 68 - Medinas " },
					{ value: "Monte Bello", text: " 69 - Monte Bello " },
					{ value: "Monteagudo", text: " 70 - Monteagudo " },
					{ value: "Monteros", text: " 71 - Monteros " },
					{ value: "Padre Monti", text: " 72 - Padre Monti " },
					{ value: "Pampa Mayo", text: " 73 - Pampa Mayo " },
					{
						value: "Quilmes y Los Sueldos",
						text: " 74 - Quilmes y Los Sueldos ",
					},
					{ value: "Raco", text: " 75 - Raco " },
					{
						value: "Ranchillos y San Miguel",
						text: " 76 - Ranchillos y San Miguel ",
					},
					{ value: "Rumi Punco", text: " 77 - Rumi Punco " },
					{
						value: "Río Chico y Nueva Trinidad",
						text: " 78 - Río Chico y Nueva Trinidad ",
					},
					{ value: "Río Colorado", text: " 79 - Río Colorado " },
					{ value: "Río Seco", text: " 80 - Río Seco " },
					{ value: "San Andrés", text: " 81 - San Andrés " },
					{
						value: "San Felipe y Santa Bárbara",
						text: " 82 - San Felipe y Santa Bárbara ",
					},
					{ value: "San Ignacio", text: " 83 - San Ignacio " },
					{ value: "San Javier", text: " 84 - San Javier " },
					{
						value: "San José de la Cocha",
						text: " 85 - San José de la Cocha ",
					},
					{
						value: "San Miguel de Tucumán",
						text: " 86 - San Miguel de Tucumán ",
					},
					{
						value: "San Pablo y Villa Nougués",
						text: " 87 - San Pablo y Villa Nougués ",
					},
					{
						value: "San Pedro de Colalao",
						text: " 88 - San Pedro de Colalao ",
					},
					{
						value: "San Pedro y San Antonio",
						text: " 89 - San Pedro y San Antonio ",
					},
					{ value: "Santa Ana", text: " 90 - Santa Ana " },
					{
						value: "Santa Cruz y La Tuna",
						text: " 91 - Santa Cruz y La Tuna ",
					},
					{ value: "Santa Lucía", text: " 92 - Santa Lucía " },
					{
						value: "Santa Rosa de Leales",
						text: " 93 - Santa Rosa de Leales ",
					},
					{
						value: "Santa Rosa y Los Rojo",
						text: " 94 - Santa Rosa y Los Rojo ",
					},
					{ value: "Sargento Moya", text: " 95 - Sargento Moya " },
					{ value: "Siete de Abril", text: " 96 - Siete de Abril " },
					{ value: "Simoca", text: " 97 - Simoca " },
					{ value: "Soldado Maldonado", text: " 98 - Soldado Maldonado " },
					{ value: "Taco Ralo", text: " 99 - Taco Ralo " },
					{ value: "Tafí Viejo", text: " 100 - Tafí Viejo " },
					{ value: "Tafí del Valle", text: " 101 - Tafí del Valle " },
					{ value: "Tapia", text: " 102 - Tapia " },
					{ value: "Teniente Berdina", text: " 103 - Teniente Berdina " },
					{ value: "Trancas", text: " 104 - Trancas " },
					{ value: "Villa Belgrano", text: " 105 - Villa Belgrano " },
					{
						value: "Villa Benjamín Araoz",
						text: " 106 - Villa Benjamín Araoz ",
					},
					{ value: "Villa Chigligasta", text: " 107 - Villa Chigligasta " },
					{ value: "Villa Quinteros", text: " 108 - Villa Quinteros " },
					{ value: "Villa de Leales", text: " 109 - Villa de Leales " },
					{ value: "Yerba Buena", text: " 110 - Yerba Buena " },
					{ value: "Yánima", text: " 111 - Yánima " },
				],

				vendedorAPDF: {}, //Se carga cuando se hace clic en exportar a pdf, con el vendedor a exportar
			};
		},
		computed: {
			rows() {
				return (this.totalRows = this.tabla_vendedores.length);
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

					var lista_vendedores = data.results;

					console.log(lista_vendedores);

					this.tabla_vendedores = lista_vendedores;
				} catch (error) {
					console.log(error);
				}
			},
			editarVendedor(item, index) {
				this.editar = item;
			},
			//Funcion para mostrar el modal
			showModal() {
				this.$refs["my-modal"].show();
			},
			showModalinfo(item, index) {
				this.infoEliminar.vendedor = item;
				this.showModal();
			},
			//Funcion para esconder el modal
			hideModal() {
				this.$refs["my-modal"].hide();
			},
			altaVendedor() {},

			//Elimino un vendedor
			async deleteVendedor(id_vendedor) {
				axios
					.delete("http://localhost:8081/vendedores/" + id_vendedor + "/")
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
			async delete_all_Vendedores() {
				var cantidad = this.selected.length;

				try {
					for (var i = 0; i < cantidad; i++) {
						axios.delete(
							"http://localhost:8081/vendedores/" +
								this.selected[i].id_vendedor +
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
				let resultSocio = (await axios.get(item.numero_socio)).data;

				this.vendedorAPDF = { ...item };

				this.vendedorAPDF.numero_socio =
					resultSocio.apellido + ", " + resultSocio.nombre;

				this.$refs.html2Pdf.generatePdf();
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
