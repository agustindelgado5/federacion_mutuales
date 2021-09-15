<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Datos </h4>   
    <b-form >
      <b-form-group label="*ID Servicio" label-for="id_servicio" @submit.stop.prevent="handleSubmit">
            <b-form-input
            id="id_servicio"
            v-model="servicio.id_servicio"
            :state="validacion.id_servicio.estado"
            type="number"
            placeholder="Ingrese el ID del servicio"
            invalid-feedback="Complete este campo"
            required
            >
            </b-form-input>
            <b-form-invalid-feedback
                id="id_servicio-live-feedback"
              >{{validacion.id_servicio.mensaje}}
            </b-form-invalid-feedback>
      </b-form-group>

      <b-form-group label="*Nombre del servicio" label-for="nombre">
        <b-form-input
          id="nombre"
          v-model="servicio.nombre"
          type="text"
          placeholder="*Ingrese el nombre del servicio"
          :state="validacion.nombre.estado"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback
                id="nombre-live-feedback"
              >{{validacion.nombre.mensaje}}
            </b-form-invalid-feedback>
      </b-form-group>
      
    </b-form>
    {{ servicio }}
    {{ data }}
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
        id_servicio: {estado:null,mensaje:""},
        nombre: {estado:null,mensaje:""},
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