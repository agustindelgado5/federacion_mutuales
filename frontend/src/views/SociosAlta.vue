<template>
  <div>
    <!-- <button @click="postSocio()">POST TEST</button> -->
    <b-form @submit="onSubmit">
      <b-form-group label="Nombre" label-for="nombre">
        <b-form-input
          id="nombre"
          v-model="socio.nombre"
          type="text"
          placeholder="ingrese un nombre"
          required
        >
        </b-form-input>
      </b-form-group>
      <b-form-group label="Apellido" label-for="apellido">
        <b-form-input
          id="apellido"
          v-model="socio.apellido"
          type="text"
          placeholder="ingrese un apellido"
          required
        >
        </b-form-input>
      </b-form-group>
      <b-form-group label="DNI" label-for="dni">
        <b-form-input
          id="dni"
          v-model="socio.dni"
          type="number"
          placeholder="ingrese un dni"
          required
        >
        </b-form-input>
      </b-form-group>

      <b-form-group label="numero_socio" label-for="numero_socio">
        <b-form-input
          id="numero_socio"
          v-model="socio.numero_socio"
          type="number"
          placeholder="ingrese un numero_socio"
          required
        >
        </b-form-input>
      </b-form-group>
      <b-form-group label="fecha_nacimiento" label-for="fecha_nacimiento">
        <b-form-input
          id="fecha_nacimiento"
          v-model="socio.fecha_nacimiento"
          type="date"
          placeholder="ingrese un fecha_nacimiento"
          required
        >
        </b-form-input>
      </b-form-group>
      <b-form-group label="calle" label-for="calle">
        <b-form-input
          id="calle"
          v-model="socio.calle"
          type="text"
          placeholder="ingrese un calle"
          required
        >
        </b-form-input>
      </b-form-group>
      <b-form-group label="localidad" label-for="localidad">
        <b-form-input
          id="localidad"
          v-model="socio.localidad"
          type="text"
          placeholder="ingrese un localidad"
          required
        >
        </b-form-input>
      </b-form-group>
      <b-form-group label="departamento" label-for="departamento">
        <b-form-input
          id="departamento"
          v-model="socio.departamento"
          type="text"
          placeholder="ingrese un departamento"
          required
        >
        </b-form-input>
      </b-form-group>
      <b-form-group label="cod_postal" label-for="cod_postal">
        <b-form-input
          id="cod_postal"
          v-model="socio.cod_postal"
          type="number"
          placeholder="ingrese un cod_postal"
          required
        >
        </b-form-input>
      </b-form-group>

      <b-form-group label="email" label-for="email">
        <b-form-input
          id="email"
          v-model="socio.email"
          type="email"
          placeholder="ingrese un email"
          required
        >
        </b-form-input>
      </b-form-group>

      <b-form-group label="tel_fijo" label-for="tel_fijo">
        <b-form-input
          id="tel_fijo"
          v-model="socio.tel_fijo"
          type="number"
          placeholder="ingrese un tel_fijo"
          required
        >
        </b-form-input>
      </b-form-group>

      <b-form-group label="tel_celular" label-for="tel_celular">
        <b-form-input
          id="tel_celular"
          v-model="socio.tel_celular"
          type="number"
          placeholder="ingrese un tel_celular"
          required
        >
        </b-form-input>
      </b-form-group>
      <b-form-group label="carencia" label-for="carencia">
        <b-form-input
          id="carencia"
          v-model="socio.carencia"
          type="date"
          placeholder="ingrese un carencia"
          required
        >
        </b-form-input>
      </b-form-group>
    </b-form>
    {{ socio }}
    {{ data }}
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";

export default {
  data() {
    return {
      socio: {},
      data: {},
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