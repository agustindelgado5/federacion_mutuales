<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    
    <b-form>
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
    <b-button class="mt-2" variant="success" block @click="postSocio()">Guardar</b-button>
    
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";


export default {
  data() {
    return {
      familiar: {},
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
      this.resetForm();
    },
    async resetForm() {
        this.socio.numero_socio = null;
        this.socio.apellido = "";
        this.socio.nombre = "";
        this.socio.dni = null;
        this.socio.fecha_nacimiento=null;
        this.socio.calle = "";
        this.socio.localidad = "";
        this.socio.departamento = "";
        this.socio.cod_postal = null;
        this.socio.tel_fijo = null;
        this.socio.tel_celular = null;
        this.socio.carencia= null;
    },
  },
};
</script>

<style>
</style>