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
					<div v-if="rows!=rowsFilter">
						<pre>Registros Fitrados: {{rowsFilter}} | Filas seleccionadas: {{ selected.length }}</pre>

					</div>
					<div v-else>
						<pre>Cantidad de registros: {{ rows }} | Filas seleccionadas: {{ selected.length }}</pre>
					</div>		
				</div>
				<div v-else>
					<div v-if="rows!=rowsFilter">
						<pre>Registros Fitrados: {{rowsFilter}} </pre>
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
					:items="tabla_mutuales"
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
											<b>Codigo:</b> {{ row.item.id_mutual }}
										</b-list-group-item>
										<b-list-group-item>
											<b>Nombre:</b> {{ row.item.nombre }}
										</b-list-group-item>
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
			<aside>
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
										<b-button block v-b-toggle.accordion-1 variant="info" style="font-size: 0.82em">
											DEPARTAMENTO
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
												<!--
											<b-form-select
												id="departamento"
												v-model="filter"
												type="text"
												taggable
												:options="options_deptos"
											>
											</b-form-select>
											-->
												<v-autocomplete
													id="departamento"
													v-model="filter"
													:items="options_deptos"
													type="text"
													solo
													filled
												></v-autocomplete>
												<div v-show="filter !=null">
  													<b-button 
													  :disabled="!filter" 
													  @click="filter = null"
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
	api.pathname = "mutuales";
	//api.port = 8000;
	api.port = 8081;

	import VueAwesomplete from "vue-awesomplete";
	import axios from "axios";
	import MutualAlta from "./MutualAlta.vue";
	import { APIControler } from "../store/APIControler";
	import MutualUpdate from "./MutualUpdate.vue";

	export default {
		components: { MutualAlta, MutualUpdate },

		data() {
			return {
				tabla_mutuales: [],
				fields: [
					{ key: "selected", label: "Seleccionar", sortable: true },
					{ key: "nombre", label: "Mutual", sortable: true },
					{ key: "direccion", label: "Direccion", sortable: true },
					{ key: "sucursal", label: "Filial", sortable: true },
					{ key: "action", label: "Acciones", variant: "secondary" },
				],
				filter: null,
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
				options_deptos: [
					{ value: null, text: "Elija un departamento",  selected:true},
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
				selected: [],
				btn_down_pdf: true, //Desabilito los botones, hasta que muestre los datos
				btn_del_full: true,
				msj_tabla: " Presione 'Mostrar' para ver los regitros ",
				btn_mostrar: false,
				btn_editar: false,
				btn_eliminar: false,
				btn_select: false,
				btn_limpiar: true,
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
				return this.totalRows =this.tabla_mutuales.length;
			},
			rowsFilter(){
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
