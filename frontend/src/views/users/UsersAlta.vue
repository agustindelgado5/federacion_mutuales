<template>
	<div>
		<h6>Los campos en (*) son obligatorios</h6>
		<h4>Datos</h4>

		<b-form>
			<b-form-group label="*Usuario"
						  label-for="username"
						  @submit.stop.prevent="handleSubmit">
				<b-form-input id="username"
							  v-model="Users.username"
							  type="text"
							  placeholder="*Ingrese el Usuario"
							  :state="validacion.username.estado"
							  invalid-feedback="Complete este campo"
							  required>
				</b-form-input>
				<b-form-invalid-feedback id="username-live-feedback">
					{{ validacion.username.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group label="*Nombre/s"
						  label-for="nombre"
						  @submit.stop.prevent="handleSubmit">
				<b-form-input id="nombre"
							  v-model="Users.nombre"
							  type="text"
							  placeholder="*Ingrese los Nombre/s"
							  :state="validacion.nombre.estado"
							  invalid-feedback="Complete este campo"
							  required>
				</b-form-input>
				<b-form-invalid-feedback id="nombre-live-feedback">
					{{ validacion.nombre.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>
			<b-form-group label="*Apellido/s"
						  label-for="apellido"
						  @submit.stop.prevent="handleSubmit">
				<b-form-input id="apellido"
							  v-model="Users.apellido"
							  type="text"
							  placeholder="*Ingrese los Apellido/s"
							  :state="validacion.apellido.estado"
							  invalid-feedback="Complete este campo"
							  required>
				</b-form-input>
				<b-form-invalid-feedback id="apellido-live-feedback">
					{{ validacion.apellido.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>
			<b-form-group label="*Email"
						  label-for="email"
						  @submit.stop.prevent="handleSubmit">
				<b-form-input id="email"
							  v-model="Users.email"
							  type="text"
							  placeholder="Ingrese un email"
							  :state="validacion.email.estado"
							  invalid-feedback="Complete este campo"
							  required>
				</b-form-input>
				<b-form-invalid-feedback id="email-live-feedback">
					{{ validacion.email.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>
			<b-form-group label="*Contraseña"
						  label-for="password"
						  @submit.stop.prevent="handleSubmit">
				<b-form-input id="password"
							  v-model="Users.password"
							  type="password"
							  placeholder="Ingrese un password"
							  :state="validacion.password.estado"
							  invalid-feedback="Complete este campo"
							  required>
				</b-form-input>
				<b-form-invalid-feedback id="password-live-feedback">
					{{ validacion.password.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>
			<b-form-group label="Es Staff" label-for="is_staff">
				<b-form-checkbox id="is_staff"
								 v-model="Users.is_staff"
								 value="true"
								 type="boolean"
								 invalid-feedback="Complete este campo"
								 required
								 unchecked-value="false">
				</b-form-checkbox>
			</b-form-group>
			<b-form-group label="Es Administrador" label-for="is_superuser">
				<b-form-checkbox id="is_superuser"
								 v-model="Users.is_superuser"
								 value="true"
								 type="boolean"
								 invalid-feedback="Complete este campo"
								 required
								 unchecked-value="false">
				</b-form-checkbox>
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
				Users: {},
				data: {},
				respuesta: {},
				op_socios: [{ value: null, text: "Elija un socio", disabled: true }],
				validacion: {
					id_user: { estado: null, mensaje: "" },
                    username: { estado: null, mensaje: "" },
					nombre: { estado: null, mensaje: "" },
					apellido: { estado: null, mensaje: "" },
					email: { estado: null, mensaje: "" },
					password: { estado: null, mensaje: "" },
				},
			};
		},
		methods: {
			async getCobrador() {
				let cobradorAPI = new APIControler();
				this.data = await cobradorAPI.getData();
			},
			async postCobrador() {
				let cobradorAPI = new APIControler();
				cobradorAPI.apiUrl.pathname = "cobradores/";
				this.respuesta = await cobradorAPI.postData(this.Users);
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
			
		},
	};
</script>

<style></style>
