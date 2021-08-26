<template>
  <div>
    <h3>Pago de afiliacion</h3>
    <h6>Los campos en (*) son obligatorios</h6>
    
    
    <b-form >
      <h4>Datos Personales: </h4>
      <b-form-group label="*N° Socio" label-for="numero_socio">
        <b-form-input
            id="numero_socio"
            v-model="socio.numero_socio"
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
          v-model="socio.nombre"
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
          v-model="socio.apellido"
          type="text"
          placeholder="*Ingrese los Apellido/s"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>
    </b-form>

    <b-button class="mt-2" variant="success" block @click="postSocio()">Generar pago</b-button>
    
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";


export default {
  data() {
    return {
      socio: {},
      data: {},
      plan: [],
      select: null,
    };
  },

  methods: {
    async getSocios() {
      let socioAPI = new APIControler();
      this.data = await socioAPI.getData();
    },
    async postSocio() {
      let socioAPI = new APIControler();
      this.data = await socioAPI.postData(this.socio);
    },
  },
};
</script>

<style>
</style>