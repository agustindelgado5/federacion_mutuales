<template>
  <div id="ordenes" class="myTable">
    <!--HEAD DE LA PAGINA -->
    <vue-headful
      title="Mis Ordenes - Federación Tucumana de Mutuales"
    ></vue-headful>

    <h2>Bienvenido/a {{this.profesional.nombre}}</h2>
    <h2>Listado de Ordenes</h2>
    <b-button @click="testFetch" class="mb-4" title="Recargar" variant="light">
      <v-icon dark style="color: black">mdi-cached</v-icon>
      Actualizar
    </b-button>

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
      :items="tabla_ordenes"
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
      <template slot="cell(numero_orden)" slot-scope="data">
        <b>{{ data.value }}</b>
      </template>
      <template slot="cell(id_mutual)" slot-scope="data">
        {{ data.value.split("/")[4] }}
      </template>

      <template slot="cell(precio)" slot-scope="data">
        $ {{ data.value }}
      </template>

      <template slot="cell(realizado)" slot-scope="data">
        <div v-if="data.value === true">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            class="bi bi-check-circle-fill"
            viewBox="0 0 16 16"
            style="color: green"
          >
            <path
              d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"
            />
          </svg>
          SI
        </div>
        <div v-else>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            class="bi bi-x-circle-fill"
            viewBox="0 0 16 16"
            style="color: red"
          >
            <path
              d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM5.354 4.646a.5.5 0 1 0-.708.708L7.293 8l-2.647 2.646a.5.5 0 0 0 .708.708L8 8.707l2.646 2.647a.5.5 0 0 0 .708-.708L8.707 8l2.647-2.646a.5.5 0 0 0-.708-.708L8 7.293 5.354 4.646z"
            />
          </svg>
          NO
        </div>
      </template>
      <template slot="cell(action)" slot-scope="row">
        <div class="mt-3">
          <b-button-group>
            <!-- ==================================CREAR PDF================================== -->
            <!-- Generar PDF -->
            <b-button
              @click="generarPDF(row.item)"
              id="btn_down_pdf"
              class="mb-0 ml-2"
              title="Generar PDF"
              variant="info"
              style="color: white"
            >
              <!-- :disabled="btn_down_pdf" -->
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-file-pdf-fill"
                viewBox="0 0 16 16"
              >
                <path
                  d="M5.523 10.424c.14-.082.293-.162.459-.238a7.878 7.878 0 0 1-.45.606c-.28.337-.498.516-.635.572a.266.266 0 0 1-.035.012.282.282 0 0 1-.026-.044c-.056-.11-.054-.216.04-.36.106-.165.319-.354.647-.548zm2.455-1.647c-.119.025-.237.05-.356.078a21.035 21.035 0 0 0 .5-1.05 11.96 11.96 0 0 0 .51.858c-.217.032-.436.07-.654.114zm2.525.939a3.888 3.888 0 0 1-.435-.41c.228.005.434.022.612.054.317.057.466.147.518.209a.095.095 0 0 1 .026.064.436.436 0 0 1-.06.2.307.307 0 0 1-.094.124.107.107 0 0 1-.069.015c-.09-.003-.258-.066-.498-.256zM8.278 4.97c-.04.244-.108.524-.2.829a4.86 4.86 0 0 1-.089-.346c-.076-.353-.087-.63-.046-.822.038-.177.11-.248.196-.283a.517.517 0 0 1 .145-.04c.013.03.028.092.032.198.005.122-.007.277-.038.465z"
                />
                <path
                  fill-rule="evenodd"
                  d="M4 0h8a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2zm.165 11.668c.09.18.23.343.438.419.207.075.412.04.58-.03.318-.13.635-.436.926-.786.333-.401.683-.927 1.021-1.51a11.64 11.64 0 0 1 1.997-.406c.3.383.61.713.91.95.28.22.603.403.934.417a.856.856 0 0 0 .51-.138c.155-.101.27-.247.354-.416.09-.181.145-.37.138-.563a.844.844 0 0 0-.2-.518c-.226-.27-.596-.4-.96-.465a5.76 5.76 0 0 0-1.335-.05 10.954 10.954 0 0 1-.98-1.686c.25-.66.437-1.284.52-1.794.036-.218.055-.426.048-.614a1.238 1.238 0 0 0-.127-.538.7.7 0 0 0-.477-.365c-.202-.043-.41 0-.601.077-.377.15-.576.47-.651.823-.073.34-.04.736.046 1.136.088.406.238.848.43 1.295a19.707 19.707 0 0 1-1.062 2.227 7.662 7.662 0 0 0-1.482.645c-.37.22-.699.48-.897.787-.21.326-.275.714-.08 1.103z"
                />
              </svg>
              <!-- ============================================================================== -->
            </b-button>
            
            <b-button
              variant="primary"
              id="button-3"
              @click="showModalinfo(row.item, row.index)"
              title="Marcar como realizada"
              style="color: white"
            >
              <v-icon class="mr-2" style="color: white"> mdi-check </v-icon>
              Declarar
            </b-button>
          </b-button-group>
        </div>
      </template>
      
    </b-table>
    <!-- ================DECLARAR ORDEN======================== -->

    <b-modal
      id="modal_declarar"
      ref="my-modal"
      hide-footer
      title="Declarar"
      ok-only
    >
      <div class="d-block text-center">
        <h3>
          Para solicitar el pago, debe ingresar el token para la orden Nº
          {{ infoDeclarar.orden.numero_orden }}
        </h3>
        
      <b-form @submit.prevent="">
      <b-form-group >
        <b-form-input
          id="servicio"
          v-model="token"
          type="text"
          placeholder="*Ingrese el token"
          @keydown.enter.prevent
        >
        </b-form-input>
      </b-form-group>
      
      </b-form>
      </div>
      <b-button class="mt-2" block @click="hideModal" title="Volver Atras"
        >Volver Atras</b-button
      >
      <b-button
        class="mt-3"
        variant="primary"
        block
        style="color: white"
        @click="declareOrden(infoDeclarar.orden.numero_orden)"
        title="Declarar"
      >
        Declarar
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
          aria-controls="table_ordenes"
        >
        </b-pagination>
      </b-col>
    </b-container>
   

    <!-- ==================================CREAR PDF================================== -->
    <vue-html2pdf
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
        <!-- PDF Content Here -->
        <section class="pdf-item">
          <h3>Federación Tucumana de Mutuales</h3>
          <img
            src="../assets/logo.jpg"
            alt="Logo Federación"
            srcset=""
            id="Logo_fed"
          />
        </section>
        <section class="pdf-item">
          <h3>Orden Médica</h3>
          <b-list-group>
            <b-list-group-item
              v-for="value in fields.slice(0, -1)"
              :key="value.key"
              >{{ value.label }}: {{ ordenAPDF[value.key] }}</b-list-group-item
            >
          </b-list-group>
        </section>
      </section>
    </vue-html2pdf>
    <!-- ============================================================================== -->
  </div>
</template>

<script>
let api = new URL("http://localhost");
api.pathname = "ordenes";
//api.port = 8000;
api.port = 8081;

import VueHtml2pdf from "vue-html2pdf";

import axios from "axios";

export default {
  components: { VueHtml2pdf },
  
  data() {
    return {
      tabla_ordenes: [],
      profesional: {},
      fields: [
        { key: "numero_orden", label: "N° Orden", sortable: true },
        { key: "servicio", label: "Servicio", sortable: true },
        { key: "id_mutual", label: "Id Mutual", sortable: true },
        { key: "fecha", label: "Fecha", sortable: true },
        { key: "hora", label: "Hora", sortable: true },
        { key: "precio", label: "Precio", sortable: true },
        { key: "realizado", label: "Realizado", sortable: true },
        { key: "action", label: "Acciones", variant: "secondary" },
      ],
      totalRows: 1, //Total de filas
      currentPage: 1, //Pagina actual
      perPage: 10, // Datos en la tabla por pagina
      buscar: "",
      token: "",
      infoDeclarar: {
        id: "modal_declarar",
        orden: -1,
      },
      ordenAPDF: {}, //Se carga cuando se hace clic en exportar a pdf, con la orden a exportar
    };
  },
  computed: {
    rows() {
      return this.tabla_ordenes.length;
    },
    id() {
      return this.tabla_ordenes.numero_orden;
    },
    items() {
      return tabla_ordenes.filter((item) => {
        return item.numero_orden
          .toLowerCase()
          .includes(this.buscar.toLowerCase());
      });
    },
  },
  methods: {
    async testFetch() {
      try { 
        if(typeof this.$route.params.prof ==="undefined" ){
          console.log("Profesional vacio")
          const baseURL="http://localhost:8081";
          const response = await axios.get(baseURL+"/profesionales/"+this.$route.query.id)
          this.profesional=response.data          
        }

        const res = await fetch(api);
        const data = await res.json();

        var lista_ordenes = data.results.filter(item=>{
          return item.id_medico.split('/')[4]==this.profesional.id_medico
          });

        this.tabla_ordenes = lista_ordenes;
      } catch (error) {
        console.log(error);
      }
    },
    
    //Funcion para mostrar el modal
    showModal() {
      this.$refs["my-modal"].show();
    },
    showModalinfo(item, index) {
      this.infoDeclarar.orden = item;
      this.showModal();
    },
    //Funcion para esconder el modal
    hideModal() {
      this.$refs["my-modal"].hide();
    },
  
    async declareOrden(nro_orden) {
      var baseURL="http://localhost:8081"
      const response = await axios.get(baseURL+"/ordenes/"+nro_orden+"/declararOrden/?token="+this.token)
      
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
        // .finally(() => this.testFetch());
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
        p1, //nro de orden
        p2, //nro de socio
        p3, //servicio
        p4, //id medico
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
        p3 = td[3].textContent || td[3].innerText;
        p4 = td[4].textContent || td[4].innerText;
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
    this.profesional=this.$route.params.prof || {}
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
