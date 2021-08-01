<template>
  <div id="socios" class="myTable">
    <h2>Listado de Socios</h2>
    <b-button @click="testFetch" class="mb-4">Mostrar</b-button>
    <b-table
      :fields="fields"
      striped
      sortable
      responsive
      hover
      :items="tabla_socios"
    >
      
      <template slot="action" slot-scope="">
        <b-button size="sm" variant="warning">
          Editar
        </b-button>
        <b-button size="sm" variant="danger">
          Eliminar
        </b-button>
      </template>


    </b-table>
  </div>
</template>

<script>
let api = new URL("http://localhost");
api.pathname = "socios";
api.port = 8000;
//api.port = 8081;

export default {
  data() {
    return {
      tabla_socios: [],
      fields: [
            {key:'numero_socio' ,label: 'N° Socio', sortable: true,},
            {key:'apellido' ,label: 'Apellido/s',sortable: true,},
            {key:'nombre' ,label: 'Nombre/s', sortable: true,},
            {key:'dni' ,label: 'DNI',sortable: true,},
            {key:'fecha_nacimiento' ,label: 'Fecha de Nacimiento', sortable: true,}, 
            //{key: 'calle' ,label: 'Direccion', sortable: true,},
            //{key:'localidad' ,label: 'Localidad', sortable: true,},
            //{key:'departamento' ,label: 'Departamento', sortable: true,},
            //{key:'cod_postal' ,label: 'Codigo Postal', sortable: true,},
            //{key: 'email' ,label: 'Mail', sortable: true,},
            //{key: 'tel_fijo',label: 'Telefono Fijo', sortable: true,},
            //{key:'tel_celular' ,label: 'Telefono Celular', sortable: true,},
            {key:'carencia',label: 'Carencia', sortable: true,},
        ],
    };
  },
  methods: {
    async testFetch() {
      try {
        const res = await fetch(api);
        const data = await res.json();

        var lista_socios = data.results;

        console.log(lista_socios);

        this.tabla_socios = lista_socios;
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
