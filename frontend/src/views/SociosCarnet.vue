<template>
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
        @click="generarPDF()"
 
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
            <img src="../assets/logo.jpg" alt="Logo Federación" srcset="" id="Logo_fed" >
          </section>
          <section class="pdf-item">
              
            <b-table
              responsive
              :items="datos"
              :no-border-collapse= false
              small
              fixed
              bordered
              head-variant="light"
            >
            </b-table>
          </section>
      </section>
    </vue-html2pdf>
  
</template>

<script>
export default {
    props:{
        datos:{},
    },

    data(){
        return {}
    },

    methods: {
        generarPDF(){
            if(this.datos !=0){
                this.$refs.html2Pdf.generatePdf();
            }
            else{
                swal("Debe tener al menos 1 registro")
            }
        },
    }


}
</script>

<style>

</style>