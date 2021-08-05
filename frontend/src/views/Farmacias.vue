<template>
  <div id="farmacias" class="myTable">
    <h2>Listado de Farmacias</h2>
    <b-button @click="testFetch" class="mb-4">Mostrar</b-button>
    <b-table
      :fields="fields"
      striped
      sortable
      responsive
      hover
      :items="tabla_farmacias"
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
api.pathname = "farmacias";
api.port = 8000;
//api.port = 8081;

export default {
  data() {
    return {
      tabla_farmacias: [],
      fields: [
            {key:'cod_farmacia' ,label: 'Codigo', sortable: true,},
            {key:'matricula_farm' ,label: 'Matricula',sortable: true,},
            {key:'cuit' ,label: 'CUIT', sortable: true,},
            {key:'farmacia' ,label: 'Farmacia',sortable: true,},
            {key:'localidad' ,label: 'Sucursal', sortable: true,}, 
            {key: 'email' ,label: 'Correo', sortable: true,},
            {key:'tel_fijo' ,label: 'Telefono Fijo', sortable: true,},
            {key:'tel_cel' ,label: 'Celular', sortable: true,},
            {key:'representante' ,label: 'Representante', sortable: true,},
        ],
    };
  },
  methods: {
    async testFetch() {
      try {
        const res = await fetch(api);
        const data = await res.json();

        var lista_farmacias = data.results;

        console.log(lista_farmacias);

        this.tabla_farmacias = lista_farmacias;
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
