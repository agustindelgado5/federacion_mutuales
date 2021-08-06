<template>
  <div>
    <button @click="postSocio()">POST TEST</button>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Datos Personales: </h4>
    
    <b-form >
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
      <b-form-group label="*DNI" label-for="dni">
        <b-form-input
          id="dni"
          v-model="socio.dni"
          type="number"
          placeholder="Ingrese un DNI"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>

      
      <b-form-group label="*Fecha de nacimiento" label-for="fecha_nacimiento">
        <b-form-input
          id="fecha_nacimiento"
          v-model="socio.fecha_nacimiento"
          type="date"
          placeholder="Ingrese una fecha"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>
      <h4>Domicilio: </h4>
      <b-form-group label="*Calle" label-for="calle">
        <b-form-input
          id="calle"
          v-model="socio.calle"
          type="text"
          placeholder="Ingrese una calle"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>
      <b-form-group label="*Localidad" label-for="localidad">
        <b-form-input
          id="localidad"
          v-model="socio.localidad"
          type="text"
          placeholder="Ingrese una localidad"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>
      <b-form-group label="*Departamento" label-for="departamento">
        <b-form-input
          id="departamento"
          v-model="socio.departamento"
          type="text"
          placeholder="Ingrese un departamento"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>
      <b-form-group label="*Codigo postal" label-for="cod_postal">
        <b-form-input
          id="cod_postal"
          v-model="socio.cod_postal"
          type="number"
          placeholder="Ingrese un numero"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>
      <h4>Contacto: </h4>
      <b-form-group label="*Email" label-for="email">
        <b-form-input
          id="email"
          v-model="socio.email"
          type="email"
          placeholder="Ingrese un email"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>

      <b-form-group label="Telefono fijo" label-for="tel_fijo">
        <b-form-input
          id="tel_fijo"
          v-model="socio.tel_fijo"
          type="number"
          placeholder="Ingrese un numero"
        >
        </b-form-input>
      </b-form-group>

      <b-form-group label="Celular" label-for="tel_celular">
        <b-form-input
          id="tel_celular"
          v-model="socio.tel_celular"
          type="number"
          placeholder="Ingrese un numero"
        >
        </b-form-input>
      </b-form-group>
      <b-form-group label="Carencia" label-for="carencia">
        <b-form-input
          id="carencia"
          v-model="socio.carencia"
          type="date"
          placeholder="Ingrese una fecha"
          invalid-feedback="Complete este campo"
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