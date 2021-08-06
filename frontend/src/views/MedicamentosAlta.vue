<template>
  <div>
    <button @click="postMedicamento()">POST TEST</button>
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
        <b-form-input
          id="sucursal"
          v-model="medicamentos.presentacion"
          type="text"
          placeholder="Describa la presentacion"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
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

      <b-form-group label="*ID Farmacia" label-for="cod_farmacia">
        <b-form-input
            id="cod_farmacia"
            v-model="medicamentos.cod_farmacia"
            type="text"
            placeholder="Ingrese un Numero"
            invalid-feedback="Complete este campo"
            required
        >
        </b-form-input>
      </b-form-group>

      
    </b-form>
    {{ medicamentos}}
    {{ data }}
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";

export default {
  data() {
    return {
      medicamentos: {},
      data: {},
    };
  },
  methods: {
    async getMedicamento() {
      let medicamentosAPI = new APIControler();
      this.data = await medicamentosAPI.getData();
    },
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