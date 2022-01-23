<template>
	<div>
		<h6>Los campos en (*) son obligatorios</h6>

		<b-form>
			<b-form-group label="*Codigo de instituto" label-for="codigo_institucion">
				<b-form-input
					id="codigo_institucion"
					v-model="instituto.codigo_institucion"
					type="text"
					placeholder="Ingrese el código"
					invalid-feedback="Complete este campo"
					required
					:disabled="true"
				>
				</b-form-input>
			</b-form-group>

			<b-form-group label="*Nombre" label-for="nombre">
				<b-form-input
					id="nombre"
					v-model="instituto.nombre"
					:state="validacion.nombre.estado"
					type="text"
					placeholder="Ingrese un Numero"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="nombre-live-feedback"
					>{{ validacion.nombre.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group label="*CUIT" label-for="cuit">
				<b-form-input
					id="cuit"
					v-model="instituto.cuit"
					:state="validacion.cuit.estado"
					type="text"
					placeholder="Ingrese un Numero"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="cuit-live-feedback"
					>{{ validacion.cuit.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group label="*Direccion" label-for="direccion">
				<b-form-input
					id="direccion"
					v-model="instituto.direccion"
					:state="validacion.direccion.estado"
					type="text"
					placeholder="Ingrese un Numero"
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
					v-model="instituto.localidad"
					:state="validacion.localidad.estado"
					type="text"
					placeholder="Ingrese un Numero"
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
					v-model="instituto.provincia"
					:state="validacion.provincia.estado"
					type="text"
					placeholder="Ingrese una provincia"
					invalid-feedback="Complete este campo"
					required
					:options="options_provincia"
				>
				</b-form-select>
				<b-form-invalid-feedback id="provincia-live-feedback"
					>{{ validacion.provincia.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group label="*Telefono" label-for="telefono">
				<b-form-input
					id="telefono"
					v-model="instituto.telefono"
					:state="validacion.telefono.estado"
					type="text"
					placeholder="Ingrese un Numero"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="telefono-live-feedback"
					>{{ validacion.telefono.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group label="*Horarios" label-for="horarios">
				<b-form-textarea
					id="horarios"
					v-model="instituto.horarios"
					:state="validacion.horarios.estado"
					type="text"
					placeholder="Ingrese un Numero"
					invalid-feedback="Complete este campo"
					required
					rows="3"
					max-rows="6"
				></b-form-textarea>
				<b-form-invalid-feedback id="horarios-live-feedback"
					>{{ validacion.horarios.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group label="*Responsable" label-for="responsable">
				<b-form-input
					id="responsable"
					v-model="instituto.responsable"
					:state="validacion.responsable.estado"
					type="text"
					placeholder="Ingrese un Numero"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="responsable-live-feedback"
					>{{ validacion.telefono.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group
				label="*Telefono del responsable"
				label-for="telefono_responsable"
			>
				<b-form-input
					id="telefono_responsable"
					v-model="instituto.telefono_responsable"
					:state="validacion.telefono_responsable.estado"
					type="text"
					placeholder="Ingrese un Numero"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="telefono_responsable-live-feedback"
					>{{ validacion.telefono_responsable.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>
		</b-form>
		<b-button class="mt-2" variant="success" block @click="putInstituto()"
			>Guardar</b-button
		>
	</div>
</template>

<script>
	import { APIControler } from "@/store/APIControler";
	import axios from "axios";

	export default {
		props: {
			instituto: {},
			updateTable: Function,
		},
		data() {
			return {
				//list_profesionales: {},
				//instituto: {},
				data: {},
				options_provincia: [
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
				validacion: {
					//id_medico: { estado: null, mensaje: "" },
					//codigo_institucion: { estado: null, mensaje: "" },
					nombre: { estado: null, mensaje: "" },
					cuit: { estado: null, mensaje: "" },
					direccion: { estado: null, mensaje: "" },
					localidad: { estado: null, mensaje: "" },
					provincia: { estado: null, mensaje: "" },

					telefono: { estado: null, mensaje: "" },
					horarios: { estado: null, mensaje: "" },

					responsable: { estado: null, mensaje: "" },
					telefono_responsable: { estado: null, mensaje: "" },
				},

				respuesta: null,
			};
		},

		methods: {
			/*
			async getProfesionales() {
				let profesionalAPI = new APIControler();
				profesionalAPI.apiUrl.pathname = "profesionales/";
				this.data = await profesionalAPI.getData(this.list_profesionales);
				this.data.forEach((element) => {
					let option = {};
					option.value =
						"http://localhost:8081/profesionales/" + element.id_medico + "/";
					option.text =
						element.id_medico +
						"-- " +
						element.apellido +
						", " +
						element.nombre;
					console.log(option);
					this.op_socios.push(option);
				});
			},
			*/

			async getInstitutos() {
				let institutoAPI = new APIControler();
				this.data = await institutoAPI.getData();
			},
			async putInstituto() {
				let respuesta = "vacio";
				// try{
				await axios
					.put(
						"http://localhost:8081/institutos/" +
							this.instituto.codigo_institucion +
							"/",
						this.instituto
					)
					.then(function (data) {
						swal("Operación Exitosa", " ", "success");
					})
					.catch(function (error) {
						swal("¡ERROR!", "Se ha detectado un problema ", "error");
						respuesta = error.response.data;
					});
				this.cargarFeedback(respuesta);
				console.log("respuesta: ", respuesta);
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
			//this.getProfesionales();
		},
	};
</script>

<style></style>
