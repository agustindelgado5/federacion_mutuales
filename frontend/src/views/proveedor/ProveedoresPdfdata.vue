<template>
	<div>
		<section slot="pdf-content">
			<section class="pdf-item">
				<b-card-group deck>
					<b-card>
						<b-card-text>
							<h6>Federación Tucumana de Mutuales</h6>
							<div>
								<b>Proveedor: </b>

								{{ PDFproveedor.nombre.toUpperCase() }}
								<b-list-group horizontal>
									<b-list-group class="col-3">
										<b-list-group-item
											><b>Nombre:</b> {{ PDFproveedor.nombre }}</b-list-group-item
										>
										<b-list-group-item
											><b>CUIT:</b> {{ PDFproveedor.cuit }}</b-list-group-item
										>
									</b-list-group>
									&nbsp;
									<b-list-group class="col-4">
										<b-list-group-item
											><b>Calle:</b> {{ PDFproveedor.direccion }}
										</b-list-group-item>
										<b-list-group-item
											><b>Provincia:</b>
											{{ PDFproveedor.provincia }}</b-list-group-item
										>
										<b-list-group-item
											><b>Localidad:</b>
											{{ PDFproveedor.localidad }}</b-list-group-item
										>
									</b-list-group>
									&nbsp;
									<b-list-group class="col-4">
										<b-list-group-item
											><b>Correo:</b> {{ PDFproveedor.email }}
										</b-list-group-item>
										<b-list-group-item
											><b>Telefono Fijo:</b>
											{{ PDFproveedor.tel_fijo }}</b-list-group-item
										>
										<b-list-group-item
											><b>Celular:</b>
											{{ PDFproveedor.tel_celular }}</b-list-group-item
										>
									</b-list-group>
								</b-list-group>
							</div>
						</b-card-text>
					</b-card>
				</b-card-group>
				<br />
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
			:enable-download="false"
			:preview-modal="true"
			:paginate-elements-by-height="1400"
			filename="DatosDelproveedor"
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
									<b>Proveedor: </b>

									{{ PDFproveedor.nombre.toUpperCase() }}
									<b-list-group horizontal>
										<b-list-group class="col-3">
											<b-list-group-item
												><b>Nombre:</b> {{ PDFproveedor.nombre }}</b-list-group-item
											>
											<b-list-group-item
												><b>CUIT:</b> {{ PDFproveedor.cuit }}</b-list-group-item
											>
										</b-list-group>
										&nbsp;
										<b-list-group class="col-4">
											<b-list-group-item
												><b>Calle:</b> {{ PDFproveedor.direccion }}
											</b-list-group-item>
											<b-list-group-item
												><b>Provincia:</b>
												{{ PDFproveedor.provincia }}</b-list-group-item
											>
											<b-list-group-item
												><b>Localidad:</b>
												{{ PDFproveedor.localidad }}</b-list-group-item
											>
										</b-list-group>
										&nbsp;
										<b-list-group class="col-4">
											<b-list-group-item
												><b>Correo:</b> {{ PDFproveedor.email }}
											</b-list-group-item>
											<b-list-group-item
												><b>Telefono Fijo:</b>
												{{ PDFproveedor.tel_fijo }}</b-list-group-item
											>
											<b-list-group-item
												><b>Celular:</b>
												{{ PDFproveedor.tel_celular }}</b-list-group-item
											>
										</b-list-group>
									</b-list-group>
								</div>
							</b-card-text>
						</b-card>
					</b-card-group>
					<br />
				</section>
			</section>
		</vue-html2pdf>
	</div>
</template>

<script>
	import VueHtml2pdf from "vue-html2pdf";
	export default {
		props: {
			PDFproveedor: {},
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
				return this.proveedor.apellido + " - " + this.proveedor.nombre;
			},
		},
	};
</script>

<style></style>
