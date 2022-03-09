<template>
	<div>
		<h6>Los campos en (*) son obligatorios</h6>
		<h4>Nueva Cirugia:</h4>

		<!-- CAMPOS REQUERIDOS -->
		<!-- codigo_intervencion -->
		<!-- descrpcion-->
		<!--nivel-->
		<!--numero de ayudantes-->
		<!--honorarios cirujano-->
		<!--honorarios ayudante-->
		<!-- observacion -->

		<!------------------------------------------------------------------------------------------->
		<b-form>
			<!-- numero_socio-->
			<b-form-group label="*Socio" label-for="numero_socio">
				<!--
				<b-form-select
					id="numero_socio"
					v-model="cirugia.numero_socio"
					type="text"
					placeholder="Ingrese un Numero"
					invalid-feedback="Complete este campo"
					:state="validacion.numero_socio.estado"
					required
					:options="op_socios"
				>
				</b-form-select>
				-->
				<v-autocomplete
					id="numero_socio"
					v-model="cirugia.numero_socio"
					:items="op_socios"
					type="text"
					solo
					filled
				></v-autocomplete>
				<b-form-invalid-feedback id="numero_socio-live-feedback"
					>{{ validacion.numero_socio.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>
			<!--codigo_institucion-->
			<b-form-group label="*Codigo de instituto" label-for="codigo_institucion">
				<!--
				<b-form-select
					id="codigo_institucion"
					v-model="cirugia.codigo_institucion"
					type="text"
					placeholder="Ingrese un Numero"
					invalid-feedback="Complete este campo"
					:state="validacion.codigo_institucion.estado"
					required
					:options="op_institucion"
				>
				</b-form-select>
				-->
				<v-autocomplete
					id="codigo_institucion"
					v-model="cirugia.codigo_institucion"
					:items="op_institucion"
					type="text"
					solo
					filled
				></v-autocomplete>
				<b-form-invalid-feedback id="codigo_institucion-live-feedback"
					>{{ validacion.codigo_institucion.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group label="*Descripcion" label-for="descripcion">
				<b-form-input
					id="descripcion"
					v-model="cirugia.descripcion"
					:state="validacion.descripcion.estado"
					type="text"
					placeholder="Ingrese una abreviatura"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="descripcion-live-feedback"
					>{{ validacion.descripcion.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group label="*Nivel" label-for="nivel">
				<b-form-input
					id="nivel"
					v-model="cirugia.nivel"
					:state="validacion.nivel.estado"
					type="number"
					placeholder="Ingrese una observacion"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="nivel-live-feedback"
					>{{ validacion.nivel.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group label="Numero de ayudantes" label-for="numero_ayudantes">
				<b-form-input
					id="numero_ayudantes"
					v-model="cirugia.numero_ayudantes"
					:state="validacion.numero_ayudantes.estado"
					type="number"
					placeholder="Ingrese el numero de ayudantes"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="numero_ayudantes-live-feedback"
					>{{ validacion.numero_ayudantes.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group label="Honorarios Cirujanos" label-for="honorario_cirujano">
				<b-form-input
					id="honorario_cirujano"
					v-model="cirugia.honorario_cirujano"
					:state="validacion.honorario_cirujano.estado"
					type="text"
					placeholder="Ingrese el honorario del cirujano "
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="honorario-live-feedback"
					>{{ validacion.honorario_cirujano.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group label="Honorarios ayudantes" label-for="honorario_ayudante">
				<b-form-input
					id="honorario_ayudante"
					v-model="cirugia.honorario_ayudante"
					:state="validacion.honorario_ayudante.estado"
					type="text"
					placeholder="Ingrese el honorario del ayudante"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="honorario_ayudante-live-feedback"
					>{{ validacion.honorario_ayudante.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group label="*Observacion" label-for="observacion">
				<b-form-input
					id="observacion"
					v-model="cirugia.observacion"
					:state="validacion.observacion.estado"
					type="text"
					placeholder="Ingrese una observacion"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="observacion-live-feedback"
					>{{ validacion.observacion.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>
		</b-form>
		<b-button class="mt-2" variant="success" block @click="putCirugia()"
			>Guardar</b-button
		>
	</div>
</template>

<script>
	import axios from "axios";
	import { APIControler } from "@/store/APIControler";

	export default {
		props: {
			cirugia: {},
			updateTable: Function,
		},
		data() {
			return {
				data: {},

				op_socios: [{ value: null, text: "Elija un socio", disabled: true }],
				op_institucion: [
					{ value: null, text: "Elija una Institución", disabled: true },
				],

				validacion: {
					//codigo_intervencion: { estado: null, mensaje: "" },
					codigo_institucion: { estado: null, mensaje: "" },
					numero_socio: { estado: null, mensaje: "" },
					descripcion: { estado: null, mensaje: "" },
					nivel: { estado: null, mensaje: "" },
					numero_ayudantes: { estado: null, mensaje: "" },
					honorario_cirujano: { estado: null, mensaje: "" },
					honorario_ayudante: { estado: null, mensaje: "" },
					observacion: { estado: null, mensaje: "" },
				},

				respuesta: null,
			};
		},

		methods: {
			getForeingKeys() {
				this.cirugia.codigo_institucion =
					"http://localhost:8081/institutos/" +
					this.cirugia.institucion.split("-")[0] +
					"/";
				this.cirugia.numero_socio =
					"http://localhost:8081/socios/" +
					this.cirugia.socio.split("-")[0] +
					"/";
			},

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
					if (element.numero_socio == this.cirugia.numero_socio) {
						this.list_socios.push(option);
					}
				});
			},
			async getInstitucion() {
				let institutoAPI = new APIControler();
				institutoAPI.apiUrl.pathname = "institutos/";
				this.data = await institutoAPI.getData(this.list_institutos);
				this.data.forEach((element) => {
					let option = {};
					option.value =
						"http://localhost:8081/institutos/" +
						element.codigo_institucion +
						"/";
					option.text = element.codigo_institucion + "-- " + element.nombre;
					console.log(option);
					this.op_institucion.push(option);
				});
			},
			async putCirugia() {
				let respuesta = "vacio";
				// try{
				await axios
					.put(
						"http://localhost:8081/cirugias/" +
							this.cirugia.codigo_intervencion +
							"/",
						this.cirugia
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
			},

			cargarFeedback(respuestaAPI) {
				let valido;
				for (let key in this.validacion) {
					valido = !respuestaAPI.hasOwnProperty(key);
					this.validacion[key].estado = valido;
					if (!valido) this.validacion[key].mensaje = respuestaAPI[key][0];
				}
			},
		},
		beforeMount() {
			this.getForeingKeys();
			this.getSocios();
			this.getInstitucion();
		},
	};
</script>

<style></style>
