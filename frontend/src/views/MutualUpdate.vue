<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Registrar nueva Mutual:</h4>

    <!-- CAMPOS REQUERIDOS -->
    <!-- nombre -->
    <!-- sucursal -->
    <!-- id_servicio -->

    <!------------------------------------------------------------------------------------------->

    <!-- nombre -->
    <b-form>
      <b-form-group label="*Nombre de la mutual" label-for="nombre">
        <b-form-input
          id="nombre"
          v-model="mutuales.nombre"
          type="text"
          placeholder="*Ingrese el Nombre"
          invalid-feedback="Complete este campo"
          required
          :state="validacion.nombre.estado"
        >
        </b-form-input>
        <b-form-invalid-feedback id="nombre-live-feedback"
          >{{ validacion.nombre.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>

      <!-- sucursal -->
      <b-form-group label="*Sucursal" label-for="sucursal">
        <b-form-select
          id="sucursal"
          v-model="mutuales.sucursal"
          type="text"
          placeholder="Ingrese una sucursal"
          invalid-feedback="Complete este campo"
          :state="validacion.sucursal.estado"
          :options="options"
          required
        >
        </b-form-select>
        <b-form-invalid-feedback id="sucursal-live-feedback"
          >{{ validacion.sucursal.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>

      <!-- id_servicio -->
      <b-form-group label="*Servicio" label-for="servicio">
        <b-form-select
          id="servicio"
          v-model="mutuales.id_servicio"
          type="text"
          placeholder="Ingrese un Numero"
          invalid-feedback="Complete este campo"
          :state="validacion.id_servicio.estado"
          required
          :options="op_servicios"
        >
        </b-form-select>
        <b-form-invalid-feedback id="numero_servicio-live-feedback"
          >{{ validacion.id_servicio.mensaje }}
        </b-form-invalid-feedback>

      </b-form-group>
    </b-form>

    <b-button class="mt-2" variant="success" block @click="putMutual()">Modificar</b-button
    >
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";
import axios from "axios";

export default {
  props: {
    mutual: {},
  },
  data() {
    return {
      mutuales: {},
      data: {},
      list_servicios: {},
      op_servicios: [
        { value: null, text: "Elija un servicio", disabled: true },
      ],
      respuesta: null,
      options: [
        { value: null, text: "Elija un departamento" },
        { value: "Burruyacú", text: "1- Burruyacú" },
        { value: "Capital", text: "2- Capital" },
        { value: "Chicligasta", text: "3- Chicligasta" },
        { value: "Cruz Alta", text: "4- Cruz Alta" },
        { value: "Famaillá", text: "5- Famaillá" },
        { value: "Graneros", text: "6- Graneros" },
        { value: "Juan Bautista Alberdi", text: "7- Juan Bautista Alberdi" },
        { value: "La Cocha", text: "8- La Cocha" },
        { value: "Leales", text: "9- Leales" },
        { value: "Lules", text: "10- Lules" },
        { value: "Monteros", text: "11- Monteros" },
        { value: "Río Chico", text: "12- Río Chico" },
        { value: "Simoca", text: "13- Simoca" },
        { value: "Tafí del Valle", text: "14- Tafí del Valle" },
        { value: "Tafí Viejo", text: "15- Tafí Viejo" },
        { value: "Trancas", text: "16- Trancas" },
        { value: "Yerba Buena", text: "17- Yerba Buena" },
      ],
      validacion: {
        nombre: { estado: null, mensaje: "" },
        sucursal: { estado: null, mensaje: "" },
        id_servicio: { estado: null, mensaje: "" },
      },
    };
  },
  created: function() {
    this.getMutual();
  },

  methods: {
    async getMutual() {
      let MutualAPI = new APIControler();
      MutualAPI.apiUrl.pathname='mutuales/'
      this.data = await mutualAPI.getData(this.mutuales);
      this.data.forEach(element => {   
        let option={}
        option.value='http://localhost:8081/mutuales/'+ element.id_mutual +'/';
        option.text=element.mutual;
        console.log(option);
        this.options.push(option);
      });
    },


    async getServicios() {
      let serviciosAPI = new APIControler();
      serviciosAPI.apiUrl.pathname = "servicios/";
      this.data = await serviciosAPI.getData(this.list_servicios);
      this.data.forEach((element) => {
        let option = {};
        option.value =
          "http://localhost:8081/servicios/" + element.id_servicio + "/";
        option.text = element.id_servicio + "-- " + element.servicio;
        console.log(option);
        this.op_servicios.push(option);
      });
    },

    async putMutual() {
      let respuesta ="vacio"
      await axios.put('http://localhost:8081/mutuales/'+this.mutual.id_mutual+ '/', this.mutual)
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

    cargarFeedback() {
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
    },

  },
  beforeMount() {
    this.getServicios();
  },
};
</script>

<style>
</style>