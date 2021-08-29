<template>
  <div id="cobradores" class="myTable">
    <!--HEAD DE LA PAGINA -->
   <vue-headful title="Cobradores - Federación Tucumana de Mutuales"></vue-headful>

    <h2>Listado de Cobradores</h2>
    <b-button @click="testFetch" class="mb-4" variant="light">
      <v-icon dark style="color: black">mdi-format-list-bulleted-square</v-icon>
      Mostrar
    </b-button>

    <!-- ================ALTA Cobradores======================== -->
    <b-button
      class="mb-4 ml-2"
      v-b-modal.modal-alta
      @click="altaCobrador()"
      title="Nuevo Cobrador"
      style="color: white"
    >
      <v-icon dark> mdi-plus </v-icon>
      Nuevo Cobrador
    </b-button>
    <b-modal id="modal-alta" hide-footer>
      <template #modal-title><h5 class="modal-title">Alta</h5></template>
      <cobradores-alta />
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
      :sticky-header="true"
      :no-border-collapse="false"
      hover
      :items="table_cobradores"
      show-empty
      :per-page="perPage"
      :current-page="currentPage"
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
            <!-- ================ELIMINAR SOCIO======================== -->

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
                  {{ infoEliminar.cobradores.cobrador}}?
                </h3>
              </div>
              <b-button
                class="mt-2"
                block
                @click="hideModal"
                title="Volver Atras"
                >Volver Atras</b-button
              >
              <b-button
                class="mt-3"
                variant="danger"
                block
                @click="deleteCobrador(infoEliminar.Cobradores.numero_socio)"
                title="Eliminar"
              >
                Eliminar
              </b-button>
            </b-modal>
          </b-button-group>
        </div>
      </template>
      <template #row-details="row">
        <b-card>
          <ul>
            <!-- Para cargar todos los campos automáticamente (habría que darle formato) -->
            <li v-for="(value, key) in row.item" :key="key">
              {{ key }}: {{ value }}
            </li>
              
              <!-- A mano, es más facil pero "menos automático" Dx -->
              <!-- <li>Edad: {{ row.item.edad }}</li>
              <li>Calle: {{ row.item.calle }}</li>
              <li>Localidad: {{ row.item.calle }}</li> -->
            
          </ul>
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
          aria-controls="table_cobradores"
        >
        </b-pagination>
      </b-col>
    </b-container>
  </div>
</template>

<script>
let api = new URL("http://localhost");
api.pathname = "Cobradores";
api.port = 8000;
//api.port = 8081;
import VueAwesomplete from "vue-awesomplete";

import FarmaciasAlta from "./FarmaciasAlta.vue";


import CobradoresAlta from './CobradoresAlta.vue';
import axios from "axios";


export default {
  components: { CobradoresAlta },
  data() {
    return {
      tabla_cobradores: [],
      fields: [
       {key:"numero_socio" ,label: "N° Socio", sortable: true,},
       {key:"id_cobrador" ,label: "id_cobrador", sortable: true,},
       {key: "apellido", sortable: true,},
       {key: "nombre",sortable: true,},
       { key: "dni", label:"DNI",sortable: true,},
       {key: "action", label: "Acciones" , variant: "secondary"},
        ],
        totalRows: 1, //Total de filas
        currentPage: 1, //Pagina actual
        perPage: 10, // Datos en la tabla por pagina
    };
  },

  computed: {
    rows() {
      return this.tabla_cobradores.length;
    },
  },

  methods: {
    async testFetch() {
      try {
        const res = await fetch(api);
        const data = await res.json();

        var lista_cobradores = data.results;

        console.log(lista_cobradores);

        this.tabla_cobradores = lista_cobradores;
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
    altaCobrador() {},
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

