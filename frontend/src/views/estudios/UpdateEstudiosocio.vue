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

			<b-form-group label="Estudios disponibles" label-for="selected">
				<v-autocomplete
					id="proveedor"
					v-model="selected"
					:items="op_estudios"
					type="text"
					solo
					filled
				></v-autocomplete>
				<!--
				<b-form-checkbox-group
					v-model="selected"
					:options="op_estudios"
					:aria-describedby="ariaDescribedby"
					name="flavour-2a"
					stacked
				></b-form-checkbox-group>
				-->
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
				selected: null,
				//selected_anterior: [],
				lista_estudios: [],

				//list_institutos: {},

				op_estudios: [
					{ value: null, text: "Elija el estudio", disabled: true },
				],

				validacion: {},

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
					this.getProveedor(element);
				});
			},
			async getProveedor(estudioSocio) {
				let idProv = estudioSocio.id_proveedor;
				let dataProv = {};
				axios
					.get(idProv)
					.then((response) => {
						// Obtenemos los datos
						dataProv = response.data;
						let option = {};
						option.value =
							"http://localhost:8081/estudios/" + estudioSocio.id_estudio + "/";
						option.text =
							estudioSocio.tipo +
							" - " +
							dataProv.id_proveedor +
							"/" +
							dataProv.nombre +
							"/" +
							dataProv.direccion +
							"/" +
							dataProv.localidad +
							"/" +
							dataProv.provincia +
							" - $" +
							estudioSocio.precio_socio;

						this.op_estudios.push(option);
					})
					.catch((error) => {
						// Capturamos los errores
						console.log("ERROR:", error);
						//return null
					});
				return await dataProv;
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
						this.selected = element.id_estudio;
					}
				});
				//this.selected_anterior = this.selected;
			},

			async getEstudiosSocios() {
				let listado = {};
				let estudiosAPI = new APIControler();
				estudiosAPI.apiUrl.pathname = "estudios_socios/";
				this.lista_estudios = await estudiosAPI.getData(listado);
			},

			async putEstudio() {
				//var id = this.Socio.numero_socio;

				let dataUP = {};
				dataUP.numero_socio =
					"http://localhost:8081/socios/" + this.Socio.numero_socio + "/";
				dataUP.id_estudio = this.selected;

				let servicioAPI = new APIControler();
				console.log(servicioAPI.apiUrl);
				servicioAPI.apiUrl.pathname = "estudios_socios/";
				let respuesta = await servicioAPI.postData(dataUP);
				console.log("RESPUESTA", respuesta);
				this.cargarFeedback(respuesta);

				this.getEstudiosSocios();
				this.updateTable();
			},

			//Validacion de los campos
			cargarFeedback() {
				let valido;
				if (!this.respuesta) this.respuesta = {};
				for (let key in this.validacion) {
					valido = !this.respuesta.hasOwnProperty(key);
					this.validacion[key].estado = valido;
					//console.log(key);
					if (!valido) this.validacion[key].mensaje = this.respuesta[key][0];
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
