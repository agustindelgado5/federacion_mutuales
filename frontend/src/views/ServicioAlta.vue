<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Datos </h4>   
    <b-form @submit.prevent="">
      <b-form-group label="*Nombre del servicio" label-for="nombre">
        <b-form-input
          id="servicio"
          v-model="servicio.servicio"
          type="text"
          placeholder="*Ingrese el nombre del servicio"
          :state="validacion.servicio.estado"
          invalid-feedback="Complete este campo"
          required
          @keydown.enter.prevent
        >
        </b-form-input>
        <b-form-invalid-feedback
                id="nombre-live-feedback"
              >{{validacion.servicio.mensaje}}
        </b-form-invalid-feedback>
      </b-form-group>
      
    </b-form>
    <b-button class="mt-2" variant="success" block @click.prevent="postServicios()">Guardar</b-button>
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";

export default {
  data() {
    return {
      servicio: {},
      data: {},
      validacion:{
        servicio: {estado:null,mensaje:""},
      }
    };
  },
  methods: {
    async getServicios() {
      let servicioAPI = new APIControler();
      this.data = await servicioAPI.getData();
    },
    async postServicios() {
      let servicioAPI = new APIControler();
      console.log(servicioAPI.apiUrl)
      servicioAPI.apiUrl.pathname='servicios/';
      let respuesta = await servicioAPI.postData(this.servicio); 
      this.cargarFeedback(respuesta)
    },

    cargarFeedback(respuestaAPI){
      for(let key in this.validacion){
        this.validacion[key].estado=true
      }
      for(let key in respuestaAPI){
        this.validacion[key].estado=false
        this.validacion[key].mensaje=respuestaAPI[key][0]
        
      }
    }
  },
};
</script>

<style>
</style>