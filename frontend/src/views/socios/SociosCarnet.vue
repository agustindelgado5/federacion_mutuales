<template>
	<div>
		<section slot="pdf-content">
			<section class="pdf-item">
				<b-card-group deck>
					<b-card>
					<!--
					<b-card
						img-src="@/assets/logo.jpg"
						img-alt="Logo Federación"
						img-left
						class="mb-3"
						img-width="90"
						img-height="90"
					>-->
						<b-card-text>
							<h6>Federación Tucumana de Mutuales</h6>
							<div>
								<b-list-group horizontal="md" style="font-size: 70%">
									<b-list-group-item>
										<b>N°: {{ carnet.numero_socio }}</b> | <b>Afiliado:</b>
										{{ carnet.afiliado }} | <b>DNI:</b>
										{{ carnet.dni }}
										{{ carnet.adherentes }}
									</b-list-group-item>
								</b-list-group>
								<b-list-group>
									&nbsp;
									<h6>Adherentes</h6>

									<b-list-group-item
										v-for="adh in carnet.adhrentes"
										:key="adh.dni"
										style="font-size: 70%"
									>
										<b>{{ adh.dni }}</b> - {{ adh.adherente }}
									</b-list-group-item>
								</b-list-group>
							</div>
						</b-card-text>
					</b-card>
				</b-card-group>
			</section>
		</section>

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
			filename="CarnetSocio"
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
						<!--
						<b-card
							img-src="../assets/logo.jpg"
							img-alt="Logo Federación"
							img-left
							class="mb-3"
							img-width="90"
							img-height="90"
						>
						-->
							<b-card-text>
								<h6>Federación Tucumana de Mutuales</h6>
								<div>
									<b-list-group horizontal="md" style="font-size: 70%">
										<b-list-group-item>
											<b>N°: {{ carnet.numero_socio }}</b> | <b>Afiliado:</b>
											{{ carnet.afiliado }} | <b>DNI:</b>
											{{ carnet.dni }}
											{{ carnet.adherentes }}
										</b-list-group-item>
									</b-list-group>
									<b-list-group>
										&nbsp;
										<h6>Adherentes</h6>

										<b-list-group-item
											v-for="adh in carnet.adhrentes"
											:key="adh.dni"
											style="font-size: 70%"
										>
											<b>{{ adh.dni }}</b> - {{ adh.adherente }}
										</b-list-group-item>
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
			carnet: {},
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
		computed: {},
	};
</script>

<style></style>
