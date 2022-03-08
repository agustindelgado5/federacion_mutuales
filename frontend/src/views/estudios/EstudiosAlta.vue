<template>
	<div>
		<h6>Los campos en (*) son obligatorios</h6>
		<h4>Nuevo Estudio:</h4>
		<b-form>
			<b-form-group label="*Tipo" label-for="tipo">
				<b-form-select
					id="tipo"
					v-model="estudio.tipo"
					type="text"
					placeholder="Ingrese un tipo"
					invalid-feedback="Complete este campo"
					:state="validacion.tipo.estado"
					required
					:options="op_tipo"
				>
				</b-form-select>
				<b-form-invalid-feedback id="tipo-live-feedback"
					>{{ validacion.tipo.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group label="Abreviatura" label-for="abreviatura">
				<b-form-input
					id="abreviatura"
					v-model="estudio.abreviatura"
					type="text"
					placeholder="*Ingrese una abreviatura"
					invalid-feedback="Complete este campo"
					:state="validacion.abreviatura.estado"
				>
				</b-form-input>
				<b-form-invalid-feedback id="abreviatura-live-feedback"
					>{{ validacion.abreviatura.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group label="*Descripción" label-for="descripcion">
				<b-form-input
					id="descripcion"
					v-model="estudio.descripcion"
					:state="validacion.descripcion.estado"
					type="text"
					placeholder="*Ingrese una descripcion"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="descripcion-live-feedback"
					>{{ validacion.descripcion.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group label="Denominación" label-for="denominación">
				<b-form-input
					id="denominación"
					v-model="estudio.denominación"
					type="text"
					placeholder="*Ingrese una denominación"
					invalid-feedback="Complete este campo"
					:state="validacion.denominación.estado"
				>
				</b-form-input>
				<b-form-invalid-feedback id="denominación-live-feedback"
					>{{ validacion.denominación.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<!-- Unidad Bioquimica -->
			<b-form-group
				label="U.B."
				label-for="ub"
				v-show="this.estudio.tipo == 'Analisis bioquimico'"
			>
				<b-form-input
					id="ub"
					v-model="estudio.ub"
					:state="validacion.ub.estado"
					type="decimal"
					placeholder="Ingrese la U.B. correspondiente al estudio "
					invalid-feedback="Complete este campo"
				>
				</b-form-input>
				<b-form-invalid-feedback id="ub-live-feedback"
					>{{ validacion.ub.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group label="N.B.U" label-for="nbu">
				<b-form-input
					id="nbu"
					v-model="estudio.nbu"
					type="number"
					placeholder="Ingrese la N.B.U. correspondiente al estudio "
					invalid-feedback="Complete este campo"
					:state="validacion.nbu.estado"
				>
				</b-form-input>
				<b-form-invalid-feedback id="ub-live-feedback"
					>{{ validacion.nbu.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group label="*Proveedor" label-for="proveedor">
				
				<v-autocomplete
					id="proveedor"
					v-model="estudio.id_proveedor"
					:items="option_proveedores"
					type="text"
					solo
					filled
				></v-autocomplete>

				<b-form-invalid-feedback id="descripcion-live-feedback"
					>{{ validacion.id_proveedor.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group label="*Precio al socio" label-for="precio_socio">
				<b-form-input
					id="precio_socio"
					v-model="estudio.precio_socio"
					:state="validacion.precio_socio.estado"
					type="decimal"
					placeholder="Ingrese el precio correspondiente al estudio "
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="ub-live-feedback"
					>{{ validacion.precio_socio.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group
				label="*Precio a la federacion"
				label-for="precio_federacion"
			>
				<b-form-input
					id="precio_federacion"
					v-model="estudio.precio_federacion"
					:state="validacion.precio_federacion.estado"
					type="decimal"
					placeholder="Ingrese el precio correspondiente al estudio "
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="ub-live-feedback"
					>{{ validacion.precio_federacion.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>
		</b-form>
	

		<b-button class="mt-2" variant="success" block @click="postEstudio()"
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
				estudio: {},
				data: {},
				//proveedores : [],

				option_proveedores: [
					{ value: null, text: "Elija un proveedor", disabled: true },
				],

				op_tipo: [
					{ value: null, text: "Elija un tipo", disabled: true },
					{ value: "Oftalmologia", text: "1- Oftalmología" },
					{ value: "Optica", text: "2- Óptica" },
					{ value: "Analisis bioquimico", text: "3- Análisis bioquímico" },
					{ value: "Odontologia", text: "4- Odontología" },
					{ value: "Diag. Imagenes", text: "5- Diag. Imágenes" },
				],

				validacion: {
					id_proveedor: { estado: null, mensaje: "" },
					tipo: { estado: null, mensaje: "" },
					//cod_estudio: { estado: null, mensaje: "" },
					nbu: { estado: null, mensaje: "" },
					precio_socio: { estado: null, mensaje: "" },
					precio_federacion: { estado: null, mensaje: "" },
					abreviatura: { estado: null, mensaje: "" },
					ub: { estado: null, mensaje: "" },
					descripcion: { estado: null, mensaje: "" },
					denominación: { estado: null, mensaje: "" },
				},

				respuesta: null,
			};
		},

		methods: {
			/*
			async getEstudios() {
				let estudioAPI = new APIControler();
				this.data = await estudioAPI.getData();
			},
			*/

			async getProveedor() {
				let _data = {};
				let proveedorAPI = new APIControler();
				proveedorAPI.apiUrl.pathname = "proveedor_estudios/";
				let proveedores = await proveedorAPI.getData(_data);
				console.log("PROVEEDORES: ", proveedores);

				proveedores.forEach((element) => {
					let option = {};
					option.value =
						"http://localhost:8081/proveedor_estudios/" +
						element.id_proveedor +
						"/";
					option.text =
						element.id_proveedor +
						" - " +
						element.nombre +
						" - " +
						element.direccion +
						" - " +
						element.localidad +
						" - " +
						element.provincia;
					this.option_proveedores.push(option);
				});
			},
			async postEstudio() {
				let estudioAPI = new APIControler();
				estudioAPI.apiUrl.pathname = "estudios/";
				this.UB_Seleccion();
				this.respuesta = await estudioAPI.postData(this.estudio);
				console.log("respuesta: ", this.respuesta);
				this.cargarFeedback();
				this.updateTable();
			},

			UB_Seleccion() {
				if (this.estudio.tipo != "Analisis bioquimico") {
					this.estudio.ub = 0;
				}
			},

			cargarFeedback() {
				let valido;
				if (!this.respuesta) this.respuesta = {};
				for (let key in this.validacion) {
					valido = !this.respuesta.hasOwnProperty(key);
					this.validacion[key].estado = valido;
					console.log(key);
					if (!valido) this.validacion[key].mensaje = this.respuesta[key][0];
				}
			},
		},
		beforeMount() {
			//this.UB_Seleccion();
			this.getProveedor();
		},
	};
</script>

<style></style>
