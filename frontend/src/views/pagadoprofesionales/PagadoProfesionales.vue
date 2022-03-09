<template>
	<v-app id="app">
		<div id="pagadoProfesionales" class="myTable">
			<vue-headful
				title="Pagado a Profesionales - Federación Tucumana de Mutuales"
			></vue-headful>

			<h2>Listado de Pagado a Profesionales</h2>
			<b-button
				@click="testFetch"
				class="mb-4"
				title="Recargar"
				variant="light"
			>
				<v-icon dark style="color: black">mdi-cached</v-icon>
				Actualizar
			</b-button>

			<!-- ================ALTA GASTO SALIENTE======================== -->
			<b-button
				class="mb-4 ml-2"
				v-b-modal.modal-alta
				@click="altaPagadoProfesional()"
				title="Nuevo Pago"
				style="color: white"
			>
				<v-icon dark> mdi-plus </v-icon>
				Nuevo Pago Saliente
			</b-button>
			<b-modal id="modal-alta" hide-footer>
				<template #modal-title><h5 class="modal-title">Alta</h5></template>
				<pagadoProfesionales-alta :updateTable="testFetch" />
			</b-modal>

			<!-- ================ELIMINAR VARIOS GASTOS======================== -->
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
						@click="delete_all_Pagos()"
					>
						Eliminar
					</b-button>
				</b-modal>
			</div>
			<!-- ======================================== -->
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
						tabla_pagadoProfesionales
							| FechaRange(filter_fechaPago.desde, filter_fechaPago.hasta)
							| ModoPago(filter_modoPago)
							| PeriodoRange(
								filter_periodo.split('-')[1],
								filter_periodo.split('-')[0]
							)
					"
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

					<template slot="cell(total)" slot-scope="data">
						<b>${{ data.value }}</b>
					</template>

					<template slot="cell(fecha)" slot-scope="data">
						{{ data.value | Date }}
					</template>
					<template slot="cell(periodo)" slot-scope="data">
						{{
							"Mes:" +
							data.value.split("-")[1] +
							" Año:" +
							data.value.split("-")[0]
						}}
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
									@click="editarPagadoProfesional(row.item, row.index)"
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
						<b-card title="Datos del pago profesional: ">
							<div>
								<b-list-group horizontal>
									<b-list-group class="col-3">
										<b-list-group-item
											><b>Id pago:</b>
											{{ row.item.id_pagoprofesional }}</b-list-group-item
										>
										<b-list-group-item>
											<b>Id Medico:</b>
											{{ row.item.medico }}
										</b-list-group-item>
										<b-list-group-item>
											<b>Total:</b>
											{{ row.item.total }}
										</b-list-group-item>
										<b-list-group-item
											><b>Fecha:</b> {{ row.item.fecha }}</b-list-group-item
										>
										<b-list-group-item
											><b>Modo de pago:</b>
											{{ row.item.modo_pago }}</b-list-group-item
										>
										<b-list-group-item
											><b>Mes pagado:</b>
											{{ row.item.periodo }}</b-list-group-item
										>
									</b-list-group>
									&nbsp;
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
							:total-rows="rows"
							:per-page="perPage"
							aria-controls="table_pagadoProfesionales"
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
											REALIZACION
										</b-button>
									</b-card-header>
									<b-collapse
										id="accordion-filter-1"
										visible
										accordion="my-accordion"
										role="tabpanel"
										style="color: black"
									>
										<b-card-body>
											<b-form-group id="input-group-4">
												<b-form-group
													label="Desde"
													label-for="fecha_inicio_desde"
												>
													<b-form-input
														id="fecha_inicio_desde"
														v-model="filter_fechaPago.desde"
														type="date"
													></b-form-input>
												</b-form-group>
												<b-form-group
													label="Hasta"
													label-for="fecha_inicio_hasta"
												>
													<b-form-input
														id="fecha_inicio_hasta"
														v-model="filter_fechaPago.hasta"
														type="date"
													></b-form-input>
												</b-form-group>

												<div style="color: black">
													{{ filter_fechaPago.desde }} <br />
													{{ filter_fechaPago.hasta }} <br />
												</div>
												<div
													v-show="
														filter_fechaPago.desde != null &&
														filter_fechaPago.hasta != null
													"
												>
													<b-button
														@click="limpiar_filtro_fechaPago()"
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
											MODO DE PAGO
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
													v-model="filter_modoPago"
													:items="opcion_modoPago"
													type="text"
													solo
													filled
												></v-autocomplete>
												<div v-show="filter_modoPago != null">
													<b-button
														@click="filter_modoPago = null"
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
			<div v-show="rows > 0">
				<b-card-group deck>
					<b-card
						text-variant="black"
						header="FILTRAR POR PERIODO"
						class="text-center"
					>
						<b-form-group id="input-group-4">
							<month-picker-input
								@change="FilterPeriodo"
								id="periodo"
								:default-month="new Date().getMonth() + 1"
								:lang="'es'"
								required
							>
							</month-picker-input>
							<br>
							<!--
							<div style="color: black">{{ filter_periodo }} <br /></div>
							-->
							<div v-show="filter_periodo != ''">
								<b-button @click="filter_periodo = ''" title="Limpiar">
									Limpiar
								</b-button>
							</div>
						</b-form-group>
					</b-card>
				</b-card-group>
			</div>

			<!-- ================ELIMINAR GASTO SALIENTE======================== -->

			<b-modal
				id="modal_eliminar"
				ref="my-modal"
				hide-footer
				title="Eliminar"
				ok-only
			>
				<div class="d-block text-center">
					<h3>
						¿Esta seguro de eliminar los datos del pago al medico
						{{ infoEliminar.pagadoProfesional.id_medico }} - Fecha
						{{ infoEliminar.pagadoProfesional.fecha }}?
					</h3>
				</div>
				<b-button class="mt-2" block @click="hideModal" title="Volver Atras"
					>Volver Atras</b-button
				>
				<b-button
					class="mt-3"
					variant="danger"
					block
					@click="
						deletePagadoProfesional(
							infoEliminar.pagadoProfesional.id_pagoprofesional
						)
					"
					title="Eliminar"
				>
					Eliminar
				</b-button>
			</b-modal>

			<b-modal id="modal-editar" hide-footer>
				<template #modal-title><h5 class="modal-title">Editar</h5></template>
				<pagadoProfesionales-update
					:pagadoProfesional="editar"
					:updateTable="testFetch"
				/>
			</b-modal>
		</div>
	</v-app>
</template>

<script>
	let api = new URL("http://localhost");
	api.pathname = "pagadoprofesionales";
	api.port = 8081;

	import PagadoProfesionalesAlta from "./PagadoProfesionalesAlta.vue";
	import PagadoProfesionalesUpdate from "./PagadoProfesionalesUpdate.vue";
	import { APIControler } from "@/store/APIControler";
	import axios from "axios";
	import _ from "lodash";
	import { mapState, mapActions } from "vuex";
	import { MonthPickerInput } from "vue-month-picker";
	export default {
		components: {
			PagadoProfesionalesAlta,
			PagadoProfesionalesUpdate,
			MonthPickerInput,
		},
		data() {
			return {
				tabla_pagadoProfesionales: [],
				fields: [
					{ key: "selected", label: "Seleccionar", sortable: true },
					{
						key: "id_pagoprofesional",
						label: "Id Pago Profesional",
						sortable: true,
					},
					{ key: "medico", label: "Id Medico", sortable: true },
					{ key: "total", label: "Total", sortable: true },
					{ key: "fecha", label: "Fecha", sortable: true },
					{ key: "modo_pago", label: "Modo de pago", sortable: true },
					{ key: "periodo", label: "Mes Pagado", sortable: true },
					{ key: "action", label: "Acciones", variant: "secondary" },
				],
				selected: [],
				filter: null,
				pageOptions: [10, 20, 40, 100, { value: 10000, text: "Todos" }],
				totalRows: 1, //Total de filas
				currentPage: 1, //Pagina actual
				perPage: 10, // Datos en la tabla por pagina
				buscar: "",
				editar: {},
				infoEliminar: {
					id: "modal_eliminar",
					pagadoProfesional: -1,
				},
				btn_down_pdf: true, //Desabilito los botones, hasta que muestre los datos
				btn_del_full: true,
				msj_tabla: " Presione 'Mostrar' para ver los regitros ",
				btn_mostrar: false,
				btn_editar: false,
				btn_eliminar: false,
				btn_select: false,
				btn_limpiar: true,

				//Opciones para filtar
				opcion_modoPago: [
					{
						value: null,
						text: "Elija un modo de pago",
						selected: true,
					},
					{ value: "Efectivo", text: "1- Efectivo" },
					{ value: "CBU", text: "2- CBU" },
					{ value: "Tarjeta de Debito", text: "3- Tarjeta de Debito" },
					{ value: "Tarjeta de Credito", text: "4- Tarjeta de Credito" },
				],

				//Campos a filtrar
				filter_fechaPago: {
					desde: null,
					hasta: null,
				},
				filter_modoPago: null,
				filter_periodo: "",
			};
		},
		computed: {
			...mapState("PagosProf", ["pagos"]),

			rows() {
				return (this.totalRows = this.tabla_pagadoProfesionales.length);
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

					var lista_pagadoProfesionales = data.results;

					console.log(lista_pagadoProfesionales);

					//this.tabla_pagadoProfesionales = lista_pagadoProfesionales;
					this.tabla_pagadoProfesionales = await this.getProfesional(
						lista_pagadoProfesionales
					);
				} catch (error) {
					console.log(error);
				}
			},

			async getProfesional(lista_pagadoProfesionales) {
				let listado = {};
				let DataReturn = [];
				let profesionalAPI = new APIControler();
				profesionalAPI.apiUrl.pathname = "profesionales/";
				let profesionales = await profesionalAPI.getData(listado);
				console.log("DATA LOS PROFESIONALES: ", profesionales);

				profesionales.forEach((element) => {
					var IdMedico =
						"http://localhost:8081/profesionales/" + element.id_medico + "/";
					lista_pagadoProfesionales.forEach((pago) => {
						if (IdMedico == pago.id_medico) {
							let datos = {};
							datos.id_pagoprofesional = pago.id_pagoprofesional;
							datos.medico =
								element.id_medico +
								"- " +
								element.apellido +
								", " +
								element.nombre;

							datos.total = pago.total;
							datos.fecha = pago.fecha;
							datos.periodo = pago.periodo;
							datos.modo_pago = pago.modo_pago;

							DataReturn.push(datos);
						}
					});
				});
				console.log("DATOS! :", DataReturn);
				return DataReturn;
			},
			editarPagadoProfesional(item, index) {
				this.editar = item;
			},
			//Funcion para mostrar el modal
			showModal() {
				this.$refs["my-modal"].show();
			},
			showModalinfo(item, index) {
				this.infoEliminar.pagadoProfesional = item;
				this.showModal();
			},
			//Funcion para esconder el modal
			hideModal() {
				this.$refs["my-modal"].hide();
			},
			altaPagadoProfesional() {},

			//Elimino un gasto
			async deletePagadoProfesional(id_pagoprofesional) {
				axios
					.delete(
						"http://localhost:8081/pagadoprofesionales/" +
							id_pagoprofesional +
							"/"
					)
					.then((datos) => {
						swal("Operación Exitosa", " ", "success");
						console.log(datos);
						this.hideModal();
						sessionStorage.removeItem("pagos");
					})
					.catch((error) => {
						swal("¡ERROR!", "Se ha detectado un problema ", "error");
						console.log(error);
						this.hideModal();
					})
					.finally(() => this.testFetch());
			},

			//Elimina todas los gastos
			async delete_all_Pagos() {
				var cantidad = this.selected.length;

				try {
					for (var i = 0; i < cantidad; i++) {
						axios.delete(
							"http://localhost:8081/pagadoprofesionales/" +
								this.selected[i].id_pagoprofesional +
								"/"
						);
						sessionStorage.removeItem("pagos");
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
			limpiar_filtro_fechaPago() {
				this.filter_fechaPago.desde = null;
				this.filter_fechaPago.hasta = null;
			},
			FilterPeriodo(date) {
				this.filter_periodo = date.from.toLocaleDateString("en-CA");
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
