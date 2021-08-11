<template>
  <div id="profesionales" class="myTable">
    <h2>Listado de Profesionales</h2>
    <b-button @click="testFetch" class="mb-4">Mostrar</b-button>

    <!-- ================ALTA PROFESIONAL======================== -->
    <b-button class="mb-4 ml-2" v-b-modal.modal-alta @click="altaProfesional()" title="Nuevo Profesional">Nuevo Profesional</b-button>
    <b-modal id="modal-alta" hide-footer> 
      <template #modal-title><h5 class="modal-title">Alta</h5></template>
      <profesionales-alta/>
    </b-modal>

    <b-table
      :fields="fields"
      striped
      sortable
      responsive
      hover
      :items="tabla_profesionales"
    >
      <template slot="cell(apellido)" slot-scope="data">
        {{data.value.toUpperCase()}}
      </template>

      <template slot="cell(nombre)" slot-scope="data">
        {{data.value.toUpperCase()}}
      </template>
    <!-- 
      <template slot="action">
        <b-button variant="warning" size="sm">Modificar</b-button>
        <b-button variant="danger" size="sm">Eliminar</b-button>
      </template>
    -->
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
api.pathname = "profesionales";
//api.port = 8000;
api.port = 8081;

import ProfesionalesAlta from './ProfesionalesAlta.vue';


export default {
  components: { ProfesionalesAlta },
  data() {
    return {
      tabla_profesionales: [],
      fields: [
        {
          key: "id_medico",
          sortable: true,
        },
        {
          key: "apellido",
          sortable: true,
        },
        {
          key: "nombre",
          sortable: true,
        },
        {
          key: "dni",
          sortable: true,
        },
        {
          key: "especialidad",
          sortable: true,
        },
        { key: "action", label: "Acciones" },
      ],
    };
  },
  methods: {
    async testFetch() {
      try {
        const res = await fetch(api);
        const data = await res.json();

        var lista_profesioales = data.results;

        console.log(lista_profesioales);

        this.tabla_profesionales = lista_profesioales;
      } catch (error) {
        console.log(error);
      }
    },
    altaProfesional(){},
    //Funcion para mostrar el modal
    showModal() {
      this.$refs["my-modal"].show();
    },
    //Funcion para esconder el modal
    hideModal() {
      this.$refs["my-modal"].hide();
    },
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
