<template>
	<div>
		<h6>Los campos en (*) son obligatorios</h6>
		<h4>Datos</h4>

		<b-form>
			<b-form-group
				label="*Socio"
				label-for="numero_socio"
				@submit.stop.prevent="handleSubmit"
			>
				<b-form-select
					id="numero_socio"
					v-model="cobrador.numero_socio"
					:state="validacion.numero_socio.estado"
					type="text"
					placeholder="Ingrese un Numero"
					invalid-feedback="Complete este campo"
					required
					:options="op_socios"
				>
				</b-form-select>
				<b-form-invalid-feedback id="numero_socio-live-feedback"
					>{{ validacion.numero_socio.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group
				label="*Nombre/s"
				label-for="nombre"
				@submit.stop.prevent="handleSubmit"
			>
				<b-form-input
					id="nombre"
					v-model="cobrador.nombre"
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
					v-model="cobrador.apellido"
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
					v-model="cobrador.dni"
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
					v-model="cobrador.fecha_cobro"
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

		<!-- {{cobrador}}
+    <br>
+    <br>
+    {{ data }} -->

		<b-button class="mt-2" variant="success" block @click="putCobrador()"
			>Modificar</b-button
		>
	</div>
</template>

<script>
	import { APIControler } from "../../store/APIControler";
	import axios from "axios";

	export default {
		props: {
			cobrador: {},
			updateTable: Function,
		},
		data() {
			return {
				list_socios: {},
				cobrador: {},
				data: {},
				options: [{ value: null, text: "Elija un cobrador", disabled: true }],
				op_socios: [{ value: null, text: "Elija un socio", disabled: true }],

				validacion: {
					numero_socio: { estado: null, mensaje: "" },
					id_cobrador: { estado: null, mensaje: "" },
					nombre: { estado: null, mensaje: "" },
					apellido: { estado: null, mensaje: "" },
					dni: { estado: null, mensaje: "" },
					fecha_cobro: { estado: null, mensaje: "" },
				},
			};
		},
		created: function () {
			//console.log('Funcion realizada');
			this.getCobrador();
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
				cobradorAPI.apiUrl.pathname = "cobrador/";
				this.data = await cobradorAPI.getData(this.cobrador);
				this.data.forEach((element) => {
					let option = {};
					option.value =
						"http://localhost:8081/cobrador/" + element.id_cobrador + "/";
					option.text = element.cobrador;
					console.log(option);
					this.options.push(option);
				});
			},

			async putCobrador() {
				let respuesta = "vacio";
				// try{
				await axios
					.put(
						"http://localhost:8081/cobradores/" +
							this.cobrador.id_cobrador +
							"/",
						this.cobrador
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

				console.log("respuesta:");
				console.log(respuesta);
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
		beforeMount() {
			this.getSocios();
		},
	};
</script>

<style></style>
