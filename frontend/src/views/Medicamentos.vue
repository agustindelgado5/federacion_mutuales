<template>
  <div id="medicamentos" class="myTable">
    <h2>Listado de Medicamentos</h2>
    <b-button @click="testFetch" class="mb-4">Mostrar</b-button>
    <b-table
      :fields="fields"
      striped
      sortable
      responsive
      hover
      :items="tabla_med"
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
api.pathname = "medicamentos";
api.port = 8000;
//api.port = 8081;

export default {
  data() {
    return {
      tabla_med: [],
      fields: [
            {key:'id_medicamento' ,label: 'Id', sortable: true,},
            {key:'nombre' ,label: 'Nombre', sortable: true,},
            {key:'presentacion' ,label: 'Presentacion',sortable: true,},
            {key:'laboratorio' ,label: 'Laboratotio', sortable: true,},
            {key:'cod_farmacia' ,label: 'Id Farmacia',sortable: true,},
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
