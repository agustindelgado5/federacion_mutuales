<template>
  <div>
  
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Nueva Orden: </h4>

    <!-- CAMPOS REQUERIDOS -->
    <!-- N° Orden -->
    <!-- N° Socio -->
    <!-- Paciente -->
    <!-- Servicio -->
    <!-- Id Medico -->
    <!-- Id Mutual -->
    <!-- Fecha -->
    <!-- Precio -->
    <!-- Realizado -->

    <!------------------------------------------------------------------------------------------->
    <b-form >
        <b-form-group label="*N° Orden" label-for="numero_orden">
            <!-- Numero de Orden -->
            <b-form-input
            id="numero_orden"
            v-model="orden.numero_orden"
            type="number"
            placeholder="Ingrese un Numero"
            invalid-feedback="Complete este campo"
            required
            >
            </b-form-input>
        </b-form-group>
      
      <!-- 
        <b-form-group label="*N° Socio" label-for="numero_socio">
            <b-form-input
            id="numero_socio"
            v-model="orden.numero_socio"
            type="number"
            placeholder="Ingrese un Numero"
            invalid-feedback="Complete este campo"
            required
            >
            </b-form-input>
        </b-form-group>
      -->
      <!-- <b-button @click="getSocios()">GET TEST</b-button> -->
      <!-- {{ list_socios }} -->
      <b-form-group label="*Socio" label-for="numero_socio">
            <b-form-select 
            id="numero_socio"
            v-model="orden.numero_socio"
            type="text"
            placeholder="Ingrese un Numero"
            invalid-feedback="Complete este campo"
            required
            :options="op_socios"
            @change="getPaciente()"
            >
            </b-form-select>
        </b-form-group>


      <!-- Paciente para el cual se emite la receta -->
      <!--
      <b-form-group label="*Paciente" label-for="paciente">
        <b-form-input
          id="paciente"
          v-model="orden.paciente"
          type="number"
          placeholder="*Ingrese el nombre completo del paciente"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>
      -->
      <!-- <b-button @click="getPaciente()">GET TEST</b-button>
      {{ list_pacientes }} -->
      <b-form-group label="*Paciente" label-for="dni_familiar">
        <b-form-select 
          id="dni_familiar"
          v-model="orden.dni_familiar"
          type="text"
          placeholder="*Ingrese el nombre completo del paciente"
          invalid-feedback="Complete este campo"
          required
          :options="list_pacientes"
        >
        </b-form-select>
      </b-form-group>

      <!-- Servicio -->
      <b-form-group label="*Servicio" label-for="servicio">
        <b-form-input
          id="servicio"
          v-model="orden.servicio"
          type="text"
          placeholder="*Ingrese el tipo de servicio"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>
      
      <!-- Id del medico -->
      <!--
      <b-form-group label="*ID Medico" label-for="id_medico">
        <b-form-input
          id="id_medico"
          v-model="orden.id_medico"
          type="number"
          placeholder="Ingrese el ID del medico"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>
      -->
      <!-- <b-button @click="getProfesionales()">GET TEST</b-button>
      {{ list_profesionales }} -->
      <b-form-group label="*Medico" label-for="id_medico">
        <b-form-select
          id="id_medico"
          v-model="orden.id_medico"
          type="text"
          placeholder="Ingrese el ID del medico"
          invalid-feedback="Complete este campo"
          required
          :options="op_profesionales"
        >
        </b-form-select>
      </b-form-group>
      <!-- Id de la mutual -->
      <!--
      <b-form-group label="*ID Mutual" label-for="id_mutual">
        <b-form-input
          id="id_mutual"
          v-model="orden.id_mutual"
          type="number"
          placeholder="Ingrese el ID de la mutual"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>
      -->
      <!-- <b-button @click="getMutuales()">GET TEST</b-button>
      {{ list_mutuales }} -->
      <b-form-group label="*ID Mutual" label-for="id_mutual">
        <b-form-select
          id="id_mutual"
          v-model="orden.id_mutual"
          type="text"
          placeholder="Ingrese el ID de la mutual"
          invalid-feedback="Complete este campo"
          required
          :options="op_mutuales"
        >
        </b-form-select>
      </b-form-group>

      <!-- Fecha de emision -->
      <b-form-group label="*Fecha" label-for="fecha">
        <b-form-input
          id="fecha"
          v-model="orden.fecha"
          type="date"
          placeholder="Ingrese una fecha"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>

      <!-- Hora -->
      <b-form-group label="*Hora" label-for="hora">
        <b-form-input
          id="hora"
          v-model="orden.hora"
          type="time"
          placeholder="Ingrese una hora"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>

      <!-- Precio -->
      <b-form-group label="*Precio" label-for="precio">
        <b-form-input
          id="precio"
          v-model="orden.precio"
          type="decimal"
          placeholder="Ingrese el precio correspondiente a la orden "
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>

      <!-- Realizado -->
      
      <b-form-group label="*Realizado" label-for="realizado">
        <b-form-checkbox
          id="realizado"
          v-model="orden.realizado"
          value="true"
          type="boolean"
          invalid-feedback="Complete este campo"
          required
          unchecked-value="false"
        >
        </b-form-checkbox>
      </b-form-group>
      

    </b-form>
    {{ orden }}
    
    <b-button class="mt-2" variant="success" block @click="postOrden()">Guardar</b-button>
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";

export default {
  data() {
    return {
      list_socios:{},
      list_profesionales: {},
      list_mutuales: {},
      list_familiar:{},
      orden: {},
      data: {},
      op_socios: [
        {value: null, text: 'Elija un socio', disabled: true},
      ],
      op_profesionales: [
        {value: null, text: 'Elija un profesional', disabled: true},
      ],
      op_mutuales: [
        {value: null, text: 'Elija una mutual', disabled: true},
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
      });
    },

    async getProfesionales() {
      let profesionalesAPI = new APIControler();
      profesionalesAPI.apiUrl.pathname='profesionales/';
      this.data = await profesionalesAPI.getData(this.list_profesionales);
      this.data.forEach(element => {   
        let option={}
        option.value='http://localhost:8081/profesionales/'+ element.id_medico +'/';
        option.text= element.id_medico +'-- '+ element.apellido +', '+ element.nombre +'-- '+ element.matricula;
        console.log(option);
        this.op_profesionales.push(option);
      });
    },

    async getMutuales() {
      let mutualesAPI = new APIControler();
      mutualesAPI.apiUrl.pathname='mutuales/';
      this.data = await mutualesAPI.getData(this.list_mutuales);
      this.data.forEach(element => {   
        let option={}
        option.value='http://localhost:8081/mutuales/'+ element.id_mutual +'/';
        option.text= element.id_mutual +'-- '+ element.nombre +', '+ element.sucursal;
        console.log(option);
        this.op_mutuales.push(option);
      });
    },

    async getPaciente() {
      let familiarAPI = new APIControler();
      familiarAPI.apiUrl.pathname='familiar/';
      this.data = await familiarAPI.getData(this.list_familiar);
      this.list_pacientes=this.list_pacientes.slice(0,1)
      this.data.forEach(element => {
        if (element.numero_socio ==this.orden.numero_socio){
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
    

    async getOrdenes() {
      let ordenAPI = new APIControler();
      this.data = await ordenAPI.getData();
    },
    async postOrden() {
      let ordenAPI = new APIControler();
      ordenAPI.apiUrl.pathname='ordenes/';
      this.data = await ordenAPI.postData(this.orden);
    },
  },
  beforeMount(){

    this.getSocios();
    this.getProfesionales()
    this.getMutuales()

 },
};
</script>

<style>
</style>