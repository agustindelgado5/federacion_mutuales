<template>
	<div>
		<h6>Los campos en (*) son obligatorios</h6>

		<b-form >
			
			<b-form-group label="*Nombre" label-for="nombre">
				<b-form-input
					id="nombre"
					v-model="planes.nombre"
					type="text"
					placeholder="Ingrese el nombre del plan"
					invalid-feedback="Complete este campo"
					:state="validacion.nombre.estado"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="nombre-live-feedback">
					{{ validacion.nombre.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

			<b-form-group label="*Precio" label-for="precio">
				<b-form-input
					id="precio"
					v-model="planes.precio"
					type="number"
					placeholder="Ingrese un el precio del plan"
					invalid-feedback="Complete este campo"
					:state="validacion.precio.estado"
					required
				>
				</b-form-input>
				<b-form-invalid-feedback id="precio-live-feedback">
					{{ validacion.precio.mensaje }}
				</b-form-invalid-feedback>
			</b-form-group>

            <!----------    Beneficios         -------------->
            <b-button
			class="my-3"
			variant="primary"
			@click="sumarBeneficios()"
			style="color: white"
			>¿Agregar beneficio?</b-button
		>
		<div v-show="btn_beneficio" v-for="(item, index) in planes.beneficios" :key="index">
			<b-form>
				<div class="d-flex  justify-content-between">

                    <h4>Beneficio: {{ index + 1 }}</h4>
                    <b-button
                        variant="danger"
                        @click="eliminarBeneficio(index)"
                        style="color: white"
                        >
                        <v-icon style="color: white"> mdi-delete </v-icon>
                        </b-button
                    >
                </div>
                <b-form-group
                    label="*Servicio"
                    label-for="servicio"
                    @submit.stop.prevent="handleSubmit"
                >
                    <b-form-select
                        id="servicio"
                        :state="validacion.beneficios[index].servicio.estado"
                        v-model="item.servicio"
                        type="text"
                        placeholder="Ingrese un Numero"
                        invalid-feedback="Complete este campo"
                        required
                        :options="op_servicios"
                    >
                    </b-form-select>
                    <b-form-invalid-feedback id="servicio-live-feedback"
                        >{{ validacion.beneficios[index].servicio.mensaje }}
                    </b-form-invalid-feedback>
                </b-form-group>
                <b-form-group
                    label="*Tipo"
                    label-for="tipo"
                    @submit.stop.prevent="handleSubmit"
                >
                    <b-form-select
                        id="tipo"
                        :state="validacion.beneficios[index].tipo.estado"
                        v-model="item.tipo"
                        type="text"
                        placeholder="Ingrese un Numero"
                        invalid-feedback="Complete este campo"
                        required
                        :options="op_tipos"
                    >
                    </b-form-select>
                    <b-form-invalid-feedback id="tipo-live-feedback"
                        >{{ validacion.beneficios[index].tipo.mensaje }}
                    </b-form-invalid-feedback>
                </b-form-group>
                <b-form-group label="*Cantidad" label-for="cantidad">
					<b-form-input
						id="cantidad"
						:state="validacion.beneficios[index].cantidad.estado"
						v-model="item.cantidad"
						type="text"
						placeholder="*Ingrese la cantidad"
						invalid-feedback="Complete este campo"
						required
					>
					</b-form-input>
					<b-form-invalid-feedback id="cantidad-live-feedback"
						>{{ validacion.beneficios[index].cantidad.mensaje }}
					</b-form-invalid-feedback>
				</b-form-group>
		    </b-form>
	    </div>
        </b-form>

		<b-button class="mt-2" variant="success" block @click="postPlan()"
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
				planes: {beneficios:[]},
				data: {},
				list_beneficio: {},
				text: "",
                op_servicios:[],
                op_tipos:[{value:1,text:"1-Descuento Porcentual"},
                          {value:2,text:"2-Descuento Fijo"},
                          {value:3,text:"3-Limite"}],
				validacion: {
					nombre: { estado: null, mensaje: "" },
					precio: { estado: null, mensaje: "" },
					beneficios: [],
				},
			};
		},

		methods: {
			
			async postPlan() {
				let planesAPI = new APIControler();
				planesAPI.apiUrl.pathname = "planes/";
				let respuesta = await planesAPI.postData(this.planes);
				this.cargarFeedback(respuesta);
				this.updateTable();
			},

			async resetForm() {
				this.planes.id_plan = null;
				this.planes.personapago = "";
				this.planes.monto = null;
				this.planes.numero_socio = null;
			},
            //Obtengo los servicios
			async getServicios() {
				let serviciosAPI = new APIControler();
				serviciosAPI.apiUrl.pathname = "servicios/";
				this.data = await serviciosAPI.getData();
                let option
				this.data.forEach((element) => {
					option = {};
					option.value = 
						"http://localhost:8081/servicios/" + element.id_servicio + "/";
					option.text = element.servicio;
					console.log(option);
					this.op_servicios.push(option);
				});
			},
            async sumarBeneficios() {
				this.btn_beneficio = true;
				// this.resetFormAdh();
				// this.cantidad=this.cantidad +1;
				this.planes.beneficios.push({
					cantidad: 0,
					tipo: '1',
					servicio: null,
				});
                this.validacion.beneficios.push({
					cantidad: { estado: null, mensaje: "" },
					tipo: { estado: null, mensaje: "" },
					servicio: { estado: null, mensaje: "" },
				});
            },
            async eliminarBeneficio(index) {
                this.planes.beneficios.splice(index,1)
                this.validacion.beneficios.splice(index,1)
            },
			cargarFeedback(respuesta) {
				let valido;
				if (!respuesta) respuesta = {};
				for (let key in this.validacion) {
					valido = !respuesta.hasOwnProperty(key);
					this.validacion[key].estado = valido;
					if (!valido) this.validacion[key].mensaje = respuesta[key][0];
				}
                this.cargarFeedbackBeneficios(respuesta)
			},
            cargarFeedbackBeneficios(respuesta) {
				let valido;
                let ok=false
                if (!respuesta.beneficios) ok=true;
                this.validacion.beneficios.forEach((b,index )=> {
                    for (let key in b) {
                        valido = ok || !respuesta.beneficios[index].hasOwnProperty(key);
                        b[key].estado = valido;
                        console.log(key);
	    				if (!valido) b[key].mensaje = respuesta.beneficios[index][key][0];
                    }
                });
				
			},
		},
		beforeMount() {
            this.getServicios()
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
