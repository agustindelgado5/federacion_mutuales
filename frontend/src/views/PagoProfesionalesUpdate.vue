<template>
	<div>
		<b-form>
			<b-form-group label="Elija la forma de pago">
				<b-form-select
					v-model="selected"
					:options="options"
					class="mb-3"
					type="text"
					required
				></b-form-select>
			</b-form-group>
			<!--
			{{ idMedico }}
			<br />
			{{ selected }}
			<br />
			{{ datos }}
			<br />
			{{ ordenes }}
			<br />
			{{ tabla_pagos }}
			-->

			<b-button class="mt-2" variant="success" block @click="putModoPago()">
				<b>GUARDAR</b>
			</b-button>
		</b-form>
	</div>
</template>

<script>
	import { APIControler } from "@/store/APIControler";
	import axios from "axios";

	export default {
		props: {
			datos: {},
			ordenes: [],
			idMedico: 0,

			updateTable: Function,
		},
		data() {
			return {
				//profesional: {},
				respuesta: {},
				selected: null,
				tabla_pagos: [],
				validarError: {
					validateStatus: function (status) {
						return status < 500; // Resolve only if the status code is less than 500
					},
				},

				options: [
					{
						value: null,
						text: "--------ELIJA UNA FORMA DE PAGO--------",
						disabled: true,
					},
					{ value: "Contado", text: "Contado" },
					{ value: "Transferencia", text: "Transferencia" },
				],
			};
		},
		methods: {
			async getPagosProfesional() {
				let profesionalAPI = new APIControler();
				profesionalAPI.apiUrl.pathname = "pagos_profesionales/";
				let response = await fetch(profesionalAPI.apiUrl);
				let dataPagos = await response.json();
				this.tabla_pagos = dataPagos.results;
			},
			//Funcion para modificar la forma de pago
			async putModoPago() {
				try {
					let pagoUpdate = {};
					let IdPago = 0;
					pagoUpdate.id_medico =
						"http://localhost:8081/profesionales/" + this.idMedico + "/";
					pagoUpdate.forma_pago = this.selected;
					pagoUpdate.mes = this.datos.mes.split("/")[0];
					pagoUpdate.anio = parseInt(this.datos.mes.split("/")[1]);

					for (let i = 0; i < this.tabla_pagos.length; i++) {
						if (
							this.tabla_pagos[i].mes == pagoUpdate.mes &&
							this.tabla_pagos[i].anio == pagoUpdate.anio
						) {
							pagoUpdate.cantidad_ordenes_mes =
								this.tabla_pagos[i].cantidad_ordenes_mes;
							pagoUpdate.total = this.tabla_pagos[i].total;
							IdPago = this.tabla_pagos[i].id_pago;
							break;
						}
					}

					console.log("PAGO A MODIFICAR : ", IdPago, pagoUpdate);
					this.respuesta = await axios.put(
						"http://localhost:8081/pagos_profesionales/" + IdPago + "/",
						pagoUpdate,
						this.validarError
					);
					const content = this.respuesta.request;
					if (content.statusText == "OK") {
						this.respuesta = "";
						console.log("¡Ordenes cargadas con exito!");
						swal("¡Carga exitosa!", " ", "success");
					} else {
						this.respuesta = JSON.parse(content.response);
						swal("¡ERROR!", "No se pudo guardar los cambios ", "error");
						console.log(this.respuesta);
					}

					//this.updateTable();
				} catch (error) {
					//this.hideModal();
					swal("¡ERROR!", "No se pudo guardar los cambios ", "error");
					console.log(error);
				}
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
			//this.show = true;
			//this.getOrdenes();
			this.getPagosProfesional();
			//this.PostPagosProfesional();
			//this.saveFile();
		},
	};
</script>

<style></style>
