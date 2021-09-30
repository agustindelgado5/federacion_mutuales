<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Nueva Cirugia:</h4>

    <!-- CAMPOS REQUERIDOS -->
    <!-- codigo_intervencion -->
    <!-- descrpcion-->
    <!-- observacion -->
    
    <!------------------------------------------------------------------------------------------->
    <b-form>
      <b-form-group label="*Codigo de intervencion" label-for="codigo_intervencion">
        <!-- codigo_intervencion -->
        <b-form-input
          id="codigo_intervencion"
          v-model="cirugia.codigo_intervencion"
          type="text"
          placeholder="Ingrese el código"
          invalid-feedback="Complete este campo"
          :state="validacion.codigo_intervencion.estado"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback id="codigo_intervencion-live-feedback"
          >{{ validacion.codigo_intervencion.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>

      

      <b-form-group label="*Descripcion" label-for="descripcion">
        <b-form-input
          id="descripcion"
          v-model="cirugia.descripcion"
          :state="validacion.descripcion.estado"
          type="text"
          placeholder="*Ingrese una abreviatura"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback id="descripcion-live-feedback"
          >{{ validacion.descripcion.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>
      
      
      <b-form-group label="*Observacion" label-for="observacion">
        <b-form-input
          id="observacion"
          v-model="cirugia.observacion"
          :state="validacion.observacion.estado"
          type="text"
          placeholder="*Ingrese una observacion"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback id="observacion-live-feedback"
          >{{ validacion.observacion.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>

    </b-form>
    <b-button class="mt-2" variant="success" block @click="postCirugia()"
      >Guardar</b-button
    >
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";

export default {
  data() {
    return {
      
      cirugia: {},
      data: {},

      validacion: {
       
        codigo_intervencion: { estado: null, mensaje: "" },
        descripcion: { estado: null, mensaje: "" },
        observacion: { estado: null, mensaje: "" },
      },
      
      respuesta: null,
    };
  },

  methods: {
    
    async getCirugias() {
      let  cirugiaAPI = new APIControler();
      this.data = await  cirugiaAPI.getData();
    },
    async postCirugia() {
      let cirugiaAPI = new APIControler();
      cirugiaAPI.apiUrl.pathname = "cirugias/";
      this.respuesta = await cirugiaAPI.postData(this.cirugia);
      this.cargarFeedback();
    },

    cargarFeedback() {
      let valido;
      if(typeof this.respuesta === 'undefined')
      {
        return
      }
      for (let key in this.validacion) {
        valido = !this.respuesta.hasOwnProperty(key);
        this.validacion[key].estado = valido;
        if (!valido) this.validacion[key].mensaje = this.respuesta[key][0];
      }
    },
  },
  beforeMount() {
  },
};
</script>

<style>

</style>