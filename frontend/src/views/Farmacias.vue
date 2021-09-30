<template>
  <div id="farmacias" class="myTable">
    <!--HEAD DE LA PAGINA -->
    <vue-headful
      title="Farmacias - Federación Tucumana de Mutuales"
    ></vue-headful>

    <h2>Listado de Farmacias</h2>
    <b-button @click="testFetch" class="mb-4" title="Recargar" variant="light">
      <v-icon dark style="color: black">mdi-cached</v-icon>
      Actualizar
    </b-button>

    <!-- ================ALTA FARMACIA======================== -->
    <b-button
      class="mb-4 ml-2"
      v-b-modal.modal-alta
      @click="altaFarmacia()"
      title="Nueva Farmacia"
      style="color: white"
    >
      <v-icon dark> mdi-plus </v-icon>
      Nueva Farmacia
    </b-button>
    <b-modal id="modal-alta" hide-footer>
      <template #modal-title><h5 class="modal-title">Alta</h5></template>
      <farmacias-alta />
    </b-modal>
    <!-- ======== Formulario de Busqueda ======== -->
    <!--
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
    -->
    <!--
    <input type="text" v-model="buscar" class="form-control" placeholder="Farmacia"/>
    -->
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

    <!-- ======== Tabla con los registros ======= -->
    <b-table
      :fields="fields"
      striped
      sortable
      responsive
      :sticky-header="true"
      :no-border-collapse="false"
      hover
      :items="tabla_farmacias"
      show-empty
      :per-page="perPage"
      :current-page="currentPage"
      :filter="filter"
      @filtered="onFiltered"

      ref="tablaregistros"
      id="tablaregistros"
    >
      <template #empty="">
        <b>No hay registros para mostrar</b>
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
              variant="warning"
              id="button-2"
              title="Editar este registro"
              v-b-modal.modal-editar
              @click="editarFarmacia(row.item, row.index)"
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
        <b-card title="Datos de la farmacia: ">
          <div>
            <b-list-group horizontal>
              <b-list-group class="col-3">
                <b-list-group-item
                  ><b>Codigo:</b> {{ row.item.cod_farmacia }}</b-list-group-item
                >
                <b-list-group-item
                  ><b>Matricula:</b>
                  {{ row.item.matricula_farm }}</b-list-group-item
                >
                <b-list-group-item
                  ><b>CUIT:</b> {{ row.item.cuit }}</b-list-group-item
                >
              </b-list-group>
              &nbsp;
              <b-list-group class="col-5">
                <b-list-group-item
                  ><b>Farmacia:</b> {{ row.item.farmacia }}</b-list-group-item
                >
                <b-list-group-item
                  ><b>Sucursal:</b> {{ row.item.localidad }}</b-list-group-item
                >
                <b-list-group-item
                  ><b>Correo:</b> {{ row.item.email }}
                </b-list-group-item>
              </b-list-group>
              &nbsp;
              <b-list-group class="col-4">
                <b-list-group-item
                  ><b>Telefono Fijo:</b>
                  {{ row.item.tel_fijo }}</b-list-group-item
                >
                <b-list-group-item
                  ><b>Celular:</b> {{ row.item.tel_celular }}</b-list-group-item
                >
                <b-list-group-item
                  ><b>Representante:</b> {{ row.item.representante }}
                </b-list-group-item>
              </b-list-group>
            </b-list-group>
          </div>
        </b-card>
      </template>
    </b-table>
    <!-- ================ELIMINAR FARMACIA======================== -->

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
          {{ infoEliminar.farmacia.farmacia }}?
        </h3>
      </div>
      <b-button class="mt-2" block @click="hideModal" title="Volver Atras"
        >Volver Atras</b-button
      >
      <b-button
        class="mt-3"
        variant="danger"
        block
        @click="deleteFarmacia(infoEliminar.farmacia.cod_farmacia)"
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
          aria-controls="tabla_farmacias"
        >
        </b-pagination>
      </b-col>
    </b-container>
    <b-modal id="modal-editar" hide-footer>
      <template #modal-title><h5 class="modal-title">Editar</h5></template>
      <farmacias-update :farmacia="editar" />
    </b-modal>
  </div>
</template>

<script>
let api = new URL("http://localhost");
api.pathname = "farmacias";
//api.port = 8000;
api.port = 8081;
import VueAwesomplete from "vue-awesomplete";

import FarmaciasAlta from "./FarmaciasAlta.vue";
import FarmaciasUpdate from "./FarmaciasUpdate.vue";

import axios from "axios";

export default {
  components: { FarmaciasAlta, FarmaciasUpdate },
  data() {
    return {
      tabla_farmacias: [],
      fields: [
        { key: "cod_farmacia", label: "Codigo", sortable: true },
        { key: "matricula_farm", label: "Matricula", sortable: true },
        { key: "cuit", label: "CUIT", sortable: true },
        { key: "farmacia", label: "Farmacia", sortable: true },
        { key: "localidad", label: "Sucursal", sortable: true },
        { key: "email", label: "Correo", sortable: true },
        { key: "tel_fijo", label: "Telefono Fijo", sortable: true },
        { key: "tel_celular", label: "Celular", sortable: true },
        { key: "representante", label: "Representante", sortable: true },
        { key: "action", label: "Acciones", variant: "secondary" },
      ],
      totalRows: 1, //Total de filas
      currentPage: 1, //Pagina actual
      perPage: 30, // Datos en la tabla por pagina
      //buscar: '',
      filter: null,
      editar: {},
      infoEliminar: {
        id: "modal_eliminar",
        farmacia: -1,
      },
    };
  },
  computed: {
    rows() {
      return this.tabla_farmacias.length;
    },
    id() {
      return this.tabla_farmacias.cod_farmacia;
    },
    /*
    items() {
      return this.tabla_farmacias.filter((item) => {
        return item.representante.toLowerCase().includes(this.buscar.toLowerCase()) ||
        item.farmacia.toLowerCase().includes(this.buscar.toLowerCase()) ||
        item.localidad.toLowerCase().includes(this.buscar.toLowerCase()) ||
        item.email.toLowerCase().includes(this.buscar.toLowerCase());
      });
    },*/
    sortOptions() {
        // Create an options list from our fields
        return this.fields
          .filter(f => f.sortable)
          .map(f => {
            return { text: f.label, value: f.key }
          })
      }

  },
  methods: {
    async testFetch() {
      try {
        const res = await fetch(api);
        const data = await res.json();

        var lista_farmacias = data.results;

        console.log(lista_farmacias);

        this.tabla_farmacias = lista_farmacias;
      } catch (error) {
        console.log(error);
      }
    },
    editarFarmacia(item, index) {
      this.editar = item;
    },
    //Funcion para mostrar el modal
    showModal() {
      this.$refs["my-modal"].show();
    },
    showModalinfo(item, index) {
      this.infoEliminar.farmacia = item;
      this.showModal();
    },
    //Funcion para esconder el modal
    hideModal() {
      this.$refs["my-modal"].hide();
    },
    altaFarmacia() {},

    async deleteFarmacia(cod_Farmacia) {
      axios
        .delete("http://localhost:8081/farmacias/" + cod_Farmacia + "/")
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
