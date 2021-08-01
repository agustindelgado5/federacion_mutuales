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
