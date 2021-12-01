<template>
  <div>
    <vue-html2pdf
        :show-layout="true"
        :float-layout="false"
        :enable-download="false"
        :preview-modal="true"
        :paginate-elements-by-height="1400"
        filename="Solicitud_Baja"
        :pdf-quality="2"
        :manual-pagination="false"
        pdf-format="a4"
        pdf-orientation="portrait"  
        pdf-content-width="95%"
        ref="html2PdfBaja"
    >
      <section class="ml-5 mt-5 py-3" slot="pdf-content">
			<p class="text-right">San Miguel de Tucumán {{nota.fecha}}</p>
			<div class="mt-5">
				<p>Sr. Ricardo Mora</p>
				<p>S______/_______D</p>
			</div>
			<div class="mt-5">
				<p class="text-justify" style="text-indent:40%">Quien suscribe {{SocioBajaMora.nombre}} {{SocioBajaMora.apellido}},
					DNI {{SocioBajaMora.dni}} Nº de afiliado {{SocioBajaMora.numero_socio}} al servicio brindado por Ricardo Mora, quien por medio de la presente
					vengo a solicitar en forma unilateral la cancelación del servicio de salud y sepelio.
				</p>
				<p>Lo cual solicito que el descuento que se hace a través de mi cobro quede cancelado.</p>
				<p>Autorizo a {{nota.nombre}}, con DNI {{nota.dni}} a PRESENTAR esta nota.</p>
			</div>
			<p class="text-right">Sin otro particular saluda atte.</p>
      </section>
    </vue-html2pdf>

	<b-form-group label-cols="auto" label="Fecha" label-for="fecha">
            <b-form-input
              id="fecha"
              v-model="nota.fecha"
              type="text"
              placeholder="Ingrese una fecha"
              invalid-feedback="Complete este campo"
              required
              >
			</b-form-input>
	</b-form-group>

	<b-form-group label-cols="auto" label="N° Socio" label-for="numero_socio">
            <b-form-input
              id="numero_socio"
              v-model="SocioBajaMora.numero_socio"
              type="number"
              placeholder="Ingrese un Numero"
              invalid-feedback="Complete este campo"
              required
              >
			</b-form-input>
	</b-form-group>

	<b-form-group label-cols="auto" label="Nombre/s" label-for="nombre">
              <b-form-input
                id="nombre"
                v-model="SocioBajaMora.nombre"
                type="text"
                placeholder="*Ingrese los Nombre/s"
                invalid-feedback="Complete este campo"
                required
              >
              </b-form-input>
            </b-form-group>
		<b-form-group label-cols="auto" label="Apellido/s" label-for="apellido">
			<b-form-input
			id="apellido"
			v-model="SocioBajaMora.apellido"
			type="text"
			placeholder="*Ingrese los Apellido/s"
			invalid-feedback="Complete este campo"
			required
			>
			</b-form-input>
		</b-form-group>
          <b-form-group label-cols="auto" label="DNI" label-for="dni">
            <b-form-input
              id="dni"
              v-model="SocioBajaMora.dni"
              type="number"
              placeholder="Ingrese un DNI"
              invalid-feedback="Complete este campo"
              required
            >
            </b-form-input>
          </b-form-group>

		  <b-form-group label-cols="auto" label="Nombre que Autoriza" label-for="nombre_nota">
            <b-form-input
              id="nombre_nota"
              v-model="nota.nombre"
              type="text"
              placeholder="Ingrese un nombre"
              invalid-feedback="Complete este campo"
              required
            >
            </b-form-input>
          </b-form-group>

		  <b-form-group label-cols="auto" label="DNI que Autoriza" label-for="dni_nota">
            <b-form-input
              id="dni_nota"
              v-model="nota.dni"
              type="text"
              placeholder="Ingrese un DNI"
              invalid-feedback="Complete este campo"
              required
            >
            </b-form-input>
          </b-form-group>
		  <b-button
				@click="generarSolicitud()"
				class="mb-4 ml-2"
				title="PDF de la baja"
				>Generar PDF</b-button
			>
	</div>
</template>

<script>
    import VueHtml2pdf from "vue-html2pdf";
export default {
    props:{
        SocioBajaMora:{},
    },
    components: { 
        VueHtml2pdf,
		},
    data(){
        
        return {

        nota:{
					fecha:null,
					nombre: "........",
					dni: "........",
				},

        }
    },

    methods: {
        async generarSolicitud(){
            if(false || this.datos !=0){
                this.$refs.html2PdfBaja.generatePdf();
            }
            else{
                swal("Debe tener al menos 1 registro")
            }
        },
    },
    beforeMount (){
      this.nota.fecha=new Date().toLocaleDateString('es-ar',{month:'long',day:'numeric',year:'numeric'});
    }


}
</script>

<style>

</style>