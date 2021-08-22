<template>
  <div id="medicamentos" class="myTable">
    <h2>Listado de Medicamentos</h2>

    <b-button @click="testFetch" class="mb-4" variant="light">
      <v-icon dark style="color:black;">mdi-format-list-bulleted-square</v-icon>
      Mostrar
    </b-button>
    <!-- ================ALTA MEDICAMENTOS======================== -->
    <b-button class="mb-4 ml-2" v-b-modal.modal-alta @click="altaMedicamento()" title="Nuevo Medicamento" style="color: white;">
      <v-icon dark>
        mdi-plus
      </v-icon>
      Nuevo Medicamento
    </b-button>
    <b-modal id="modal-alta" hide-footer> 
      <template #modal-title><h5 class="modal-title">Alta</h5></template>
      <medicamento-alta/>
    </b-modal>
    
    <b-table
      :fields="fields"
      striped
      sortable
      responsive
      hover
      :items="tabla_med"
      show-empty
      :sticky-header= true
      :no-border-collapse= false
    >
    <!-- 
      <template slot="action">
        <b-button variant="warning" size="sm">Modificar</b-button>
        <b-button variant="danger" size="sm">Eliminar</b-button>
      </template>
    -->
      <template #empty="">
        <b>No hay registros para mostrar</b>
      </template>

      <template slot="cell(cod_farmacia)" slot-scope="data">
        {{data.value.split('/')[4]}}
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
    </b-table>
  </div>
</template>

<script>
let api = new URL("http://localhost");
api.pathname = "medicamentos";
//api.port = 8000;
api.port = 8081;

import MedicamentoAlta from './MedicamentosAlta.vue';
export default {
  components: { MedicamentoAlta },
  data() {
    return {
      tabla_med: [],
      fields: [
            {key:'id_medicamento' ,label: 'ID', sortable: true,},
            {key:'nombre' ,label: 'Nombre', sortable: true,},
            {key:'presentacion' ,label: 'Presentacion',sortable: true,},
            {key:'laboratorio' ,label: 'Laboratotio', sortable: true,},
            {key:'cod_farmacia' ,label: 'Farmacia',sortable: true,},
            { key: "action", label: "Acciones", variant: "secondary" },
        ],
    };
  },
  methods: {
    async testFetch() {
      try {
        const res = await fetch(api);
        const data = await res.json();

        var lista_med = data.results;

        console.log(lista_med);

        this.tabla_med = lista_med;
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
    altaMedicamento() {},
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
