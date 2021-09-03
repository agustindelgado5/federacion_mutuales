<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Datos </h4>   
    <b-button @click="getSocios()">GET TEST</b-button>
      {{ list_socios }}
      <b-form-group label="*Socio" label-for="numero_socio">
        <b-form-select
          id="numero_socio"
          v-model="Cobradores.numero_socio"
          type="text"
          placeholder="Ingrese un Numero"
          invalid-feedback="Complete este campo"
          required
          :options="op_socios"
        >
        </b-form-select>
      </b-form-group>
   
    <b-form >
      <b-form-group label="*id cobrador" label-for="id_cobrador">
           
        <b-form-input
          id="id_cobrador"
          v-model="Cobradores.id_cobrador"
          type="number"
          placeholder="Ingrese un Numero"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
     </b-form-group>

      <b-form-group label="*Nombre/s" label-for="nombre">
        <b-form-input
          id="nombre"
          v-model="Cobradores.nombre"
          type="text"
          placeholder="*Ingrese los Nombre/s"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>
      <b-form-group label="*Apellido/s" label-for="apellido">
        <b-form-input
          id="apellido"
          v-model="Cobradores.apellido"
          type="text"
          placeholder="*Ingrese los Apellido/s"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>
      <b-form-group label="*DNI" label-for="dni">
        <b-form-input
          id="dni"
          v-model="Cobradores.dni"
          type="number"
          placeholder="Ingrese un DNI"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>

      
      <b-form-group label="*Fecha de Cobro" label-for="fecha_cobro">
        <b-form-input
          id="fecha_cobro"
          v-model="Cobradores.fecha_cobro"
          type="date"
          placeholder="Ingrese una fecha"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>
    
    </b-form>
    {{ Cobradores }}
    {{ data }}
    <b-button class="mt-2" variant="success" block @click="postCobrador()">POST TEST</b-button>
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";

export default {
  data() {
    return {
      list_socios:{},
      Cobradores: {},
      data: {},
      op_socios: [
        {value: null, text: 'Elija un socio', disabled: true},
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
        option.value='http://localhost:8080/socios/'+ element.numero_socio +'/';
        option.text= element.numero_socio +'-- '+ element.apellido +', '+ element.nombre ;
        console.log(option);
        this.op_socios.push(option);
        
      });
    },

    async getCobrador() {
      let cobradorAPI = new APIControler();
      this.data = await cobradorAPI.getData();
    },
    async postCobrador() {
      let cobradorAPI = new APIControler();
      cobradorAPI.apiUrl.pathname='cobradores/'
      this.data = await cobradorAPI.postData(this.Cobradores);
    },
  },
};
</script>

<style>
</style>