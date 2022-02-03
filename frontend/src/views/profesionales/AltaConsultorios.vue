<template>
	<div>
		<b-form>
			<b-form-group label="*Id Medico" label-for="id_medico" v-show="false">
				<b-form-input
					id="id_medico"
					v-model="profesional.id_medico"
					type="number"
					:disabled="true"
					required
				>
				</b-form-input>
			</b-form-group>

			<b-form-group
				label="Consultorios disponibles"
				label-for="codigo_institucion"
				v-slot="{ ariaDescribedby }"
			>
				<b-form-checkbox-group
					v-model="selected"
					:options="op_consultorios"
					:aria-describedby="ariaDescribedby"
					name="flavour-2a"
					stacked
				></b-form-checkbox-group>
			</b-form-group>

			{{ selected }}
			{{ consultorios }}
		</b-form>
		<b-button class="mt-2" variant="success" block @click="postInstituto()"
			>Guardar</b-button
		>
	</div>
</template>

<script>
	import axios from "axios";
	import { APIControler } from "@/store/APIControler";

	export default {
		props: {
			profesional: {},
			updateTable: Function,
		},
		data() {
			return {
				//list_profesionales: {},
				instituto: {},
				data: {},
				selected: [],
				consultorios: [],

				op_consultorios: [
					{ value: null, text: "Elija los consultorios", disabled: true },
				],

				validacion: {
					//id_medico: { estado: null, mensaje: "" },
					//codigo_institucion: { estado: null, mensaje: "" },
				},

				respuesta: null,
			};
		},

		methods: {
			//Obtengo los servicios
			async getInstitutos() {
				let institutosAPI = new APIControler();
				institutosAPI.apiUrl.pathname = "institutos/";
				this.data = await institutosAPI.getData(this.instituto);
				this.data.forEach((element) => {
					let option = {};
					option.value =
						"http://localhost:8081/institutos/" +
						element.codigo_institucion +
						"/";
					option.text = element.nombre;
					console.log(option);
					this.op_consultorios.push(option);
				});
			},
			

			async postInstituto() {
				var id = this.profesional.id_medico;

				if (this.selected.length > 0) {
					for (var i = 0; i < this.selected.length; i++) {
						axios
							.post("http://localhost:8081/institutos_profesional/", {
								id_medico: "http://localhost:8081/profesionales/" + id + "/",
								codigo_institucion: this.selected[i],
							})
							.then((data) => {
								console.log(data);
								console.log("¡Consultorios cargados con exito!");
							})
							.catch((error) => {
								console.log(error);
							});

						swal("Carga exitosa", "", "success");
					}
				} else {
					swal("¡ERROR!", "Debe seleccionar al menos un servicio", "error");
				}

				//this.cargarFeedback();
				this.updateTable();
			},
			

			async getInstitutosProfesionales() {
				let listado = {};
				let institutosAPI = new APIControler();
				institutosAPI.apiUrl.pathname = "institutos_profesional/";
				this.consultorios = await institutosAPI.getData(listado);

			},

		
			

			/*
			cargarFeedback() {
				let valido;
				if (typeof this.respuesta === "undefined") {
					return;
				}
				for (let key in this.validacion) {
					valido = !this.respuesta.hasOwnProperty(key);
					this.validacion[key].estado = valido;
					if (!valido) this.validacion[key].mensaje = this.respuesta[key][0];
				}
			},
			*/
		},
		beforeMount() {
			//this.getProfesionales();
			this.getInstitutos();
		},
	};
</script>

<style></style>
