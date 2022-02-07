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
											{{
												PDFprofesional.fecha_ingreso | Date
											}}</b-list-group-item
										>
										<b-list-group-item
											><b>Matricula:</b>
											{{ PDFprofesional.matricula }}</b-list-group-item
										>
										<b-list-group-item
											><b>DNI:</b> {{ PDFprofesional.dni }}</b-list-group-item
										>
									</b-list-group>
									&nbsp;
									<b-list-group class="col-5">
										<b-list-group-item
											><b>Calle:</b> {{ PDFprofesional.domicilio }}
										</b-list-group-item>
										<b-list-group-item
											><b>Provincia:</b>
											{{ PDFprofesional.provincia }}</b-list-group-item
										>
										<b-list-group-item
											><b>Localidad:</b>
											{{ PDFprofesional.localidad }}</b-list-group-item
										>
									</b-list-group>
									&nbsp;
									<b-list-group class="col-4">
										<b-list-group-item
											><b>Correo:</b> {{ PDFprofesional.email }}
										</b-list-group-item>
										<b-list-group-item
											><b>Telefono Fijo:</b>
											{{ PDFprofesional.tel_fijo }}</b-list-group-item
										>
										<b-list-group-item
											><b>Celular:</b>
											{{ PDFprofesional.tel_celular }}</b-list-group-item
										>
									</b-list-group>
								</b-list-group>
							</div>
						</b-card-text>
					</b-card>
				</b-card-group>
				<br />
				<b-card title="Datos Bancarios: ">
					<div>
						<b-list-group horizontal>
							<b-list-group class="col-5">
								<b-list-group-item
									><b>Banco:</b> {{ PDFprofesional.banco }}</b-list-group-item
								>
								<b-list-group-item
									><b>CBU:</b> {{ PDFprofesional.cbu }}</b-list-group-item
								>
								<b-list-group-item
									><b>Alias del CBU:</b>
									{{ PDFprofesional.alias_cbu }}</b-list-group-item
								>
							</b-list-group>
							&nbsp;
							<b-list-group class="col-5">
								<b-list-group-item
									><b>Tipo de cuenta:</b>
									{{ PDFprofesional.tipo_cuenta }}</b-list-group-item
								>
								<b-list-group-item
									><b>Titular de la cuenta:</b>
									{{ PDFprofesional.titular_cuenta }}</b-list-group-item
								>
							</b-list-group>
						</b-list-group>
					</div>
				</b-card>
				<br />
				<b-card title="Consultorios: ">
					<div>
						<b-table
							hover
							:items="PDFprofesional.list_consultorios"
							:fields="fields_consultorios"
							:sticky-header="true"
							:no-border-collapse="true"
							show-empty
						>
							<template #empty="">
								<b>No hay registros para mostrar</b>
							</template>
						</b-table>
					</div>
				</b-card>
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
												{{
													PDFprofesional.fecha_ingreso | Date
												}}</b-list-group-item
											>
											<b-list-group-item
												><b>Matricula:</b>
												{{ PDFprofesional.matricula }}</b-list-group-item
											>
											<b-list-group-item
												><b>DNI:</b> {{ PDFprofesional.dni }}</b-list-group-item
											>
										</b-list-group>
										&nbsp;
										<b-list-group class="col-5">
											<b-list-group-item
												><b>Calle:</b> {{ PDFprofesional.domicilio }}
											</b-list-group-item>
											<b-list-group-item
												><b>Provincia:</b>
												{{ PDFprofesional.provincia }}</b-list-group-item
											>
											<b-list-group-item
												><b>Localidad:</b>
												{{ PDFprofesional.localidad }}</b-list-group-item
											>
										</b-list-group>
										&nbsp;
										<b-list-group class="col-4">
											<b-list-group-item
												><b>Correo:</b> {{ PDFprofesional.email }}
											</b-list-group-item>
											<b-list-group-item
												><b>Telefono Fijo:</b>
												{{ PDFprofesional.tel_fijo }}</b-list-group-item
											>
											<b-list-group-item
												><b>Celular:</b>
												{{ PDFprofesional.tel_celular }}</b-list-group-item
											>
										</b-list-group>
									</b-list-group>
								</div>
							</b-card-text>
						</b-card>
					</b-card-group>
					<br />
					<b-card title="Datos Bancarios: ">
						<div>
							<b-list-group horizontal>
								<b-list-group class="col-5">
									<b-list-group-item
										><b>Banco:</b> {{ PDFprofesional.banco }}</b-list-group-item
									>
									<b-list-group-item
										><b>CBU:</b> {{ PDFprofesional.cbu }}</b-list-group-item
									>
									<b-list-group-item
										><b>Alias del CBU:</b>
										{{ PDFprofesional.alias_cbu }}</b-list-group-item
									>
								</b-list-group>
								&nbsp;
								<b-list-group class="col-5">
									<b-list-group-item
										><b>Tipo de cuenta:</b>
										{{ PDFprofesional.tipo_cuenta }}</b-list-group-item
									>
									<b-list-group-item
										><b>Titular de la cuenta:</b>
										{{ PDFprofesional.titular_cuenta }}</b-list-group-item
									>
								</b-list-group>
							</b-list-group>
						</div>
					</b-card>
					<br />
					<b-card title="Consultorios: ">
						<div>
							<b-table
								hover
								:items="PDFprofesional.list_consultorios"
								:fields="fields_consultorios"
								:sticky-header="true"
								:no-border-collapse="true"
								show-empty
							>
								<template #empty="">
									<b>No hay registros para mostrar</b>
								</template>
							</b-table>
						</div>
					</b-card>
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
			return {
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
