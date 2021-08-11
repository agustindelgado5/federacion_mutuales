<template>
  <div id="recetas" class="myTable">
    <h2>Listado de Recetas</h2>
    <b-button @click="testFetch" class="mb-4">Mostrar</b-button>
    
    <!-- ================ALTA RECETASS======================== -->
    <b-button class="mb-4 ml-2" v-b-modal.modal-alta @click="altaReceta()" title="Nueva Receta">Nueva Receta</b-button>
    <b-modal id="modal-alta" hide-footer> 
      <template #modal-title><h5 class="modal-title">Alta</h5></template>
      <recetas-alta/>
    </b-modal>
    
    <b-table
      :fields="fields"
      striped
      sortable
      responsive
      hover
      :items="tabla_recetas"
    >
    <!-- 
      <template slot="action">
        <b-button variant="warning" size="sm">Modificar</b-button>
        <b-button variant="danger" size="sm">Eliminar</b-button>
      </template>
    -->
      <template slot="cell(numero_socio)" slot-scope="data">
        {{data.value.split('/')[4]}}
      </template>
      <template slot="cell(dni_familiar)" slot-scope="data">
        {{data.value.split('/')[4]}}
      </template>
      <template slot="cell(id_medicamento)" slot-scope="data">
        {{data.value.split('/')[4]}}
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
api.pathname = "recetas";
//api.port = 8000;
api.port = 8081;

import RecetasAlta from './RecetasAlta.vue';

export default {
  components: { RecetasAlta },
  data() {
    return {
      tabla_recetas: [],
      fields: [
            {key:'numero_socio' ,label: 'N° Socio', sortable: true,},
            {key:'dni_familiar' ,label: 'Paciente', sortable: true,},
            {key:'diagnostico' ,label: 'Diagnostico',sortable: true,},
            {key:'id_medicamento' ,label: 'Id Medicamento',sortable: true,},
            {key:'cod_farmacia' ,label: 'Id Farmacia',sortable: true,},
            {key:'fecha' ,label: 'Fecha', sortable: true,},
            {key:'carencia' ,label: 'Carencia', sortable: true,},
            { key: "action", label: "Acciones" },  
        ],
    };
  },
  methods: {
    async testFetch() {
      try {
        const res = await fetch(api);
        const data = await res.json();

        var lista_recetas = data.results;

        console.log(lista_recetas);

        this.tabla_recetas = lista_recetas;
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
    altaReceta(){},
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
