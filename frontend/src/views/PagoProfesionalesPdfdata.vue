<template>
	<div>
		<section slot="pdf-content">
			<h3>Comprobante de pago</h3>

			<b-list-group horizontal>
				<b-list-group-item>
					<b>ID: {{ orden_data.ID }}</b>
				</b-list-group-item>
				<b-list-group-item>
					<b>Profesional:</b> {{ orden_data.profesional }}
				</b-list-group-item>
			</b-list-group>
			<br />
			<b-list-group>
				<b-list-group-item>
					<b>MES: {{ orden_data.mes }}</b>
				</b-list-group-item>
				<b-list-group-item
					v-for="orden in orden_data.ordenes"
					:key="orden.num_orden"
				>
					{{ orden.num_orden }} - {{ orden.fecha }} - {{ orden.hora }} - ${{
						orden.precio
					}}
				</b-list-group-item>
			</b-list-group>
			<br />
			<b-list-group horizontal>
				<b-list-group-item>
					<b>Forma de Pago: {{ orden_data.modo_pago }}</b>
				</b-list-group-item>
				<b-list-group-item>
					<b>TOTAL: ${{ orden_data.total }}</b>
				</b-list-group-item>
			</b-list-group>
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
			filename="DetallePago"
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
					<h3>Federación Tucumana de Mutuales</h3>
					<!--
							<img
								src="../assets/logo.jpg"
								alt="Logo Federación"
								srcset=""
								id="Logo_fed"
							/>
							-->
				</section>
				<section class="pdf-item">
					<h3>Comprobante de pago</h3>

					<b-list-group horizontal>
						<b-list-group-item>
							<b>ID: {{ orden_data.ID }}</b>
						</b-list-group-item>
						<b-list-group-item>
							<b>Profesional:</b> {{ orden_data.profesional }}
						</b-list-group-item>
					</b-list-group>
					<br />
					<b-list-group>
						<b-list-group-item>
							<b>MES: {{ orden_data.mes }}</b>
						</b-list-group-item>
						<b-list-group-item
							v-for="orden in orden_data.ordenes"
							:key="orden.num_orden"
						>
							{{ orden.num_orden }} - {{ orden.fecha }} - {{ orden.hora }} - ${{
								orden.precio
							}}
						</b-list-group-item>
					</b-list-group>
					<br />
					<b-list-group horizontal>
						<b-list-group-item>
							<b>Forma de Pago: {{ orden_data.modo_pago }}</b>
						</b-list-group-item>
						<b-list-group-item>
							<b>TOTAL: ${{ orden_data.total }}</b>
						</b-list-group-item>
					</b-list-group>
				</section>
			</section>
		</vue-html2pdf>
	</div>
</template>

<script>
	import VueHtml2pdf from "vue-html2pdf";
	export default {
		props: {
			orden_data: {},
		},
		components: {
			VueHtml2pdf,
		},

		data() {
			return {
				/*
				fields_consultorios: [
					{
						key: "codigo_institucion",
						label: "Codigo",
						sortable: true,
					},

					{ key: "nombre", label: "Nombre", sortable: true },

					{ key: "direccion", label: "Direccion", sortable: true },
					{ key: "localidad", label: "Localidad", sortable: true },
					{ key: "provincia", label: "Provincia", sortable: true },

					{ key: "horariosAtencion", label: "Horarios", sortable: true },

					///{ key: "action", label: "Acciones", variant: "secondary" },
				],
				*/
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
		computed: {
			NameFile() {
				return this.profesional.apellido + " - " + this.profesional.nombre;
			},
		},
	};
</script>

<style></style>
