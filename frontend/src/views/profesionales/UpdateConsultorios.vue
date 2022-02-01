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

			<!-- 
				{{ selected }}
			<br />
			{{ selected_anterior }}
			
			<br />
			{{ instituto }}
			<br />
			{{ data }}
			-->
		</b-form>
		<b-button class="mt-2" variant="success" block @click="putInstituto()"
			>Guardar</b-button
		>
	</div>
</template>

<script>
	import axios from "axios";
	import { APIControler } from "@/store/APIControler";
	import data from "../../infomenu";

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
				selected_anterior: [],
				consultorios: [],

				list_institutos: {},

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
			//Obtengo los consultorios
			async getInstitutos() {
				let institutosAPI = new APIControler();
				institutosAPI.apiUrl.pathname = "institutos/";
				this.instituto = await institutosAPI.getData(this.instituto);
				this.instituto.forEach((element) => {
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

			//Obtengo los consultorios ya seleccionados
			async getOpcionesSelected() {
				let listado = {};
				let opcionesAPI = new APIControler();
				opcionesAPI.apiUrl.pathname = "institutos_profesional/";
				this.data = await opcionesAPI.getData(listado);
				this.data.forEach((element) => {
					if (
						element.id_medico ==
						"http://localhost:8081/profesionales/" +
							this.profesional.id_medico +
							"/"
					) {
						console.log("Entro al if");
						this.selected.push(element.codigo_institucion);
					}
				});
				this.selected_anterior = this.selected;

				//this.new_selected=  this.selected + this.selected_anterior;
			},

			async getInstitutosProfesionales() {
				let listado = {};
				let institutosAPI = new APIControler();
				institutosAPI.apiUrl.pathname = "institutos_profesional/";
				this.consultorios = await institutosAPI.getData(listado);
			},

			async putInstituto() {
				var id = this.profesional.id_medico;
				//console.log("Selected for edit: ", this.selected, "length:", this.selected.length);

				/*
				En caso de agregar un nuevo elemento, hago el post
				*/
				for (var i = 0; i < this.selected.length; i++) {
					/*
					console.log(
						"id_medico: ",
						id,
						"consultorio:",
						this.selected[i],
						"cargado: ",
						await this.estaCargado(id, this.selected[i])
					);
					*/
					if ((await this.estaCargado(id, this.selected[i])) == null) {
						this.postInstituto(id, this.selected[i]);
						this.updateTable();
					}
				}

				/*
				En caso de sacar un nuevo elemento, hago el delete
				*/

				let diferencia = this.selected_anterior.filter(
					(elemento) => this.selected.indexOf(elemento) == -1
				);
				console.log("elemento a eliminar: ", diferencia);
				if (diferencia != null) {
					diferencia.forEach((element) => {
						for (let j = 0; j < this.consultorios.length; j++) {
							if (this.consultorios[j].codigo_institucion == element) {
								this.DeleteInstituto(this.consultorios[j].id_inst_prof);
								this.updateTable();
								break;
							}
						}
					});
					//this.DeleteInstituto(id, diferencia);
				}
				swal("Carga exitosa", "", "success");

				this.getInstitutosProfesionales();
			},
			//Me fijo si el servicio ya esta cargado
			async estaCargado(id, consultorio) {
				/*
				console.log(
					"id_medico: http://localhost:8081/profesionales/" + id + "/",
					"codigo_institucion",
					consultorio
				);
				*/

				try {
					let valor = {};
					axios
						.get("http://localhost:8081/institutos_profesional/", {
							id_medico: "http://localhost:8081/profesionales/" + id + "/",
							codigo_institucion: consultorio,
						})
						.then((datos) => {
							if (datos != null) {
								console.log("¡El consultorio ya se encuentra cargado!");
								///return true;
							}
							valor = datos;
							return valor;
						});
					//valor = true;
				} catch (error) {
					console.log(error);
					//valor = false;
					return null;
				}

				//return valor;
			},
			//Hago un post de un nuevo instituto
			async postInstituto(id, consultorio) {
				try {
					axios.post("http://localhost:8081/institutos_profesional/", {
						id_medico: "http://localhost:8081/profesionales/" + id + "/",
						codigo_institucion: consultorio,
					});

					console.log("¡Consultorios cargados con exito!");
				} catch (error) {
					console.log(error);
				}
			},

			//Hago una eliminacion de un registro
			async DeleteInstituto(id) {
				try {
					axios
						.delete("http://localhost:8081/institutos_profesional/" + id + "/")
						.then((datos) => {
							console.log("¡Consultorio eliminado con exito!");
							//console.log(datos);
						});
				} catch (error) {
					console.log(
						"¡No se pudo eliminar el consultorio: " + consultorio + "!" + error
					);
				}
			},
		},
		beforeMount() {
			//this.getProfesionales();
			this.getInstitutos();
			this.getInstitutosProfesionales();
			this.getOpcionesSelected();
		},
	};
</script>

<style></style>
