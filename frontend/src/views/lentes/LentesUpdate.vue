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
						>Datos:</b-button
					>
				</b-card-header>
				<b-collapse
					id="accordion-1"
					visible
					accordion="my-accordion"
					role="tabpanel"
				>
					<b-card-body>
						
						<b-form-group label="*Diametro del cristal" label-for="diametro_cristal">
							<b-form-input
								id="diametro_cristal"
								v-model="lente.diametro_cristal"
								:state="validacion.diametro_cristal.estado"
								type="text"
								placeholder="*Ingrese un diametro"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="diametro_cristal-live-feedback"
								>{{ validacion.diametro_cristal.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="*Largo de las Patillas" label-for="largo_patillas">
							<b-form-input
								id="largo_patillas"
								v-model="lente.largo_patillas"
								:state="validacion.largo_patillas.estado"
								type="number"
								placeholder="*Ingrese una medida"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="largo_patillas-live-feedback"
								>{{ validacion.largo_patillas.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="*Ancho del puente" label-for="ancho_puente">
							<b-form-input
								id="ancho_puente"
								v-model="lente.ancho_puente"
								:state="validacion.ancho_puente.estado"
								type="number"
								placeholder="*Ingrese una medida"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="ancho_puente-live-feedback"
								>{{ validacion.ancho_puente.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
						<b-form-group label="Marca" label-for="marca">
							<b-form-input
								id="marca"
								v-model="lente.marca"
								:state="validacion.marca.estado"
								type="text"
								placeholder="*Ingrese una marca"
								invalid-feedback="Complete este campo"
								
							>
							</b-form-input>
							<b-form-invalid-feedback id="marca-live-feedback"
								>{{ validacion.marca.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="Color" label-for="color">
							<b-form-input
								id="color"
								v-model="lente.color"
								:state="validacion.color.estado"
								type="text"
								placeholder="*Ingrese un color"
								invalid-feedback="Complete este campo"
								
							>
							</b-form-input>
							<b-form-invalid-feedback id="color-live-feedback"
								>{{ validacion.color.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="Material" label-for="material">
							<b-form-input
								id="material"
								v-model="lente.material"
								:state="validacion.material.estado"
								type="text"
								placeholder="*Ingrese un material"
								invalid-feedback="Complete este campo"
								
							>
							</b-form-input>
							<b-form-invalid-feedback id="material-live-feedback"
								>{{ validacion.material.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
						
						<b-form-group label="Descripcion" label-for="descripcion">
							<b-form-input
								id="descripcion"
								v-model="lente.descripcion"
								:state="validacion.descripcion.estado"
								type="text"
								placeholder="*Ingrese la descripcion"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="descripcion-live-feedback"
								>{{ validacion.descripcion.mensaje }}
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
						>Precios:</b-button
					>
				</b-card-header>
				<b-collapse
					id="accordion-2"
					visible
					accordion="my-accordion"
					role="tabpanel"
				>
					<b-card-body>
						<b-form-group label="Precio Optica" label-for="precio_optica">
							<b-form-input
								id="precio_optica"
								v-model="lente.precio_optica"
								:state="validacion.precio_optica.estado"
								type="number"
								placeholder="*Ingrese el precio de optica"
								invalid-feedback="Complete este campo"
							>
							</b-form-input>
							<b-form-invalid-feedback id="precio_optica-live-feedback"
								>{{ validacion.precio_optica.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="Precio Mutual" label-for="precio_mutual">
							<b-form-input
								id="precio_mutual"
								v-model="lente.precio_mutual"
								:state="validacion.precio_mutual.estado"
								type="number"
								placeholder="*Ingrese el precio de la mutual"
								invalid-feedback="Complete este campo"
							>
							</b-form-input>
							<b-form-invalid-feedback id="precio_mutual-live-feedback"
								>{{ validacion.precio_mutual.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="Precio Venta" label-for="precio_venta">
							<b-form-input
								id="precio_venta"
								v-model="lente.precio_venta"
								:state="validacion.precio_venta.estado"
								type="number"
								placeholder="*Ingrese el precio de la venta"
								invalid-feedback="Complete este campo"
							>
							</b-form-input>
							<b-form-invalid-feedback id="precio_venta-live-feedback"
								>{{ validacion.precio_venta.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="Precio Tarjeta" label-for="precio_tarjeta">
							<b-form-input
								id="precio_tarjeta"
								v-model="lente.precio_tarjeta"
								:state="validacion.precio_tarjeta.estado"
								type="number"
								placeholder="*Ingrese el precio de la tarjeta"
								invalid-feedback="Complete este campo"
							>
							</b-form-input>
							<b-form-invalid-feedback id="precio_tarjeta-live-feedback"
								>{{ validacion.precio_tarjeta.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="Stock" label-for="stock">
							<b-form-input
								id="stock"
								v-model="lente.stock"
								:state="validacion.stock.estado"
								type="number"
								placeholder="*Ingrese el stock"
								invalid-feedback="Complete este campo"
							>
							</b-form-input>
							<b-form-invalid-feedback id="stock-live-feedback"
								>{{ validacion.stock.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
					</b-card-body>
				</b-collapse>
			</b-card>
		</b-form>
		<b-button class="mt-2" variant="success" block @click="putLente()"
			>Guardar</b-button
		>
	</div>
</template>

<script>
	import { APIControler } from "@/store/APIControler";
	import axios from "axios";

	export default {
		props: {
			lente: {},
			updateTable: Function,
		},
		data() {
			return {
				ventasOpticas: {},
				data: {},
				respuesta: {},

				options: [{ value: null, text: "Elija una venta", disabled: true }],

				text: "",

				validacion: {
					id_lente: { estado: null, mensaje: "" },
					diametro_cristal: { estado: null, mensaje: "" },
					largo_patillas: { estado: null, mensaje: "" },
					ancho_puente: { estado: null, mensaje: "" },
					marca: { estado: null, mensaje: "" },
					color: { estado: null, mensaje: "" },
					material: { estado: null, mensaje: "" },
					descripcion: { estado: null, mensaje: "" },
					precio_optica: { estado: null, mensaje: "" },
					precio_mutual: { estado: null, mensaje: "" },
					precio_venta: { estado: null, mensaje: "" },
					precio_tarjeta: { estado: null, mensaje: "" },
					stock: { estado: null, mensaje: "" },
				},
			};
		},

		methods: {
			/*
			async getVentasOpticas() {
				let ventasOpticasAPI = new APIControler();
				ventasOpticasAPI.apiUrl.pathname = "ventasOpticas/";
				this.data = await ventasOpticasAPI.getData(this.ventasOpticas);
				this.data.forEach((element) => {
					let option = {};
					option.value =
						"http://localhost:8081/ventasOpticas/" +
						element.codigo_seguimiento +
						"/";
					option.text = element.ventasOpticas;
					console.log(option);
					this.options.push(option);
				});
			},
			*/

			// async getLentes() {
			// 	let lenteAPI = new APIControler();
			// 	this.data = await lenteAPI.getData();
			// },
			async putLente() {
				let respuesta = "vacio";
				// try{
				await axios
					.put(
						"http://localhost:8081/lentes/" + this.lente.id_lente + "/",
						this.lente
					)
					.then(function (data) {
						console.log("Data");
						console.log(data);
						swal("Operación Exitosa", " ", "success");
					})
					.catch(function (error) {
						const mje=error.response.status < 500
							? "Los datos no son válidos"
							: "Se ha detectado un problema ";
						swal("¡ERROR!", mje, "error");
						respuesta = error.response.data;
					});
				this.respuesta=respuesta
				this.cargarFeedback()
				this.updateTable()
				//this.resetForm();
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
		beforeMount() {},
	};
</script>

<style></style>
