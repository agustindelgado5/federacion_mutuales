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
						
						<b-form-group label="*Material del cristal" label-for="material">
							<b-form-input
								id="material"
								v-model="cristal.material"
								:state="validacion.material.estado"
								type="text"
								placeholder="*Ingrese un diametro"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="material-live-feedback"
								>{{ validacion.material.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="*Esfera" label-for="esfera">
							<b-form-input
								id="esfera"
								v-model="cristal.esfera"
								:state="validacion.esfera.estado"
								type="number"
								placeholder="*Ingrese un valor"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="esfera-live-feedback"
								>{{ validacion.esfera.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="*Cilindro" label-for="cilindro">
							<b-form-input
								id="cilindro"
								v-model="cristal.cilindro"
								:state="validacion.cilindro.estado"
								type="number"
								placeholder="*Ingrese un valor"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="cilindro-live-feedback"
								>{{ validacion.cilindro.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
						<b-form-group label="Eje" label-for="eje">
							<b-form-input
								id="eje"
								v-model="cristal.eje"
								:state="validacion.eje.estado"
								type="text"
								placeholder="*Ingrese un valor"
								invalid-feedback="Complete este campo"
								
							>
							</b-form-input>
							<b-form-invalid-feedback id="eje-live-feedback"
								>{{ validacion.eje.mensaje }}
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
						
						<b-form-group label="Precio Laboratorio" label-for="precio_laboratorio">
							<b-form-input
								id="precio_laboratorio"
								v-model="cristal.precio_laboratorio"
								:state="validacion.precio_laboratorio.estado"
								type="number"
								placeholder="*Ingrese el precio de optica"
								invalid-feedback="Complete este campo"
								
							>
							</b-form-input>
							<b-form-invalid-feedback id="precio_laboratorio-live-feedback"
								>{{ validacion.precio_laboratorio.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="Precio Optica" label-for="precio_optica">
							<b-form-input
								id="precio_optica"
								v-model="cristal.precio_optica"
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
								v-model="cristal.precio_mutual"
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
								v-model="cristal.precio_venta"
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
								v-model="cristal.precio_tarjeta"
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

						<b-form-group label="*Stock" label-for="stock">
							<b-form-input
								id="stock"
								v-model="cristal.stock"
								:state="validacion.stock.estado"
								type="number"
								placeholder="*Ingrese el stock"
								invalid-feedback="Complete este campo"
								required
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
		<b-button class="mt-2" variant="success" block @click="postCristal()"
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
				cristal: {},
				ventasOpticas: {},
				data: {},

				options: [{ value: null, text: "Elija una venta", disabled: true }],

				text: "",

				validacion: {
					id_cristal: { estado: null, mensaje: "" },
					material: { estado: null, mensaje: "" },
					esfera: { estado: null, mensaje: "" },
					cilindro: { estado: null, mensaje: "" },
					eje: { estado: null, mensaje: "" },
					precio_laboratorio: { estado: null, mensaje: "" },
					precio_optica: { estado: null, mensaje: "" },
					precio_mutual: { estado: null, mensaje: "" },
					precio_venta: { estado: null, mensaje: "" },
					precio_tarjeta: { estado: null, mensaje: "" },
					stock: { estado: null, mensaje: "" },
				},

				respuesta: null,
			};
		},

		methods: {
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

			async getCristales() {
				let cristalAPI = new APIControler();
				this.data = await cristalAPI.getData();
			},
			async postCristal() {
				let cristalAPI = new APIControler();
				cristalAPI.apiUrl.pathname = "cristales/";
				this.respuesta = await cristalAPI.postData(this.cristal);
				this.cargarFeedback();
				this.updateTable();
			},

			cargarFeedback() {
				let valido;
				this.respuesta=this.respuesta || {}
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
