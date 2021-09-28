<template>
  <div id="mutuales" class="myTable">
    <!--HEAD DE LA PAGINA -->
    <vue-headful
      title="Mutuales - Federación Tucumana de Mutuales"
    ></vue-headful>

    <h2>Listado de Mutuales</h2>
    <b-button @click="testFetch" class="mb-4" title="Recargar" variant="light">
      <v-icon dark style="color: black">mdi-cached</v-icon>
      Actualizar
    </b-button>

    <!-- ================ALTA MUTUAL======================== -->
    <b-button
      class="mb-4 ml-2"
      v-b-modal.modal-alta
      @click="altaMutual()"
      title="Nueva Mutual"
      style="color: white"
    >
      <v-icon dark> mdi-plus </v-icon>
      Nueva Mutual
    </b-button>
    <b-modal id="modal-alta" hide-footer>
      <template #modal-title><h5 class="modal-title">Alta</h5></template>
      <mutual-alta/>
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
      :items="tabla_mutuales"
      show-empty
      :per-page="perPage"
      :current-page="currentPage"
      ref="tablaregistros"
      id="tablaregistros"
    >
      <template #empty="">
        <b>No hay registros para mostrar</b>
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
              @click="editarMutual(row.item, row.index)"
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
        <b-card title="Datos de la Mutual: ">
          <div>
            <b-list-group horizontal>
              <b-list-group class="col-6">
                <b-list-group-item>
                  <b>Codigo:</b> {{ row.item.id_mutual }}
                </b-list-group-item>
                <b-list-group-item>
                  <b>Nombre:</b> {{ row.item.nombre }}
                </b-list-group-item>
                <b-list-group-item>
                  <b>Servicios:</b>
                  <div v-for="servicios in data" :key="servicios.id_mutual">    
                    <div v-for="tareas in server_mutual" :key="tareas.id_servicio" >
                      <div v-if="servicios.id_mutual.split('/')[4]==row.item.id_mutual && servicios.id_servicio.split('/')[4]==tareas.id_servicio">
                          <ul>
                              <li><b>{{tareas.id_servicio}}:</b> {{tareas.servicio}} </li>
                          </ul>
                      </div>
                        
                    </div>
                    
                  </div>
                </b-list-group-item>
              </b-list-group>
            </b-list-group>
          </div>
        </b-card>
      </template>
    </b-table>
    <!-- ================MODIFICAR UNA MUTUAL======================== -->
    <b-modal id="modal-editar"  hide-footer > 
      <template #modal-title><h5 class="modal-title">Editar: {{editar.id_mutual}}- {{editar.nombre}}</h5></template>
        
      <mutual-update :mutual="editar"/>
    </b-modal>

    <!-- ================ELIMINAR MUTUAL======================== -->
    <b-modal
      id="modal_eliminar"
      ref="modal_eliminar"
      hide-footer
      title="Eliminar"
      ok-only
    >
      <div class="d-block text-center">
        <h3>
          ¿Esta seguro de eliminar los datos de
          {{ infoEliminar.mutual.nombre }}?
        </h3>
      </div>
      <b-button class="mt-2" block @click="hideModal" title="Volver Atras"
        >Volver Atras</b-button
      >
      <b-button
        class="mt-3"
        variant="danger"
        block
        @click="deleteMutual(infoEliminar.mutual.id_mutual)"
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
          aria-controls="table_mutuales"
        >
        </b-pagination>
      </b-col>
    </b-container>
    
  </div>
</template>

<script>
let api = new URL("http://localhost");
api.pathname = "mutuales";
//api.port = 8000;
api.port = 8081;

import VueAwesomplete from "vue-awesomplete";
import axios from "axios";
import MutualAlta from "./MutualAlta.vue";
import { APIControler } from "../store/APIControler";
import MutualUpdate from './MutualUpdate.vue';

export default {
  components: { MutualAlta, MutualUpdate },

  data() {
    return {
      tabla_mutuales: [],
      fields: [
        { key: "nombre", label: "Mutual", sortable: true },
        { key: "sucursal", label: "Filial", sortable: true },
        { key: "action", label: "Acciones", variant: "secondary" },
      ],
      totalRows: 1, //Total de filas
      currentPage: 1, //Pagina actual
      perPage: 10, // Datos en la tabla por pagina
      buscar: "",
      infoEliminar: {
        id: "modal_eliminar",
        mutual: -1,
      },
      servicios:{},
      data:{},
      editar:{},
      server_mutual: [
        //{
          //id_servicio:0,
          //servicio:'' 
       // }
      ]
    };
  },
  computed: {
    max(){
      var id = this.rows-1
      return this.tabla_mutuales[id].id_mutual;
    },
    rows() {
      return this.tabla_mutuales.length;
    },
    id() {
      return this.tabla_mutuales.id_mutual;
    },
    items() {
      return tabla_mutuales.filter((item) => {
        return item.id_mutual.toLowerCase().includes(this.buscar.toLowerCase());
      });
    },
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
    //Funcion para mostrar el modal
    showModal() {
      this.$refs["modal_eliminar"].show();
    },

    showModalinfo(item, index) {
      console.log("Mostrando info eliminar");
      console.log(this.infoEliminar);
      this.infoEliminar.mutual = item;
      this.showModal();
    },

    //Funcion para esconder el modal
    hideModal() {
      this.$refs["modal_eliminar"].hide();
    },
    altaMutual() {},

    //Editar medicamento
    editarMutual(item, index){
      this.editar=item;
    },

    async deleteMutual(id_mutual) {
      axios
        .delete("http://localhost:8081/mutuales/" + id_mutual + "/")
        .then((datos) => {
          swal("Operación Exitosa", " ", "success");
          console.log(datos);
          this.hideModal();
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
        p1, //mutual
        p2, //sucursal
        // p3,
        // p4;
        input = this.$refs.buscadorlista;
      filter = input.value.toUpperCase();
      table = document.getElementById("tablaregistros");
      tr = table.getElementsByTagName("tr");

      // Loop through all list items, and hide those who don't match the search query
      for (i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td");
        p1 = td[0].textContent || td[0].innerText;
        p2 = td[1].textContent || td[1].innerText;
        // p3 = td[2].textContent || td[2].innerText;
        // p4 = td[3].textContent || td[3].innerText;
        // txtValue = p1 + p2 + p3 + p4;
        txtValue = p1 + p2;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    },

    async getServicios() {
      var count =0;
      let serviciosAPI = new APIControler();
      serviciosAPI.apiUrl.pathname='servicio_mutual/';
      this.data = await serviciosAPI.getData(this.servicios);
      this.data.forEach(element => {   
          console.log(element);
          this.getPublic(element.id_servicio)
      });
    },

    
    async getPublic(id) {
      //let url = 'http://localhost:8081/'+ id + '/'
      
      axios.get(id)
      .then(response=>{
        console.log(response)
        this.server_mutual.push(response.data)        
        //this.server_mutual[count].id_servicio=response.data.id_servicio
        //this.server_mutual[count].servicio=response.data.servicio
      })
      .catch(error=>{
        console.log(error)
      })
    },

    
    
  },
  beforeMount() {
    this.testFetch();
    this.getServicios();
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
