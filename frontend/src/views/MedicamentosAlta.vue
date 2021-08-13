<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Datos </h4>   
    <b-form >
      <b-form-group label="*ID" label-for="id_medicamento">
        <b-form-input
            id="id_medicamento"
            v-model="medicamentos.id_medicamento"
            type="number"
            placeholder="Ingrese un Numero"
            invalid-feedback="Complete este campo"
            required
        >
        </b-form-input>
      </b-form-group>
      <b-form-group label="*Nombre" label-for="nombre">
        <b-form-input
            id="nombre"
            v-model="medicamentos.nombre"
            type="text"
            placeholder="Ingrese el nombre"
            invalid-feedback="Complete este campo"
            required
        >
        </b-form-input>
      </b-form-group>
      
      <b-form-group label="*Presentacion" label-for="presentacion">
        <b-form-textarea
          id="presentacion"
          v-model="medicamentos.presentacion"
          type="text"
          placeholder="Describa la presentacion"
          invalid-feedback="Complete este campo"
          required
          rows="3"
          max-rows="6"
        >
        </b-form-textarea>
      </b-form-group>
      <b-form-group label="*Laboratorio" label-for="laboratorio">
        <b-form-input
            id="laboratorio"
            v-model="medicamentos.laboratorio"
            type="text"
            placeholder="Ingrese el nombre"
            invalid-feedback="Complete este campo"
            required
        >
        </b-form-input>
      </b-form-group>
      
      <b-button @click="getFarmacias()">GET TEST</b-button>
      {{farmacias}}
      <b-form-group label="*Farmacia" label-for="cod_farmacia">
        <b-form-select
            id="cod_farmacia"
            v-model="medicamentos.cod_farmacia"
            type="text"
            placeholder="Ingrese un Numero"
            invalid-feedback="Complete este campo"
            required
            :options="options"
        >
        </b-form-select>
      </b-form-group>
      

      
    </b-form>
    {{ medicamentos}}
    {{ data }}
     <b-button class="mt-2" variant="success" block @click="postMedicamento()">POST TEST</b-button>
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
      ]
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
      this.data = await medicamentosAPI.postData(this.medicamentos);
    },
  },
};
</script>

<style>
</style>