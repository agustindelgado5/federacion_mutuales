<template>
	<div>
		<!--
		{{ datos }}
		<br />
		<br />
		{{ consultorios }}
		-->
		<b-form>
			<div v-for="elem in datos" :key="elem.id_medico">
				<div
					v-for="cons in elem.list_consultorios"
					:key="cons.codigo_institucion"
				>
					<h6>{{ cons.nombre }}</h6>
					<b>
						{{ cons.direccion }} - {{ cons.localidad }} - {{ cons.provincia }}
					</b>

					<b-form-textarea
						v-model="cons.horariosAtencion"
						class="mb-3"
						type="text"
						rows="3"
						max-rows="6"
					></b-form-textarea>
					{{ cons.horariosAtencion }}
				</div>
			</div>

			<b-button class="mt-2" variant="success" block @click="putDatos()">
				<b>GUARDAR</b>
			</b-button>
		</b-form>
	</div>
</template>

<script>
	import axios from "axios";
	//import { APIControler } from "@/store/APIControler";

	export default {
		props: {
			datos: {},
			consultorios: [],
			updateTable: Function,
		},
		data() {
			return {
				horarioChanged: null,
				respuesta: {},
			};
		},

		methods: {
			putDatos() {
				let id =
					"http://localhost:8081/profesionales/" +
					this.datos[0].id_medico +
					"/";
				this.datos[0].list_consultorios.forEach((cons) => {
					this.putHorario(id, cons);
				});
			},

			async getConsultorio(idMedico, instituto) {
				let consultorioAmodificar = {};

				this.consultorios.forEach((element) => {
					let CodInst =
						"http://localhost:8081/institutos/" +
						instituto.codigo_institucion +
						"/";
					if (
						element.id_medico == idMedico &&
						element.codigo_institucion == CodInst
					) {
						consultorioAmodificar.id_inst_prof = element.id_inst_prof;
						consultorioAmodificar.id_medico = element.id_medico;
						consultorioAmodificar.codigo_institucion =
							element.codigo_institucion;
						consultorioAmodificar.horarios = instituto.horariosAtencion;
					}
				});

				return await consultorioAmodificar;
			},

			//Funcion para modificar la forma de pago
			async putHorario(idMedico, consultorio) {
				try {
					let consultorioAmodificar = await this.getConsultorio(
						idMedico,
						consultorio
					);
					console.log("REGISTRO A MODIFICAR: ", consultorioAmodificar);
					this.respuesta = await axios.put(
						"http://localhost:8081/institutos_profesional/" +
							consultorioAmodificar.id_inst_prof +
							"/",
						consultorioAmodificar
					);
					const content = this.respuesta.request;
					if (content.statusText == "OK") {
						this.respuesta = "";
						swal("Carga Exitosa", " ", "success");
					} else {
						//console.log(content.response);
						this.respuesta = JSON.parse(content.response);
						swal("¡ERROR!", "Los datos no son válidos", "error");
					}
				} catch (error) {
					swal("¡ERROR!", "Se ha detectado un problema ", "error");
					console.log(error);
				}
				//this.cargarFeedback();
				this.updateTable();
			},
		},
		beforeMount() {
			//this.getProfesionales();
		},
	};
</script>

<style></style>
