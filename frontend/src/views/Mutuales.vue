<template>
  <div id="mutuales" class="myTable">
    <h2>Listado de Mutuales</h2>
    <b-button @click="testFetch" class="mb-4">Mostrar</b-button>

    <!-- ================ALTA MUTUAL======================== -->
    <b-button class="mb-4 ml-2" v-b-modal.modal-alta @click="altaMutual()" title="Nueva Mutual">Nueva Mutual</b-button>
    <b-modal id="modal-alta" hide-footer> 
      <template #modal-title><h5 class="modal-title">Alta</h5></template>
      <mutual-alta/>
    </b-modal>

    <b-table
      :fields="fields"
      striped
      sortable
      responsive
      hover
      :items="tabla_mutuales"
    >
    
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
              >Editar</b-button
            >

            <b-button
              variant="danger"
              id="button-3"
              @click="showModal"
              title="Eliminar este registro"
              >Eliminar</b-button
            >

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
api.pathname = "mutuales";
//api.port = 8000;
api.port = 8081;

import MutualAlta from './MutualAlta.vue';

export default {
  components: { MutualAlta },
  data() {
    return {
      tabla_mutuales: [],
      fields: [
            {key:'nombre' ,label: 'Mutual', sortable: true,},
            {key:'sucursal' ,label: 'Filial',sortable: true,},
            { key: "action", label: "Acciones" },
        ],
    };
  },
  methods: {
    async testFetch() {
      try {
        const res = await fetch(api);
        const data = await res.json();

        var lista_mutuales = data.results;

        console.log(lista_mutuales);

        this.tabla_mutuales = lista_mutuales;
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
    altaMutual() {},
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
