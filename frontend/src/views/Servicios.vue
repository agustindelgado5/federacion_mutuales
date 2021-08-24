<template>
  <div id="servicios" class="myTable">

    <!--HEAD DE LA PAGINA -->
    <vue-headful title="Servicios - Federación Tucumana de Mutuales"></vue-headful>

    <h2>Listado de Servicios</h2>
    <b-button @click="testFetch" class="mb-4" variant="light">
      <v-icon dark style="color:black;">mdi-format-list-bulleted-square</v-icon>
      Mostrar
    </b-button>

    <!-- ================ALTA SERVICIO======================== -->
    <b-button class="mb-4 ml-2" v-b-modal.modal-alta @click="altaServicio()" title="Nuevo Servicio" style="color: white;">
      <v-icon dark>
        mdi-plus
      </v-icon>
      Nuevo Servicio
    </b-button>
    <b-modal id="modal-alta" hide-footer> 
      <template #modal-title><h5 class="modal-title">Alta</h5></template>
      <servicio-alta/>
    </b-modal>

    <b-table
      :fields="fields"
      striped
      sortable
      responsive
      hover
      :items="tabla_servicios"
      small
      :sticky-header= true
      :no-border-collapse= false
      show-empty
      :per-page="perPage"
      :current-page="currentPage"
    >
      <template #empty="">
        <b>No hay registros para mostrar</b>
      </template>

      <template slot="cell(servicio)" slot-scope="data">
        {{data.value.toUpperCase()}}
      </template>
    
      <template slot="cell(action)" slot-scope="">
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
            >
              <v-icon class="mr-2">
                mdi-pencil
              </v-icon>
              Editar
            </b-button>

            <b-button
              variant="danger"
              id="button-3"
              @click="showModal"
              title="Eliminar este registro"
            >
              <v-icon class="mr-2">
                mdi-delete
              </v-icon>
              Eliminar
            </b-button>

            <b-modal ref="my-modal" hide-footer title="Eliminar">
              <div class="d-block text-center">
                <!--
                <h3>¿Esta seguro de eliminar los datos de ... ?</h3>
                -->
                <h3>¿Esta seguro de eliminar el servicio de ... ?</h3>
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
                title="Eliminar"
                >Eliminar</b-button
              >
            </b-modal>
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

import ServicioAlta from './ServicioAlta.vue';

export default {
  components: { ServicioAlta },
  data() {
    return {
      tabla_servicios: [],
      fields: [
            {key:'servicio' ,label: 'Servicio', sortable: true,},
            //{key:'carencia' ,label: 'Carencia',sortable: true,},
            { key: "action", label: "Acciones" , variant: "secondary",},
        ],
        totalRows: 1, //Total de filas
        currentPage: 1, //Pagina actual
        perPage: 10, // Datos en la tabla por pagina
    };
  },

  computed: {
    rows() {
      return this.tabla_servicios.length;
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
    //Funcion para mostrar el modal
    showModal() {
      this.$refs["my-modal"].show();
    },
    //Funcion para esconder el modal
    hideModal() {
      this.$refs["my-modal"].hide();
    },
    altaServicio() {},
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
