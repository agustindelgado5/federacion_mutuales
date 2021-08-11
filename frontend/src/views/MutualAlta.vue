<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Datos </h4>   
    <b-form >
      <b-form-group label="*Nombre de la mutual" label-for="nombre">
        <b-form-input
          id="nombre"
          v-model="mutuales.nombre"
          type="text"
          placeholder="*Ingrese el Nombre"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>
      <b-form-group label="*Sucursal" label-for="sucursal">
        <b-form-input
          id="sucursal"
          v-model="mutuales.sucursal"
          type="text"
          placeholder="Ingrese una sucursal"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
    </b-form-group>
    </b-form>
    {{ mutuales }}
    {{ data }}
    <b-button class="mt-2" variant="success" block @click="postMutual()">POST TEST</b-button>
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";

export default {
  data() {
    return {
      mutuales: {},
      data: {},
    };
  },
  methods: {
    async getMutual() {
      let mutualAPI = new APIControler();
      this.data = await mutualAPI.getData();
    },
    async postMutual() {
      let mutualAPI = new APIControler();
      mutualAPI.apiUrl.pathname='mutuales/'
      this.data = await mutualAPI.postData(this.mutuales);
    },
  },
};
</script>

<style>
</style>