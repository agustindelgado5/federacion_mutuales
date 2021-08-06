<template>
  <div id="ordenes" class="myTable">
    <h2>Listado de Ordenes</h2>
    <b-button @click="testFetch" class="mb-4">Mostrar</b-button>
    <b-table
      :fields="fields"
      striped
      sortable
      responsive
      hover
      :items="tabla_ordenes"
    >
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
    <!-- 
      <template slot="action">
        <b-button variant="warning" size="sm">Modificar</b-button>
        <b-button variant="danger" size="sm">Eliminar</b-button>
      </template>
    -->
    </b-table>
  </div>
</template>

<script>
let api = new URL("http://localhost");
api.pathname = "ordenes";
api.port = 8000;
//api.port = 8081;

export default {
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
            {key:'precio' ,label: 'Precio', sortable: true,},
            {key:'realizado' ,label: 'Realizado', sortable: true,},  
        ],
    };
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
