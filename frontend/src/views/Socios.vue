<template>
  <div id="socios" class="myTable">
    <!--HEAD DE LA PAGINA -->
    <vue-headful title="Socios - Federación Tucumana de Mutuales"></vue-headful>

    <h2>Listado de Socios</h2>

    <b-button @click="testFetch" class="mb-4" title="Mostrar" variant="light">
      <v-icon dark style="color: black">mdi-format-list-bulleted-square</v-icon>
      Mostrar
    </b-button>

    <!-- ================ALTA SOCIO======================== -->
    <b-button
      class="mb-4 ml-2"
      v-b-modal.modal-alta
      @click="altaSocio()"
      title="Nuevo Socio"
      style="color: white"
    >
      <v-icon dark> mdi-plus </v-icon>
      Nuevo Socio
    </b-button>
    <b-modal id="modal-alta" hide-footer>
      <template #modal-title>
        <h5 class="modal-title">Alta</h5>
      </template>
      <socios-alta />
    </b-modal>

    <!-- ================ PAGO DE AFILIACION ======================== -->
    <b-button
      @click="GenerarPagoAfiliacion()"
      class="mb-4 ml-2"
      id="btn_Pago_afiliacion"
      title="Pago Afiliacion"
      >Pago de Afiliacion</b-button
    >

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
        </b-input-group-prepend>
        <b-form-input
          v-model="buscar"
          type="text"
          placeholder="Busque un registro"
          v-on:keyup="buscarnow()"
          ref="buscadorlista"
        ></b-form-input>
      </b-input-group>
    </div>
    <!-- ======================================== -->

    <!-- ======== Tabla con los registros ======= -->
    <b-table
      :fields="fields"
      striped
      sortable
      responsive
      :sticky-header="true"
      :no-border-collapse="false"
      hover
      :items="tabla_socios"
      show-empty
      :per-page="perPage"
      :current-page="currentPage"
      ref="tablaregistros"
      id="tablaregistros"
      small
    >
      <template #empty="">
        <b>No hay registros para mostrar</b>
      </template>
      
      <template slot="cell(numero_socio)" slot-scope="data">
        <b>{{ data.value }}</b>
      </template>

      <template slot="cell(apellido)" slot-scope="data">
        {{ data.value.toUpperCase() }}
      </template>

      <template slot="cell(nombre)" slot-scope="data">
        {{ data.value.toUpperCase() }}
      </template>

      <template slot="cell(departamento)" slot-scope="data">
        {{ data.value.toUpperCase() }}
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

      <template slot="cell(apellido)" slot-scope="row">
        {{ row.value.toUpperCase() }}
      </template>

      <template slot="cell(nombre)" slot-scope="row">
        {{ row.value.toUpperCase() }}
      </template>

      <template slot="cell(action)" slot-scope="row">
        <div class="mt-3">
          <b-button-group>
            <b-button
              variant="info"
              id="button-1"
              title="Mostrar Info"
              @click="row.toggleDetails"
            >
              {{ row.detailsShowing ? "Ocultar" : "Mostrar" }} Detalles
            </b-button>

            <b-button
              variant="warning"
              id="button-2"
              title="Editar este registro"
            >
              <v-icon class="mr-2"> mdi-pencil </v-icon>
              Editar
            </b-button>

            <b-button
              variant="danger"
              id="button-3"
              @click="showModalinfo(row.item, row.index)"
              title="Eliminar este registro"
            >
              <v-icon class="mr-2"> mdi-delete </v-icon>
              Eliminar
            </b-button>

            <!-- ================ELIMINAR SOCIO======================== -->
            <b-modal
              id="modal_eliminar"
              ref="my-modal"
              hide-footer
              title="Eliminar"
              ok-only
            >
              <div class="d-block text-center">
                <h3>
                  ¿Esta seguro de eliminar los datos de
                  {{ infoEliminar.socio.apellido }},
                  {{ infoEliminar.socio.nombre }} ?
                </h3>
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
                @click="deleteSocio(infoEliminar.socio.numero_socio)"
                title="Eliminar"
              >
                Eliminar
              </b-button>
            </b-modal>
            <!-- ==================================================== -->
          </b-button-group>
        </div>
      </template>

      <template #row-details="row">
        <b-card title="Datos del titular: " >
          <div>
            <b-list-group horizontal>
              <b-list-group>
                <b-list-group-item><b>Nombre Completo:</b> {{ row.item.apellido.toUpperCase() }}, {{ row.item.nombre.toUpperCase() }}</b-list-group-item>
                <b-list-group-item><b>DNI:</b> {{ row.item.dni }}</b-list-group-item>
                <b-list-group-item><b>Fecha de Nacimiento:</b> {{ row.item.fecha_nacimiento }}</b-list-group-item>
                <b-list-group-item><b>Edad:</b> {{ row.item.edad }}</b-list-group-item>
              </b-list-group>
              &nbsp;
              <b-list-group>
                <b-list-group-item><b>Domicilio:</b> {{ row.item.calle.toUpperCase() }} - {{ row.item.localidad.toUpperCase() }} </b-list-group-item>
                <b-list-group-item><b>Departamento:</b> {{ row.item.departamento.toUpperCase() }}</b-list-group-item>
                <b-list-group-item><b>Codigo Postal:</b> {{ row.item.cod_postal }}</b-list-group-item>
                <b-list-group-item><b>Correo:</b> {{ row.item.email }} </b-list-group-item>
              </b-list-group>
              &nbsp;
              <b-list-group>
                <b-list-group-item><b>Telefono Fijo:</b> {{ row.item.tel_fijo }}</b-list-group-item>
                <b-list-group-item><b>Celular:</b> {{ row.item.tel_celular }}</b-list-group-item>
                <b-list-group-item><b>Carencia:</b> {{ row.item.carencia }} </b-list-group-item>
              </b-list-group>
                
            </b-list-group>
          </div>
        </b-card>
        <!--
        <b-button
          class="mt-2"
          size="sm"
          title="Ver mas"
          style="color: white;"  
          @click="getFamiliar()"
        >
          <b>(↓)</b>  
        </b-button>
        -->
        <b-card title="Adherentes: " >  
          <div>
            <b-list-group horizontal>
              <div v-for="adherente in data" :key="adherente.dni_familiar">
                <div v-if="adherente.numero_socio.split('/')[4]==row.item.numero_socio">
                  <b-list-group>
                    <b-list-group-item><b>DNI:</b> {{ adherente.dni_familiar }}</b-list-group-item>
                    <b-list-group-item><b>Nombre Completo:</b> {{ adherente.apellido.toUpperCase() }}, {{ adherente.nombre.toUpperCase() }}</b-list-group-item>
                    <b-list-group-item><b>Fecha de Nacimiento:</b> {{ adherente.fecha_nacimiento }}</b-list-group-item>
                    <b-list-group-item><b>Carencia:</b> {{adherente.carencia }} </b-list-group-item>
                  </b-list-group>
                  &nbsp;
                </div>
              </div>
            </b-list-group>
          </div>
        </b-card>
      </template>
    </b-table>

    <b-container fluid>
      <b-col class="my-1">
        <b-pagination
          v-model="currentPage"
          align="center"
          pills
          :total-rows="rows"
          :per-page="perPage"
          aria-controls="table_socios"
        >
        </b-pagination>
      </b-col>
    </b-container>
  </div>
</template>

<script>
let api = new URL("http://localhost");
api.pathname = "socios";
//api.port = 8000; //Cambien uds los puertos
api.port = 8081;


import VueAwesomplete from "vue-awesomplete";
import SociosAlta from "./SociosAlta.vue";
import axios from "axios";
import { APIControler } from "../store/APIControler";


export default {
  components: { SociosAlta,VueAwesomplete },
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
        { key: "departamento", label: "Departamento", sortable: true },
        //{key:'cod_postal' ,label: 'Codigo Postal', sortable: true,},
        //{key: 'email' ,label: 'Mail', sortable: true,},
        //{key: 'tel_fijo',label: 'Telefono Fijo', sortable: true,},
        //{key:'tel_celular' ,label: 'Telefono Celular', sortable: true,},
        { key: "carencia", label: "Carencia", sortable: true },
        { key: "action", label: "Acciones", variant: "secondary" },
      ],
      totalRows: 1, //Total de filas
      currentPage: 1, //Pagina actual
      perPage: 10, // Datos en la tabla por pagina
      list_familiares:{},
      datos_familiar: {},
      data:{},
      buscar: "",
      infoEliminar: {
        id: "modal_eliminar",
        socio: -1,
      },
    };
  },

  computed: {
    rows() {
      return this.tabla_socios.length;
    },
    id() {
      return this.tabla_socios.numero_socio;
    },
    items() {
      return tabla_socios.filter((item) => {
        return item.numero_socio
          .toLowerCase()
          .includes(this.buscar.toLowerCase());
      });
    },
  },
  
  created: function() {
    //console.log('Funcion realizada');
    this.getFamiliar();
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

    async getFamiliar() {
      let familiarAPI = new APIControler();
      familiarAPI.apiUrl.pathname='familiar/';
      this.data = await familiarAPI.getData(this.list_familiares);
      this.data.forEach(element => {   
          console.log(element);
      });
      /*
      try {
        this.api.pathname='familiar'
        const res = await fetch(api);
        const data = await res.json();

        var lista = data.results;
        console.log(lista);

        this.list_familiares = lista;
      } catch (error) {
        console.log(error);
      }
      */
    },
    // Funcion para mostrar el modal
    showModal() {
      this.$refs["my-modal"].show();
    },

    showModalinfo(item, index) {
      this.infoEliminar.socio = item;
      this.showModal();
    },
    //Funcion para esconder el modal
    hideModal() {
      this.$refs["my-modal"].hide();
    },

    info(numero_socio) {
      alert("id: " + numero_socio);
    },

    showModalinfo(item, index) {
      this.infoEliminar.socio = item;
      this.showModal();
    },

    altaSocio() {},

    async deleteSocio(numero_socio) {
      axios
        .delete("http://localhost:8081/socios/" + numero_socio + "/")
        .then((datos) => {
          swal("Operación Exitosa", " ", "success");
          console.log(datos);
        })
        .catch((error) => {
          swal("¡ERROR!", "Se ha detectado un problema ", "error");
          console.log(error);
        })
        .finally(() => this.testFetch());
    },

    async buscarnow() {
      // Declare variables
      var input,
        filter,
        table,
        tr,
        td,
        i,
        txtValue,
        NumSocio,
        Apellido,
        Nombre,
        DNI;
      input = this.$refs.buscadorlista;
      filter = input.value.toUpperCase();
      table = document.getElementById("tablaregistros");
      tr = table.getElementsByTagName("tr");

      // Loop through all list items, and hide those who don't match the search query
      for (i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td");
        NumSocio = td[0].textContent || td[0].innerText;
        Apellido = td[1].textContent || td[1].innerText;
        Nombre = td[2].textContent || td[2].innerText;
        DNI = td[3].textContent || td[3].innerText;
        txtValue = NumSocio + Apellido + Nombre + DNI;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    },

    GenerarPagoAfiliacion() {},
   
  },
  beforeMount(){
    this.testFetch()
  }
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
