<template>
	<v-app id="app">
		<div id="lentes" class="myTable">
			<!--HEAD DE LA PAGINA -->
			<vue-headful
				title="Lentes - Federación Tucumana de Mutuales"
			></vue-headful>

			<h2>Listado de Lentes</h2>
			<b-button
				@click="testFetch"
				class="mb-4"
				title="Recargar"
				variant="light"
			>
				<v-icon dark style="color: black">mdi-cached</v-icon>
				Actualizar
			</b-button>

			<!-- ================ALTA Lentes======================== -->
			<b-button
				class="mb-4 ml-2"
				v-b-modal.modal-alta
				@click="altaLente()"
				title="Nuevo Lente"
				style="color: white"
			>
				<v-icon dark> mdi-plus </v-icon>
				Nuevo Lente
			</b-button>
			<b-modal id="modal-alta" hide-footer>
				<template #modal-title><h5 class="modal-title">Alta</h5></template>
				<lentes-alta :updateTable="testFetch"/>
			</b-modal>

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
						@click="delete_all_Lentes()"
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
			<!-- ======================================== -->
			<section>
				<!-- ======== Tabla con los registros ======= -->

				<b-table
					:fields="fields"
					striped
					sortable
					responsive
					hover
					:items="tabla_lentes"
					show-empty
					:per-page="perPage"
					:current-page="currentPage"
					:no-border-collapse="false"
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

					<template slot="cell(codigo_optica)" slot-scope="data">
						<b>{{ data.value }}</b>
					</template>

					<template slot="cell(precio_laboratorio)" slot-scope="data">
						<b>${{ data.value }}</b>
					</template>

					<template slot="cell(precio_mutual)" slot-scope="data">
						<b>${{ data.value }}</b>
					</template>
					<template slot="cell(precio_tarjeta)" slot-scope="data">
						<b>${{ data.value }}</b>
					</template>
					<template slot="cell(precio_venta)" slot-scope="data">
						<b>${{ data.value }}</b>
					</template>
					<template slot="cell(precio_optica)" slot-scope="data">
						<b>${{ data.value }}</b>
					</template>

					<template slot="cell(action)" slot-scope="row">
						<div class="mt-3">
							<b-button-group>
								<b-button
									variant="warning"
									id="button-2"
									title="Editar este registro"
									v-b-modal.modal-editar
									@click="editarLente(row.item, row.index)"
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
							aria-controls="tabla_lentes"
						>
						</b-pagination>
					</b-col>
				</b-container>
			</section>

			<!-- ================ELIMINAR Lente======================== -->
			<b-modal
				id="modal_eliminar"
				ref="my-modal"
				hide-footer
				title="Eliminar"
				ok-only
			>
				<div class="d-block text-center">
					<h3>
						¿Esta seguro de eliminar los datos del registro
						{{ infoEliminar.lente.codigo_optica }}?
					</h3>
				</div>
				<b-button class="mt-2" block @click="hideModal" title="Volver Atras"
					>Volver Atras</b-button
				>
				<b-button
					class="mt-3"
					variant="danger"
					block
					@click="deleteLente(infoEliminar.lente.codigo_optica)"
					title="Eliminar"
				>
					Eliminar
				</b-button>
			</b-modal>

			<!-- ================EDITAR Lente======================== -->
			<b-modal id="modal-editar" hide-footer>
				<template #modal-title><h5 class="modal-title">Editar</h5></template>
				<lentes-update :lente="editar" :updateTable="testFetch" />
			</b-modal>

			<!-- ==================================CREAR PDF================================== -->
			<!-- <vue-html2pdf
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
 
     
          <h3>Federación Tucumana de Mutuales</h3>
          <img
            src="../assets/logo.jpg"
            alt="Logo Federación"
            srcset=""
            id="Logo_fed"
          />
        </section>
        <section class="pdf-item">
          <h3>Orden Médica</h3> -->
			<!-- <b-table
              :fields="fields"
              responsive
              :items="tabla_cirugias"
              :no-border-collapse= false
              small
              fixed
              bordered
              head-variant="light"
            >
              
                {{data.value.split('/')[4]}}
              </template> 
            </b-table> -->
			<!-- 
          <b-list-group>
            <b-list-group-item
              v-for="value in fields.slice(0, -1)"
              :key="value.key"
              >{{ value.label }}: {{ ordenAPDF[value.key] }}</b-list-group-item
            >
          </b-list-group>
        </section>
      </section>
    </vue-html2pdf>  -->
			<!-- ============================================================================== -->
		</div>
	</v-app>
</template>

<script>
	let api = new URL("http://localhost");
	api.pathname = "lentes";
	//api.port = 8000;
	api.port = 8081;

	import LentesAlta from "./LentesAlta.vue";
	import LentesUpdate from "./LentesUpdate.vue";
	import VueHtml2pdf from "vue-html2pdf";

	import axios from "axios";

	export default {
		components: { LentesAlta, LentesUpdate, VueHtml2pdf },
		data() {
			return {
				tabla_lentes: [],
				fields: [
					{ key: "selected", label: "Seleccionar", sortable: true },
					{ key: "codigo_optica", label: "Codigo Optica", sortable: true },
					//{ key: "codigo_seguimiento", label: "Codigo Seguimiento", sortable: true },
					{ key: "medida_lente", label: "Medida Lente", sortable: true },
					{ key: "patillas", label: "Patillas", sortable: true },
					{ key: "marca", label: "Marca", sortable: true },
					{ key: "descripcion", label: "Descripcion", sortable: true },
					{
						key: "precio_laboratorio",
						label: "Precio Laboratorio",
						sortable: true,
					},
					{ key: "precio_optica", label: "Precio Optica", sortable: true },
					{ key: "precio_mutual", label: "Precio Mutual", sortable: true },
					{ key: "precio_venta", label: "Precio Venta", sortable: true },
					{ key: "precio_tarjeta", label: "Precio Tarjeta", sortable: true },
					{ key: "stock", label: "Stock", sortable: true },
					{ key: "action", label: "Acciones", variant: "secondary" },
				],
				totalRows: 1, //Total de filas
				currentPage: 1, //Pagina actual
				perPage: 10, // Datos en la tabla por pagina
				buscar: "",
				editar: {},
				selected: [],
				infoEliminar: {
					id: "modal_eliminar",
					lente: -1,
				},
				filter: null,

				btn_down_pdf: true, //Desabilito los botones, hasta que muestre los datos
				btn_del_full: true,
				btn_mostrar: false,
				btn_editar: false,
				btn_pagado: false,
				btn_eliminar: false,
				btn_select: false,
				btn_limpiar: true,
			};
		},
		computed: {
			rows() {
				return (this.totalRows = this.tabla_lentes.length);
			},
			id() {
				return this.tabla_lentes.codigo_optica;
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

					var lista_lentes = data.results;

					console.log(lista_lentes);

					this.tabla_lentes = lista_lentes;
				} catch (error) {
					console.log(error);
				}
			},
			editarLente(item, index) {
				this.editar = item;
			},
			//Funcion para mostrar el modal
			showModal() {
				this.$refs["my-modal"].show();
			},
			showModalinfo(item, index) {
				this.infoEliminar.lente = item;
				this.showModal();
			},
			//Funcion para esconder el modal
			hideModal() {
				this.$refs["my-modal"].hide();
			},
			altaLente() {},

			async deleteLente(codigo_optica) {
				axios
					.delete("http://localhost:8081/lentes/" + codigo_optica + "/")
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

			//Funcion para eliminar todos los socios seleccionados
			async delete_all_Lentes() {
				var cantidad = this.selected.length;

				try {
					for (var i = 0; i < cantidad; i++) {
						axios.delete(
							"http://localhost:8081/lentes/" +
								this.selected[i].codigo_optica +
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

			onFiltered(filteredItems) {
				// Trigger pagination to update the number of buttons/pages due to filtering
				this.totalRows = filteredItems.length;
				this.currentPage = 1;
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
</style>
