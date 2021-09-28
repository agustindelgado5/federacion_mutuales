<template>
  <div id="listadoPagos" class="myTable">
    <vue-headful
      title="Listado de Pagos a los Profesionales - Federación Tucumana de Mutuales"
    ></vue-headful>

    <h2>Listado de Pagos a los Profesionales</h2>
    <b-button @click="getOrdenes()" class="mb-4" title="Recargar" variant="light">
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
          id="buscadorlista"
        ></b-form-input>
      </b-input-group>
    </div>
    <!-- ======================================== -->
    <!-- 
    <section class="container">
    -->
    <section>
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

      <template slot="cell(profesional)" slot-scope="data">
        {{ data.value.toUpperCase() }}
      </template>

      <template slot="cell(precio)" slot-scope="data">
        <b>$ {{ data.value }}</b>
      </template>

      

      <template slot="cell(fecha)" slot-scope="data">
        {{ data.value.split('-')[2] }}/{{ data.value.split('-')[1] }}/{{ data.value.split('-')[0] }}
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
              @click="editarPago(row.item, row.index)"
            >
              <!-- :disabled="btn_editar" -->
              <v-icon class="mr-2"> mdi-pencil </v-icon>
              Editar
            </b-button>

            <b-button 
              @click="generarPDF(row.item)"
              id="btn_down_pdf" 
              
              title="Generar PDF" 
              variant="danger" 
              style="color: white;"
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-file-pdf-fill" viewBox="0 0 16 16">
                <path d="M5.523 10.424c.14-.082.293-.162.459-.238a7.878 7.878 0 0 1-.45.606c-.28.337-.498.516-.635.572a.266.266 0 0 1-.035.012.282.282 0 0 1-.026-.044c-.056-.11-.054-.216.04-.36.106-.165.319-.354.647-.548zm2.455-1.647c-.119.025-.237.05-.356.078a21.035 21.035 0 0 0 .5-1.05 11.96 11.96 0 0 0 .51.858c-.217.032-.436.07-.654.114zm2.525.939a3.888 3.888 0 0 1-.435-.41c.228.005.434.022.612.054.317.057.466.147.518.209a.095.095 0 0 1 .026.064.436.436 0 0 1-.06.2.307.307 0 0 1-.094.124.107.107 0 0 1-.069.015c-.09-.003-.258-.066-.498-.256zM8.278 4.97c-.04.244-.108.524-.2.829a4.86 4.86 0 0 1-.089-.346c-.076-.353-.087-.63-.046-.822.038-.177.11-.248.196-.283a.517.517 0 0 1 .145-.04c.013.03.028.092.032.198.005.122-.007.277-.038.465z"/>
                <path fill-rule="evenodd" d="M4 0h8a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2zm.165 11.668c.09.18.23.343.438.419.207.075.412.04.58-.03.318-.13.635-.436.926-.786.333-.401.683-.927 1.021-1.51a11.64 11.64 0 0 1 1.997-.406c.3.383.61.713.91.95.28.22.603.403.934.417a.856.856 0 0 0 .51-.138c.155-.101.27-.247.354-.416.09-.181.145-.37.138-.563a.844.844 0 0 0-.2-.518c-.226-.27-.596-.4-.96-.465a5.76 5.76 0 0 0-1.335-.05 10.954 10.954 0 0 1-.98-1.686c.25-.66.437-1.284.52-1.794.036-.218.055-.426.048-.614a1.238 1.238 0 0 0-.127-.538.7.7 0 0 0-.477-.365c-.202-.043-.41 0-.601.077-.377.15-.576.47-.651.823-.073.34-.04.736.046 1.136.088.406.238.848.43 1.295a19.707 19.707 0 0 1-1.062 2.227 7.662 7.662 0 0 0-1.482.645c-.37.22-.699.48-.897.787-.21.326-.275.714-.08 1.103z"/>
              </svg>
              Generar PDF
            </b-button>
          </b-button-group>
        </div>
      </template>
     
      </b-table>

      <b-modal id="modal-editar" hide-footer ref="my-modal">
      <template #modal-title>
        <h5 class="modal-title">Editar: {{editar.numero_orden}}</h5>
      </template>
      <b-form>
        <b-form-group
          label="Elija la forma de pago"
        >
          <b-form-select
            v-model="selected"
            :options="options"
            class="mb-3"
            type="text"
            required
          ></b-form-select>
        </b-form-group>
        
        <b-button class="mt-2" variant="success" block @click="putModoPago(editar.numero_orden)">
          <b>GUARDAR</b>
        </b-button>
      </b-form>
      </b-modal>
      <!-- ==================================CREAR PDF================================== -->
      <vue-html2pdf
      :show-layout="false"
      :float-layout="true"
      :enable-download="false"
      :preview-modal="true"
      :paginate-elements-by-height="1400"
      filename="DetallePago"
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
          <h3>Comprobante de pago</h3>
           
            

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
    </section>
    <!---
    <aside>
      <div>
        <b-card-group deck>
          <b-card bg-variant="primary" text-variant="white" header="FILTRAR POR AÑO" class="text-center">
            <b-card-text>
             
            </b-card-text>
          </b-card>
        </b-card-group>
      </div>
    </aside>
    -->

  </div>
  
</template>

<script>

let api = new URL("http://localhost");
api.pathname = "ordenes";
//api.port = 8000;
api.port = 8081;


import axios from "axios";
import VueHtml2pdf from "vue-html2pdf";
import { APIControler } from "../store/APIControler";
import swal from 'sweetalert';


export default {
  components: { VueHtml2pdf },
  data() {
    return {
      tabla_profesionales: [],
      data: {},
      tabla_ordenes:[],
      //profesionales:[],
      fields: [
        {
          key: "id_medico",
          label: "ID",
          sortable: true,
        },
        {
          key: "profesional",
          label: "Nombre Completo",
          sortable: true,
        },
        {
          key: "mes",
          label: "Mes",
          sortable: true,
        },
        {
          key: "numero_orden",
          label: "N° de Orden",
          sortable: true,
        },
        {
          key: "fecha",
          label: "Fecha",
          sortable: true,
        },
        {
          key: "precio",
          label: "Precio",
          sortable: true,
        },
        {
          key: "formaPago",
          label: "Forma de Pago",
          sortable: true,
        },
        { key: "action", label: "Acciones", variant: "secondary" },
      ],
      buscar: "",
      editar: {},
      selected:null,
      totalRows: 1, //Total de filas
      currentPage: 1, //Pagina actual
      perPage: 30, // Datos en la tabla por pagina
      ordenAPDF: {},
      options:[
        {value: null, text :'--------ELIJA UNA FORMA DE PAGO--------', disabled: true},
        {value: 'Contado', text :'Contado'},
        {value: 'Transferencia', text :'Transferencia'},
      ] 
    };
  },

  computed: {
    rows() {
      return this.tabla_ordenes.length;
    },
  },

  methods: {
    
    async getProfesional(id) {
      let profesionalAPI = new APIControler();
      profesionalAPI.apiUrl.pathname = "profesionales/" + id;
      let response = await fetch(profesionalAPI.apiUrl);
      let data = await response.json();
      return data;
    },
    

    async getOrdenes() {
      try {
        const res = await fetch(api);
        const data = await res.json();
        var lista_orden = data.results;
        var modo_pago = null;

        for (var i = 0; i < lista_orden.length; i++) {
           var medico = await this.getProfesional(lista_orden[i].id_medico.split('/')[4]);
           lista_orden[i].id_medico = medico.id_medico;
           lista_orden[i].profesional = medico.apellido + ', ' + medico.nombre;
           lista_orden[i].dni = medico.dni;
           lista_orden[i].formaPago = modo_pago;
           //lista_orden[i].mes= formatMesAnio(lista_orden[i].fecha.split('-')[1],lista_orden[i].fecha.split('-')[0]);
           lista_orden[i].mes= lista_orden[i].fecha.split('-')[1]+'/'+lista_orden[i].fecha.split('-')[0];
        }
        console.log(lista_orden);
        
        


        this.tabla_ordenes = lista_orden;

        //this.btn_down_pdf=false;  //Habilito los botones

        if(this.tabla_ordenes.length==0){
          this.msj_tabla = " No se encuentran regitros en esta tabla ";
        }
        //this.saveFile();

      } catch (error) {
        console.log(error);
      }
    },


    //altaProfesional() {},
    //Funcion para mostrar el modal
    showModal() {
      this.$refs["my-modal"].show();
    },
    
    //Funcion para esconder el modal
    hideModal() {
      this.$refs["my-modal"].hide();
    },

    formatMesAnio(mes, anio){
      var meses =[
        ('ENE','01'),
        ('FEB','02'),
        ('MAR','03'),
        ('ABR','04'),
        ('MAY','05'),
        ('JUN','06'),
        ('JUL','07'),
        ('AGO','08'),
        ('SEP','09'),
        ('OCT','10'),
        ('NOV','11'),
        ('DIC','12'),
      ];
      let mesMM = meses.filter(meses => meses[0]== mes);
      return mesMM +'/'+ anio;
    },


    editarPago(item, index) {
      this.editar = item;
      console.log(this.editar);
      this.showModal();
    },

    putModoPago(num_orden){
      try{
        for(var i=0; i<this.tabla_ordenes.length; i++){
          if(this.tabla_ordenes[i].numero_orden == num_orden){
            this.tabla_ordenes[i].formaPago=this.selected;
            break;
          }
          
        }
        this.hideModal();
        swal('¡ESTADO GUARDADO¡', ' ', 'success');
        console.log(this.tabla_ordenes);
        //this.getOrdenes();
      }
      catch(error){
        this.hideModal();
        swal('¡ERROR¡', 'No se pudo guardar los cambios ', 'error');
        console.log(error);
        //this.getOrdenes();
      }
      finally{
        return this.tabla_ordenes;
      }
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
        idMedico,
        Medico,
        Mes,
        NumOrden,
        Date_,
        Precio,
      input = document.getElementById("buscadorlista");
      filter = input.value.toUpperCase();
      table = document.getElementById("tablaregistros");
      tr = table.getElementsByTagName("tr");

      // Loop through all list items, and hide those who don't match the search query
      for (i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td");
        idMedico = td[0].textContent || td[0].innerText;
        Medico = td[1].textContent || td[1].innerText;
        Mes = td[2].textContent || td[2].innerText;
        NumOrden = td[3].textContent || td[3].innerText;
        Date_ = td[4].textContent || td[4].innerText;
        Precio = td[5].textContent || td[5].innerText;
        txtValue = idMedico + Medico + Mes + NumOrden + Date_ + Precio;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    },

    generarPDF(item){
      this.ordenAPDF = {...item};
      this.$refs.html2Pdf.generatePdf();
    },

    //Creo archivo JSON
    saveFile() {
      const data = JSON.stringify(this.tabla_ordenes)
      window.localStorage.setItem('arr', data);
      console.log(JSON.parse(window.localStorage.getItem('arr')))
    }
  },
  beforeMount() {
    this.getOrdenes();
    //this.saveFile();
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
/*
.container {
  float: left;
  width: 85%
}
aside{
  float: right;
  width: 15%;
}
*/
</style>
