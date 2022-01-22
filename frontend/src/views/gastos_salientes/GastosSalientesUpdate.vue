<template>
	<div>
		<h6>Los campos en (*) son obligatorios</h6>
		<h4>Datos</h4>

		<b-form>
			<!-- nro_ticket -->
			<b-form-group
				label="*Numero de Ticket"
				label-for="nro_ticket"
				@submit.stop.prevent="handleSubmit"
			>
				<b-form-input
					id="nro_ticket"
					v-model="gastoSaliente.nro_ticket"
					type="number"
					placeholder="Ingrese el numero del ticket"
					:state="validacion.nro_ticket.estado"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="nro_ticket-live-feedback"
					>{{ validacion.nro_ticket.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<!-- descripcion -->
			<b-form-group label="*Descripcion" label-for="descripcion">
				<b-form-input
					id="descripcion"
					v-model="gastoSaliente.descripcion"
					type="text"
					placeholder="*Ingrese la descripcion del gasto"
					:state="validacion.descripcion.estado"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="descripcion-live-feedback"
					>{{ validacion.descripcion.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<!-- total -->
			<b-form-group
				label="*Total"
				label-for="total"
				@submit.stop.prevent="handleSubmit"
			>
				<b-form-input
					id="total"
					v-model="gastoSaliente.total"
					type="number"
					:state="validacion.total.estado"
					placeholder="Ingrese el total del gasto"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="total-live-feedback">
					{{ validacion.total.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<!-- fecha -->
			<b-form-group label="*Fecha" label-for="fecha">
				<b-form-input
					id="fecha"
					v-model="gastoSaliente.fecha"
					:state="validacion.fecha.estado"
					type="date"
					placeholder="Ingrese una fecha"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="fecha-live-feedback">
					{{ validacion.fecha.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>
		</b-form>
		<b-button class="mt-2" variant="success" block @click="putGastoSaliente()"
			>Modificar</b-button
		>
	</div>
</template>

<script>
	import { APIControler } from "@/store/APIControler";
	import axios from "axios";

	export default {
		props: {
			gastoSaliente: {},
			updateTable: Function,
		},
		data() {
			return {
				gastosSalientes: {},
				data: {},
				options: [{ value: null, text: "Elija una gasto", disabled: true }],

				validacion: {
					nro_ticket: { estado: null, mensaje: "" },
					descripcion: { estado: null, mensaje: "" },
					total: { estado: null, mensaje: "" },
					fecha: { estado: null, mensaje: "" },
				},
			};
		},
		created: function () {
			this.getGastosSalientes();
		},
		methods: {
			async getGastosSalientes() {
				let gastoSalienteAPI = new APIControler();
				gastoSalienteAPI.apiUrl.pathname = "gastosSalientes/";
				this.data = await gastoSalienteAPI.getData(this.gastosSalientes);
				this.data.forEach((element) => {
					let option = {};
					option.value =
						"http://localhost:8081/gastosSalientes/" + element.id_gasto + "/";
					option.text = element.gastoSaliente;
					console.log(option);
					this.options.push(option);
				});
			},

			async putGastoSaliente() {
				let respuesta = "vacio";
				await axios
					.put(
						"http://localhost:8081/gastosSalientes/" +
							this.gastoSaliente.id_gasto +
							"/",
						this.gastoSaliente
					)
					.then(function (data) {
						swal("Operación Exitosa", " ", "success");
					})
					.catch(function (error) {
						const mje =
							error.response.status < 500
								? "Los datos no son válidos"
								: "Se ha detectado un problema ";
						swal("¡ERROR!", mje, "error");
						respuesta = error.response.data;
					});
				this.cargarFeedback(respuesta);
				this.updateTable();
				// console.log("respuesta:");
				// console.log(respuesta);
			},

			cargarFeedback(respuestaAPI) {
				console.log("respuestaAPI");
				console.log(respuestaAPI);
				let valido;
				for (let key in this.validacion) {
					valido = !respuestaAPI.hasOwnProperty(key);
					this.validacion[key].estado = valido;
					console.log(key);

					if (!valido) this.validacion[key].mensaje = respuestaAPI[key][0];
				}
			},
		},
	};
</script>

<style></style>
