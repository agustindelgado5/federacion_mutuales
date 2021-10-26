<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Datos </h4>   
    <b-form >

      <b-form-group label="*Nombre del servicio" label-for="nombre">
        <b-form-input
          id="nombre"
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
                id="servicio-live-feedback"
              >{{validacion.servicio.mensaje}}
            </b-form-invalid-feedback>
      </b-form-group>
      
    </b-form>
    <b-button class="mt-2" variant="success" block @click="putServicios()">Modificar</b-button>
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";
import axios from "axios";

export default {
  props: {
    servicio: {},
  },
  data() {
    return {
      servicios: {},
      data: {},
      options: [
        {value: null, text: 'Elija un servicio', disabled: true},
      ],
      validacion:{
        servicio: {estado:null,mensaje:""},
      }
    };
  },
  created: function() {
    this.getServicios();
  },

  methods: {
    async getServicios() {
      let servicioAPI = new APIControler();
      servicioAPI.apiUrl.pathname='servicios/'
      this.data = await servicioAPI.getData(this.servicios);
      this.data.forEach(element => {   
        let option={}
        option.value='http://localhost:8081/servicios/'+ element.id_servicio +'/';
        option.text=element.servicio;
        console.log(option);
        this.options.push(option);
      });
    },

    async putServicios() {
      let respuesta ="vacio"
      await axios.put('http://localhost:8081/servicios/'+this.servicio.id_servicio+ '/', this.servicio)
      .then(function (data){
        swal("Operación Exitosa", " ", "success");
      })
      .catch(function (error) {
        swal("¡ERROR!", "Se ha detectado un problema ", "error");
        respuesta=error.response.data;
      })
      this.cargarFeedback(respuesta)
      console.log("respuesta:");
      console.log(respuesta);
    },

    cargarFeedback(respuestaAPI){
      console.log("respuestaAPI")
      console.log(respuestaAPI)
      let valido;
      for(let key in this.validacion){
        valido=!(respuestaAPI.hasOwnProperty(key))
        this.validacion[key].estado=valido
        console.log(key)

        if (!valido)
          this.validacion[key].mensaje=respuestaAPI[key][0]
      }
    }
  },
};
</script>

<style>
</style>