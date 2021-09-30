<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Nueva Cirugia:</h4>

    <!-- CAMPOS REQUERIDOS -->
    <!-- codigo_intervencion -->
    <!-- descrpcion-->
    <!--nivel-->
    <!--numero de ayudantes-->
    <!--honorarios cirujano-->
    <!--honorarios ayudante-->
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
      
      
      
        <b-form-group label="*Nivel" label-for="nivel">
        <b-form-input
          id="nivel"
          v-model="cirugia.nivel"
          :state="validacion.nivel.estado"
          type="number"
          placeholder="*Ingrese una observacion"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback id="nivel-live-feedback"
          >{{ validacion.nivel.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>

       <b-form-group label="*Numero de ayudantes" label-for="numero_ayudantes">
        <b-form-input
          id="numero_ayudantes"
          v-model="cirugia.numero_ayudantes"
          :state="validacion.numero_ayudantes.estado"
          type="number"
          placeholder="*Ingrese el numero de ayudantes"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback id="numero_ayudantes-live-feedback"
          >{{ validacion.numero_ayudantes.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>

      <b-form-group label="*Honorarios Cirujanos" label-for="honorario_cirujano">
        <b-form-input
          id="honorario_cirujano"
          v-model="cirugia.honorario_cirujano"
          :state="validacion.honorario_cirujano.estado"
          type="text"
          placeholder="*Ingrese el honorario del cirujano "
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback id="honorario-live-feedback"
          >{{ validacion.honorario_cirujano.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>

      <b-form-group label="*Honorarios ayudantes" label-for="honorario_ayudante">
        <b-form-input
          id="honorario_ayudante"
          v-model="cirugia.honorario_ayudante"
          :state="validacion.honorario_ayudante.estado"
          type="text"
          placeholder="*Ingrese el honorario del ayudante"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback id="honorario_ayudante-live-feedback"
          >{{ validacion.honorario_ayudante.mensaje }}
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
        nivel: { estado: null, mensaje: "" },
        numero_ayudantes: { estado: null, mensaje: "" },
        honorario_cirujano: { estado: null, mensaje: "" },
        honorario_ayudante: { estado: null, mensaje: "" },
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