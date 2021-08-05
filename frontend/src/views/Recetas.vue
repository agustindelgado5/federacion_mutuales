<template>
  <div id="recetas" class="myTable">
    <h2>Listado de Recetas</h2>
    <b-button @click="testFetch" class="mb-4">Mostrar</b-button>
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
    </b-table>
  </div>
</template>

<script>
let api = new URL("http://localhost");
api.pathname = "recetas";
api.port = 8000;
//api.port = 8081;

export default {
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
