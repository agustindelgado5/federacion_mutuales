<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Datos </h4>   
    <b-form @submit.stop.prevent>
      <b-form-group label="*ID" label-for="id_medicamento" @submit.stop.prevent="handleSubmit">
        <b-form-input
            id="id_medicamento"
            v-model="medicamentos.id_medicamento"
            type="number"
            :state="validacion.id_medicamento.estado"
            placeholder="Ingrese un Numero"
            invalid-feedback="Complete este campo"
            required
        >
        </b-form-input>
        <b-form-invalid-feedback
          id="id_medicamento-live-feedback"
        >
          {{validacion.id_medicamento.mensaje}}
        </b-form-invalid-feedback>
      </b-form-group>

      <b-form-group label="*Nombre" label-for="nombre" @submit.stop.prevent="handleSubmit">
        <b-form-input
            id="nombre"
            v-model="medicamentos.nombre"
            type="text"
            placeholder="Ingrese el nombre"
            invalid-feedback="Complete este campo"
            :state="validacion.nombre.estado"
            required
        >
        </b-form-input>
        <b-form-invalid-feedback
          id="nombre-live-feedback"
        >
          {{validacion.nombre.mensaje}}
        </b-form-invalid-feedback>
      </b-form-group>
      
      <b-form-group label="*Presentacion" label-for="presentacion" @submit.stop.prevent="handleSubmit">
        <b-form-textarea
          id="presentacion"
          v-model="medicamentos.presentacion"
          type="text"
          placeholder="Describa la presentacion"
          invalid-feedback="Complete este campo"
          :state="validacion.presentacion.estado"
          required
          rows="3"
          max-rows="6"
        >
        </b-form-textarea>
        <b-form-invalid-feedback
          id="presentacion-live-feedback"
        >
          {{validacion.presentacion.mensaje}}
        </b-form-invalid-feedback>
      </b-form-group>
      <b-form-group label="*Laboratorio" label-for="laboratorio" @submit.stop.prevent="handleSubmit">
        <b-form-input
            id="laboratorio"
            v-model="medicamentos.laboratorio"
            type="text"
            :state="validacion.laboratorio.estado"
            placeholder="Ingrese el nombre"
            invalid-feedback="Complete este campo"
            aria-describedby="input-live-help input-live-feedback"
            required
        >
          <b-form-invalid-feedback id="input-live-feedback">
            Debe ingresar al menos 100 caracteres.
          </b-form-invalid-feedback>
        </b-form-input>
        <b-form-invalid-feedback
          id="laboratorio-live-feedback"
        >
          {{validacion.laboratoriomensaje}}
        </b-form-invalid-feedback>
      </b-form-group>
      
      <b-form-group label="*Farmacia" label-for="cod_farmacia" @submit.stop.prevent="handleSubmit">
        <b-form-select
            id="cod_farmacia"
            v-model="medicamentos.cod_farmacia"
            type="text"
            placeholder="Ingrese un Numero"
            invalid-feedback="Complete este campo"
            required
            :state="validacion.cod_farmacia.estado"
            :options="options"
        >
        </b-form-select>
        <b-form-invalid-feedback
          id="cod_farmacia-live-feedback"
        >
          {{validacion.cod_farmacia.mensaje}}
        </b-form-invalid-feedback>
      </b-form-group>
      

      
    </b-form>
     <b-button class="mt-2"  variant="success" block @click="postMedicamento()">Guardar</b-button>
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";


export default {
  data() {
    return {
      medicamentos: {},
      farmacias:{},
      data: {},
      
      options: [
        {value: null, text: 'Elija una farmacia', disabled: true},
      ],

      text: '',
      validacion:{
        id_medicamento: {estado:null,mensaje:""},
        nombre: {estado:null,mensaje:""},
        presentacion: {estado:null,mensaje:""},
        laboratorio: {estado:null,mensaje:""},
        cod_farmacia: {estado:null,mensaje:""},
      },
    };
  },
  
  
  methods: {
    async getFarmacias() {
      let farmaciaAPI = new APIControler();
      farmaciaAPI.apiUrl.pathname='farmacias/'
      this.data = await farmaciaAPI.getData(this.farmacias);
      this.data.forEach(element => {   
        let option={}
        option.value='http://localhost:8081/farmacias/'+ element.cod_farmacia +'/';
        option.text=element.farmacia;
        console.log(option);
        this.options.push(option);
      });
    },
    /*
    async getMedicamento() {
      let medicamentosAPI = new APIControler();
      this.data = await medicamentosAPI.getData();
    },*/

    async postMedicamento() {
      let medicamentosAPI = new APIControler();
      medicamentosAPI.apiUrl.pathname='medicamentos/'
      //this.data = await medicamentosAPI.postData(this.medicamentos);
      let respuesta = await medicamentosAPI.postData(this.medicamentos);
      this.cargarFeedback(respuesta);
      this.resetForm();
    },

    
    async resetForm() {
        
        this.medicamentos.id_medicamento = null;
        this.medicamentos.nombre = "";
        this.medicamentos.presentacion = "";
        this.medicamentos.laboratorio = "";
        this.medicamentos.cod_farmacia = "";

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
  beforeMount(){
    this.getFarmacias();
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