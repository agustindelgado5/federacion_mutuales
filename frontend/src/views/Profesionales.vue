<template>
  <div id="profesionales" class="myTable">
    <h2>Listado de Profesionales</h2>
    <b-button @click="testFetch" class="mb-4">Mostrar</b-button>
    <b-table
      :fields="fields"
      striped
      sortable
      responsive
      hover
      :items="tabla_profesionales"
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
api.pathname = "profesionales";
api.port = 8000;
//api.port = 8081;

export default {
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
