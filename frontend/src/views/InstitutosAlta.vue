<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Nuevo Instituto:</h4>

    <!-- CAMPOS REQUERIDOS -->
    <!-- codigo_instituto -->
    
    
    <!------------------------------------------------------------------------------------------->

    <b-form>
      <b-form-group label="*Codigo de instituto" label-for="codigo_institucion">
        <!-- codigo_institucion -->
        <b-form-input
          id="codigo_institucion"
          v-model="instituto.codigo_institucion"
          type="text"
          placeholder="Ingrese el código"
          invalid-feedback="Complete este campo"
          :state="validacion.codigo_institucion.estado"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback id="codigo_institucion-live-feedback"
          >{{ validacion.codigo_institucion.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>
      <b-form-group label="*Profesional" label-for="id_medico"  @submit.stop.prevent="handleSubmit">
        <b-form-select
          id="id_medico"
          v-model="instituto.id_medico"
          :state="validacion.id_medico.estado"
          type="text"
          placeholder="Ingrese un Numero"
          invalid-feedback="Complete este campo"
          required
          :options="op_profesionales"
        >
        </b-form-select>
        <b-form-invalid-feedback
                id="id_medico-live-feedback"
              >{{validacion.id_medico.mensaje}}
            </b-form-invalid-feedback>
      </b-form-group>

      

     

    </b-form>
    <b-button class="mt-2" variant="success" block @click="postInstituto()"
      >Guardar</b-button
    >
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";

export default {
  data() {
    return {
      list_profesionales:{},
      instituto: {},
      data: {},
       op_profesionales: [
        {value: null, text: 'Elija un profesional', disabled: true},
      ],
      validacion: {
        id_medico:{estado:null,mensaje:""},
        codigo_institucion: { estado: null, mensaje: "" },
        
      },
      
      respuesta: null,
    };
  },

  methods: {
    
    async getProfesionales() {
      let profesionalAPI = new APIControler();
      profesionalAPI.apiUrl.pathname='profesionales/';
      this.data = await profesionalAPI.getData(this.list_profesionales);
      this.data.forEach(element => {   
        let option={}
        option.value='http://localhost:8081/profesionales/'+ element.id_medico +'/';
        option.text= element.id_medico +'-- '+ element.apellido +', '+ element.nombre ;
        console.log(option);
        this.op_socios.push(option);
        
      });
    },
    
    async getInstitutos() {
      let  institutoAPI = new APIControler();
      this.data = await  institutoAPI.getData();
    },
    async postInstituto() {
      let institutoAPI = new APIControler();
      institutoAPI.apiUrl.pathname = "institutos/";
      this.respuesta = await institutoAPI.postData(this.instituto);
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
    this.getProfesionales();
  },
};
</script>

<style>

</style>