<template>
  <div id="socios" class="myTable">

    <!-- ======== Formulario de Busqueda ======== -->
    <div>
      <b-input-group size="sm" class="mb-2">
        <b-input-group-prepend is-text>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            class="bi bi-search"
            viewBox="0 0 16 16"
          >
            <path
              d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"
            />
          </svg>
          <!--
          <b-icon icon="search"></b-icon>
          -->
        </b-input-group-prepend>
        <b-form-input
          type="search"
          placeholder="Busque un registro"
        ></b-form-input>
      </b-input-group>
    </div>
    <!-- ======================================== -->

    <h2>Listado de Socios</h2>
    <b-button @click="testFetch" class="mb-4" title="Mostrar">Mostrar</b-button>

    <!-- ================ALTA SOCIO======================== -->
    <b-button class="mb-4 ml-2" v-b-modal.modal-alta @click="altaSocio()" title="Nuevo Socio">Nuevo Socio</b-button>
    <b-modal id="modal-alta"  hide-footer> 
      <template #modal-title><h5 class="modal-title">Alta</h5></template>
      <socios-alta/>
    </b-modal>

    <!-- ======== Tabla con los registros ======= -->
    <b-table
      :fields="fields"
      striped
      sortable
      responsive
      sticky-header
      hover
      :items="tabla_socios"
    >
      <template slot="cell(apellido)" slot-scope="data">
        {{data.value.toUpperCase()}}
      </template>

      <template slot="cell(nombre)" slot-scope="data">
        {{data.value.toUpperCase()}}
      </template>

      <!--Libreria Luxon para formatear las fechas, no esta del todo bien aun XD
      -->
      <!-- 
      <template slot="cell(fecha_nacimiento)" slot-scope="data">
        {{data.value|luxon}}
      </template>

      <template slot="cell(carencia)" slot-scope="data">
        {{data.value|luxon}}
      </template>
      -->
     

      <template slot="cell(action)" slot-scope="">
        <div class="mt-3">
          <b-button-group>
            <b-button variant="info" id="button-1" title="Mostrar Info"
              > Mostrar Info</b-button
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
                @click="deleteSocio()"
                >Eliminar</b-button
              >
            </b-modal>
          </b-button-group>
        </div>
      </template>
    </b-table>
    <!-- ========================================= -->
  </div>
</template>

<script>
let api = new URL("http://localhost");
api.pathname = "socios";
//api.port = 8000; //Cambien uds los puertos
api.port = 8081;

//import Holmes from "holmes-js";
import VueAwesomplete from 'vue-awesomplete';
import SociosAlta from './SociosAlta.vue';

export default {
  components: { SociosAlta, VueAwesomplete },
  data() {
    return {
      tabla_socios: [],
      fields: [
        { key: "numero_socio", label: "N° Socio", sortable: true },
        { key: "apellido", label: "Apellido/s", sortable: true },
        { key: "nombre", label: "Nombre/s", sortable: true },
        { key: "dni", label: "DNI", sortable: true },
        {
          key: "fecha_nacimiento",
          label: "Fecha de Nacimiento",
          sortable: true,
        },
        //{key: 'calle' ,label: 'Direccion', sortable: true,},
        //{key:'localidad' ,label: 'Localidad', sortable: true,},
        //{key:'departamento' ,label: 'Departamento', sortable: true,},
        //{key:'cod_postal' ,label: 'Codigo Postal', sortable: true,},
        //{key: 'email' ,label: 'Mail', sortable: true,},
        //{key: 'tel_fijo',label: 'Telefono Fijo', sortable: true,},
        //{key:'tel_celular' ,label: 'Telefono Celular', sortable: true,},
        { key: "carencia", label: "Carencia", sortable: true },
        { key: "action", label: "Acciones", variant: "secondary" },
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
    //Funcion para mostrar el modal
    showModal() {
      this.$refs["my-modal"].show();
    },
    //Funcion para esconder el modal
    hideModal() {
      this.$refs["my-modal"].hide();
    },
    
   

    altaSocio() {},

    deleteSocio(){},

    changeSkills() {
      this.$refs.skills.list(['Angular', 'React', 'Vue'])
    },
    /*
    buscar() {
      Holmes({
        input: ".search input", // predeterminado: input [type = search]
        find: ".results div", // querySelectorAll que coincide con cada uno de los resultados individualmente
      });
    },
    */
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
