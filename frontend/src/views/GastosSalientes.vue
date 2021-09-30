<template>
  <div id="gastosSalientes" class="myTable">
    <vue-headful
      title="Gastos Salientes - Federación Tucumana de Mutuales"
    ></vue-headful>

    <h2>Listado de gastos salientes</h2>
    <b-button @click="testFetch" class="mb-4" title="Recargar" variant="light">
      <v-icon dark style="color: black">mdi-cached</v-icon>
      Actualizar
    </b-button>

    <!-- ================ALTA GASTO SALIENTE======================== -->
    <b-button
      class="mb-4 ml-2"
      v-b-modal.modal-alta
      @click="altaGastoSaliente()"
      title="Nuevo Gasto"
      style="color: white"
    >
      <v-icon dark> mdi-plus </v-icon>
      Nuevo Gasto Saliente
    </b-button>
    <b-modal id="modal-alta" hide-footer>
      <template #modal-title><h5 class="modal-title">Alta</h5></template>
      <gastosSalientes-alta />
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
      :items="tabla_gastosSalientes"
      show-empty
      :per-page="perPage"
      :current-page="currentPage"
      :sticky-header="true"
      :no-border-collapse="false"
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
              @click="editarGastoSaliente(row.item, row.index)"
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
        <b-card title="Datos del gasto saliente: ">
          <div>
            <b-list-group horizontal>
              <b-list-group class="col-3">
                <b-list-group-item
                  ><b>Id gasto:</b> {{ row.item.id_gasto }}</b-list-group-item
                >
                <b-list-group-item
                  ><b>Numero de ticket:</b>
                  {{ row.item.nro_ticket }}</b-list-group-item
                >
                <b-list-group-item
                  ><b>Descripcion:</b> {{ row.item.descripcion }}</b-list-group-item
                >
                <b-list-group-item
                  ><b>Total:</b> {{ row.item.total }}</b-list-group-item
                >
                <b-list-group-item
                  ><b>Fecha:</b> {{ row.item.fecha }}</b-list-group-item
                >
              </b-list-group>
              &nbsp;
            </b-list-group>
          </div>
        </b-card>
      </template>
    </b-table>
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
          ¿Esta seguro de eliminar los datos de
          {{ infoEliminar.gastoSaliente.descripcion }} - Nro ticket  
          {{ infoEliminar.gastoSaliente.nro_ticket }}?
        </h3>
      </div>
      <b-button class="mt-2" block @click="hideModal" title="Volver Atras"
        >Volver Atras</b-button
      >
      <b-button
        class="mt-3"
        variant="danger"
        block
        @click="deleteGastoSaliente(infoEliminar.gastoSaliente.id_gasto)"
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
          :total-rows="rows"
          :per-page="perPage"
          aria-controls="table_gastosSalientes"
        >
        </b-pagination>
      </b-col>
    </b-container>
    <b-modal id="modal-editar" hide-footer>
      <template #modal-title><h5 class="modal-title">Editar</h5></template>
      <gastosSalientes-update :gastoSaliente="editar" />
    </b-modal>
  </div>
</template>

<script>
let api = new URL("http://localhost");
api.pathname = "gastosSalientes";
api.port = 8081;
import VueAwesomplete from "vue-awesomplete";

import GastosSalientesAlta from "./GastosSalientesAlta.vue";
import GastosSalientesUpdate from "./GastosSalientesUpdate.vue";

import axios from "axios";

export default {
  components: { GastosSalientesAlta, GastosSalientesUpdate },
  data() {
    return {
      tabla_gastosSalientes: [],
      fields: [
        { key: "id_gasto", label: "Id Gasto", sortable: true },
        { key: "nro_ticket", label: "Numero de Ticket", sortable: true },
        { key: "descripcion", label: "Descripcion", sortable: true },
        { key: "total", label: "Total", sortable: true },
        { key: "fecha", label: "Fecha", sortable: true },
        { key: "action", label: "Acciones", variant: "secondary" },
      ],
      totalRows: 1, //Total de filas
      currentPage: 1, //Pagina actual
      perPage: 10, // Datos en la tabla por pagina
      buscar: "",
      editar: {},
      infoEliminar: {
        id: "modal_eliminar",
        gastoSaliente: -1,
      },
    };
  },
  computed: {
    rows() {
      return this.tabla_gastosSalientes.length;
    },
    id() {
      return this.tabla_gastosSalientes.id_gasto;
    },
    items() {
      return tabla_gastosSalientes.filter((item) => {
        return item.id_gasto
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

        var lista_gastosSalientes = data.results;

        console.log(lista_gastosSalientes);

        this.tabla_gastosSalientes = lista_gastosSalientes;
      } catch (error) {
        console.log(error);
      }
    },
    editarGastoSaliente(item, index) {
      this.editar = item;
    },
    //Funcion para mostrar el modal
    showModal() {
      this.$refs["my-modal"].show();
    },
    showModalinfo(item, index) {
      this.infoEliminar.gastoSaliente = item;
      this.showModal();
    },
    //Funcion para esconder el modal
    hideModal() {
      this.$refs["my-modal"].hide();
    },
    altaGastoSaliente() {},

    async deleteGastoSaliente(id_gasto) {
      axios
        .delete("http://localhost:8081/gastosSalientes/" + id_gasto + "/")
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

    async buscarnow() {
      // Declare variables
      var input,
        filter,
        table,
        tr,
        td,
        i,
        txtValue,
        p1, //id_gasto
        p2, //nro_ticket
        p3, //descripcion
      input = this.$refs.buscadorlista;
      filter = input.value.toUpperCase();
      table = document.getElementById("tablaregistros");
      tr = table.getElementsByTagName("tr");

      // Loop through all list items, and hide those who don't match the search query
      for (i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td");
        p1 = td[0].textContent || td[0].innerText;
        p2 = td[1].textContent || td[1].innerText;
        p3 = td[2].textContent || td[2].innerText;
        txtValue = p1 + p2 + p3;
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
