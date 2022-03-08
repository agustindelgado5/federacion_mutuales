<template>
	<v-app id="app">
		<div id="users" class="myTable">
			<!--HEAD DE LA PAGINA -->
			<vue-headful
				title="Users - Federación Tucumana de Mutuales"
			></vue-headful>

			<h2>Listado de Users</h2>
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
				@click="altaUser()"
				title="Nuevo User"
				style="color: white"
			>
				<v-icon dark> mdi-plus </v-icon>
				Nuevo User
			</b-button>
			<b-modal id="modal-alta" hide-footer>
				<template #modal-title><h5 class="modal-title">Alta</h5></template>
				<users-alta :updateTable="testFetch" />
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
						@click="delete_all_Users()"
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
					:items="tabla_users"
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

					<template slot="cell(id_user)" slot-scope="data">
						<b>{{ data.value }}</b>
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
										name: 'user',
										params: { id: row.item },
										query: { id: row.item.id_user },
									}"
									variant="primary"
									id="button-4"
									title="Ver socios del user"
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
									@click="editarUser(row.item, row.index)"
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
						<b-card title="Datos del user: ">
							<div>
								<b-list-group horizontal>
									<b-list-group class="col-3">
										<b-list-group-item
											><b>ID:</b> {{ row.item.id_user }}</b-list-group-item
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
							¿Esta seguro de eliminar los datos del user
							{{ infoEliminar.user.id_user }}?
						</h3>
					</div>
					<b-button class="mt-2" block @click="hideModal" title="Volver Atras"
						>Volver Atras</b-button
					>
					<b-button
						class="mt-3"
						variant="danger"
						block
						@click="deleteUser(infoEliminar.user.id_user)"
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
							aria-controls="table_users"
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

				<!-- 

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
											SOCIO
										</b-button>
									</b-card-header>
									<b-collapse
										id="accordion-1"
										visible
										accordion="my-accordion"
										role="tabpanel"
									>
										<b-card-body>
											<b-form-group id="input-group-1">
												<v-autocomplete
													id="socio"
													v-model="filter_socio"
													:items="options_socio"
													type="text"
													solo
													filled
												></v-autocomplete>
												<div v-show="filter_socio != null">
													<b-button
														@click="filter_socio = null"
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
				-->
			</aside>

			<b-modal id="modal-editar" hide-footer>
				<template #modal-title><h5 class="modal-title">Editar</h5></template>
				<users-update :user="editar" :updateTable="testFetch" />
			</b-modal>

			<!-- ==================================CREAR PDF================================== -->
			<vue-html2pdf
				:show-layout="false"
				:float-layout="true"
				:enable-download="false"
				:preview-modal="true"
				:paginate-elements-by-height="1400"
				filename="DetalleUser"
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
						<h3>User</h3>

						<b-list-group>
							<b-list-group-item
								v-for="value in fields.slice(0, -1)"
								:key="value.key"
								>{{ value.label }}:
								{{ userAPDF[value.key] }}</b-list-group-item
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
    api.pathname = "/auth/users/";
	//api.port = 8000;
	api.port = 8081;

    import { Fetcher } from "@/store/utils/Fetcher";
	import UsersAlta from "../users/UsersAlta.vue";
	import UsersUpdate from "../users/UsersUpdate.vue";
	import VueHtml2pdf from "vue-html2pdf";
	import axios from "axios";

	export default {
		components: { UsersAlta, UsersUpdate, VueHtml2pdf },
		data() {
			return {
               
				fetcher: new Fetcher(),
                
				tabla_users: [],
				fields: [
					{ key: "selected", label: "Seleccionar", sortable: true },
					{ key: "id_user", label: "ID User", sortable: true },
                    { key: "username", label: "username", sortable: true },
					{ key: "apellido", label: "Apellido", sortable: true },
					{ key: "nombre", label: "Nombre", sortable: true },
					{ key: "email", label: "email", sortable: true },
					{ key: "is_staff", label: "Es del Staff", sortable: true },
                    { key: "is_superuser", label: "Es un Administrador", sortable: true },
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
					user: -1,
				},
				selected: [],
				//Botones
				btn_down_pdf: false, //Desabilito los botones, hasta que muestre los datos
				btn_del_full: true,
				btn_limpiar: true,
				msj_tabla: " Presione 'Mostrar' para ver los regitros ",
				btn_mostrar: false,
				btn_editar: false,
				btn_users: false,
				btn_eliminar: false,
				btn_select: false,
				//Campos a filtrar
				filter_socio: null,

				//Opciones de filtrado
				options_socio: [
					{ value: null, text: "Elija un socio", selected: true },
				],

				userAPDF: {}, //Se carga cuando se hace clic en exportar a pdf, con el user a exportar
			};
		},
		computed: {
			rows() {
				return (this.totalRows = this.tabla_users.length);
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

					var lista_users = data.results;

					console.log(lista_users);

					this.tabla_users = lista_users;

					this.tabla_users.forEach((element) => {
						let opcionSoc = {};

						opcionSoc.value = element.numero_socio;
						opcionSoc.text = element.numero_socio.split("/")[4];

						if (this.options_socio.find((x) => x.value == opcionSoc.value)) {
							console.log(opcionSoc, " ya se encuentra en el listado");
						} else {
							this.options_socio.push(opcionSoc);
						}
					});
				} catch (error) {
					console.log(error);
				}
			},
			editarUser(item, index) {
				this.editar = item;
			},
			//Funcion para mostrar el modal
			showModal() {
				this.$refs["my-modal"].show();
			},
			showModalinfo(item, index) {
				this.infoEliminar.user = item;
				this.showModal();
			},
			//Funcion para esconder el modal
			hideModal() {
				this.$refs["my-modal"].hide();
			},
			altaUser() {},

			//Elimino un user
			async deleteUser(id_user) {
				axios
                    .delete("http://localhost:8081/admin/auth/user/" + id_user + "/")
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
			async delete_all_Users() {
				var cantidad = this.selected.length;

				try {
					for (var i = 0; i < cantidad; i++) {
						axios.delete(
							"http://localhost:8081/users/" +
								this.selected[i].id_user +
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

				this.userAPDF = { ...item };

				this.userAPDF.numero_socio =
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
