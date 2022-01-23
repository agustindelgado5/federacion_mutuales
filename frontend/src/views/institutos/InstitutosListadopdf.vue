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
									responsive="sm"
									hover
									:items="PDFinstituto"
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
			filename="ListadoInstitutos"
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
							responsive="sm"
							small
							hover
							:items="PDFinstituto"
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
			PDFinstituto: {},
		},
		components: {
			VueHtml2pdf,
		},

		data() {
			return {
				fields: [
					{
						key: "codigo_institucion",
						label: "Codigo",
						sortable: true,
					},

					{ key: "nombre", label: "Nombre", sortable: true },
					{ key: "cuit", label: "CUIT", sortable: true },
					{ key: "direccion", label: "Direccion", sortable: true },
					{ key: "localidad", label: "Localidad", sortable: true },
					{ key: "provincia", label: "Provincia", sortable: true },
					{ key: "telefono", label: "Telefono", sortable: true },
					{ key: "horarios", label: "Horarios", sortable: true },
					{ key: "responsable", label: "Responsable", sortable: true },
					{
						key: "telefono_reponsable",
						label: "Telefono Responsable",
						sortable: true,
					},
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
