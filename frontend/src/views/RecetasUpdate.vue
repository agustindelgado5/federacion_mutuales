<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Modificar Receta: </h4>

    <!-- CAMPOS REQUERIDOS -->
    <!-- Id Receta -->
    <!-- Numero de Socio -->
    <!-- Paciente para el cual se emite la receta -->
    <!-- Diagnostico -->
    <!-- Id del medicamento -->
    <!-- Id de la farmacia -->
    <!-- Fecha de emision -->
    <!-- Carencia -->

    <!------------------------------------------------------------------------------------------->

     <!-- Numero de Socio -->
      <!-- <b-button @click="getSocios()">GET TEST</b-button>
      {{ list_socios }} -->
      <b-form-group label="*Socio" label-for="numero_socio">
        <b-form-select
          id="numero_socio"
          v-model="receta.numero_socio"
          type="text"
          placeholder="Ingrese un Numero"
          invalid-feedback="Complete este campo"
          required
          :state="validacion.numero_socio.estado"
          :options="op_socios"
          @change="getPaciente()"
        >
        </b-form-select>
        <b-form-invalid-feedback id="numero_socio-live-feedback"
          >{{ validacion.numero_socio.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>

    
    <b-form >

      <!-- Paciente para el cual se emite la receta -->
      <!-- <b-button @click="getPaciente()">GET TEST</b-button>
      {{ list_pacientes }} -->
      <b-form-group label="*Paciente" label-for="paciente">
        <b-form-select
          id="paciente"
          v-model="receta.paciente"
          type="text"
          :state="validacion.paciente.estado"
          placeholder="*Ingrese el nombre completo del paciente"
          invalid-feedback="Complete este campo"
          required
          :options="list_pacientes"
        >
        </b-form-select>
        <b-form-invalid-feedback id="paciente-live-feedback"
          >{{ validacion.paciente.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>

      <!-- Diagnostico -->
      <b-form-group label="*Diagnostico" label-for="diagnostico">
        <b-form-input
          id="diagnostico"
          v-model="receta.diagnostico"
          type="text"
          :state="validacion.diagnostico.estado"
          placeholder="Ingrese el diagnóstico"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback id="diagnostico-live-feedback"
          >{{ validacion.diagnostico.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>
      
      <!-- Id del medicamento -->
      <!-- <b-button @click="getMedicamentos()">GET TEST</b-button>
      {{ list_medicamentos }} -->
      <b-form-group label="*Medicamento" label-for="id_medicamento">
        <b-form-select
          id="id_medicamento"
          v-model="receta.id_medicamento"
          type="text"
          :state="validacion.id_medicamento.estado"
          placeholder="Ingrese el ID del medicamento"
          invalid-feedback="Complete este campo"
          required
          :options="op_medicamentos"
        >
        </b-form-select>
        <b-form-invalid-feedback id="id_medicamento-live-feedback"
          >{{ validacion.id_medicamento.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>

      <!-- Id de la farmacia -->
      <!-- <b-button @click="getFarmacias()">GET TEST</b-button>
      {{list_farmacias}} -->
      <b-form-group label="*Farmacia" label-for="cod_farmacia">
        <b-form-select
            id="cod_farmacia"
            v-model="receta.cod_farmacia"
            type="text"
            placeholder="Ingrese un Numero"
            :state="validacion.cod_farmacia.estado"
            invalid-feedback="Complete este campo"
            required
            :options="op_farmacias"
        >
        </b-form-select>
        <b-form-invalid-feedback id="cod_farmacia-live-feedback"
          >{{ validacion.cod_farmacia.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>

      <b-form-group data-app label="*Medico" label-for="id_medico">
          <v-autocomplete
            id="id_medico"
            v-model="receta.id_medico"
            :items="op_profesionales"
            :state="validacion.id_medico.estado"
            type="text"
            solo
            placeholder="Ingrese el ID del medico"
            invalid-feedback="Complete este campo"
            required
          ></v-autocomplete>

        <!-- <b-form-invalid-feedback id="id_medico-live-feedback"
          >{{ validacion.id_medico.mensaje }}
        </b-form-invalid-feedback> -->
      </b-form-group>
      
      <!-- Fecha de emision -->
      <b-form-group label="*Fecha" label-for="fecha">
        <b-form-input
          id="fecha"
          v-model="receta.fecha"
          :state="validacion.fecha.estado"
          type="date"
          placeholder="Ingrese una fecha"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback id="fecha-live-feedback"
          >{{ validacion.fecha.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>
      
      <b-form-group label="Carencia" label-for="carencia">
        <b-form-input
          id="carencia"
          v-model="receta.carencia"
          :state="validacion.carencia.estado"
          type="date"
          placeholder="Ingrese una fecha"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback id="carencia-live-feedback"
          >{{ validacion.carencia.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>
    </b-form>
    <!-- {{ receta }}
    {{ data }} -->
     <b-button class="mt-2" variant="success" block @click="putReceta()">Modificar receta</b-button>
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";
import axios from "axios";

export default {
  props: {
    receta: {},
  },
  data() {
    return {
      list_socios:{},
      list_familiar:{},
      list_medicamentos:{},
      list_farmacias:{},
      data: {},
      op_socios: [
        {value: null, text: 'Elija un socio', disabled: true},
      ],
      op_medicamentos: [
        {value: null, text: 'Elija un medicamento', disabled: true},
      ],
      op_profesionales: [
        { value: null, text: "Elija un profesional", disabled: true },
      ],
    
      op_farmacias: [
        {value: null, text: 'Elija una farmacia', disabled: true},
      ],
      list_pacientes:[
        {value: null, text: 'Elija una persona', disabled: true},
      ],
      validacion: {
        // id_receta: { estado: null, mensaje: "" },
        numero_socio: { estado: null, mensaje: "" },
        diagnostico: { estado: null, mensaje: "" },
        paciente: { estado: null, mensaje: "" },
        id_medicamento: { estado: null, mensaje: "" },
        cod_farmacia: { estado: null, mensaje: "" },
        fecha: { estado: null, mensaje: "" },
        id_medico: { estado: null, mensaje: "" },
        carencia: { estado: null, mensaje: "" },
      },
    };
  },
  methods: {
    async getSocios() {
      let socioAPI = new APIControler();
      socioAPI.apiUrl.pathname='socios/';
      this.data = await socioAPI.getData(this.list_socios);
      this.data.forEach(element => {   
        let option={}
        option.value='http://localhost:8081/socios/'+ element.numero_socio +'/';
        option.text= element.numero_socio +'-- '+ element.apellido +', '+ element.nombre ;
        console.log(option);
        this.op_socios.push(option);
        if (element.numero_socio==this.receta.numero_socio){
          this.list_pacientes.push(option);
        }
      });
    },

    async getMedicamentos() {
      let medicamentosAPI = new APIControler();
      medicamentosAPI.apiUrl.pathname='medicamentos/';
      this.data = await medicamentosAPI.getData(this.list_medicamentos);
      this.data.forEach(element => {   
        let option={}
        option.value='http://localhost:8081/medicamentos/'+ element.id_medicamento +'/';
        option.text= element.id_medicamento +'-- '+  element.nombre ;
        console.log(option);
        this.op_medicamentos.push(option);
      });
    },

    async getFarmacias() {
      let farmaciaAPI = new APIControler();
      farmaciaAPI.apiUrl.pathname='farmacias/'
      this.data = await farmaciaAPI.getData(this.list_farmacias);
      this.data.forEach(element => {   
        let option={}
        option.value='http://localhost:8081/farmacias/'+ element.cod_farmacia +'/';
        option.text=element.farmacia;
        console.log(option);
        this.op_farmacias.push(option);
      });
    },
  
    async getPaciente() {
      let familiarAPI = new APIControler();
      familiarAPI.apiUrl.pathname='familiar/';
      this.data = await familiarAPI.getData(this.list_familiar);
      let option_titular = {};
      option_titular.value = this.receta.numero_socio;
      console.log("this.receta.numero_socio")
      console.log(this.receta.numero_socio)
      option_titular.text = "Titular";
      this.list_pacientes.push(option_titular);

      this.data.forEach(element => {
        if (element.numero_socio ==this.receta.numero_socio){
            //let option_titular={}
            let option_adherente={}
            //option_titular.value='http://localhost:8081/socios/'+ element.numero_socio +'/';
            //option_titular.text='Titular';
            //option_titular.text= socios.dni +'-- '+ socios.apellido +', '+ socios.nombre ;
            //console.log(option_titular);
            //this.list_pacientes.push(option_titular);

            option_adherente.value='http://localhost:8081/familiar/'+ element.dni_familiar +'/';
            option_adherente.text= element.dni_familiar +'-- '+ element.apellido +', '+ element.nombre ;
            console.log(option_adherente);
            this.list_pacientes.push(option_adherente);
          }   
      });
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
    async getRecetas() {
      let recetaAPI = new APIControler();
      this.data = await recetaAPI.getData();
    },
    async putReceta() {
      let respuesta ="vacio"
      await axios.put('http://localhost:8081/recetas/'+this.receta.id_receta+ '/', this.receta)
      .then(function (data){
        
        swal("Operación Exitosa", " ", "success");
      })
      .catch(function (error) {
        swal("¡ERROR!", "Se ha detectado un problema ", "error");
        respuesta=error.response.data;
        
        //console.log(error.response.data);
      })
      this.cargarFeedback(respuesta)




      // let recetaAPI = new APIControler();
      // recetaAPI.apiUrl.pathname='recetas/';
      // let respuesta = await recetaAPI.putData(this.receta);
      // this.cargarFeedback(respuesta);
    },
      cargarFeedback(respuesta) {
      let valido;
      for (let key in this.validacion) {
        valido = !respuesta.hasOwnProperty(key);
        this.validacion[key].estado = valido;
        if (!valido) this.validacion[key].mensaje = respuesta[key][0];
      }
    },
  },
  beforeMount() {
    this.getSocios();
    this.getMedicamentos();
    this.getFarmacias();
    this.getProfesionales();
    this.getPaciente()
  },
};
</script>

<style>
</style>