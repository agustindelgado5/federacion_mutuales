<template>
	<div>
		<section slot="pdf-content">
			<section class="pdf-item">
				<b-card-group deck>
					<b-card>
						<b-card-text>
							<h6>Federación Tucumana de Mutuales</h6>
							<div>
								<b>Nombre Completo: </b>
								{{ PDFprofesional.apellido.toUpperCase() }},
								{{ PDFprofesional.nombre.toUpperCase() }}
								<b-list-group horizontal>
									<b-list-group class="col-3">
										<b-list-group-item
											><b>Fecha de ingreso:</b>
											{{ PDFprofesional.fecha_ingreso }}</b-list-group-item
										>
										<b-list-group-item
											><b>Matricula:</b>
											{{ PDFprofesional.matricula }}</b-list-group-item
										>
										<b-list-group-item
											><b>DNI:</b> {{ PDFprofesional.cuit }}</b-list-group-item
										>
									</b-list-group>
									&nbsp;
									<b-list-group class="col-5">
										<b-list-group-item
											><b>Provincia:</b>
											{{ PDFprofesional.provincia }}</b-list-group-item
										>
										<b-list-group-item
											><b>Localidad:</b>
											{{ PDFprofesional.localidad }}</b-list-group-item
										>
										<b-list-group-item
											><b>Correo:</b> {{ PDFprofesional.email }}
										</b-list-group-item>
									</b-list-group>
									&nbsp;
									<b-list-group class="col-4">
										<b-list-group-item
											><b>Telefono Fijo:</b>
											{{ PDFprofesional.tel_fijo }}</b-list-group-item
										>
										<b-list-group-item
											><b>Celular:</b>
											{{ PDFprofesional.tel_celular }}</b-list-group-item
										>
										<b-list-group-item
											><b>Calle:</b> {{ PDFprofesional.domicilio }}
										</b-list-group-item>
									</b-list-group>
								</b-list-group>
							</div>
						</b-card-text>
					</b-card>
				</b-card-group>
			</section>
		</section>
		<br />
		<b-button
			@click="generarPDF()"
			class="mb-4 ml-2"
			title="Descargar"
			variant="info"
			style="color: white"
			>DESCARGAR</b-button
		>

		<vue-html2pdf
			:show-layout="false"
			:float-layout="true"
			:enable-download="true"
			:preview-modal="true"
			:paginate-elements-by-height="1400"
			filename="DatosDelProfesional"
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
				<section class="pdf-item">
					<b-card-group deck>
						<b-card>
							<b-card-text>
								<h6>Federación Tucumana de Mutuales</h6>
								<div>
									<b>Nombre Completo: </b>
									{{ PDFprofesional.apellido.toUpperCase() }},
									{{ PDFprofesional.nombre.toUpperCase() }}
									<b-list-group horizontal>
										<b-list-group class="col-3">
											<b-list-group-item
												><b>Fecha de ingreso:</b>
												{{ PDFprofesional.fecha_ingreso }}</b-list-group-item
											>
											<b-list-group-item
												><b>Matricula:</b>
												{{ PDFprofesional.matricula }}</b-list-group-item
											>
											<b-list-group-item
												><b>DNI:</b>
												{{ PDFprofesional.cuit }}</b-list-group-item
											>
										</b-list-group>
										&nbsp;
										<b-list-group class="col-5">
											<b-list-group-item
												><b>Provincia:</b>
												{{ PDFprofesional.provincia }}</b-list-group-item
											>
											<b-list-group-item
												><b>Localidad:</b>
												{{ PDFprofesional.localidad }}</b-list-group-item
											>
											<b-list-group-item
												><b>Correo:</b> {{ PDFprofesional.email }}
											</b-list-group-item>
										</b-list-group>
										&nbsp;
										<b-list-group class="col-4">
											<b-list-group-item
												><b>Telefono Fijo:</b>
												{{ PDFprofesional.tel_fijo }}</b-list-group-item
											>
											<b-list-group-item
												><b>Celular:</b>
												{{ PDFprofesional.tel_celular }}</b-list-group-item
											>
											<b-list-group-item
												><b>Calle:</b> {{ PDFprofesional.domicilio }}
											</b-list-group-item>
										</b-list-group>
									</b-list-group>
								</div>
							</b-card-text>
						</b-card>
					</b-card-group>
				</section>
			</section>
		</vue-html2pdf>
	</div>
</template>

<script>
	import VueHtml2pdf from "vue-html2pdf";
	export default {
		props: {
			PDFprofesional: {},
		},
		components: {
			VueHtml2pdf,
		},

		data() {
			return {};
		},

		methods: {
			generarPDF() {
				console.log("Creando Archivo");
				this.$refs.html2Pdf.generatePdf();
			},
			onShown() {
				// Focus the cancel button when the overlay is showing
				this.$refs.cancel.focus();
			},
			onHidden() {
				// Focus the show button when the overlay is removed
				this.$refs.show.focus();
			},
		},
		beforeMount() {
			//this.generarPDF();
		},
		computed: {
			NameFile() {
				return this.profesional.apellido + " - " + this.profesional.nombre;
			},
		},
	};
</script>

<style></style>
