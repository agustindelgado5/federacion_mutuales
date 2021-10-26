<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Modificar Estudio:</h4>

    <!-- CAMPOS REQUERIDOS -->
    <!-- id_estudio -->
    <!-- tipo -->
    <!-- cod_estudio -->
    <!-- abreviatura -->
    <!-- UB -->
    <!-- activo -->
    <!-- descripcion -->
    <!-- denominación -->
    
    <!------------------------------------------------------------------------------------------->
    <b-form>
      <b-form-group label="*Codigo del Estudio" label-for="cod_estudio">
        <!-- Numero de Estudio -->
        <b-form-input
          id="cod_estudio"
          v-model="estudio.cod_estudio"
          type="text"
          placeholder="Ingrese el código"
          invalid-feedback="Complete este campo"
          :state="validacion.cod_estudio.estado"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback id="cod_estudio-live-feedback"
          >{{ validacion.cod_estudio.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>

      <b-form-group label="*Tipo" label-for="tipo">
        <b-form-select
          id="tipo"
          v-model="estudio.tipo"
          type="text"
          placeholder="Ingrese un tipo"
          invalid-feedback="Complete este campo"
          :state="validacion.tipo.estado"
          required
          :options="op_tipo"
        >
        </b-form-select>
        <b-form-invalid-feedback id="tipo-live-feedback"
          >{{ validacion.tipo.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>

      <b-form-group label="*Abreviatura" label-for="abreviatura">
        <b-form-input
          id="abreviatura"
          v-model="estudio.abreviatura"
          :state="validacion.abreviatura.estado"
          type="text"
          placeholder="*Ingrese una abreviatura"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback id="abreviatura-live-feedback"
          >{{ validacion.abreviatura.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>
      
      
      <b-form-group label="*Descripción" label-for="descripcion">
        <b-form-input
          id="descripcion"
          v-model="estudio.descripcion"
          :state="validacion.descripcion.estado"
          type="text"
          placeholder="*Ingrese una descripcion"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback id="descripcion-live-feedback"
          >{{ validacion.descripcion.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>


      <b-form-group label="*Denominación" label-for="denominación">
        <b-form-input
          id="denominación"
          v-model="estudio.denominación"
          :state="validacion.denominación.estado"
          type="text"
          placeholder="*Ingrese una denominación"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback id="denominación-live-feedback"
          >{{ validacion.denominación.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>


      <!-- Unidad Bioquimica -->
      <b-form-group label="*U.B." label-for="ub"
      v-show="this.estudio.tipo=='Analisis bioquimico'">
        <b-form-input
          id="ub"
          v-model="estudio.ub"
          :state="validacion.ub.estado"
          type="decimal"
          placeholder="Ingrese la U.B. correspondiente al estudio "
          invalid-feedback="Complete este campo"
          
        >
        </b-form-input>
        <b-form-invalid-feedback id="ub-live-feedback"
          >{{ validacion.ub.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>
    </b-form>
    <b-button class="mt-2" variant="success" block @click="putEstudio()"
      >Modificar</b-button
    >
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";
import axios from "axios";

export default {

  props: {
    estudio: {},
  },
  data() {
    return {
      
      data: {},
      
      op_tipo: [{ value: null, text: "Elija un tipo", disabled: true },
        { value:"Oftalmologia", text: "1- Oftalmología"},
        { value:"Optica", text: "2- Óptica"},
        { value:"Analisis bioquimico", text: "3- Análisis bioquímico"},
        { value:"Odontologia", text: "4- Odontología"},
        { value:"Diag. Imagenes", text: "5- Diag. Imágenes"},],


      
      validacion: {
        tipo: { estado: null, mensaje: "" },
        cod_estudio: { estado: null, mensaje: "" },
        abreviatura: { estado: null, mensaje: "" },
        ub: { estado: null, mensaje: "" },
        descripcion: { estado: null, mensaje: "" },
        denominación: { estado: null, mensaje: "" },
      },
      
      respuesta: null,
    };
  },

  methods: {
    
    async getEstudios() {
      let estudioAPI = new APIControler();
      this.data = await estudioAPI.getData();
    },
    async putEstudio() {
      let respuesta ="vacio"
      await axios.put("http://localhost:8081/estudios/"+this.estudio.id_estudio+ '/', this.estudio)
      .then(function (data){
        swal("Operación Exitosa", " ", "success");
      })
      .catch(function (error) {
        swal("¡ERROR!", "Se ha detectado un problema ", "error");
        respuesta=error.response.data;
      })
      this.cargarFeedback(respuesta)
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