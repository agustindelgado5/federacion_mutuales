<template>
	<div>
		<h6>Los campos en (*) son obligatorios</h6>

		<b-form>
			<b-form-group label="*Socio" label-for="numero_socio">
				<b-form-select
					id="numero_socio"
					v-model="orden.numero_socio"
					type="text"
					placeholder="Ingrese un Numero"
					invalid-feedback="Complete este campo"
					:state="validacion.numero_socio.estado"
					required
					:options="op_socios"
					@change="getPaciente()"
				>
				</b-form-select>
				<b-form-invalid-feedback id="numero_socio-live-feedback">
					{{ validacion.numero_socio.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<!-- Paciente para el cual se emite la receta -->

			<b-form-group label="*Paciente" label-for="paciente">
				<b-form-select
					id="dni_familiar"
					v-model="orden.paciente"
					type="text"
					placeholder="*Ingrese el nombre completo del paciente"
					:state="validacion.paciente.estado"
					invalid-feedback="Complete este campo"
					required
					:options="list_pacientes"
				>
				</b-form-select>
				<b-form-invalid-feedback id="paciente-live-feedback">
					{{ validacion.paciente.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<!-- Servicio -->
			<b-form-group label="*Servicio" label-for="servicio">
				<b-form-input
					id="servicio"
					v-model="orden.servicio"
					:state="validacion.servicio.estado"
					type="text"
					placeholder="*Ingrese el tipo de servicio"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="servicio-live-feedback">
					{{ validacion.servicio.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<!-- Id del medico -->

			<b-form-group data-app label="*Medico" label-for="id_medico">
				<v-autocomplete
					id="id_medico"
					v-model="orden.id_medico"
					:items="op_profesionales"
					type="text"
					solo
					placeholder="Ingrese el ID del medico"
					invalid-feedback="Complete este campo"
					required
				></v-autocomplete>

				<b-form-invalid-feedback id="id_medico-live-feedback">
					{{ validacion.id_medico.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<!-- Id de la mutual -->

			<b-form-group label="*ID Mutual" label-for="id_mutual">
				<b-form-select
					id="id_mutual"
					v-model="orden.id_mutual"
					:state="validacion.id_mutual.estado"
					type="text"
					placeholder="Ingrese el ID de la mutual"
					invalid-feedback="Complete este campo"
					required
					:options="op_mutuales"
				>
				</b-form-select>
				<b-form-invalid-feedback id="id_mutual-live-feedback">
					{{ validacion.id_mutual.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<!-- Fecha de emision -->
			<b-form-group label="*Fecha" label-for="fecha">
				<b-form-input
					id="fecha"
					v-model="orden.fecha"
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

			<!-- Hora -->
			<b-form-group label="*Hora" label-for="hora">
				<b-form-input
					id="hora"
					v-model="orden.hora"
					:state="validacion.hora.estado"
					type="time"
					placeholder="Ingrese una hora"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="hora-live-feedback">
					{{ validacion.hora.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<!-- Precio Socio-->
			<b-form-group label="*Precio Socio" label-for="preciosocio">
				<b-form-input
					id="preciosocio"
					v-model="orden.preciosocio"
					:state="validacion.preciosocio.estado"
					type="decimal"
					placeholder="Ingrese el precio que paga el socio correspondiente a la orden "
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="preciosocio-live-feedback">
					{{ validacion.preciosocio.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<!-- Precio -->
			<b-form-group label="*Precio Mutual" label-for="preciomutual">
				<b-form-input
					id="preciomutual"
					v-model="orden.preciomutual"
					:state="validacion.preciomutual.estado"
					type="decimal"
					placeholder="Ingrese el precio que paga la Mutual correspondiente a la orden "
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="preciomutual-live-feedback">
					{{ validacion.preciomutual.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<!-- Realizado -->

			<b-form-group label="*Realizado" label-for="realizado">
				<b-form-checkbox
					id="realizado"
					v-model="orden.realizado"
					value="true"
					type="boolean"
					invalid-feedback="Complete este campo"
					required
					unchecked-value="false"
				>
				</b-form-checkbox>
			</b-form-group>

			<b-form-group label="*Presentada" label-for="presentada">
				<b-form-checkbox
					id="presentada"
					v-model="orden.presentada"
					value="true"
					type="boolean"
					invalid-feedback="Complete este campo"
					required
					unchecked-value="false"
				>
				</b-form-checkbox>
			</b-form-group>

			<b-form-group
				label="*Fecha Presentacion"
				label-for="fechapresentacion"
				v-show="this.orden.presentada == 'true'"
			>
				<b-form-input
					id="fechapresentacion"
					v-model="orden.fechapresentacion"
					type="date"
					placeholder="Ingrese una fecha"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
			</b-form-group>
		</b-form>

		<b-button class="mt-2" variant="success" block @click="postOrden()"
			>Guardar</b-button
		>
	</div>
</template>

<script>
	import { APIControler } from "@/store/APIControler";
	export default {
		props: {
			updateTable: Function,
		},

		data() {
			return {
				list_socios: {},
				list_profesionales: {},
				list_mutuales: {},
				list_familiar: {},
				orden: {},
				data: {},
				op_socios: [{ value: null, text: "Elija un socio", disabled: true }],
				op_profesionales: [
					{ value: null, text: "Elija un profesional", disabled: true },
				],
				op_mutuales: [
					{ value: null, text: "Elija una mutual", disabled: true },
				],
				list_pacientes: [
					{ value: null, text: "Elija una persona", disabled: true },
				],
				validacion: {
					numero_orden: { estado: null, mensaje: "" },
					numero_socio: { estado: null, mensaje: "" },
					paciente: { estado: null, mensaje: "" },
					servicio: { estado: null, mensaje: "" },
					id_medico: { estado: null, mensaje: "" },
					id_mutual: { estado: null, mensaje: "" },
					fecha: { estado: null, mensaje: "" },
					hora: { estado: null, mensaje: "" },
					preciosocio: { estado: null, mensaje: "" },
					preciomutual: { estado: null, mensaje: "" },
				},
				respuesta: null,
			};
		},

		methods: {
			async getSocios() {
				let socioAPI = new APIControler();
				socioAPI.apiUrl.pathname = "socios/";
				this.data = await socioAPI.getData(this.list_socios);
				this.data.forEach((element) => {
					let option = {};
					option.value =
						"http://localhost:8081/socios/" + element.numero_socio + "/";
					option.text =
						element.numero_socio +
						"-- " +
						element.apellido +
						", " +
						element.nombre;
					console.log(option);
					this.op_socios.push(option);
				});
			},

			async getProfesionales() {
				let profesionalesAPI = new APIControler();
				profesionalesAPI.apiUrl.pathname = "profesionales/";
				this.data = await profesionalesAPI.getData(this.list_profesionales);
				this.data.forEach((element) => {
					let option = {};
					option.value =
						"http://localhost:8081/profesionales/" + element.id_medico + "/";
					option.text =
						element.id_medico +
						"-- " +
						element.apellido +
						", " +
						element.nombre +
						"; Mat: " +
						element.matricula +
						" ; " +
						element.especialidad;
					console.log(option);
					this.op_profesionales.push(option);
				});
			},

			async getMutuales() {
				let mutualesAPI = new APIControler();
				mutualesAPI.apiUrl.pathname = "mutuales/";
				this.data = await mutualesAPI.getData(this.list_mutuales);
				this.data.forEach((element) => {
					let option = {};
					option.value =
						"http://localhost:8081/mutuales/" + element.id_mutual + "/";
					option.text =
						element.id_mutual +
						"-- " +
						element.nombre +
						", " +
						element.sucursal;
					console.log(option);
					this.op_mutuales.push(option);
				});
			},

			async getPaciente() {
				let familiarAPI = new APIControler();
				familiarAPI.apiUrl.pathname = "familiar/";
				this.data = await familiarAPI.getData(this.list_familiar);
				this.list_pacientes = this.list_pacientes.slice(0, 1); //renueva la lista, y deja el primer elemento (Elija una persona)
				let option_titular = {};
				// option_titular.value='http://localhost:8081/socios/'+ this.orden.numero_socio +'/';
				option_titular.value = this.orden.numero_socio;
				option_titular.text = "Titular";
				// option_titular.text= socios.dni +' -- '+ socios.apellido +', '+ socios.nombre ;

				this.list_pacientes.push(option_titular);

				this.data.forEach((element) => {
					if (element.numero_socio == this.orden.numero_socio) {
						//let option_titular={}
						let option_adherente = {};
						//console.log(option_titular);
						//this.list_pacientes.push(option_titular);

						option_adherente.value =
							"http://localhost:8081/familiar/" + element.dni_familiar + "/";
						option_adherente.text =
							element.dni_familiar +
							"-- " +
							element.apellido +
							", " +
							element.nombre;
						console.log(option_adherente);
						this.list_pacientes.push(option_adherente);
					}
				});
			},

			async getOrdenes() {
				let ordenAPI = new APIControler();
				this.data = await ordenAPI.getData();
			},
			async postOrden() {
				let ordenAPI = new APIControler();
				ordenAPI.apiUrl.pathname = "ordenes/";
				this.respuesta = await ordenAPI.postData(this.orden);
				this.cargarFeedback();

				this.updateTable();
			},

			cargarFeedback() {
				let valido;
				for (let key in this.validacion) {
					valido = !this.respuesta.hasOwnProperty(key);
					this.validacion[key].estado = valido;
					if (!valido) this.validacion[key].mensaje = this.respuesta[key][0];
				}
			},
		},
		beforeMount() {
			this.getSocios();
			this.getProfesionales();
			this.getMutuales();
		},
	};
</script>

<style></style>
