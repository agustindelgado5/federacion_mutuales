<template>
	<v-app id="app">
		<div id="mutuales" class="myTable">
			<!--HEAD DE LA PAGINA -->
			<vue-headful
				title="Mutuales - Federación Tucumana de Mutuales"
			></vue-headful>

			<h2>Listado de Mutuales</h2>
			<b-button
				@click="testFetch"
				class="mb-4"
				title="Recargar"
				variant="light"
			>
				<v-icon dark style="color: black">mdi-cached</v-icon>
				Actualizar
			</b-button>

			<!-- ================ALTA MUTUAL======================== -->
			<b-button
				class="mb-4 ml-2"
				v-b-modal.modal-alta
				@click="altaMutual()"
				title="Nueva Mutual"
				style="color: white"
			>
				<v-icon dark> mdi-plus </v-icon>
				Nueva Mutual
			</b-button>
			<b-modal id="modal-alta" hide-footer>
				<template #modal-title><h5 class="modal-title">Alta</h5></template>
				<mutual-alta />
			</b-modal>
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
			<!-- ================ELIMINAR VARIOS MUTUALES======================== -->
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
						@click="delete_all_Mutuales()"
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

			<!-- ======== Tabla con los registros ======= -->

			<section class="container">
				<b-table
					:fields="fields"
					striped
					sortable
					responsive
					:sticky-header="true"
					:no-border-collapse="false"
					hover
					:items="
						tabla_mutuales
							| fecha_inicio_range(
								filter_fechaInicio.desde,
								filter_fechaInicio.hasta
							)
							| fecha_ingreso_range(
								filter_fechaIngreso.desde,
								filter_fechaIngreso.hasta
							)
							| Localidad(
								filter_localidad
							)
							| Sucursal(
								filter_departamento
							)
							| Representante(
								filter_representante
							)
							| Correo(
								filter_correo
							)
					"
					show-empty
					:per-page="perPage"
					:current-page="currentPage"
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

					<template slot="cell(fecha_inicio)" slot-scope="data">
						{{ data.value | FormatStringToDate }}
					</template>

					<template slot="cell(fecha_ingreso)" slot-scope="data">
						{{ data.value | FormatStringToDate }}
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
									@click="editarMutual(row.item, row.index)"
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
						<b-card title="Datos de la Mutual: ">
							<div>
								<b-list-group horizontal>
									<b-list-group class="col-6">
										<b-list-group-item>
											<b>Codigo:</b> {{ row.item.id_mutual }} |
											<b>Matricula:</b> {{ row.item.matricula }} |
											<b>Codigo:</b> {{ row.item.cuit }}
										</b-list-group-item>
										<b-list-group-item>
											<b>Nombre:</b> {{ row.item.nombre }}
										</b-list-group-item>
										<b-list-group-item>
											<b>Direccion:</b> {{ row.item.direccion }}
											<b>Localidad:</b> {{ row.item.localidad }} <b>Filial:</b>
											{{ row.item.sucursal }}
										</b-list-group-item>
									</b-list-group>
								</b-list-group>
								<b-list-group horizontal>
									<b-list-group class="col-6">
										<b-list-group-item>
											<b>Correo:</b> {{ row.item.email }} | <b>Telefono:</b>
											{{ row.item.telefono }}
										</b-list-group-item>
										<b-list-group-item>
											<b>Autoridad:</b> {{ row.item.representante }} |
											<b>Fecha Inicio:</b> {{ row.item.fecha_inicio }} |
											<b>Fecha Ingreso:</b> {{ row.item.fecha_ingreso }}
										</b-list-group-item>
									</b-list-group>
								</b-list-group>
								<b-list-group horizontal>
									<b-list-group class="col-6">
										<b-list-group-item>
											<b>Servicios:</b>
											<div v-for="servicios in data" :key="servicios.id_mutual">
												<div
													v-for="tareas in server_mutual"
													:key="tareas.id_servicio"
												>
													<div
														v-if="
															servicios.id_mutual.split('/')[4] ==
																row.item.id_mutual &&
															servicios.id_servicio.split('/')[4] ==
																tareas.id_servicio
														"
													>
														<ul>
															<li>
																<b>{{ tareas.id_servicio }}:</b>
																{{ tareas.servicio }}
															</li>
														</ul>
													</div>
												</div>
											</div>
										</b-list-group-item>
									</b-list-group>
								</b-list-group>
							</div>
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
							aria-controls="table_mutuales"
						>
						</b-pagination>
					</b-col>
				</b-container>
				<!-- ================MODIFICAR UNA MUTUAL======================== -->
				<b-modal id="modal-editar" hide-footer>
					<template #modal-title
						><h5 class="modal-title">
							Editar: {{ editar.id_mutual }}- {{ editar.nombre }}
						</h5></template
					>

					<mutual-update :mutual="editar" />
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
											LOCALIDAD
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
									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button
											block
											v-b-toggle.accordion-2
											variant="info"
											style="font-size: 0.82em"
										>
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
											v-b-toggle.accordion-3
											variant="info"
											style="font-size: 0.82em"
										>
											REPRESENTANTE
										</b-button>
									</b-card-header>
									<b-collapse
										id="accordion-3"
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
												<div v-show="filter_representante!= null">
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
									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button
											block
											v-b-toggle.accordion-4
											variant="info"
											style="font-size: 0.82em"
										>
											CORREO
										</b-button>
									</b-card-header>
									<b-collapse
										id="accordion-4"
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
								</b-card>
							</div>

							<div class="accordion" role="tablist">
								<b-card no-body>
									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button
											block
											v-b-toggle.accordion-5
											variant="info"
											style="font-size: 0.82em"
										>
											INICIO
										</b-button>
									</b-card-header>
									<b-collapse
										id="accordion-5"
										visible
										accordion="my-accordion"
										role="tabpanel"
										style="color: black"
									>
										<b-card-body>
											<b-form-group id="input-group-4">
												<b-form-group label="Desde" label-for="fecha_inicio_desde">
													<b-form-input
														id="fecha_inicio_desde"
														v-model="filter_fechaInicio.desde"
														type="date"
													></b-form-input>
												</b-form-group>
												<b-form-group label="Hasta" label-for="fecha_inicio_hasta">
													<b-form-input
														id="fecha_inicio_hasta"
														v-model="filter_fechaInicio.hasta"
														type="date"
													></b-form-input>
												</b-form-group>

												<div style="color: black">
													{{ filter_fechaInicio.desde }} <br />
													{{ filter_fechaInicio.hasta }} <br />
												</div>
												<div
													v-show="
														filter_fechaInicio.desde != null &&
														filter_fechaInicio.hasta != null
													"
												>
													<b-button
														@click="limpiar_filtro_fechaInicio()"
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
											v-b-toggle.accordion-6
											variant="info"
											style="font-size: 0.82em"
										>
											INGRESO
										</b-button>
									</b-card-header>
									<b-collapse
										id="accordion-6"
										visible
										accordion="my-accordion"
										role="tabpanel"
										style="color: black"
									>
										<b-card-body>
											<b-form-group id="input-group-4">
												<b-form-group label="Desde" label-for="fecha_ingreso_desde">
													<b-form-input
														id="fecha_ingreso_desde"
														v-model="filter_fechaIngreso.desde"
														type="date"
													></b-form-input>
												</b-form-group>
												<b-form-group label="Hasta" label-for="fecha_ingreso_hasta">
													<b-form-input
														id="fecha_ingreso_hasta"
														v-model="filter_fechaIngreso.hasta"
														type="date"
													></b-form-input>
												</b-form-group>
												<div style="color: black">
													{{ filter_fechaIngreso.desde }} <br />
													{{ filter_fechaIngreso.hasta }} <br />
												</div>
												<div
													v-show="
														filter_fechaIngreso.desde != null &&
														filter_fechaIngreso.hasta != null
													"
												>
													<b-button
														@click="limpiar_filtro_fechaIngreso()"
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
			<!-- ================ELIMINAR MUTUAL======================== -->
			<b-modal
				id="modal_eliminar"
				ref="modal_eliminar"
				hide-footer
				title="Eliminar"
				ok-only
			>
				<div class="d-block text-center">
					<h3>
						¿Esta seguro de eliminar los datos de
						{{ infoEliminar.mutual.nombre }}?
					</h3>
				</div>
				<b-button class="mt-2" block @click="hideModal" title="Volver Atras"
					>Volver Atras</b-button
				>
				<b-button
					class="mt-3"
					variant="danger"
					block
					@click="deleteMutual(infoEliminar.mutual.id_mutual)"
					title="Eliminar"
				>
					Eliminar
				</b-button>
			</b-modal>
		</div>
	</v-app>
</template>

<script>
	let api = new URL("http://localhost");
	api.pathname = "mutuales/";
	//api.port = 8000;
	api.port = 8081;

	import axios from "axios";
	import MutualAlta from "./MutualAlta.vue";
	import { APIControler } from "@/store/APIControler";
	import MutualUpdate from "./MutualUpdate.vue";

	export default {
		components: { MutualAlta, MutualUpdate },

		data() {
			return {
				tabla_mutuales: [],
				fields: [
					{ key: "selected", label: "Seleccionar", sortable: true },
					{ key: "matricula", label: "Matricula", sortable: true },
					{ key: "nombre", label: "Mutual", sortable: true },
					{ key: "direccion", label: "Direccion", sortable: true },
					{ key: "localidad", label: "Localidad", sortable: true },
					{ key: "sucursal", label: "Filial", sortable: true },
					{ key: "cuit", label: "CUIT", sortable: true },
					{ key: "email", label: "Email", sortable: true },
					{ key: "telefono", label: "Telefono", sortable: true },
					{ key: "representante", label: "Autoridad", sortable: true },
					{ key: "fecha_inicio", label: "Fecha Inicio", sortable: true },
					{ key: "fecha_ingreso", label: "Fecha Ingreso", sortable: true },

					{ key: "action", label: "Acciones", variant: "secondary" },
				],
				filter: null,
				pageOptions: [10, 20, 40, 100, { value: 10000, text: "Todos" }],
				totalRows: 1, //Total de filas
				currentPage: 1, //Pagina actual
				perPage: 10, // Datos en la tabla por pagina
				buscar: "",
				infoEliminar: {
					id: "modal_eliminar",
					mutual: -1,
				},
				servicios: {},
				data: {},
				editar: {},

				//Opciones de filtro
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
				options_deptos: [
					{ value: null, text: "Elija un departamento", selected: true },
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
				options_representante: [
					{ value: null, text: "Elija un representante", selected: true },
				],
				options_correo: [
					{ value: null, text: "Elija un correo", selected: true },
				],
				selected: [],
				//Botones
				btn_down_pdf: true, //Desabilito los botones, hasta que muestre los datos
				btn_del_full: true,
				msj_tabla: " Presione 'Mostrar' para ver los regitros ",
				btn_mostrar: false,
				btn_editar: false,
				btn_eliminar: false,
				btn_select: false,
				btn_limpiar: true,
				
				//Campos a filtrar
				filter_correo : null,
				filter_localidad : null,
				filter_departamento: null,
				filter_representante: null,
				filter_fechaInicio: {
					desde: null,
					hasta: null,
				},

				filter_fechaIngreso: {
					desde: null,
					hasta: null,
				},

				server_mutual: [
					//{
					//id_servicio:0,
					//servicio:''
					// }
				],
			};
		},
		computed: {
			max() {
				var id = this.rows - 1;
				return this.tabla_mutuales[id].id_mutual;
			},
			rows() {
				return (this.totalRows = this.tabla_mutuales.length);
			},
			rowsFilter() {
				return this.totalRows;
			},
			id() {
				return this.tabla_mutuales.id_mutual;
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

					var lista_mutuales = data.results;

					console.log(lista_mutuales);

					this.tabla_mutuales = lista_mutuales;

					this.tabla_mutuales.forEach((element) => {
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
			//Funcion para mostrar el modal
			showModal() {
				this.$refs["modal_eliminar"].show();
			},

			showModalinfo(item, index) {
				console.log("Mostrando info eliminar");
				console.log(this.infoEliminar);
				this.infoEliminar.mutual = item;
				this.showModal();
			},

			//Funcion para esconder el modal
			hideModal() {
				this.$refs["modal_eliminar"].hide();
			},
			altaMutual() {},

			//Editar medicamento
			editarMutual(item, index) {
				this.editar = item;
			},
			//Elimina una mutual
			async deleteMutual(id_mutual) {
				axios
					.delete("http://localhost:8081/mutuales/" + id_mutual + "/")
					.then((datos) => {
						swal("Operación Exitosa", " ", "success");
						console.log(datos);
						this.hideModal();
					})
					.catch((error) => {
						swal("¡ERROR!", "Se ha detectado un problema ", "error");
						console.log(error);
					})
					.finally(() => this.testFetch());
			},
			//Elimina todas las mutuales
			async delete_all_Mutuales() {
				var cantidad = this.selected.length;

				try {
					for (var i = 0; i < cantidad; i++) {
						axios.delete(
							"http://localhost:8081/mutuales/" +
								this.selected[i].id_mutual +
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

			//Funcion de busqueda
			onFiltered(filteredItems) {
				// Trigger pagination to update the number of buttons/pages due to filtering
				this.totalRows = filteredItems.length;
				this.currentPage = 1;
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

			limpiar_filtro_fechaInicio() {
				this.filter_fechaInicio.desde = null;
				this.filter_fechaInicio.hasta = null;
			},

			limpiar_filtro_fechaIngreso() {
				this.filter_fechaIngreso.desde = null;
				this.filter_fechaIngreso.hasta = null;
			},

			async getServicios() {
				var count = 0;
				let serviciosAPI = new APIControler();
				serviciosAPI.apiUrl.pathname = "servicio_mutual/";
				this.data = await serviciosAPI.getData(this.servicios);
				this.data.forEach((element) => {
					console.log(element);
					this.getPublic(element.id_servicio);
				});
			},

			async getPublic(id) {
				//let url = 'http://localhost:8081/'+ id + '/'

				axios
					.get(id)
					.then((response) => {
						console.log(response);
						this.server_mutual.push(response.data);
						//this.server_mutual[count].id_servicio=response.data.id_servicio
						//this.server_mutual[count].servicio=response.data.servicio
					})
					.catch((error) => {
						console.log(error);
					});
			},
		},
		beforeMount() {
			this.testFetch();
			this.getServicios();
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
