<template>
	<v-app id="app">
		<div id="planes" class="myTable">
			<!--HEAD DE LA PAGINA -->
			<vue-headful
				title="Planes - Federación Tucumana de Mutuales"
			></vue-headful>

			<h2>Listado de Planes</h2>

			<b-button @click="testFetch" class="mb-4" title="Recargar" variant="light">
				<v-icon dark style="color: black">mdi-cached</v-icon>
				Actualizar
			</b-button>
			<!-- ================ALTA PLANES======================== -->
			<b-button
				class="mb-4 ml-2"
				v-b-modal.modal-alta
				@click="altaPlan()"
				title="Nuevo Pago de Plan"
				style="color: white"
			>
				<v-icon dark> mdi-plus </v-icon>
				Nuevo Plan
			</b-button>
			<b-modal id="modal-alta" hide-footer>
				<template #modal-title>
					<h5 class="modal-title">Alta</h5>
				</template>
				<planes-alta :updateTable="testFetch" />
			</b-modal>
			<!-- =========================================================== -->
			
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

			<!-- ================ELIMINAR VARIOS PLANES======================== -->
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
						@click="delete_all_Planes()"
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
					:items="tabla_planes"
					show-empty
					:sticky-header="false"
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
					
					<template slot="cell(precio)" slot-scope="data">
						${{ data.value }}
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
									@click="editarPlan(row.item, row.index)"
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
										><b>Nombre del Plan:</b>
										{{ row.item.nombre }}</b-list-group-item
									>
									<b-list-group-item
										><b>Precio:</b>
										${{ row.item.precio }}</b-list-group-item
									>
                                        <b-card title="Beneficios: " v-if="row.item.beneficios.length>0">
								
                                            <b-list-group horizontal >
                                                <div
                                                    v-for="beneficio in row.item.beneficios"
                                                    :key="beneficio.id"
                                                >
                                                    
                                                        <b-list-group>
                                                            <b-list-group-item>
                                                                <b>Servicio:</b>
                                                                {{servicios.find(s=>{
                                                                    return s.id_servicio == beneficio.servicio.split('/')[4]
                                                                }).servicio}}
                                                            </b-list-group-item>
                                                            <b-list-group-item>
                                                                <b>Tipo:</b>
                                                                {{tipos[beneficio.tipo-1]}}
                                                            </b-list-group-item>
                                                            <b-list-group-item>
                                                                <p>

                                                                <b>Cantidad: </b>
                                                                {{beneficio.tipo==2?"$":""}}{{beneficio.cantidad}}{{beneficio.tipo==1?"%":""}}
                                                                </p>
                                                            </b-list-group-item>
                                                        </b-list-group>
                                                    
                                                </div>
                                            </b-list-group>
                                        </b-card>
                                        <b-list-group-item v-else>
                                            Sin beneficios
                                        </b-list-group-item>

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
							aria-controls="table_planes"
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
					<planes-update :planes="editar" :updateTable="testFetch" />
				</b-modal>
				<!-- ================ELIMINAR UN PLAN======================== -->
				<b-modal
					id="modal_eliminar"
					ref="my-modal"
					hide-footer
					title="Eliminar"
					ok-only
				>
					<div class="d-block text-center">
						<h3>
							¿Esta seguro de eliminar los datos del plan '{{
								infoEliminar.plan.nombre}}'?
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
						@click="deletePlan(infoEliminar.plan.id_plan)"
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
				<!-- <div>
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
				</div> -->
			</aside>
		</div>
	</v-app>
</template>

<script>
	let api = new URL("http://localhost");
	api.pathname = "planes/";
	//api.port = 8000;
	api.port = 8081;

	import PlanesAlta from "./PlanesAlta.vue";
	import PlanesUpdate from "./PlanesUpdate.vue";
	import axios from "axios";

	import { APIControler } from "@/store/APIControler";
	import swal from "sweetalert";

	export default {
		components: { PlanesAlta, PlanesUpdate },
		data() {
			return {
				tabla_planes: [],
                servicios:[],
				fields: [
					{ key: "selected", label: "Seleccionar", sortable: true },
					{ key: "id_plan", label: "ID", sortable: true },
					{ key: "nombre", label: "Nombre", sortable: true },
					{ key: "precio", label: "Precio", sortable: true },
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
					plan: -1,
				},
				btn_del_full: true,
				btn_mostrar: false,
				btn_editar: false,
				btn_eliminar: false,
				btn_select: false,
				btn_limpiar: true,
                tipos:["1-Descuento Porcentual",
                          "2-Descuento Fijo",
                          "3-Limite"],
			};
		},
		computed: {
			rows() {
				return (this.totalRows = this.tabla_planes.length);
			},
			rowsFilter() {
				return this.totalRows;
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
			
			async testFetch() {
				try {
					const res = await fetch(api);
					const data = await res.json();

					this.tabla_planes = data.results;


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
				this.infoEliminar.plan = item;
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

			//Alta de medicamento
			altaPlan() {},

			//Editar medicamento
			editarPlan(item, index) {
				this.editar = item;
			},

            async getServicios() {
				let serviciosAPI = new APIControler();
				serviciosAPI.apiUrl.pathname = "servicios/";
				this.servicios= await serviciosAPI.getData()
                // .then(servicios=>{
                //     let s=[]
                //     for (d in servicios){
                //         {

                //         }
                //         s.push
                //     }
                // })


                // let option
				// this.data.forEach((element) => {
				// 	option = {};
				// 	option.value = 
				// 		"http://localhost:8081/servicios/" + element.id_servicio + "/";
				// 	option.text = element.servicio;
				// 	console.log(option);
				// 	this.op_servicios.push(option);
				// });
			},

            getServicio(id){
                if(this.servicios==[]){
                    return getServicios().then(()=>{
                        return this.getServicio(id)
                    })
                }
                else{
                    return this.servicios.find(s=>{
                        return s.id_servicio == id
                    })
                }
            },
			//Funcion para eliminar el medicamento
			async deletePlan(id) {
				axios
					.delete("http://localhost:8081/planes/" + id + "/")
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
			async delete_all_Planes() {
				var cantidad = this.selected.length;

				try {
					for (var i = 0; i < cantidad; i++) {
						axios.delete(
							"http://localhost:8081/planes/" + this.selected[i].id_plan + "/"
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

		},

		beforeMount() {
			this.testFetch();
            this.getServicios()
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
