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
      <servicio-alta />
    </b-modal>

    <!-- ======== Formulario de Busqueda ======== -->
    <div>
      <b-input-group size="sm" class="mb-2">
        <b-input-group-prepend is-text>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            class="bi bi-search"
            viewBox="0 0 16 16"
          >
            <path
              d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"
            />
          </svg>
        </b-input-group-prepend>
        <b-form-input
          v-model="buscar"
          type="text"
          placeholder="Busque un registro"
          v-on:keyup="buscarnow()"
          ref="buscadorlista"
        ></b-form-input>
      </b-input-group>
    </div>
    <!-- ======================================== -->
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
    >
      <template #empty="">
        <b>No hay registros para mostrar</b>
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
    </b-table>
    <!-- ================ELIMINAR SERVICIO======================== -->
            <b-modal
              id="modal_eliminar"
              ref="my-modal"
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
                @click="hideModal"
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
      <servicio-update :servicio="editar" />
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
        { key: "id_servicio", label: "Nº de servicio", sortable: true },
        { key: "servicio", label: "Servicio", sortable: true },
        { key: "action", label: "Acciones", variant: "secondary" },
      ],
      totalRows: 1, //Total de filas
      currentPage: 1, //Pagina actual
      perPage: 20, // Datos en la tabla por pagina

      buscar: "",
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
    items() {
      return tabla_servicios.filter((item) => {
        return item.id_servicio
          .toLowerCase()
          .includes(this.buscar.toLowerCase());
      });
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
    showModalinfo(item, index) {
      this.infoEliminar.servicio = item;
      this.showModal();
    },
    //Funcion para mostrar el modal
    showModal() {
      this.$refs["my-modal"].show();
    },
    //Funcion para esconder el modal
    hideModal() {
      this.$refs["my-modal"].hide();
    },

    altaServicio() {},

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
          this.hideModal();
          }
        );
    },

    async buscarnow() {
      // Declare variables

      var input, filter, table, tr, td, i, txtValue, id, servicio;

      input = this.$refs.buscadorlista;
      filter = input.value.toUpperCase();
      table = document.getElementById("tablaregistros");
      tr = table.getElementsByTagName("tr");

      // Loop through all list items, and hide those who don't match the search query
      for (i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td");
        id = td[0].textContent || td[0].innerText;
        servicio = td[1].textContent || td[1].innerText;
        txtValue = id + servicio;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
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
