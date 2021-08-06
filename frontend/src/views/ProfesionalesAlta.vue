<template>
  <div>
    <button @click="postProfesional()">POST TEST</button>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Datos Personales: </h4>
    <b-form-group label="*Id Medico" label-for="id_medico">
        <b-form-input
          id="id_medico"
          v-model="profesional.id_medico"
          type="number"
          placeholder="Ingrese un Numero"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
    </b-form-group>
    <b-form-group label="*Matricula" label-for="matricula">
        <b-form-input
          id="matricula"
          v-model="profesional.matricula"
          type="number"
          placeholder="Ingrese un Numero"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
    </b-form-group>
    <b-form >
      <b-form-group label="*Nombre/s" label-for="nombre">
        <b-form-input
          id="nombre"
          v-model="profesional.nombre"
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
          v-model="profesional.apellido"
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
          v-model="profesional.dni"
          type="number"
          placeholder="Ingrese un DNI"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>

      
      <b-form-group label="*Fecha de ingreso" label-for="fecha_ingreso">
        <b-form-input
          id="fecha_ingreso"
          v-model="profesional.fecha_ingreso"
          type="date"
          placeholder="Ingrese una fecha"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>
      <b-form-group label="*Especialidad" label-for="especialidad">
        <b-form-input
          id="especialidad"
          v-model="profesional.especialidad"
          type="text"
          placeholder="*Ingrese la Especialidad"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>
      <h4>Domicilio: </h4>
      <b-form-group label="*Calle" label-for="domicilio">
        <b-form-input
          id="domicilio"
          v-model="profesional.domicilio"
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
          v-model="profesional.localidad"
          type="text"
          placeholder="Ingrese una localidad"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>
      <b-form-group label="*Provincia" label-for="provincia">
        <b-form-input
          id="provincia"
          v-model="profesional.provincia"
          type="text"
          placeholder="Ingrese una provincia"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>
      
      <h4>Contacto: </h4>
      <b-form-group label="*Email" label-for="email">
        <b-form-input
          id="email"
          v-model="profesional.email"
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
          v-model="profesional.tel_fijo"
          type="number"
          placeholder="Ingrese un numero"
        >
        </b-form-input>
      </b-form-group>

      <b-form-group label="Celular" label-for="tel_celular">
        <b-form-input
          id="tel_celular"
          v-model="profesional.tel_celular"
          type="number"
          placeholder="Ingrese un numero"
        >
        </b-form-input>
      </b-form-group>
    </b-form>
    {{ profesional }}
    {{ data }}
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";

export default {
  data() {
    return {
      profesional: {},
      data: {},
    };
  },
  methods: {
    async getProfesional() {
      let profesionalAPI = new APIControler();
      this.data = await profesionalAPI.getData();
    },
    async postProfesional() {
      let profesionalAPI = new APIControler();
      profesionalAPI.apiUrl.pathname='profesionales/'
      this.data = await profesionalAPI.postData(this.profesional);
    },
  },
};
</script>

<style>
</style>