<template>
  <div id="servicios" class="myTable">
    <!--HEAD DE LA PAGINA -->
    <vue-headful
      title="Servicios - Federación Tucumana de Mutuales"
    ></vue-headful>

    <h2>Listado de Servicios</h2>
    <b-button @click="testFetch" class="mb-4" title="Recargar" variant="light">
      <v-icon dark style="color: black">mdi-cached</v-icon>
      Actualizar
    </b-button>

    <!-- ================ALTA SERVICIO======================== -->
    <b-button
      class="mb-4 ml-2"
      v-b-modal.modal-alta
      @click="altaServicio()"
      title="Nuevo Servicio"
      style="color: white"
    >
      <v-icon dark> mdi-plus </v-icon>
      Nuevo Servicio
    </b-button>
    <b-modal id="modal-alta" hide-footer>
      <template #modal-title><h5 class="modal-title">Alta</h5></template>
      <servicio-alta :updateTable="testFetch"/>
    </b-modal>

    <!-- ================ELIMINAR VARIOS SERVICIOS======================== -->
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
				ref="modal-eliminarTodo"
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

				<b-button class="mt-2" block @click="(hideModal('modal-eliminarTodo'))" title="Volver Atras">
					Volver Atras
				</b-button>

				<b-button
					class="mt-3"
					variant="danger"
					block
					title="Eliminar"
					@click="delete_all_Servicios()"
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
      style="width:100%; padding-bottom:1em;"
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

    <!-- ======================================== -->

		<div v-if="rows > 0">
			<div v-if="selected.length > 0">
				<pre>Cantidad de registros: {{ rows }} | Filas seleccionadas: {{selected.length}}</pre>
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

    <!-- ======== Tabla con los registros ======= -->
    <b-table
      :fields="fields"
      striped
      sortable
      responsive
      hover
      :items="tabla_servicios"
      small
      :sticky-header="true"
      :no-border-collapse="false"
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

      <template slot="cell(servicio)" slot-scope="data">
        {{ data.value.toUpperCase() }}
      </template>

      <template slot="cell(action)" slot-scope="row">
        <div class="mt-3">
          <b-button-group>
            <!--
            <b-button variant="info" id="button-1" title="Mostrar Info"
              >Mostrar Info</b-button
            >
            -->

            <b-button
              variant="warning"
              id="button-2"
              title="Editar este registro"
              v-b-modal.modal-editar
              @click="editarServicio(row.item, row.index)"
              :disabled="btn_editar"
            >
              <v-icon class="mr-2"> mdi-pencil </v-icon>
              Editar
            </b-button>

            <b-button
              variant="danger"
              id="button-3"
              @click="showModalEliminar(row.item, row.index)"
              :disabled="btn_eliminar"
              title="Eliminar este registro"
            >
              <v-icon class="mr-2"> mdi-delete </v-icon>
              Eliminar
            </b-button>

          </b-button-group>
        </div>
      </template>
    </b-table>
    <!-- ================ELIMINAR SERVICIO======================== -->
            <b-modal
              id="modal_eliminar"
              ref="modal_eliminar"
              hide-footer
              title="Eliminar"
              ok-only
            >
              <div class="d-block text-center">
                <h3>
                  ¿Esta seguro de eliminar el servicio de '{{
                    infoEliminar.servicio.servicio
                  }}' ?
                </h3>
              </div>
              <b-button
                class="mt-2"
                block
                @click="hideModal('modal_eliminar')"
                title="Volver Atras"
              >
                Volver Atras
              </b-button>

              <b-button
                class="mt-3"
                variant="danger"
                block
                title="Eliminar"
                @click="deleteServicio(infoEliminar.servicio.id_servicio)"
              >
                Eliminar
              </b-button>
            </b-modal>
<!-- ================MODAL EDITAR SERVICIO======================== -->

    <b-modal id="modal-editar" hide-footer>
      <template #modal-title><h5 class="modal-title">Editar</h5></template>
      <servicio-update :servicio="editar" :updateTable="testFetch"/>
    </b-modal>

    <b-container fluid>
      <b-col class="my-1">
        <b-pagination
          v-model="currentPage"
          align="center"
          pills
          :total-rows="rows"
          :per-page="perPage"
          aria-controls="table_servicios"
        >
        </b-pagination>
      </b-col>
    </b-container>
  </div>
</template>

<script>
let api = new URL("http://localhost");
api.pathname = "servicios";
//api.port = 8000;
api.port = 8081;

import ServicioAlta from "./ServicioAlta.vue";
import ServicioUpdate from "./ServicioUpdate.vue";
import axios from "axios";

export default {
  components: { ServicioAlta,ServicioUpdate },
  data() {
    return {
      tabla_servicios: [],
      fields: [
        { key: "selected", label: "", sortable: true },
        { key: "id_servicio", label: "Nº de servicio", sortable: true },
        { key: "servicio", label: "Servicio", sortable: true },
        { key: "action", label: "Acciones", variant: "secondary" },
      ],
      totalRows: 1, //Total de filas
      currentPage: 1, //Pagina actual
      perPage: 20, // Datos en la tabla por pagina
      filter: null,
      selected: [],
			btn_down_pdf: true, //Desabilito los botones, hasta que muestre los datos
			btn_del_full: true,
			msj_tabla: " Presione 'Mostrar' para ver los regitros ",
			btn_mostrar: false,
			btn_editar: false,
			btn_eliminar: false,
			btn_select: false,
			btn_limpiar: true,
      //buscar: "",
      editar: {},
      infoEliminar: {
        servicio: -1,
      },
    };
  },

  computed: {
    rows() {
      return this.tabla_servicios.length;
    },
    id() {
      return this.tabla_servicios.id_servicio;
    },
    sortOptions() {
      // Create an options list from our fields
      return this.fields
        .filter(f => f.sortable)
          .map(f => {
            return { text: f.label, value: f.key }
          })
    },
  },

  methods: {
    async testFetch() {
      try {
        const res = await fetch(api);
        const data = await res.json();

        var lista_servicios = data.results;

        console.log(lista_servicios);

        this.tabla_servicios = lista_servicios;
      } catch (error) {
        console.log(error);
      }
    },
    editarServicio(item, index) {
      this.editar = item;
    },
    //Muestra el modal de eliminar
    showModalEliminar(item, index) {
      this.infoEliminar.servicio = item;
      this.showModal("modal_eliminar");
    },

    //Muestra el modal de eliminar seleccionados
    showModalEliminarTodo(item, index) {
      this.infoEliminar.servicio = item;
      this.showModal("modal-eliminarTodo");
    },
    //Funcion para mostrar el modal
    showModal(id_ref) {
      this.$refs[id_ref].show();
    },
    //Funcion para esconder el modal
    hideModal(id_ref) {
      this.$refs[id_ref].hide();
    },

    altaServicio() {},

    //Elimino un servicio
    async deleteServicio(id) {
      axios
        .delete("http://localhost:8081/servicios/" + id + "/")
        .then((datos) => {
          swal("Operación Exitosa", " ", "success");
          console.log(datos);
        })
        .catch((error) => {
          swal("¡ERROR!", "Se ha detectado un problema ", "error");
          console.log(error);
        })
        .finally(() => {
          this.testFetch()
          this.hideModal("modal_eliminar");
          }
        );
    },

    //Elimina todas los servicios
			async delete_all_Servicios() {
				var cantidad = this.selected.length;

				try {
					for (var i = 0; i < cantidad; i++) {
						axios.delete(
							"http://localhost:8081/servicios/" +
								this.selected[i].id_servicio +
								"/"
						);
						if (this.selected.length == 0) {
							console.log("Eliminacion Exitosa");
							break;
						}
					}
					this.hideModal("modal-eliminarTodo");
					swal("Eliminacion Exitosa", " ", "success");
				} catch (error) {
					this.hideModal("modal-eliminarTodo");
					swal("¡ERROR!", "Se ha detectado un problema ", "error");
					console.log(error);
				} finally {
					this.testFetch();
				}
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

    //Funcion de busqueda
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length
      this.currentPage = 1
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
