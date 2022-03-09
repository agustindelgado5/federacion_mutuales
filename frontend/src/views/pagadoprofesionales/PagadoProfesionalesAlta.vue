<template>
	<div>
		<h6>Los campos en (*) son obligatorios</h6>
		<h4>Registrar nuevo pago a profesional:</h4>

		<b-form>
			<!-- id_medico -->

			<b-form-group data-app label="*Medico" label-for="id_medico">
				<v-autocomplete
					id="id_medico"
					v-model="pagadoProfesional.id_medico"
					:items="op_profesionales"
					type="text"
					solo
					placeholder="Ingrese el ID del medico"
					invalid-feedback="Complete este campo"
					required
				></v-autocomplete>

				<b-form-invalid-feedback id="id_medico-live-feedback">
					{{ validacion.id_medico.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<!-- total -->
			<b-form-group label="*Total" label-for="total">
				<b-form-input
					id="total"
					v-model="pagadoProfesional.total"
					type="number"
					:state="validacion.total.estado"
					placeholder="Ingrese el total del pago"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="total-live-feedback">
					{{ validacion.total.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<!-- fecha -->
			<b-form-group label="*Fecha" label-for="fecha">
				<b-form-input
					id="fecha"
					v-model="pagadoProfesional.fecha"
					:state="validacion.fecha.estado"
					type="date"
					placeholder="Ingrese una fecha"
					invalid-feedback="Complete este campo"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="fecha-live-feedback">
					{{ validacion.fecha.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<!--modo_pago-->
			<b-form-group label="*Modo De Pago" label-for="modo_pago">
				<b-form-select
					id="modo_pago"
					v-model="pagadoProfesional.modo_pago"
					:state="validacion.modo_pago.estado"
					type="text"
					placeholder="Ingrese la modp de pago"
					invalid-feedback="Complete este campo"
					required
					:options="options1"
				>
				</b-form-select>
				<b-form-invalid-feedback id="modo_pago-live-feedback">
					{{ validacion.modo_pago.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group
				title="El mes que corresponde el pago"
				label="*Mes"
				label-for="periodo"
				@submit.stop.prevent="handleSubmit"
			>
				<month-picker-input
					@change="setPeriodo"
					id="periodo"
					:state="validacion.periodo.estado"
					:default-month="new Date().getMonth() + 1"
					:lang="'es'"
					required
				>
				</month-picker-input>
				<b-form-invalid-feedback id="modo_pago-live-feedback">
					{{ validacion.periodo.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>
		</b-form>
		<b-button
			class="mt-2"
			variant="success"
			block
			@click="postPagadoProfesionales()"
			>Guardar</b-button
		>
	</div>
</template>

<script>
	import { APIControler } from "@/store/APIControler";
	import { mapState, mapActions } from "vuex";
	import { MonthPickerInput } from "vue-month-picker";
	export default {
		components: {
			MonthPickerInput,
		},
		props: {
			updateTable: Function,
		},
		data() {
			return {
				pagadoProfesional: {},
				data: {},
				op_profesionales: [
					{ value: null, text: "Elija un profesional", disabled: true },
				],
				list_profesionales: [],
				validacion: {
					id_medico: { estado: null, mensaje: "" },
					total: { estado: null, mensaje: "" },
					fecha: { estado: null, mensaje: "" },
					modo_pago: { estado: null, mensaje: "" },
					periodo: { estado: null, mensaje: "" },
				},
				respuesta: {},
				options1: [
					{
						value: null,
						text: "Elija un modo de pago",
						selected: true,
					},
					{ value: "Efectivo", text: "1- Efectivo" },
					{ value: "CBU", text: "2- CBU" },
					{ value: "Tarjeta de Debito", text: "3- Tarjeta de Debito" },
					{ value: "Tarjeta de Credito", text: "4- Tarjeta de Credito" },
				],
				meses: [
					{ value: "Enero", text: "01- Enero" },
					{ value: "Febrero", text: "02- Febrero" },
					{ value: "Marzo", text: "03- Marzo" },
					{ value: "Abril", text: "04- Abril" },
					{ value: "Mayo", text: "05- Mayo" },
					{ value: "Junio", text: "06- Junio" },
					{ value: "Julio", text: "07- Julio" },
					{ value: "Agosto", text: "08- Agosto" },
					{ value: "Septiembre", text: "09- Septiembre" },
					{ value: "Octubre", text: "10- Octubre" },
					{ value: "Noviembre", text: "11- Noviembre" },
					{ value: "Diciembre", text: "12- Diciembre" },
				],
			};
		},
		methods: {
			setPeriodo(date) {
				this.pagadoProfesional.periodo = date.from.toLocaleDateString("en-CA");
			},
			async getProfesionales() {
				let profesionalesAPI = new APIControler();
				profesionalesAPI.apiUrl.pathname = "profesionales/";
				this.data = await profesionalesAPI.getData(this.list_profesionales);
				this.data.forEach((element) => {
					let option = {};
					option.value =
						"http://localhost:8081/profesionales/" + element.id_medico + "/";
					option.text =
						element.id_medico +
						"-- " +
						element.apellido +
						", " +
						element.nombre +
						"; Mat: " +
						element.matricula +
						" ; " +
						element.especialidad;
					console.log(option);
					this.op_profesionales.push(option);
				});
			},
			async getPagadoProfesionales() {
				let PagadoProfesionalAPI = new APIControler();
				this.data = await PagadoProfesionalAPI.getData();
			},
			async postPagadoProfesionales() {
				let PagadoProfesionalAPI = new APIControler();
				PagadoProfesionalAPI.apiUrl.pathname = "pagadoprofesionales/";
				this.respuesta = await PagadoProfesionalAPI.postData(
					this.pagadoProfesional
				);
				this.cargarFeedback();
				sessionStorage.removeItem("pagos");
				this.updateTable();
			},

			cargarFeedback() {
				let valido;
				this.respuesta = this.respuesta || {};
				for (let key in this.validacion) {
					valido = !this.respuesta.hasOwnProperty(key);
					this.validacion[key].estado = valido;
					//console.log(key);
					if (!valido) this.validacion[key].mensaje = this.respuesta[key][0];
				}
			},
		},
		beforeMount() {
			this.getProfesionales();
		},
	};
</script>

<style></style>
