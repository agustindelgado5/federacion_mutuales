<template>
  <div>
    <button @click="postFarmacia()">POST TEST</button>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Registrar nueva farmacia: </h4>

    <!-- CAMPOS REQUERIDOS -->
    <!-- cod_farmacia -->
    <!-- matricula_farm -->
    <!-- farmacia -->
    <!-- cuit -->
    <!-- localidad -->
    <!-- direccion -->
    <!-- cod_postal -->
    <!-- email -->
    <!-- tel_fijo -->
    <!-- tel_celular -->
    <!-- representante -->

    <!------------------------------------------------------------------------------------------->

    <b-form >
        <!-- cod_farmacia -->
        <b-form-group label="*ID Farmacia" label-for="cod_farmacia" @submit.stop.prevent="handleSubmit">
            <b-form-input
            id="cod_farmacia"
            v-model="farmacia.cod_farmacia"
            type="number"
            placeholder="Ingrese el ID de la farmacia"
            invalid-feedback="Complete este campo"
            required
            >
            </b-form-input>
        </b-form-group>

        <!-- matricula_farm -->
        <b-form-group label="*Matricula Farmacia" label-for="matricula_farm" @submit.stop.prevent="handleSubmit">
            <b-form-input
            id="matricula_farm"
            v-model="farmacia.matricula_farm"
            type="number"
            placeholder="Ingrese la matricula de la farmacia"
            invalid-feedback="Complete este campo"
            required
            >
            </b-form-input>
        </b-form-group>

      <!-- farmacia -->
      <b-form-group label="*Farmacia" label-for="farmacia">
        <b-form-input
          id="farmacia"
          v-model="farmacia.farmacia"
          type="text"
          placeholder="*Ingrese el nombre de la farmacia"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>

      <!-- cuit -->
        <b-form-group label="*CUIT Farmacia" label-for="cuit" @submit.stop.prevent="handleSubmit">
            <b-form-input
            id="cuit"
            v-model="farmacia.cuit"
            type="number"
            placeholder="Ingrese el CUIT de la farmacia"
            invalid-feedback="Complete este campo"
            required
            >
            </b-form-input>
        </b-form-group>

      <!-- localidad -->
      <b-form-group label="*Localidad" label-for="localidad">
        <b-form-input
          id="localidad"
          v-model="farmacia.localidad"
          type="text"
          placeholder="*Ingrese la localidad"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>

      <!-- direccion -->
      <b-form-group label="*Direccion" label-for="direccion">
        <b-form-input
          id="direccion"
          v-model="farmacia.direccion"
          type="text"
          placeholder="*Ingrese la direccion"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>

      <!-- cod_postal -->
        <b-form-group label="*Codigo postal" label-for="cod_postal" @submit.stop.prevent="handleSubmit">
            <b-form-input
            id="cod_postal"
            v-model="farmacia.cod_postal"
            type="number"
            placeholder="Ingrese el codigo postal"
            invalid-feedback="Complete este campo"
            required
            >
            </b-form-input>
        </b-form-group>

     <!-- email -->
     <b-form-group label="*Email" label-for="email">
        <b-form-input
          id="email"
          v-model="farmacia.email"
          type="email"
          placeholder="Ingrese un email"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group> 

    <!-- tel_fijo -->
    <b-form-group label="Telefono fijo" label-for="tel_fijo">
        <b-form-input
          id="tel_fijo"
          v-model="farmacia.tel_fijo"
          type="number"
          placeholder="Ingrese un numero de telefono fijo"
        >
        </b-form-input>
    </b-form-group>

    <!-- tel_celular -->
    <b-form-group label="Telefono Celular" label-for="tel_celular">
        <b-form-input
          id="tel_celular"
          v-model="farmacia.tel_celular"
          type="number"
          placeholder="Ingrese un numero de telefono celular"
        >
        </b-form-input>
      </b-form-group>

    <!-- representante -->
    <b-form-group label="*Representante" label-for="representante">
        <b-form-input
          id="representante"
          v-model="farmacia.representante"
          type="text"
          placeholder="*Ingrese el nombre del representante"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
    </b-form-group>

    </b-form>
    {{ farmacia }}
    {{ data }}
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";

export default {
  data() {
    return {
      farmacia: {},
      data: {},
    };
  },
  methods: {
    async getFarmacias() {
      let farmaciaAPI = new APIControler();
      this.data = await farmaciaAPI.getData();
    },
    async postOrden() {
      let farmaciaAPI = new APIControler();
      farmaciaAPI.apiUrl.pathname='farmacias/';
      this.data = await farmaciaAPI.postData(this.farmacia);
    },
  },
};
</script>

<style>
</style>