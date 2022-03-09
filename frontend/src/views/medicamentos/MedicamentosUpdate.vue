<template>
	<div>
		<h6>Los campos en (*) son obligatorios</h6>
		<h4>Datos</h4>
		<b-form @submit.stop.prevent>
			<b-form-group
				label="*ID"
				label-for="id_medicamento"
				@submit.stop.prevent="handleSubmit"
			>
				<b-form-input
					id="id_medicamento"
					v-model="item_med.id_medicamento"
					type="number"
					:state="validacion.id_medicamento.estado"
					placeholder="Ingrese un Numero"
					invalid-feedback="Complete este campo"
					disabled
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="id_medicamento-live-feedback">
					{{ validacion.id_medicamento.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group
				label="*Nombre"
				label-for="nombre"
				@submit.stop.prevent="handleSubmit"
			>
				<b-form-input
					id="nombre"
					v-model="item_med.nombre"
					type="text"
					placeholder="Ingrese el nombre"
					invalid-feedback="Complete este campo"
					:state="validacion.nombre.estado"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="nombre-live-feedback">
					{{ validacion.nombre.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group
				label="*Presentacion"
				label-for="presentacion"
				@submit.stop.prevent="handleSubmit"
			>
				<b-form-textarea
					id="presentacion"
					v-model="item_med.presentacion"
					type="text"
					placeholder="Describa la presentacion"
					invalid-feedback="Complete este campo"
					:state="validacion.presentacion.estado"
					required
					rows="3"
					max-rows="6"
				>
				</b-form-textarea>
				<b-form-invalid-feedback id="presentacion-live-feedback">
					{{ validacion.presentacion.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>
			<b-form-group
				label="*Laboratorio"
				label-for="laboratorio"
				@submit.stop.prevent="handleSubmit"
			>
				<b-form-input
					id="laboratorio"
					v-model="item_med.laboratorio"
					type="text"
					:state="validacion.laboratorio.estado"
					placeholder="Ingrese el nombre"
					invalid-feedback="Complete este campo"
					aria-describedby="input-live-help input-live-feedback"
					required
				>
					<b-form-invalid-feedback id="input-live-feedback">
						Debe ingresar al menos 100 caracteres.
					</b-form-invalid-feedback>
				</b-form-input>
				<b-form-invalid-feedback id="laboratorio-live-feedback">
					{{ validacion.laboratorio.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group
				label="*Farmacia"
				label-for="cod_farmacia"
				@submit.stop.prevent="handleSubmit"
			>
				<!--
				<b-form-select
					id="cod_farmacia"
					v-model="item_med.cod_farmacia"
					type="text"
					placeholder="Ingrese un Numero"
					invalid-feedback="Complete este campo"
					required
					:state="validacion.cod_farmacia.estado"
					:options="options"
				>
				</b-form-select>
				-->
				<v-autocomplete
					id="cod_farmacia"
					v-model="item_med.cod_farmacia"
					:items="options"
					type="text"
					solo
					filled
				></v-autocomplete>
				<b-form-invalid-feedback id="cod_farmacia-live-feedback">
					{{ validacion.cod_farmacia.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>
		</b-form>

		<b-button class="mt-2" variant="success" block @click="putMedicamento()"
			>Guardar</b-button
		>
	</div>
</template>

<script>
	import { APIControler } from "@/store/APIControler";
	import axios from "axios";

	export default {
		props: {
			item_med: {},
			updateTable: Function,
		},
		data() {
			return {
				// medicamentos: {},
				farmacias: {},
				data: {},
				respuesta: {},
				options: [{ value: null, text: "Elija una farmacia", disabled: true }],
				validacion: {
					id_medicamento: { estado: null, mensaje: "" },
					nombre: { estado: null, mensaje: "" },
					presentacion: { estado: null, mensaje: "" },
					laboratorio: { estado: null, mensaje: "" },
					cod_farmacia: { estado: null, mensaje: "" },
				},
			};
		},
		created: function () {
			//console.log('Funcion realizada');
			this.getFarmacias();
		},
		methods: {
			getForeingKeys() {
				this.item_med.cod_farmacia = "http://localhost:8081/farmacias/"+this.item_med.farmacia.split('-')[0]+"/";
			},
			async getFarmacias() {
				let farmaciaAPI = new APIControler();
				farmaciaAPI.apiUrl.pathname = "farmacias/";
				this.data = await farmaciaAPI.getData(this.farmacias);
				this.data.forEach((element) => {
					let option = {};
					option.value =
						"http://localhost:8081/farmacias/" + element.cod_farmacia + "/";
					option.text = element.farmacia;
					console.log(option);
					this.options.push(option);
				});
			},

			async putMedicamento() {
				let resp = "vacio";
				await axios
					.put(
						"http://localhost:8081/medicamentos/" +
							this.item_med.id_medicamento +
							"/",
						this.item_med
					)
					.then(function () {
						swal("Operación Exitosa", " ", "success");
					})
					.catch(function (error) {
						const mje =
							error.response.status < 500
								? "Los datos no son válidos"
								: "Se ha detectado un problema ";
						swal("¡ERROR!", mje, "error");
						resp = error.response.data;
					});
				this.respuesta = resp;
				this.cargarFeedback();
				this.updateTable();
			},
			cargarFeedback() {
				let valido;
				for (let key in this.validacion) {
					valido = !this.respuesta.hasOwnProperty(key);
					this.validacion[key].estado = valido;
					//console.log(key);
					if (!valido) this.validacion[key].mensaje = this.respuesta[key][0];
				}
			},
		},
		beforeMount() {
			this.getForeingKeys();
		},
	};
</script>

<style></style>
