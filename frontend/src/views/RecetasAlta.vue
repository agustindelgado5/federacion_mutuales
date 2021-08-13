<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Nueva Receta: </h4>

    <!-- CAMPOS REQUERIDOS -->
    <!-- Numero de Socio -->
    <!-- Paciente para el cual se emite la receta -->
    <!-- Diagnostico -->
    <!-- Id del medicamento -->
    <!-- Id de la farmacia -->
    <!-- Fecha de emision -->
    <!-- Carencia -->

    <!------------------------------------------------------------------------------------------->

    

    
    <b-form >
      <!-- Numero de Socio -->
        
        <b-form-group label="*N° Orden" label-for="numero_orden">
          <b-form-input
            id="numero_orden"
            v-model="receta.numero_orden"
            type="number"
            placeholder="Ingrese un Numero"
            invalid-feedback="Complete este campo"
            required
          >
          </b-form-input>
        </b-form-group>
        <!-- Numero de Socio -->
        <!--
        <b-form-group label="*N° Socio" label-for="numero_socio">
            <b-form-input
            id="numero_socio"
            v-model="receta.numero_socio"
            type="number"
            placeholder="Ingrese un Numero"
            invalid-feedback="Complete este campo"
            required
            >
            </b-form-input>
        </b-form-group>
        -->
      <b-button @click="getSocios()">GET TEST</b-button>
      {{ list_socios }}
      <b-form-group label="*Socio" label-for="numero_socio">
        <b-form-select
          id="numero_socio"
          v-model="receta.numero_socio"
          type="text"
          placeholder="Ingrese un Numero"
          invalid-feedback="Complete este campo"
          required
          :options="op_socios"
        >
        </b-form-select>
      </b-form-group>

      <!-- Paciente para el cual se emite la receta -->
      <!-- 
      <b-form-group label="*Paciente" label-for="dni_familiar">
        <b-form-input
          id="dni_familiar"
          v-model="receta.dni_familiar"
          type="text"
          placeholder="*Ingrese el nombre completo del paciente"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>
      -->
      <b-button @click="getPaciente()">GET TEST</b-button>
      {{ list_pacientes }}
      <b-form-group label="*Paciente" label-for="dni_familiar">
        <b-form-select
          id="dni_familiar"
          v-model="receta.dni_familiar"
          type="text"
          placeholder="*Ingrese el nombre completo del paciente"
          invalid-feedback="Complete este campo"
          required
          :options="list_pacientes"
        >
        </b-form-select>
      </b-form-group>

      <!-- Diagnostico -->
      <b-form-group label="*Diagnostico" label-for="diagnostico">
        <b-form-input
          id="diagnostico"
          v-model="receta.diagnostico"
          type="text"
          placeholder="*Ingrese el diagnostico"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>
      
      <!-- Id del medicamento -->
      <!--
      <b-form-group label="*ID Medicamento" label-for="id_medicamento">
        <b-form-input
          id="id_medicamento"
          v-model="receta.id_medicamento"
          type="number"
          placeholder="Ingrese el ID del medicamento"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>
      -->
      <b-button @click="getMedicamentos()">GET TEST</b-button>
      {{ list_medicamentos }}
      <b-form-group label="*Medicamento" label-for="id_medicamento">
        <b-form-select
          id="id_medicamento"
          v-model="receta.id_medicamento"
          type="text"
          placeholder="Ingrese el ID del medicamento"
          invalid-feedback="Complete este campo"
          required
          :options="op_medicamentos"
        >
        </b-form-select>
      </b-form-group>

      <!-- Id de la farmacia -->
      <!--
      <b-form-group label="*ID Farmacia" label-for="cod_farmacia">
        <b-form-input
          id="cod_farmacia"
          v-model="receta.cod_farmacia"
          type="number"
          placeholder="Ingrese el ID de la farmacia"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>
      -->

      <b-button @click="getFarmacias()">GET TEST</b-button>
      {{list_farmacias}}
      <b-form-group label="*Farmacia" label-for="cod_farmacia">
        <b-form-select
            id="cod_farmacia"
            v-model="receta.cod_farmacia"
            type="text"
            placeholder="Ingrese un Numero"
            invalid-feedback="Complete este campo"
            required
            :options="op_farmacias"
        >
        </b-form-select>
      </b-form-group>
    </b-form>
    {{ receta }}
    {{ data }}
     <b-button class="mt-2" variant="success" block @click="postReceta()">POST TEST</b-button>
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";

export default {
  data() {
    return {
      list_socios:{},
      list_familiar:{},
      list_medicamentos:{},
      list_farmacias:{},
      receta: {},
      data: {},
      op_socios: [
        {value: null, text: 'Elija un socio', disabled: true},
      ],
      op_medicamentos: [
        {value: null, text: 'Elija un medicamento', disabled: true},
      ],
      op_farmacias: [
        {value: null, text: 'Elija un medicamento', disabled: true},
      ],
      list_pacientes:[
        {value: null, text: 'Elija una persona', disabled: true},
      ],
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

    async getRecetas() {
      let recetaAPI = new APIControler();
      this.data = await recetaAPI.getData();
    },
    async postReceta() {
      let recetaAPI = new APIControler();
      recetaAPI.apiUrl.pathname='recetas/';
      this.data = await recetaAPI.postData(this.receta);
    },
  },
};
</script>

<style>
</style>