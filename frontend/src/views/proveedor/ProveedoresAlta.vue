<template>
	<div>
		<h6>Los campos en (*) son obligatorios</h6>

		<b-form>
			<b-card no-body class="mb-1">
				<b-card-header header-tag="header" class="p-1" role="tab">
					<b-button
						block
						v-b-toggle.accordion-1
						style="background-color: darkorange"
						>Datos Principales:</b-button
					>
				</b-card-header>
				<b-collapse
					id="accordion-1"
					visible
					accordion="my-accordion"
					role="tabpanel"
				>
					<b-card-body>
						<b-form-group label="*Nombre" label-for="nombre">
							<b-form-input
								id="nombre"
								v-model="proveedor.nombre"
								type="text"
								placeholder="Ingrese un nombre"
								invalid-feedback="Complete este campo"
								:state="validacion.nombre.estado"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="nombre-live-feedback">
								{{ validacion.nombre.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="*CUIT" label-for="cuit">
							<b-form-input
								id="cuit"
								v-model="proveedor.cuit"
								:state="validacion.cuit.estado"
								type="number"
								placeholder="Ingrese un cuit"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="cuit-live-feedback">
								{{ validacion.cuit.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
					</b-card-body>
				</b-collapse>
			</b-card>
			<b-card no-body class="mb-1">
				<b-card-header header-tag="header" class="p-1" role="tab">
					<b-button
						block
						v-b-toggle.accordion-2
						style="background-color: darkorange"
						>Direccion:</b-button
					>
				</b-card-header>
				<b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
					<b-card-body>
						<b-form-group label="*Calle" label-for="direccion">
							<b-form-input
								id="direccion"
								v-model="proveedor.direccion"
								:state="validacion.direccion.estado"
								type="text"
								placeholder="Ingrese una calle"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="direccion-live-feedback"
								>{{ validacion.direccion.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
						<b-form-group label="*Localidad" label-for="localidad">
							<b-form-input
								id="localidad"
								v-model="proveedor.localidad"
								:state="validacion.localidad.estado"
								type="text"
								placeholder="Ingrese una localidad"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="localidad-live-feedback"
								>{{ validacion.localidad.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
						<b-form-group label="*Provincia" label-for="provincia">
							<b-form-select
								id="provincia"
								v-model="proveedor.provincia"
								:state="validacion.provincia.estado"
								type="text"
								placeholder="Ingrese una provincia"
								invalid-feedback="Complete este campo"
								required
								:options="options"
							>
							</b-form-select>
						</b-form-group>
					</b-card-body>
				</b-collapse>
			</b-card>

			<b-card no-body class="mb-1">
				<b-card-header header-tag="header" class="p-1" role="tab">
					<b-button
						block
						v-b-toggle.accordion-3
						style="background-color: darkorange"
						>Contacto:</b-button
					>
				</b-card-header>
				<b-collapse id="accordion-3" accordion="my-accordion" role="tabpanel">
					<b-card-body>
						<b-form-group label="Email" label-for="email">
							<b-form-input
								id="email"
								v-model="proveedor.email"
								:state="validacion.email.estado"
								type="email"
								placeholder="Ingrese un email"
								invalid-feedback="Complete este campo"
							>
							</b-form-input>
							<b-form-invalid-feedback id="email-live-feedback"
								>{{ validacion.email.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="Telefono fijo" label-for="tel_fijo">
							<b-form-input
								id="tel_fijo"
								v-model="proveedor.tel_fijo"
								:state="validacion.tel_fijo.estado"
								type="number"
								placeholder="Ingrese un numero"
							>
							</b-form-input>
							<b-form-invalid-feedback id="tel_fijo-live-feedback"
								>{{ validacion.tel_fijo.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="Celular" label-for="tel_celular">
							<b-form-input
								id="tel_celular"
								v-model="proveedor.tel_celular"
								:state="validacion.tel_celular.estado"
								type="number"
								placeholder="Ingrese un numero"
							>
							</b-form-input>
							<b-form-invalid-feedback id="tel_celular-live-feedback"
								>{{ validacion.tel_celular.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
					</b-card-body>
				</b-collapse>
			</b-card>
		</b-form>
		<b-button
			class="mt-2"
			variant="success"
			block
			@click.prevent="postproveedor()"
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
				proveedor: {},
				respuesta: {},
				validacion: {
					id_proveedor: { estado: null, mensaje: "" },
					nombre: { estado: null, mensaje: "" },
					cuit: { estado: null, mensaje: "" },
					direccion: { estado: null, mensaje: "" },
					provincia: { estado: null, mensaje: "" },
					localidad: { estado: null, mensaje: "" },
					email: { estado: null, mensaje: "" },
					tel_fijo: { estado: null, mensaje: "" },
					tel_celular: { estado: null, mensaje: "" },
				},
				options: [
					{ value: "Buenos Aires", text: "1- Buenos Aires" },
					{ value: "Catamarca", text: "2- Catamarca" },
					{ value: "Chaco", text: "3- Chaco" },
					{ value: "Chubut", text: "4- Chubut" },
					{ value: "Córdoba", text: "5- Córdoba" },
					{ value: "Corrientes", text: "6- Corrientes" },
					{ value: "Entre Ríos", text: "7- Entre Ríos" },
					{ value: "Formosa", text: "8- Formosa" },
					{ value: "Jujuy", text: "9- Jujuy" },
					{ value: "La Pampa", text: "10- La Pampa" },
					{ value: "La Rioja", text: "11- La Rioja" },
					{ value: "Mendoza", text: "12- Mendoza" },
					{ value: "Misiones", text: "13- Misiones" },
					{ value: "Neuquén", text: "14- Neuquén" },
					{ value: "Río Negro", text: "15- Río Negro" },
					{ value: "Salta", text: "16- Salta" },
					{ value: "San Juan", text: "17- San Juan" },
					{ value: "San Luis", text: "18- San Luis" },
					{ value: "Santa Cruz", text: "19- Santa Cruz" },
					{ value: "Santa Fe", text: "20- Santa Fe" },
					{ value: "Santiago del Estero", text: "21- Santiago del Estero" },
					{ value: "Tierra del Fuego", text: "22- Tierra del Fuego" },
					{ value: "Tucumán", text: "23- Tucumán" },
				],
			};
		},
		methods: {
			async getproveedor() {
				let proveedorAPI = new APIControler();
				this.data = await proveedorAPI.getData();
			},
			async postproveedor() {
				let proveedorAPI = new APIControler();
				proveedorAPI.apiUrl.pathname = "proveedor_estudios/";
				this.respuesta = await proveedorAPI.postData(this.proveedor);
				this.cargarFeedback();

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
	};
</script>

<style></style>
