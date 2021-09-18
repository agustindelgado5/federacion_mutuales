<template>
  <div id="recetas" class="myTable">
    <!--HEAD DE LA PAGINA -->
    <vue-headful
      title="Recetas - Federación Tucumana de Mutuales"
    ></vue-headful>

    <h2>Listado de Recetas</h2>
    <b-button @click="testFetch" class="mb-4" title="Recargar" variant="light">
      <v-icon dark style="color: black">mdi-cached</v-icon>
      Actualizar
    </b-button>

    <!-- ================ALTA RECETAS======================== -->
    <b-button
      class="mb-4 ml-2"
      v-b-modal.modal-alta
      @click="altaReceta()"
      title="Nueva Receta"
      style="color: white"
    >
      <v-icon dark> mdi-plus </v-icon>
      Nueva Receta
    </b-button>
    <b-modal id="modal-alta" hide-footer>
      <template #modal-title><h5 class="modal-title">Alta</h5></template>
      <recetas-alta />
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
      hover
      :items="tabla_recetas"
      show-empty
      :per-page="perPage"
      :current-page="currentPage"
      :no-border-collapse="false"
      ref="tablaregistros"
      id="tablaregistros"
    >
      <!-- :sticky-header="true" -->
      <template #empty="">
        <b>No hay registros para mostrar</b>
      </template>
      <template slot="cell(numero_socio)" slot-scope="data">
        {{ data.value.split("/")[4] }}
      </template>
      <template slot="cell(paciente)" slot-scope="data">
        {{ data.value.split("/")[4] }}
      </template>
      <template slot="cell(id_medicamento)" slot-scope="data">
        {{ data.value.split("/")[4] }}
      </template>
      <template slot="cell(cod_farmacia)" slot-scope="data">
        {{ data.value.split("/")[4] }}
      </template>

      <template slot="cell(action)" slot-scope="row">
        <div class="mt-3">
          <b-button-group>
            <!-- <b-button variant="info" id="button-1" title="Mostrar Info"
              >Mostrar Info</b-button
            > -->

            <b-button
              variant="warning"
              id="button-2"
              title="Editar este registro"
              v-b-modal.modal-editar
              @click="editarReceta(row.item, row.index)"
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
    </b-table>

    <!-- ================ELIMINAR RECETA======================== -->

    <b-modal
      id="modal_eliminar"
      ref="my-modal"
      hide-footer
      title="Eliminar"
      ok-only
    >
      <div class="d-block text-center">
        <h3>
          ¿Esta seguro de eliminar los datos de la receta
          {{ infoEliminar.receta.id_receta }}?
        </h3>
      </div>
      <b-button class="mt-2" block @click="hideModal" title="Volver Atras"
        >Volver Atras</b-button
      >
      <b-button
        class="mt-3"
        variant="danger"
        block
        @click="deleteReceta(infoEliminar.receta.id_receta)"
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
          aria-controls="table_receta"
        >
        </b-pagination>
      </b-col>
    </b-container>
    <b-modal id="modal-editar" hide-footer>
      <template #modal-title><h5 class="modal-title">Editar</h5></template>
      <recetas-update :receta="editar" />
    </b-modal>

  </div>
</template>

<script>
let api = new URL("http://localhost");
api.pathname = "recetas";
//api.port = 8000;
api.port = 8081;

import RecetasAlta from "./RecetasAlta.vue";
import RecetasUpdate from "./RecetasUpdate.vue";
import axios from "axios";


export default {
  components: { RecetasAlta,RecetasUpdate },
  data() {
    return {
      tabla_recetas: [],
      fields: [
        { key: "id_receta", label: "N° Receta", sortable: true },
        { key: "numero_socio", label: "N° Socio", sortable: true },
        { key: "paciente", label: "Paciente", sortable: true },
        { key: "diagnostico", label: "Diagnostico", sortable: true },
        { key: "id_medicamento", label: "Id Medicamento", sortable: true },
        { key: "cod_farmacia", label: "Id Farmacia", sortable: true },
        { key: "fecha", label: "Fecha", sortable: true },
        { key: "carencia", label: "Carencia", sortable: true },
        { key: "action", label: "Acciones", variant: "secondary" },
      ],
      totalRows: 1, //Total de filas
      currentPage: 1, //Pagina actual
      perPage: 10, // Datos en la tabla por pagina
      buscar: "",
      editar: {},
      infoEliminar: {
        receta: -1,
      },
    };
  },
  computed: {
    rows() {
      return this.tabla_recetas.length;
    },
    id() {
      return this.tabla_recetas.id_receta;
    },
    items() {
      return tabla_recetas.filter((item) => {
        return item.id_receta
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

        var lista_recetas = data.results;

        console.log(lista_recetas);

        this.tabla_recetas = lista_recetas;
      } catch (error) {
        console.log(error);
      }
    },
    editarReceta(item, index) {
      this.editar = item;
    },
    //Muestra el modal de eliminar
    showModalinfo(item, index) {
      this.infoEliminar.receta = item;
      this.showModal();
    },
    //Funcion para mostrar el modal
    showModal() {
      this.$refs["my-modal"].show();
    },
    //Funcion para esconder el modal
    hideModal() {
      this.$refs["my-modal"].hide();
    },
    altaReceta() {},
    
    async deleteReceta(nro_receta) {
        axios
          .delete("http://localhost:8081/recetas/" + nro_receta + "/")
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
          p1, //nro de receta
          p2, //nro de socio
          p3, //paciente
          p4, //diagnostico
          p5; //fecha
        input = this.$refs.buscadorlista;
        filter = input.value.toUpperCase();
        table = document.getElementById("tablaregistros");
        tr = table.getElementsByTagName("tr");

        // Loop through all list items, and hide those who don't match the search query
        for (i = 1; i < tr.length; i++) {
          td = tr[i].getElementsByTagName("td");
          p1 = td[0].textContent || td[0].innerText;
          p2 = td[1].textContent || td[1].innerText;
          p4 = td[2].textContent || td[2].innerText;
          p3 = td[3].textContent || td[3].innerText;
          p5 = td[6].textContent || td[6].innerText;
          txtValue = p1 + p2 + p3 + p4 + p5;
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
