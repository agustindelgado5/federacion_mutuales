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

    <b-button @click="generarPDF()" class="mb-4 ml-2" title="Generar PDF">Generar PDF</b-button>

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
    >
    <!-- 
      <template slot="action">
        <b-button variant="warning" size="sm">Modificar</b-button>
        <b-button variant="danger" size="sm">Eliminar</b-button>
      </template>
    -->
      <template #empty="">
        <b>No hay registros para mostrar</b>
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
              @click="editarMedicamento()"
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
        :enable-download="true"
        :preview-modal="true"
        :paginate-elements-by-height="1400"
        filename="hee hee"
        :pdf-quality="2"
        :manual-pagination="false"
        pdf-format="a4"
        pdf-orientation="landscape"
        pdf-content-width="800px"
 
        @progress="onProgress($event)"
        @hasStartedGeneration="hasStartedGeneration()"
        @hasGenerated="hasGenerated($event)"
        ref="html2Pdf"
    >
      <section slot="pdf-content">
            <!-- PDF Content Here -->
            <h2>Listado de Medicamentos</h2>
            <b-table
              :fields="fields"
              responsive
              :items="tabla_med"
              show-empty
              :no-border-collapse= false
            >
              <template slot="cell(cod_farmacia)" slot-scope="data">
                {{data.value.split('/')[4]}}
              </template>
            </b-table>
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
            {key:'id_medicamento' ,label: 'ID', sortable: true,},
            {key:'nombre' ,label: 'Nombre', sortable: true,},
            {key:'presentacion' ,label: 'Presentacion',sortable: true,},
            {key:'laboratorio' ,label: 'Laboratotio', sortable: true,},
            {key:'cod_farmacia' ,label: 'Farmacia',sortable: true,},
            { key: "action", label: "Acciones", variant: "secondary" },
      ],
      buscar: '',
      infoEliminar:{
        id:"modal_eliminar",
        medicamento: -1
      },

    };
  },
  methods: {
    async testFetch() {
      try {
        const res = await fetch(api);
        const data = await res.json();

        var lista_med = data.results;

        console.log(lista_med);

        this.tabla_med = lista_med;
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

    generarPDF(){
      this.$refs.html2Pdf.generatePdf();
    },

    altaMedicamento() {},

    editarMedicamento() {},

    async deleteMedicamento(id){
    
     axios.delete('http://localhost:8081/medicamentos/'+ id +'/')
     .then(datos =>{
       swal("Carga Exitosa", " ", "success");
       console.log(datos);
     })
     .catch(error=>{
       swal("¡ERROR!", "Se ha detectado un problema ", "error")
       console.log(error);
     })
     .finally(() => this.testFetch());
    },

    async buscarnow() {
        // Declare variables
        
        var input, filter, table, tr, td, i, txtValue, IdMed, Medicamento, Laboratorio, Farmacia;
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
