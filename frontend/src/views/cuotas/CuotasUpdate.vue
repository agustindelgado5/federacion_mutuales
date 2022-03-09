<template>
	<div>
		<h6>Los campos en (*) son obligatorios</h6>
		<h4>Datos</h4>
		<b-form @submit.stop.prevent>
			<!--
			<b-form-group label="*ID">
				<b-form-input
					id="id_cuota"
					:disabled="true"
					v-model="item_cuot.id_cuota"
					type="number"
					:state="validacion.id_cuota.estado"
					placeholder="Ingrese un Numero"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="id_cuota-live-feedback">
					{{ validacion.id_cuota.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>
			-->

			<b-form-group label="*Socio" label-for="numero_socio">
				<!--
				<b-form-select
					id="numero_socio"
					v-model="cuotas.numero_socio"
					type="text"
					placeholder="Ingrese un Numero"
					invalid-feedback="Complete este campo"
					required
					:state="validacion.numero_socio.estado"
					:options="op_socios"
				>
				</b-form-select>
				-->
				<v-autocomplete
					id="numero_socio"
					v-model="cuotas.numero_socio"
					:items="op_socios"
					type="text"
					solo
					filled
				></v-autocomplete>
				<b-form-invalid-feedback id="numero_socio-live-feedback">
					{{ validacion.numero_socio.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<!-- {{ list_familiar }} -->
			<b-form-group label="*Persona que pagó">
				<b-form-input
					id="personapago"
					v-model="item_cuot.personapago"
					type="text"
					placeholder="Ingrese el nombre de la persona que pagó"
					invalid-feedback="Complete este campo"
					:state="validacion.personapago.estado"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="personapago-live-feedback">
					{{ validacion.personapago.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>
			<b-form-group
				label="*Monto"
				label-for="monto"
				@submit.stop.prevent="handleSubmit"
			>
				<b-form-input
					id="monto"
					v-model="item_cuot.monto"
					type="number"
					:state="validacion.monto.estado"
					placeholder="Ingrese un Numero"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="monto-live-feedback">
					{{ validacion.monto.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>
			
			<b-form-group
				title="El mes que corresponde la cuota"
				label="Mes"
				label-for="periodo"
				@submit.stop.prevent="handleSubmit"
			>
				<month-picker-input 
					@change="setPeriodo" 
					:default-month="new Date(item_cuot).getMonth()+1" 
					:lang="'es'">
				</month-picker-input>
			</b-form-group>
			
			<b-form-group label="Pagada" title="Indica si la cuota fue pagada">
				<b-form-checkbox
					v-model="item_cuot.pagado"					
					type="boolean"
					:state="validacion.pagado.estado"
					invalid-feedback="Complete este campo"
					required
					unchecked-value="false"
				>
				</b-form-checkbox>
			</b-form-group>

			<b-form-group 
				v-if="item_cuot.pagado==true"
				label="Fecha de pago"
				label-for="fecharealizacion"
			>
				<b-form-input
					id="fecharealizacion"
					v-model="item_cuot.fecharealizacion"
					type="date"
					:state="validacion.fecharealizacion.estado"
					placeholder="Ingrese una Fecha"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="fecharealizacion-live-feedback">
					{{ validacion.fecharealizacion.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group
				v-if="item_cuot.pagado==true"
				label="*Persona que pagó"
				label-for="personapago"
				@submit.stop.prevent="handleSubmit"
			>
				<b-form-input
					id="personapago"
					v-model="item_cuot.personapago"
					type="text"
					placeholder="Ingrese el nombre de la persona que pagó"
					invalid-feedback="Complete este campo"
					:state="validacion.personapago.estado"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="personapago-live-feedback">
					{{ validacion.personapago.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group v-if="item_cuot.pagado==true" label="*Método de pago" label-for="metodoPago">
				<b-form-select
					id="metodoPago"
					v-model="item_cuot.metodoPago"
					:state="validacion.metodoPago.estado"
					type="text"
					placeholder="Ingrese un método de pago"
					invalid-feedback="Complete este campo"
					required
					:options="op_metodosPago"
				>
				</b-form-select>
				<b-form-invalid-feedback id="metodoPago-live-feedback"
					>{{ validacion.metodoPago.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>
		</b-form>

		<b-button class="mt-2" variant="success" block @click="putCuota()"
			>Modificar</b-button
		>
	</div>
</template>

<script>
	import { APIControler } from "@/store/APIControler";
	import axios from "axios";
	import { MonthPickerInput } from 'vue-month-picker'

	export default {
		components: {
			MonthPickerInput,
  		},
		props: {
			item_cuot: {},
      		updateTable: Function,
		},
		data() {
			return {
				list_socios: {},
				data: {},
				list_familiar: {},
				op_socios: [{ value: null, text: "Elija un socio", disabled: true }],
				options: [{ value: null, text: "Elija un socio", disabled: true }],
				op_metodosPago: [
					{ value: "Mercado pago", text: "Mercado pago" },
					{ value: "Transferencia bancaria", text: "Transferencia bancaria" },
					{ value: "Otro", text: "Otro" },
					{ value: "Cobrador", text: "Cobrador" },
				],
				validacion: {
					id_cuota: { estado: null, mensaje: "" },
					monto: { estado: null, mensaje: "" },
					periodo: { estado: null, mensaje: "" },
					pagado: { estado: null, mensaje: "" },
					numero_socio: { estado: null, mensaje: "" },
					personapago: { estado: null, mensaje: "" },
					fecharealizacion: { estado: null, mensaje: "" },
					metodoPago: { estado: null, mensaje: "" },
				},
			};
		},

		methods: {
			setPeriodo (date) {
				console.log("mostrando date: ", date.from)
				this.item_cuot.periodo = date.from.toLocaleDateString('en-CA')
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
				});
			},
			async putCuota() {
				let respuesta = "vacio";

				await axios
					.put(
						"http://localhost:8081/cuotas/" + this.item_cuot.id_cuota + "/",
						this.item_cuot
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
				if (!respuestaAPI) respuestaAPI = {};
				let valido;
				for (let key in this.validacion) {
					valido = !respuestaAPI.hasOwnProperty(key);
					this.validacion[key].estado = valido;
					if (!valido) this.validacion[key].mensaje = respuestaAPI[key][0];
				}
			},
		},
		beforeMount() {
			this.getSocios();
		},
		/*
  computed: {
      validation() {
        return this.text.length > 0 ? true : false;
      },
    }
  */
	};
</script>

<style></style>
