<template>
  <div id="cobradores" class="myTable">
    <!--HEAD DE LA PAGINA -->
    <vue-headful
      title="Cobradores - Federación Tucumana de Mutuales"
    ></vue-headful>

    <h2>Listado de Cobradores</h2>
    <b-button @click="testFetch" class="mb-4" title="Recargar" variant="light">
      <v-icon dark style="color: black">mdi-cached</v-icon>
      Actualizar
    </b-button>

    <!-- ================ALTA Cobradores======================== -->
    <b-button
      class="mb-4 ml-2"
      v-b-modal.modal-alta
      @click="altaCobrador()"
      title="Nueva Cobrador"
      style="color: white"
    >
      <v-icon dark> mdi-plus </v-icon>
      Nuevo Cobrador
    </b-button>
    <b-modal id="modal-alta" hide-footer>
      <template #modal-title><h5 class="modal-title">Alta</h5></template>
      <cobradores-alta />
    </b-modal>
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
      :items="tabla_cobradores"
      show-empty
      :per-page="perPage"
      :current-page="currentPage"
      ref="tablaregistros"
      id="tablaregistros"
    >
      <template #empty="">
        <b>No hay registros para mostrar</b>
      </template>

       <template #cell(selected)="{ rowSelected }">
        <template v-if="rowSelected">
          <span aria-hidden="true">&check;</span>
          <span class="sr-only">Selected</span>
        </template>
        <template v-else>
          <span aria-hidden="true">&nbsp;</span>
          <span class="sr-only">Not selected</span>
        </template>
      </template>

      <template slot="cell(numero_socio)" slot-scope="data">
        {{data.value.split('/')[4]}}
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
              {{ row.detailsShowing ? "Ocultar" : "Mostrar" }} detalles
            </b-button>

            <b-button
               variant="warning"
               id="button-2"
               title="Editar este registro"
              v-b-modal.modal-editar
              @click="editarCobrador(row.item, row.index)"
              
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
            
          </b-button-group>
        </div>
      </template>
      <template #row-details="row">
        <b-card title="Datos del cobrador: " >
          <div>
            <b-list-group horizontal>
              <b-list-group class="col-3">  
                <b-list-group-item><b>id cobrador:</b> {{ row.item.id_cobrador }}</b-list-group-item>
                <b-list-group-item><b>N socio:</b> {{ row.item.numero_socio.split('/')[4] }}</b-list-group-item>
            
              </b-list-group>
              &nbsp;
              <b-list-group class="col-5">
                <b-list-group-item><b>Apellido:</b> {{ row.item.apellido }}</b-list-group-item>
                <b-list-group-item><b>Nombre:</b> {{ row.item.nombre }}</b-list-group-item>
                <b-list-group-item><b>DNI:</b> {{ row.item.dni }} </b-list-group-item>
              </b-list-group>
      
                
            </b-list-group>
          </div>            
        </b-card>
      </template>
    </b-table>
    <!-- ================ELIMINAR Cobrador======================== -->

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
                  {{ infoEliminar.cobrador.apellido}},{{infoEliminar.cobrador.nombre}}?
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
                @click="deleteCobrador(infoEliminar.cobrador.id_cobrador)"
                title="Eliminar"
              >
                Eliminar
              </b-button>
            </b-modal>
    <b-container fluid>
      <b-col class="my-1">
        <b-pagination
          v-model="currentPage"
          align="center"
          pills
          :total-rows="rows"
          :per-page="perPage"
          aria-controls="table_cobradores"
        >
        </b-pagination>
      </b-col>
    </b-container>
    <b-modal id="modal-editar" hide-footer>
      <template #modal-title><h5 class="modal-title">Editar</h5></template>
     <cobradores-update :cobrador="editar" />
   </b-modal>
  </div>
</template>

<script>
let api = new URL("http://localhost");
api.pathname = "cobradores";
//api.port = 8000;
api.port = 8081;
import VueAwesomplete from "vue-awesomplete";

import CobradoresAlta from './CobradoresAlta.vue';
import CobradoresUpdate from './CobradoresUpdate.vue';
import axios from "axios";

export default {
  components: { CobradoresAlta,CobradoresUpdate },
  data() {
    return {
      tabla_cobradores: [],
      fields: [
       {key:"numero_socio" ,label: "N° Socio", sortable: true,},
       {key:"id_cobrador" ,label: "ID Cobrador", sortable: true,},
       {key: "apellido", sortable: true,},
       {key: "nombre",sortable: true,},
       { key: "dni", label:"DNI",sortable: true,},
       {key: "action", label: "Acciones" , variant: "secondary"},
        ],
        totalRows: 1, //Total de filas
        currentPage: 1, //Pagina actual
        perPage: 10, // Datos en la tabla por pagina
        buscar: "",
        editar:{},
        infoEliminar: {
        id: "modal_eliminar",
        cobrador: -1,
      },
    };
  },
  computed: {
    rows() {
      return this.tabla_cobradores.length;
    },
    id() {
      return this.tabla_cobradores.id_cobrador;
    },
    items() {
      return tabla_cobradores.filter((item) => {
        return item.id_cobrador
          .toLowerCase()
          .includes(this.buscar.toLowerCase());
      });
    },
  },
  methods: {
    async testFetch() {
      try {
        const res = await fetch(api);
        const data = await res.json();

        var lista_cobradores = data.results;

        console.log(lista_cobradores);

        this.tabla_cobradores = lista_cobradores;
      } catch (error) {
        console.log(error);
      }
    },
    editarCobrador(item, index) {
      this.editar = item;
    },
    //Funcion para mostrar el modal
    showModal() {
      this.$refs["my-modal"].show();
    },
    showModalinfo(item, index) {
      this.infoEliminar.cobrador = item;
      this.showModal();
    },
    //Funcion para esconder el modal
    hideModal() {
      this.$refs["my-modal"].hide();
    },
    altaCobrador() {},
    async deleteCobrador(id_cobrador) {
        axios.delete("http://localhost:8081/cobradores/" + id_cobrador + "/")
        .then((datos) => {
          swal("Operación Exitosa", " ", "success");
          console.log(datos);
          this.hideModal();
        })
        .catch((error) => {
          swal("¡ERROR!", "Se ha detectado un problema ", "error");
          console.log(error);
          this.hideModal();
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
        p1,//id_cobrador
        p2,//n socio
        p3,//apellido cobrador
        p4;//Nombre cobrador
      input = this.$refs.buscadorlista;
      filter = input.value.toUpperCase();
      table = document.getElementById("tablaregistros");
      tr = table.getElementsByTagName("tr");

      // Loop through all list items, and hide those who don't match the search query
      for (i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td");
        p1 = td[0].textContent || td[0].innerText;
        p2 = td[1].textContent || td[1].innerText;
        p3 = td[2].textContent || td[2].innerText;
        p4 = td[3].textContent || td[3].innerText;
        txtValue = p1 + p2 + p3 + p4;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    },
    
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
