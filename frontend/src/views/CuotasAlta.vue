<template>
    <div>
        <h6>Los campos en (*) son obligatorios</h6>
        <h4>Datos </h4>
        <b-form @submit.stop.prevent>
            <b-form-group label="*ID" label-for="id_cuota" @submit.stop.prevent="handleSubmit">
                <b-form-input id="id_cuota"
                              v-model="cuotas.id_cuota"
                              type="number"
                              :state="validacion.id_cuota.estado"
                              placeholder="Ingrese un Numero"
                              invalid-feedback="Complete este campo"
                              required>
                </b-form-input>
                <b-form-invalid-feedback id="id_cuota-live-feedback">
                    {{validacion.id_cuota.mensaje}}
                </b-form-invalid-feedback>
            </b-form-group>

            <b-form-group label="*Socio" label-for="numero_socio">
                <b-form-select id="numero_socio"
                               v-model="cuotas.numero_socio"
                               type="text"
                               placeholder="Ingrese un Numero"
                               invalid-feedback="Complete este campo"
                               required
                               :state="validacion.numero_socio.estado"
                               :options="op_socios">
                </b-form-select>
                <b-form-invalid-feedback id="numero_socio-live-feedback">
                    {{validacion.numero_socio.mensaje}}
                </b-form-invalid-feedback>
            </b-form-group>

            {{ list_familiar }}
            <b-form-group label="*Personapago" label-for="personapago" @submit.stop.prevent="handleSubmit">
                <b-form-input id="personapago"
                              v-model="cuotas.personapago"
                              type="text"
                              placeholder="Ingrese el nombre de la persona que pago"
                              invalid-feedback="Complete este campo"
                              :state="validacion.personapago.estado"
                              required>
                </b-form-input>
                <b-form-invalid-feedback id="personapago-live-feedback">
                    {{validacion.personapago.mensaje}}
                </b-form-invalid-feedback>
            </b-form-group>
            <b-form-group label="*Monto" label-for="monto" @submit.stop.prevent="handleSubmit">
                <b-form-input id="monto"
                                v-model="cuotas.monto"
                                type="number"
                                :state="validacion.monto.estado"
                                placeholder="Ingrese un Numero"
                                invalid-feedback="Complete este campo"
                                required>
                </b-form-input>
                <b-form-invalid-feedback id="monto-live-feedback">
                    {{validacion.monto.mensaje}}
                </b-form-invalid-feedback>
            </b-form-group>
            <b-form-group label="*Fecha Realizacion" label-for="fecharealizacion" @submit.stop.prevent="handleSubmit">
                <b-form-input id="fecharealizacion"
                                v-model="cuotas.fecharealizacion"
                                type="date"
                                :state="validacion.fecharealizacion.estado"
                                placeholder="Ingrese una Fecha"
                                invalid-feedback="Complete este campo"
                                required>
                </b-form-input>
                <b-form-invalid-feedback id="fecharealizacion-live-feedback">
                    {{validacion.fecharealizacion.mensaje}}
                </b-form-invalid-feedback>
            </b-form-group>
            </b-form>
        </b-form>
        <b-button class="mt-2" variant="success" block @click="postCuota()">Guardar</b-button>
    </div>
</template>

<script>
import { APIControler } from "../store/APIControler";


export default {
  data() {
    return {
      list_socios: {},
      cuotas: {},
      data: {},
      list_familiar: {},
      op_socios: [{ value: null, text: "Elija un socio", disabled: true }],
      options: [
        {value: null, text: 'Elija un socio', disabled: true},
      ],

      text: '',
      validacion:{
        id_cuota: {estado:null,mensaje:""},
        personapago: {estado:null,mensaje:""},
        monto: {estado:null,mensaje:""},
        numero_socio: { estado: null, mensaje: "" },
        fecharealizacion: {estado: null, mensaje:""},
      },
    };
  },


methods: {
    async getPaciente() {
        let familiarAPI = new APIControler();
        familiarAPI.apiUrl.pathname = "familiar/";
        this.data = await familiarAPI.getData(this.list_familiar);
        // this.list_pacientes=this.list_pacientes.slice(0,1)
        let option_titular = {};
        // option_titular.value='http://localhost:8081/socios/'+ this.orden.numero_socio +'/';
        option_titular.value = this.orden.numero_socio;
        option_titular.text = "Titular";
        // option_titular.text= socios.dni +' -- '+ socios.apellido +', '+ socios.nombre ;
        this.list_familiar.push(option_titular);
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
    async postCuota() {
      let cuotasAPI = new APIControler();
      cuotasAPI.apiUrl.pathname='cuotas/'
      let respuesta = await cuotasAPI.postData(this.cuotas);
      this.cargarFeedback(respuesta);
      this.resetForm();
    },


    async resetForm() {

        this.cuotas.id_cuota = null;
        this.cuotas.personapago = "";
        this.cuotas.monto = null;
        this.cuotas.numero_socio = null;

    },


    cargarFeedback(respuestaAPI){
      for(let key in this.validacion){
        this.validacion[key].estado=true
      }
      for(let key in respuestaAPI){
        this.validacion[key].estado=false
        this.validacion[key].mensaje=respuestaAPI[key][0]
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

<style>
</style>