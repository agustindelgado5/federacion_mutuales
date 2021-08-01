<template>
  <div id="mutuales" class="myTable">
    <h2>Listado de Mutuales</h2>
    <b-button @click="testFetch" class="mb-4">Mostrar</b-button>
    <b-table
      :fields="fields"
      striped
      sortable
      responsive
      hover
      :items="tabla_mutuales"
    >
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
api.pathname = "mutuales";
api.port = 8000;
//api.port = 8081;

export default {
  data() {
    return {
      tabla_mutuales: [],
      fields: [
            {key:'nombre' ,label: 'Mutual', sortable: true,},
            {key:'sucursal' ,label: 'Filial',sortable: true,},
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
