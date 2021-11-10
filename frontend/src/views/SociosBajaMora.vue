<template>
    <vue-html2pdf
        :show-layout="false"
        :float-layout="true"
        :enable-download="false"
        :preview-modal="true"
        :paginate-elements-by-height="1400"
        filename="Solicitud_Baja"
        :pdf-quality="2"
        :manual-pagination="false"
        pdf-format="a4"
        pdf-orientation="portrait"  
        pdf-content-width="80%"
        @click="generarSolicitud()"
 
        @progress="onProgress($event)"
        @startPagination="startPagination()"
        @hasPaginated="hasPaginated()"
        @beforeDownload="beforeDownload($event)"
        @hasDownloaded="hasDownloaded($event)" 
        ref="html2PdfBaja"
    >
      <section slot="pdf-content">
        <!-- PDF Content Here -->
          <section class="pdf-item">
            <img src="../assets/logo.jpg" alt="Logo Federación" srcset="" id="Logo_fed" >
          </section>
          <section class="pdf-item">
              Viendo que puedo poner je
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
        generarSolicitud(){
            if(false || this.datos !=0){
                this.$refs.html2PdfBaja.generatePdf();
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