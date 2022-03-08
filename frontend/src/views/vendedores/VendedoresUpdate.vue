<template>
	<div>
		<h6>Los campos en (*) son obligatorios</h6>
		<h4>Datos</h4>

		<b-form>
			<b-form-group label="*Socio"
						  label-for="numero_socio"
						  @submit.stop.prevent="handleSubmit">
				<b-form-select id="numero_socio"
							   v-model="vendedor.numero_socio"
							   :state="validacion.numero_socio.estado"
							   type="text"
							   placeholder="Ingrese un Numero"
							   invalid-feedback="Complete este campo"
							   required
							   :options="op_socios">
				</b-form-select>
				<b-form-invalid-feedback id="numero_socio-live-feedback">
					{{ validacion.numero_socio.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group label="*Nombre/s"
						  label-for="nombre"
						  @submit.stop.prevent="handleSubmit">
				<b-form-input id="nombre"
							  v-model="vendedor.nombre"
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
							  v-model="vendedor.apellido"
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
			<b-form-group label="*DNI"
						  label-for="dni"
						  @submit.stop.prevent="handleSubmit">
				<b-form-input id="dni"
							  v-model="vendedor.dni"
							  type="text"
							  placeholder="Ingrese un DNI"
							  :state="validacion.dni.estado"
							  invalid-feedback="Complete este campo"
							  required>
				</b-form-input>
				<b-form-invalid-feedback id="dni-live-feedback">
					{{ validacion.dni.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group label="*Fecha de nacimiento"
						  label-for="fecha_nacimiento"
						  @submit.stop.prevent="handleSubmit">
				<b-form-input id="fecha_cobro"
							  v-model="vendedor.fecha_nacimiento"
							  type="date"
							  placeholder="Ingrese una fecha"
							  :state="validacion.fecha_nacimiento.estado"
							  invalid-feedback="Complete este campo"
							  required>
				</b-form-input>
				<b-form-invalid-feedback id="fecha_nacimiento-live-feedback">
					{{ validacion.fecha_nacimiento.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>
			<b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
				<b-card-body>
					<b-form-group label="*Calle" label-for="direccion">
						<b-form-input id="direccion"
									  v-model="vendedor.direccion"
									  :state="validacion.direccion.estado"
									  type="text"
									  placeholder="Ingrese una calle"
									  invalid-feedback="Complete este campo"
									  required>
						</b-form-input>
						<b-form-invalid-feedback id="direccion-live-feedback">
							{{ validacion.direccion.mensaje }}
						</b-form-invalid-feedback>
					</b-form-group>
					<b-form-group label="*Localidad" label-for="localidad">
						<b-form-input id="localidad"
									  v-model="vendedor.localidad"
									  :state="validacion.localidad.estado"
									  type="text"
									  placeholder="Ingrese una localidad"
									  invalid-feedback="Complete este campo"
									  required>
						</b-form-input>
						<b-form-invalid-feedback id="localidad-live-feedback">
							{{ validacion.localidad.mensaje }}
						</b-form-invalid-feedback>
					</b-form-group>
					<b-form-group label="*Provincia" label-for="provincia">
						<b-form-select id="provincia"
									   v-model="vendedor.provincia"
									   :state="validacion.provincia.estado"
									   type="text"
									   placeholder="Ingrese una provincia"
									   invalid-feedback="Complete este campo"
									   required
									   :options="options">
						</b-form-select>
					</b-form-group>
					<b-form-group label="*Codigo Postal" label-for="cod_postal">
						<b-input id="cod_postal"
								 v-model="vendedor.cod_postal"
								 :state="validacion.cod_postal.estado"
								 type="number"
								 placeholder="Ingrese un codigo postal"
								 invalid-feedback="Complete este campo"
								 required>
						</b-input>
					</b-form-group>
				</b-card-body>
			</b-collapse>

			<b-card no-body class="mb-1">
				<b-card-header header-tag="header" class="p-1" role="tab">
					<b-button block
							  v-b-toggle.accordion-3
							  style="background-color: darkorange">Contacto:</b-button>
				</b-card-header>
				<b-collapse id="accordion-3" accordion="my-accordion" role="tabpanel">
					<b-card-body>

						<b-form-group label="Telefono fijo" label-for="tel_fijo">
							<b-form-input id="tel_fijo"
										  v-model="vendedor.tel_fijo"
										  :state="validacion.tel_fijo.estado"
										  type="number"
										  placeholder="Ingrese un numero">
							</b-form-input>
							<b-form-invalid-feedback id="tel_fijo-live-feedback">
								{{ validacion.tel_fijo.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="Celular" label-for="tel_celular">
							<b-form-input id="tel_celular"
										  v-model="vendedor.tel_celular"
										  :state="validacion.tel_celular.estado"
										  type="number"
										  placeholder="Ingrese un numero">
							</b-form-input>
							<b-form-invalid-feedback id="tel_celular-live-feedback">
								{{ validacion.tel_celular.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
					</b-card-body>
				</b-collapse>
			</b-card>
		</b-form>

		<!-- {{vendedor}}
+    <br>
+    <br>
+    {{ data }} -->

		<b-button class="mt-2" variant="success" block @click="putVendedor()"
			>Modificar</b-button
		>
	</div>
</template>

<script>
	import { APIControler } from "../../store/APIControler";
	import axios from "axios";

	export default {
		props: {
			vendedor: {},
			updateTable: Function,
		},
		data() {
			return {
				list_socios: {},
				vendedor: {},
				data: {},
				options: [{ value: null, text: "Elija un vendedor", disabled: true }],
				op_socios: [{ value: null, text: "Elija un socio", disabled: true }],

                validacion: {
                    numero_socio: { estado: null, mensaje: "" },
                    //id_vendedor: { estado: null, mensaje: "" },
                    nombre: { estado: null, mensaje: "" },
                    apellido: { estado: null, mensaje: "" },
                    dni: { estado: null, mensaje: "" },
                    fecha_nacimiento: { estado: null, mensaje: "" },
                    calle: { estado: null, mensaje: "" },
                    localidad: { estado: null, mensaje: "" },
                    departamento: { estado: null, mensaje: "" },
                    cod_postal: { estado: null, mensaje: "" },
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
		created: function () {
			//console.log('Funcion realizada');
			this.getVendedor();
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
			async getVendedor() {
				let vendedorAPI = new APIControler();
				vendedorAPI.apiUrl.pathname = "vendedor/";
				this.data = await vendedorAPI.getData(this.vendedor);
				this.data.forEach((element) => {
					let option = {};
					option.value =
						"http://localhost:8081/vendedor/" + element.id_vendedor + "/";
					option.text = element.vendedor;
					console.log(option);
					this.options.push(option);
				});
			},

			async putVendedor() {
				let respuesta = "vacio";
				// try{
				await axios
					.put(
						"http://localhost:8081/vendedores/" +
							this.vendedor.id_vendedor +
							"/",
						this.vendedor
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
