<template>
	<div>
		<b-form>
			<!-- v-show="false" :disabled="true" -->
			<b-form-group
				label="*Numero del socio"
				label-for="numero_socio"
				v-show="false"
			>
				<b-form-input
					id="numero_socio"
					v-model="Socio.numero_socio"
					type="number"
					:disabled="true"
					required
				>
				</b-form-input>
			</b-form-group>

			<b-form-group
				label="Estudios disponibles"
				label-for="codigo_institucion"
				v-slot="{ ariaDescribedby }"
			>
				<b-form-checkbox-group
					v-model="selected"
					:options="op_estudios"
					:aria-describedby="ariaDescribedby"
					name="flavour-2a"
					stacked
				></b-form-checkbox-group>
			</b-form-group>
		</b-form>
		<b-button class="mt-2" variant="success" block @click="putEstudio()"
			>Guardar</b-button
		>
	</div>
</template>

<script>
	import axios from "axios";
	import { APIControler } from "@/store/APIControler";

	export default {
		props: {
			Socio: {},
			updateTable: Function,
		},
		data() {
			return {
				//list_profesionales: {},
				estudio: {},
				data: {},
				selected: [],
				selected_anterior: [],
				lista_estudios: [],

				//list_institutos: {},

				op_estudios: [
					{ value: null, text: "Elija los consultorios", disabled: true },
				],

				respuesta: null,
			};
		},

		methods: {
			//Obtengo los consultorios
			async getEstudios() {
				let estudiosAPI = new APIControler();
				estudiosAPI.apiUrl.pathname = "estudios/";
				this.estudio = await estudiosAPI.getData(this.estudio);
				this.estudio.forEach((element) => {
					let option = {};
					option.value =
						"http://localhost:8081/estudios/" + element.id_estudio + "/";
					option.text =
						element.tipo +
						" - " +
						element.proveedor +
						" - $" +
						element.precio_socio;
					console.log(option);
					this.op_estudios.push(option);
				});
			},

			//Obtengo los consultorios ya seleccionados
			async getOpcionesSelected() {
				let listado = {};
				let opcionesAPI = new APIControler();
				opcionesAPI.apiUrl.pathname = "estudios_socios/";
				this.data = await opcionesAPI.getData(listado);
				this.data.forEach((element) => {
					if (
						element.numero_socio ==
						"http://localhost:8081/socios/" + this.Socio.numero_socio + "/"
					) {
						console.log("Entro al if");
						this.selected.push(element.id_estudio);
					}
				});
				this.selected_anterior = this.selected;
			},

			async getEstudiosSocios() {
				let listado = {};
				let estudiosAPI = new APIControler();
				estudiosAPI.apiUrl.pathname = "estudios_socios/";
				this.lista_estudios = await estudiosAPI.getData(listado);
			},

			async putEstudio() {
				var id = this.Socio.numero_socio;

				/*
				En caso de agregar un nuevo elemento, hago el post
				*/
				for (var i = 0; i < this.selected.length; i++) {
					if ((await this.estaCargado(id, this.selected[i])) == null) {
						this.postEstudio(id, this.selected[i]);
						//this.updateTable();
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
						for (let j = 0; j < this.lista_estudios.length; j++) {
							if (this.lista_estudios[j].id_estudio == element) {
								this.DeleteEstudio(this.lista_estudios[j].id_estudio_socio);
								this.updateTable();
								break;
							}
						}
					});
					//this.DeleteInstituto(id, diferencia);
				}
				swal("Carga exitosa", "", "success");

				this.getEstudiosSocios();
				this.updateTable();
			},
			//Me fijo si el estudio ya esta cargado
			async estaCargado(id, estudio) {
				try {
					let idSocio = "http://localhost:8081/socios/" + id + "/";
					let IdEstudio = estudio;

					for (let j = 0; j < this.lista_estudios.length; j++) {
						if (
							this.lista_estudios[j].id_estudio == IdEstudio &&
							this.lista_estudios[j].numero_socio == idSocio
						) {
							return this.lista_estudios[j];
						}
					}
					return null;
				} catch (error) {
					console.log(error);
					//valor = false;
					return null;
				}
			},
			//Hago un post de un nuevo estudio
			async postEstudio(id, estudio) {
				try {
					axios.post("http://localhost:8081/estudios_socios/", {
						numero_socio: "http://localhost:8081/socios/" + id + "/",
						id_estudio: estudio,
					});

					console.log("¡Estudios cargados con exito!");
				} catch (error) {
					console.log(error);
				}
			},

			//Hago una eliminacion de un registro
			async DeleteEstudio(id) {
				try {
					axios
						.delete("http://localhost:8081/estudios_socios/" + id + "/")
						.then((datos) => {
							console.log("¡Estudio eliminado con exito!");
							//console.log(datos);
						});
				} catch (error) {
					console.log(
						"¡No se pudo eliminar el consultorio: " + id + "!" + error
					);
				}
			},
		},
		beforeMount() {
			this.getEstudios();
			//this.getProfesionales();
			//this.getInstitutos();
			this.getEstudiosSocios();
			this.getOpcionesSelected();
		},
	};
</script>

<style></style>
