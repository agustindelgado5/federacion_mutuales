<template>
  <div id="ordenes" class="myTable">

    <!--HEAD DE LA PAGINA -->
    <vue-headful title="Ordenes - Federación Tucumana de Mutuales"></vue-headful>

    <h2>Listado de Ordenes</h2>
    <b-button @click="testFetch" class="mb-4" title="Recargar" variant="light">
      <v-icon dark style="color:black;">mdi-cached</v-icon>
      Actualizar
    </b-button>

    <!-- ================ALTA ORDENES======================== -->
    <b-button class="mb-4 ml-2" v-b-modal.modal-alta @click="altaOrden()" title="Nueva Orden" style="color: white;">
      <v-icon dark>
        mdi-plus
      </v-icon>
      Nueva Orden
    </b-button>
    <b-modal id="modal-alta" hide-footer> 
      <template #modal-title><h5 class="modal-title">Alta</h5></template>
      <ordenes-alta/>
    </b-modal>

    <b-table
      :fields="fields"
      striped
      sortable
      responsive
      hover
      :items="tabla_ordenes"
      show-empty
      :per-page="perPage"
      :current-page="currentPage"
      :sticky-header= true
      :no-border-collapse= false
    >
      <template #empty="">
        <b>No hay registros para mostrar</b>
      </template>
      <template slot="cell(numero_orden)" slot-scope="data">
        <b>{{data.value}}</b>
      </template>
      <template slot="cell(numero_socio)" slot-scope="data">
        {{data.value.split('/')[4]}}
      </template>
      <template slot="cell(paciente)" slot-scope="data">
        {{data.value.split('/')[4]}}
      </template>
      <template slot="cell(id_medico)" slot-scope="data">
        {{data.value.split('/')[4]}}
      </template>
      <template slot="cell(id_mutual)" slot-scope="data">
        {{data.value.split('/')[4]}}
      </template>

      <template slot="cell(precio)" slot-scope="data">
        $ {{data.value}}
      </template>

      <template slot="cell(realizado)" slot-scope="data">
        <div v-if="data.value === true">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle-fill" viewBox="0 0 16 16" style="color: green">
            <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/>
          </svg>
          SI
        </div>
        <div v-else>
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x-circle-fill" viewBox="0 0 16 16" style="color: red">
            <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM5.354 4.646a.5.5 0 1 0-.708.708L7.293 8l-2.647 2.646a.5.5 0 0 0 .708.708L8 8.707l2.646 2.647a.5.5 0 0 0 .708-.708L8.707 8l2.647-2.646a.5.5 0 0 0-.708-.708L8 7.293 5.354 4.646z"/>
          </svg>
          NO
        </div>
      </template>
      <template slot="cell(action)" slot-scope="">
        <div class="mt-3">
          <b-button-group>
            <b-button variant="info" id="button-1" title="Mostrar Info"
              >Mostrar Info</b-button
            >

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
                <h3>¿Esta seguro de eliminar los datos de ... ?</h3>
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
    <!-- 
      <template slot="action">
        <b-button variant="warning" size="sm">Modificar</b-button>
        <b-button variant="danger" size="sm">Eliminar</b-button>
      </template>
    -->
    </b-table>

    <b-container fluid>
      <b-col class="my-1">
        <b-pagination
          v-model="currentPage"
          align="center"
          pills 
          :total-rows="rows"
          :per-page="perPage"
          aria-controls="table_ordenes"
        >
        </b-pagination>
      </b-col>
    </b-container>

  </div>
</template>

<script>
let api = new URL("http://localhost");
api.pathname = "ordenes";
//api.port = 8000;
api.port = 8081;

import OrdenesAlta from './OrdenesAlta.vue';

export default {
  components: { OrdenesAlta },
  data() {
    return {
      tabla_ordenes: [],
      fields: [
            {key:'numero_orden' ,label: 'N° Orden', sortable: true,},
            {key:'numero_socio' ,label: 'N° Socio', sortable: true,},
            {key:'paciente' ,label: 'Paciente',sortable: true,},
            {key:'servicio' ,label: 'Servicio', sortable: true,},
            {key:'id_medico' ,label: 'Id Medico',sortable: true,},
            {key:'id_mutual' ,label: 'Id Mutual',sortable: true,},
            {key:'fecha' ,label: 'Fecha', sortable: true,},
            {key:'hora' ,label: 'Hora', sortable: true,},
            {key:'precio' ,label: 'Precio', sortable: true,},
            {key:'realizado' ,label: 'Realizado', sortable: true,},
            { key: "action", label: "Acciones" , variant: "secondary"},  
      ],
      totalRows: 1, //Total de filas
      currentPage: 1, //Pagina actual
      perPage: 3, // Datos en la tabla por pagina
    };
  },
  computed: {
      rows() {
        return this.tabla_ordenes.length;
      },
  },
  methods: {
    async testFetch() {
      try {
        const res = await fetch(api);
        const data = await res.json();

        var lista_ordenes = data.results;

        console.log(lista_ordenes);

        this.tabla_ordenes = lista_ordenes;
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
    altaOrden(){},
  },
  beforeMount(){
    this.testFetch()
  }
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
