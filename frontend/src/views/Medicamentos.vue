<template>
  <div id="medicamentos" class="myTable">

    <!--HEAD DE LA PAGINA -->
    <vue-headful title="Medicamentos - Federación Tucumana de Mutuales"></vue-headful>

    <h2>Listado de Medicamentos</h2>

    <b-button @click="testFetch" class="mb-4" variant="light">
      <v-icon dark style="color:black;">mdi-format-list-bulleted-square</v-icon>
      Mostrar
    </b-button>
    <!-- ================ALTA MEDICAMENTOS======================== -->
    <b-button class="mb-4 ml-2" v-b-modal.modal-alta @click="altaMedicamento()" title="Nuevo Medicamento" style="color: white;">
      <v-icon dark>
        mdi-plus
      </v-icon>
      Nuevo Medicamento
    </b-button>
    <b-modal id="modal-alta" hide-footer> 
      <template #modal-title><h5 class="modal-title">Alta</h5></template>
      <medicamento-alta/>
    </b-modal>

    <b-button @click="generarPDF()"
      id="btn_down_pdf" 
      class="mb-4 ml-2" 
      title="Generar PDF" 
      variant="danger" 
      style="color: white;"
      :disabled="btn_down_pdf"
    >
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-file-pdf-fill" viewBox="0 0 16 16">
        <path d="M5.523 10.424c.14-.082.293-.162.459-.238a7.878 7.878 0 0 1-.45.606c-.28.337-.498.516-.635.572a.266.266 0 0 1-.035.012.282.282 0 0 1-.026-.044c-.056-.11-.054-.216.04-.36.106-.165.319-.354.647-.548zm2.455-1.647c-.119.025-.237.05-.356.078a21.035 21.035 0 0 0 .5-1.05 11.96 11.96 0 0 0 .51.858c-.217.032-.436.07-.654.114zm2.525.939a3.888 3.888 0 0 1-.435-.41c.228.005.434.022.612.054.317.057.466.147.518.209a.095.095 0 0 1 .026.064.436.436 0 0 1-.06.2.307.307 0 0 1-.094.124.107.107 0 0 1-.069.015c-.09-.003-.258-.066-.498-.256zM8.278 4.97c-.04.244-.108.524-.2.829a4.86 4.86 0 0 1-.089-.346c-.076-.353-.087-.63-.046-.822.038-.177.11-.248.196-.283a.517.517 0 0 1 .145-.04c.013.03.028.092.032.198.005.122-.007.277-.038.465z"/>
        <path fill-rule="evenodd" d="M4 0h8a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2zm.165 11.668c.09.18.23.343.438.419.207.075.412.04.58-.03.318-.13.635-.436.926-.786.333-.401.683-.927 1.021-1.51a11.64 11.64 0 0 1 1.997-.406c.3.383.61.713.91.95.28.22.603.403.934.417a.856.856 0 0 0 .51-.138c.155-.101.27-.247.354-.416.09-.181.145-.37.138-.563a.844.844 0 0 0-.2-.518c-.226-.27-.596-.4-.96-.465a5.76 5.76 0 0 0-1.335-.05 10.954 10.954 0 0 1-.98-1.686c.25-.66.437-1.284.52-1.794.036-.218.055-.426.048-.614a1.238 1.238 0 0 0-.127-.538.7.7 0 0 0-.477-.365c-.202-.043-.41 0-.601.077-.377.15-.576.47-.651.823-.073.34-.04.736.046 1.136.088.406.238.848.43 1.295a19.707 19.707 0 0 1-1.062 2.227 7.662 7.662 0 0 0-1.482.645c-.37.22-.699.48-.897.787-.21.326-.275.714-.08 1.103z"/>
      </svg>
      Generar PDF
    </b-button>

    <b-button
      class="mb-4 ml-2"
      variant="danger"
      id="btn_del_full"
      title="Eliminar todos los registros"
      style="color: white;"
      :disabled="btn_del_full"
      v-b-modal.modal-eliminarTodo 
    >
      <v-icon class="mr-2" style="color: white;">
        mdi-delete
      </v-icon>
        Eliminar todos los registros
    </b-button>

    

    <!--
    <div v-for="item in tabla_med" :key="item.id_medicamento">
    -->
    <div>  
      <b-modal id="modal-eliminarTodo" hide-footer title="Eliminar" ok-only>
        <div class="d-block text-center">
          <h3>¿Esta seguro de eliminar todos los datos ?</h3>
        </div>
        <b-button
          class="mt-2"
          block
          @click="hideModal"
          title="Volver Atras"
        >
          Volver Atras
        </b-button>

        <b-button
          class="mt-3"
          variant="danger"
          block
          title="Eliminar"
          @click="delete_all_Medicamentos(item)"
        >
          Eliminar
        </b-button>
      </b-modal>
    </div>

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
    <pre>Cantidad de registros: {{rows}}</pre> 
    <pre>Filas seleccionadas: {{selected.length}}</pre>
    <pre>Filas seleccionadas: {{selected}}</pre>
    <b-table
      :fields="fields"
      striped
      sortable
      responsive
      hover
      :items="tabla_med"
      show-empty
      :sticky-header= true
      :no-border-collapse= false
      ref="tablaregistros"
      id="tablaregistros"
      selectable
      select-mode="multi"
      @row-selected="seleccionar_una"
    >

      <template #empty="">
        <!--
        <b>No hay registros para mostrar</b>
        -->
        <b>{{msj_tabla}}</b>
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

      <template slot="cell(cod_farmacia)" slot-scope="data">
        {{data.value.split('/')[4]}}
      </template>
      
      <template slot="cell(action)" slot-scope="row">
        <div class="mt-3">
          <b-button-group>
            <b-button variant="info" id="button-1" title="Mostrar Info" @click="info(row.item.id_medicamento)">
              Mostrar Info
            </b-button>

            <b-button
              variant="warning"
              id="button-2"
              title="Editar este registro"
              v-b-modal.modal-editar 
              @click="editarMedicamento(row.item, row.index)"
            >
              <v-icon class="mr-2">
                mdi-pencil
              </v-icon>
              Editar
            </b-button>

            <b-modal id="modal-editar" hide-footer> 
              <template #modal-title><h5 class="modal-title">Editar</h5></template>
                <medicamento-update/>
            </b-modal>

            <b-button
              variant="danger"
              id="button-3"
              @click="showModalinfo(row.item, row.index)"
              title="Eliminar este registro"
            >
              <v-icon class="mr-2">
                mdi-delete
              </v-icon>
              Eliminar
            </b-button>
            

            <b-modal id="modal_eliminar" ref="my-modal" hide-footer title="Eliminar" ok-only>
              <div class="d-block text-center">
                <h3>¿Esta seguro de eliminar los datos de '{{infoEliminar.medicamento.nombre}}'?</h3>
              </div>
              <b-button
                class="mt-2"
                block
                @click="hideModal"
                title="Volver Atras"
              >
                Volver Atras
              </b-button>

              <b-button
                class="mt-3"
                variant="danger"
                block
                title="Eliminar"
                @click="deleteMedicamento(infoEliminar.medicamento.id_medicamento)"
              >
                Eliminar
              </b-button>
            </b-modal>
          </b-button-group>
        </div>
      </template>
    </b-table>

    <vue-html2pdf
        :show-layout="false"
        :float-layout="true"
        :enable-download="false"
        :preview-modal="true"
        :paginate-elements-by-height="1400"
        filename="Listado de Medicamentos"
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
            <img src="../assets/logo.jpg" alt="Logo Federación" srcset="" id="Logo_fed" >
          </section>
          <section class="pdf-item">
              
          <h3>Listado de Medicamentos</h3>
            <b-table
              :fields="fields != 'action'"
              responsive
              :items="tabla_med"
              :no-border-collapse= false
              small
              fixed
              bordered
              head-variant="light"
            >
              <template slot="cell(cod_farmacia)" slot-scope="data">
                {{data.value.split('/')[4]}}
              </template>
            </b-table>
          </section>
      </section>
    </vue-html2pdf>
  </div>
</template>

<script>
let api = new URL("http://localhost");
api.pathname = "medicamentos";
//api.port = 8000;
api.port = 8081;

import MedicamentoAlta from './MedicamentosAlta.vue';
import MedicamentoUpdate from './MedicamentosUpdate.vue';
import axios from 'axios';
import VueHtml2pdf from 'vue-html2pdf';

export default {
  components: {MedicamentoAlta, MedicamentoUpdate,VueHtml2pdf},
  data() {
    return {
      tabla_med: [],
      fields: [
            {key:'selected' ,label: 'Seleccionar', sortable: true,},
            {key:'id_medicamento' ,label: 'ID', sortable: true,},
            {key:'nombre' ,label: 'Nombre', sortable: true,},
            {key:'presentacion' ,label: 'Presentacion',sortable: true,},
            {key:'laboratorio' ,label: 'Laboratorio', sortable: true,},
            {key:'cod_farmacia' ,label: 'Farmacia',sortable: true,},
            { key: "action", label: "Acciones", variant: "secondary" },
      ],
      
      buscar: '',
      selected: [],
      infoEliminar:{
        id:"modal_eliminar",
        medicamento: -1
      },
      btn_down_pdf : true, //Desabilito los botones, hasta que muestre los datos
      btn_del_full : true,
      msj_tabla: " Presione 'Mostrar' para ver los regitros ",

    };
  },
  computed: {
    rows() {
      return this.tabla_med.length;
    },
  },
  methods: {
    async testFetch() {
      try {
        const res = await fetch(api);
        const data = await res.json();

        var lista_med = data.results;

        console.log(lista_med);

        this.tabla_med = lista_med;

        //Habilito los botones
        this.btn_down_pdf=false;
        this.btn_del_full=false;
        
        if(this.tabla_med.length==0){
          this.msj_tabla = " No se encuentran regitros en esta tabla ";
        }
        
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

    info(id){
      alert('id: ' + id);
    },

    showModalinfo(item, index) {
      this.infoEliminar.medicamento=item;
      this.showModal();
    },

    //Funciones de seleccion
    seleccionar_una(items) {
      this.selected = items
    },

    seleccionar_todas() {
      this.$refs.tablaregistros.selectAllRows()
    },

    limpiar_seleccion() {
      this.$refs.tablaregistros.clearSelected()
    },
    /*
    filtrarFilas(){
      this.fields.forEach(filas=>{
        let option={}
        if(filas.key!='action'){
          option = filas
        }
        this.fields.push(option)
      })
    },
    */
    //Funcion para crear el PDF
    generarPDF(){
      if(this.tabla_med.length !=0){
        this.$refs.html2Pdf.generatePdf();
      }
      else{
        swal("Debe tener al menos 1 registro")
      }
    },


    altaMedicamento() {},

    editarMedicamento(item, index) {},

    //Funcion para eliminar el medicamento
    async deleteMedicamento(id){
    
     axios.delete('http://localhost:8081/medicamentos/'+ id +'/')
     .then(datos =>{
       swal("Eliminacion Exitosa", " ", "success");
       console.log(datos);
     })
     .catch(error=>{
       swal("¡ERROR!", "Se ha detectado un problema ", "error")
       console.log(error);
     })
     .finally(() => this.testFetch());
    },

    //Funcion para eliminar todos los medicamentos
    async delete_all_Medicamentos(){
      var cantidad = this.tabla_med.length;
      if (cantidad<1){
        swal("Debe tener al menos 1 registro")
      }
      else{
        try{
          //this.tabla_med.splice(0, cantidad);
          axios.delete('http://localhost:8081/medicamentos/'+ tabla_med.id_medicamento +'/')
          if(this.tabla_med.length==0){
            swal("Eliminacion Exitosa", " ", "success");
          }
        }catch(error){
          swal("¡ERROR!", "Se ha detectado un problema ", "error")
          console.log(error);
        }finally{this.testFetch}
      } 
    },
    /*
    async delete_all_Medicamentos(item){
      //var aux=0, cant=this.tabla_med.length;
      try{
        axios.delete('http://localhost:8081/medicamentos/'+ item.id_medicamento +'/')
        if(this.tabla_med==null){
          swal("Eliminacion Exitosa", " ", "success");
        }
        else{
          //swal("¡ERROR!", "No se han podido eliminar todos los registros", "error")
        }
      }catch (error) {
        swal("¡ERROR!", "Se ha detectado un problema ", "error")
        console.log(error);
      //swal("¡ERROR!", "{error}", "error")
      }finally{this.testFetch}
    },
    */ 

    //Funcion de busqueda
    async buscarnow() {
        // Declare variables
        
        var input, 
            filter, 
            table, 
            tr, td, i, 
            txtValue, IdMed, 
            Medicamento, Laboratorio, Farmacia;

        input = this.$refs.buscadorlista;
        filter = input.value.toUpperCase();
        table = document.getElementById('tablaregistros');
        tr = table.getElementsByTagName('tr');

        // Loop through all list items, and hide those who don't match the search query
        for (i = 1; i < tr.length; i++) {
            td = tr[i].getElementsByTagName("td");
            IdMed = td[0].textContent || td[0].innerText;
            Medicamento = td[1].textContent || td[1].innerText;
            Laboratorio = td[3].textContent || td[3].innerText;
            Farmacia = td[4].textContent || td[4].innerText;
            txtValue = IdMed + Medicamento + Laboratorio + Farmacia;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    },

    
    async beforeDownload ({ html2pdf, options, pdfContent }) {
      await html2pdf().set(options).from(pdfContent).toPdf().get('pdf').then((pdf) => {
        const totalPages = pdf.internal.getNumberOfPages()
          for (let i = 1; i <= totalPages; i++) {
            pdf.setPage(i)
            pdf.setFontSize(10)
            pdf.setTextColor(150)
            pdf.text('Página ' + i + ' of ' + totalPages, (pdf.internal.pageSize.getWidth() * 0.88), (pdf.internal.pageSize.getHeight() - 0.3))
          } 
        }).save()
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
