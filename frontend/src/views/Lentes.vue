<template>
  <div id="lentes" class="myTable">
    <!--HEAD DE LA PAGINA -->
    <vue-headful
      title="Lentes - Federación Tucumana de Mutuales"
    ></vue-headful>

    <h2>Listado de Lentes</h2>
    <b-button @click="testFetch" class="mb-4" title="Recargar" variant="light">
      <v-icon dark style="color: black">mdi-cached</v-icon>
      Actualizar
    </b-button>

    <!-- ================ALTA Lentes======================== -->
    <b-button
      class="mb-4 ml-2"
      v-b-modal.modal-alta
      @click="altaLente()"
      title="Nuevo Lente"
      style="color: white"
    >
      <v-icon dark> mdi-plus </v-icon>
      Nuevo Lente
    </b-button>
    <b-modal id="modal-alta" hide-footer>
      <template #modal-title><h5 class="modal-title">Alta</h5></template>
      <lentes-alta />
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
      :items="tabla_lentes"
      show-empty
      :per-page="perPage"
      :current-page="currentPage"
      :no-border-collapse="false"
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
              variant="warning"
              id="button-2"
              title="Editar este registro"
              v-b-modal.modal-editar
              @click="editarLente(row.item, row.index)"
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
      <!-- 
      <template slot="action">
        <b-button variant="warning" size="sm">Modificar</b-button>
        <b-button variant="danger" size="sm">Eliminar</b-button>
      </template>
    -->
    </b-table>
    <!-- ================ELIMINAR Lente======================== -->

    <b-modal
      id="modal_eliminar"
      ref="my-modal"
      hide-footer
      title="Eliminar"
      ok-only
    >
      <div class="d-block text-center">
        <h3>
          ¿Esta seguro de eliminar los datos de la cirugia
          {{ infoEliminar.lente.codigo_optica }}?
        </h3>
      </div>
      <b-button class="mt-2" block @click="hideModal" title="Volver Atras"
        >Volver Atras</b-button
      >
      <b-button
        class="mt-3"
        variant="danger"
        block
        @click="deleteCirugia(infoEliminar.lente.codigo_optica)"
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
          aria-controls="tabla_lentes"
        >
        </b-pagination>
      </b-col>
    </b-container>
    <b-modal id="modal-editar" hide-footer>
      <template #modal-title><h5 class="modal-title">Editar</h5></template>
      <lentes-update :lente="editar" />
    </b-modal>

    <!-- ==================================CREAR PDF================================== -->
    <!-- <vue-html2pdf
      :show-layout="false"
      :float-layout="true"
      :enable-download="false"
      :preview-modal="true"
      :paginate-elements-by-height="1400"
      filename="DetalleOrden"
      :pdf-quality="2"
      :manual-pagination="false"
      pdf-format="a4"
      pdf-orientation="portrait"
      pdf-content-width="80%"
      @progress="onProgress($event)"
      @startPagination="startPagination()"
      @hasPaginated="hasPaginated()"
      @beforeDownload="beforeDownload($event)"
      @hasDownloaded="hasDownloaded($event)"
      ref="html2Pdf"
    >
      <section slot="pdf-content">
 
     
          <h3>Federación Tucumana de Mutuales</h3>
          <img
            src="../assets/logo.jpg"
            alt="Logo Federación"
            srcset=""
            id="Logo_fed"
          />
        </section>
        <section class="pdf-item">
          <h3>Orden Médica</h3> -->
          <!-- <b-table
              :fields="fields"
              responsive
              :items="tabla_cirugias"
              :no-border-collapse= false
              small
              fixed
              bordered
              head-variant="light"
            >
              
                {{data.value.split('/')[4]}}
              </template> 
            </b-table> -->
<!-- 
          <b-list-group>
            <b-list-group-item
              v-for="value in fields.slice(0, -1)"
              :key="value.key"
              >{{ value.label }}: {{ ordenAPDF[value.key] }}</b-list-group-item
            >
          </b-list-group>
        </section>
      </section>
    </vue-html2pdf>  -->
    <!-- ============================================================================== -->
  </div>
</template>

<script>
let api = new URL("http://localhost");
api.pathname = "lentes";
//api.port = 8000;
api.port = 8081;

import LentesAlta from "./LentesAlta.vue";
import LentesUpdate from "./LentesUpdate.vue";
import VueHtml2pdf from "vue-html2pdf";

import axios from "axios";

export default {
  components: { LentesAlta, LentesUpdate, VueHtml2pdf },
  data() {
    return {
      tabla_lentes: [],
      fields: [
        { key: "codigo_optica", label: "Codigo Optica", sortable: true },
        { key: "codigo_seguimiento", label: "Codigo Seguimiento", sortable: true },
        { key: "medida_lente", label: "Medida Lente", sortable: true },
        { key: "patillas", label: "Patillas", sortable: true },
        { key: "marca", label: "Marca", sortable: true },
        { key: "descripcion", label: "Descripcion", sortable: true },
        { key: "precio_laboratorio", label: "Precio Laboratorio", sortable: true },
        { key: "precio_optica", label: "Precio Optica", sortable: true },
        { key: "precio_mutual", label: "Precio Mutual", sortable: true },
        { key: "precio_venta", label: "Precio Venta", sortable: true },
        { key: "precio_tarjeta", label: "Precio Tarjeta", sortable: true },
        { key: "stock", label: "Stock", sortable: true },
        { key: "action", label: "Acciones", variant: "secondary" },
      ],
      totalRows: 1, //Total de filas
      currentPage: 1, //Pagina actual
      perPage: 10, // Datos en la tabla por pagina
      buscar: "",
      editar: {},
      infoEliminar: {
        id: "modal_eliminar",
        lente: -1,
      },
    };
  },
  computed: {
    rows() {
      return this.tabla_lentes.length;
    },
    id() {
      return this.tabla_lentes.codigo_optica
      ;
    },
    items() {
      return tabla_lentes.filter((item) => {
        return item.codigo_optica
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

        var lista_lentes = data.results;

        console.log(lista_lentes);

        this.tabla_lentes = lista_lentes;
      } catch (error) {
        console.log(error);
      }
    },
    editarLente(item, index) {
      this.editar = item;
    },
    //Funcion para mostrar el modal
    showModal() {
      this.$refs["my-modal"].show();
    },
    showModalinfo(item, index) {
      this.infoEliminar.lente = item;
      this.showModal();
    },
    //Funcion para esconder el modal
    hideModal() {
      this.$refs["my-modal"].hide();
    },
    altaLente() {},

    async deleteLente(codigo_optica) {
      axios
        .delete("http://localhost:8081/lentes/" + codigo_optica + "/")
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
        p1, //codigo_optica
        p2, //medida_lente
        p3; //patillas
        p4; //marca
        p5; //descripcion
       
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
        p4 = td[3].textContent || td[2].innerText;
        p5 = td[4].textContent || td[2].innerText;
        
        
        txtValue = p1 + p2 + p3 + p4 + p5  ;
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
