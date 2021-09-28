<template>
  <div id="profesionales" class="myTable">
    <vue-headful
      title="Profesionales - Federación Tucumana de Mutuales"
    ></vue-headful>

    <h2>Listado de Profesionales</h2>
    <b-button @click="testFetch" class="mb-4" title="Recargar" variant="light">
      <v-icon dark style="color: black">mdi-cached</v-icon>
      Actualizar
    </b-button>

    <!-- ================ALTA PROFESIONAL======================== -->
    <b-button
      class="mb-4 ml-2"
      v-b-modal.modal-alta
      @click="altaProfesional()"
      title="Nuevo Profesional"
      style="color: white"
    >
      <v-icon dark> mdi-plus </v-icon>
      Nuevo Profesional
    </b-button>
    <b-modal id="modal-alta" hide-footer>
      <template #modal-title><h5 class="modal-title">Alta</h5></template>
      <profesionales-alta />
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
          id="buscadorlista"
        ></b-form-input>
      </b-input-group>
    </div>
    <!-- ======================================== -->

    <b-table
      :fields="fields"
      striped
      sortable
      responsive
      hover
      :items="tabla_profesionales"
      show-empty
      :per-page="perPage"
      :current-page="currentPage"
      :sticky-header="true"
      :no-border-collapse="false"
      ref="tablaregistros"
      id="tablaregistros"
    >
      <template #empty="">
        <b>No hay registros para mostrar</b>
      </template>

      <template slot="cell(id_medico)" slot-scope="data">
        <b>{{ data.value }}</b>
      </template>

      <template slot="cell(apellido)" slot-scope="data">
        {{ data.value.toUpperCase() }}
      </template>

      <template slot="cell(nombre)" slot-scope="data">
        {{ data.value.toUpperCase() }}
      </template>
      <!-- 
      <template slot="action">
        <b-button variant="warning" size="sm">Modificar</b-button>
        <b-button variant="danger" size="sm">Eliminar</b-button>
      </template>
    -->
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
              @click="editarProfesional(row.item, row.index)"
            >
              <!-- :disabled="btn_editar" -->
              <v-icon class="mr-2"> mdi-pencil </v-icon>
              Editar
            </b-button>


            
            <b-button
            
              :to="{name:'ordenesProf',params:{prof: row.item}, query:{id: row.item.id_medico}}"
              variant="primary"
              id="button-3"
              title="Ver ordenes asociadas"
            >
              <!-- @click="ordenesProfesional(row.item)" -->
            <v-icon dark style="color:black;">mdi-format-list-bulleted-square</v-icon>                  
            Ordenes
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
        <b-card title="Datos del Profesional: ">
          <div>
            <b-list-group horizontal>
              <b-list-group class="col-3">
                <b-list-group-item
                  ><b>Fecha de ingreso:</b> {{ row.item.fecha_ingreso }}</b-list-group-item
                >
                <b-list-group-item
                  ><b>Matricula:</b>
                  {{row.item.matricula}}</b-list-group-item
                >
                <b-list-group-item
                  ><b>CUIT:</b> {{ row.item.cuit }}</b-list-group-item
                >
              </b-list-group>
              &nbsp;
              <b-list-group class="col-5">
                <b-list-group-item
                  ><b>Provincia:</b> {{ row.item.provincia }}</b-list-group-item
                >
                <b-list-group-item
                  ><b>Localidad:</b> {{ row.item.localidad }}</b-list-group-item
                >
                <b-list-group-item
                  ><b>Correo:</b> {{ row.item.email }}
                </b-list-group-item>
              </b-list-group>
              &nbsp;
              <b-list-group class="col-4">
                <b-list-group-item
                  ><b>Telefono Fijo:</b>
                  {{ row.item.tel_fijo }}</b-list-group-item
                >
                <b-list-group-item
                  ><b>Celular:</b> {{ row.item.tel_celular }}</b-list-group-item
                >
                <b-list-group-item
                  ><b>Calle:</b> {{ row.item.domicilio }}
                </b-list-group-item>
              </b-list-group>
            </b-list-group>
          </div>
        </b-card>
      </template>
    </b-table>
    <!-- 
    <b-modal id="modal-modificar" hide-footer> 
      <template #modal-title><h5 class="modal-title">Modificar Profesional</h5></template>
      <profesionales-alta/>
    </b-modal> -->
    <b-modal id="modal-editar" hide-footer>
      <template #modal-title>
        <h5 class="modal-title">Editar</h5>
      </template>
      <!-- {{ editar }} -->
      <profesionales-update :item_prof="editar" />
    </b-modal>

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
          {{ infoEliminar.profesional.apellido }},
          {{ infoEliminar.profesional.nombre }} ?
        </h3>
      </div>
      <b-button class="mt-2" block @click="hideModal" title="Volver Atras"
        >Volver Atras</b-button
      >
      <b-button
        class="mt-3"
        variant="danger"
        block
        title="Eliminar"
        @click="deleteProfesional(infoEliminar.profesional.id_medico)"
        >Eliminar</b-button
      >
    </b-modal>

    <b-container fluid>
      <b-col class="my-1">
        <b-pagination
          v-model="currentPage"
          align="center"
          pills
          :total-rows="rows"
          :per-page="perPage"
          aria-controls="table_profesionales"
        >
        </b-pagination>
      </b-col>
    </b-container>
  </div>
</template>

<script>
let api = new URL("http://localhost");
api.pathname = "profesionales";
//api.port = 8000;
api.port = 8081;

import ProfesionalesAlta from "./ProfesionalesAlta.vue";
import ProfesionalesUpdate from "./ProfesionalesUpdate.vue";
import axios from "axios";

export default {
  components: { ProfesionalesAlta, ProfesionalesUpdate },
  data() {
    return {
      tabla_profesionales: [],
      fields: [
        {
          key: "id_medico",
          label: "ID",
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
          label: "DNI",
          sortable: true,
        },
        {
          key: "especialidad",
          sortable: true,
        },
        { key: "action", label: "Acciones", variant: "secondary" },
      ],
      buscar: "",
      editar: {},
      totalRows: 1, //Total de filas
      currentPage: 1, //Pagina actual
      perPage: 3, // Datos en la tabla por pagina
      infoEliminar: {
        id: "modal_eliminar",
        profesional: -1,
      },
    };
  },

  computed: {
    rows() {
      return this.tabla_profesionales.length;
    },
    id() {
      return this.tabla_profesionales.id_medico;
    },
    items() {
      return tabla_profesionales.filter((item) => {
        return item.id_medico.toLowerCase().includes(this.buscar.toLowerCase());
      });
    },
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
    altaProfesional() {},
    //Funcion para mostrar el modal
    showModal() {
      this.$refs["my-modal"].show();
    },
    showModalinfo(item, index) {
      this.infoEliminar.profesional = item;
      this.showModal();
    },
    //Funcion para esconder el modal
    hideModal() {
      this.$refs["my-modal"].hide();
    },
    async deleteProfesional(id_medico) {
      axios
        .delete("http://localhost:8081/profesionales/" + id_medico + "/")
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
    editarProfesional(item, index) {
      this.editar = item;
    },
    ordenesProfesional(item) {
      this.editar = item;
      
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
      input = document.getElementById("buscadorlista");
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
  },
  beforeMount() {
    this.testFetch();
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
