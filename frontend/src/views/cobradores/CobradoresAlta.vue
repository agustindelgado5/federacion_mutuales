<template>
	<div>
		<h6>Los campos en (*) son obligatorios</h6>
		<h4>Datos</h4>

		<b-form>
			<b-form-group
				label="*Nombre/s"
				label-for="nombre"
				@submit.stop.prevent="handleSubmit"
			>
				<b-form-input
					id="nombre"
					v-model="Cobradores.nombre"
					type="text"
					placeholder="*Ingrese los Nombre/s"
					:state="validacion.nombre.estado"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="nombre-live-feedback"
					>{{ validacion.nombre.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>
			<b-form-group
				label="*Apellido/s"
				label-for="apellido"
				@submit.stop.prevent="handleSubmit"
			>
				<b-form-input
					id="apellido"
					v-model="Cobradores.apellido"
					type="text"
					placeholder="*Ingrese los Apellido/s"
					:state="validacion.apellido.estado"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="apellido-live-feedback"
					>{{ validacion.apellido.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>
			<b-form-group
				label="*DNI"
				label-for="dni"
				@submit.stop.prevent="handleSubmit"
			>
				<b-form-input
					id="dni"
					v-model="Cobradores.dni"
					type="text"
					placeholder="Ingrese un DNI"
					:state="validacion.dni.estado"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="dni-live-feedback"
					>{{ validacion.dni.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group
				label="*Fecha de cobro"
				label-for="fecha_cobro"
				@submit.stop.prevent="handleSubmit"
			>
				<b-form-input
					id="fecha_cobro"
					v-model="Cobradores.fecha_cobro"
					type="date"
					placeholder="Ingrese una fecha"
					:state="validacion.fecha_cobro.estado"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="fecha_cobro-live-feedback"
					>{{ validacion.fecha_cobro.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>
		</b-form>
		<b-button class="mt-2" variant="success" block @click="postCobrador()"
			>Enviar</b-button
		>
	</div>
</template>

<script>
	import { APIControler } from "../../store/APIControler";

	export default {
		props: {
			updateTable: Function,
		},
		data() {
			return {
				list_socios: {},
				Cobradores: {},
				data: {},
				respuesta: {},
				op_socios: [{ value: null, text: "Elija un socio", disabled: true }],
				validacion: {
					numero_socio: { estado: null, mensaje: "" },
					//id_cobrador: { estado: null, mensaje: "" },
					nombre: { estado: null, mensaje: "" },
					apellido: { estado: null, mensaje: "" },
					dni: { estado: null, mensaje: "" },
					fecha_cobro: { estado: null, mensaje: "" },
				},
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

			async getCobrador() {
				let cobradorAPI = new APIControler();
				this.data = await cobradorAPI.getData();
			},
			async postCobrador() {
				let cobradorAPI = new APIControler();
				cobradorAPI.apiUrl.pathname = "cobradores/";
				this.respuesta = await cobradorAPI.postData(this.Cobradores);
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
			this.getSocios();
		},
	};
</script>

<style></style>
