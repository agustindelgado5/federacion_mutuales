<template>
	<div>
		<section slot="pdf-content">
			<section class="pdf-item">
				<b-card-group deck>
					<b-card>
						<b-card-text>
							<h6>Federación Tucumana de Mutuales</h6>
							<div>
								<b-table
									:fields="fields"
									striped
									sortable
									responsive="sm"
									hover
									:items="PDFreceta"
									:sticky-header="true"
									:no-border-collapse="false"
									ref="tablaregistros"
									id="tablaregistros"
								></b-table>
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
			filename="ListadoFarmacias"
			:pdf-quality="2"
			:manual-pagination="false"
			pdf-format="legal"
			pdf-orientation="portrait"
			pdf-content-width="100%"
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
							</b-card-text>
						</b-card>
					</b-card-group>
					<div class="table">
                        <b-table
						:fields="fields"
						striped
						sortable
						responsive="sm"
                        small
						hover
						:items="PDFreceta"
						:sticky-header="true"
						:no-border-collapse="false"
						ref="tablaregistros"
						id="tablaregistros"
					></b-table>
                    </div>
				</section>
			</section>
		</vue-html2pdf>
	</div>
</template>

<script>
	import VueHtml2pdf from "vue-html2pdf";
	export default {
		props: {
			PDFreceta: {},
		},
		components: {
			VueHtml2pdf,
		},

		data() {
			return {
				fields: [
					
					{ key: "id_receta", label: "N° Receta", sortable: true },
					{ key: "numero_socio", label: "N° Socio", sortable: true },
					{ key: "paciente", label: "Paciente", sortable: true },
					{ key: "diagnostico", label: "Diagnostico", sortable: true },
					{ key: "id_medicamento", label: "Id Medicamento", sortable: true },
					{ key: "cod_farmacia", label: "Id Farmacia", sortable: true },
					{ key: "fecha", label: "Fecha", sortable: true },
					{ key: "carencia", label: "Carencia", sortable: true },
				],
			};
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
		computed: {},
	};
</script>

<style></style>
