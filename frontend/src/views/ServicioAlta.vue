<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Datos </h4>   
    <b-form >
      <b-form-group label="*Nombre del servicio" label-for="nombre">
        <b-form-input
          id="nombre"
          v-model="servicios.nombre"
          type="text"
          placeholder="*Ingrese el nombre del servicio"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>
      <b-form-group label="*Carencia" label-for="carencia">
        <b-form-input
          id="carencia"
          v-model="servicios.carencia"
          type="number"
          placeholder="Ingrese la carencia en meses"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
    </b-form-group>
    </b-form>
    {{ servicios }}
    {{ data }}
    <b-button class="mt-2" variant="success" block @click="postServicio()">POST TEST</b-button>
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";

export default {
  data() {
    return {
      servicios: {},
      data: {},
    };
  },
  methods: {
    async getServicio() {
      let servicioAPI = new APIControler();
      this.data = await servicioAPI.getData();
    },
    async postServicio() {
      let servicioAPI = new APIControler();
      servicioAPI.apiUrl.pathname='servicios/'
      this.data = await servicioAPI.postData(this.servicios);
    },
  },
};
</script>

<style>
</style>