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
        
        <b-form-group label="*N° Socio" label-for="numero_socio">
            <!-- Numero de Socio -->
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

      <!-- Paciente para el cual se emite la receta -->
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

      <!-- Id de la farmacia -->
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
      receta: {},
      data: {},
    };
  },
  methods: {
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