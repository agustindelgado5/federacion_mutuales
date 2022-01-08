<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Registrar nueva gasto saliente: </h4>

    <!-- CAMPOS REQUERIDOS -->
    <!-- id_gasto -->
    <!-- nro_ticket -->
    <!-- descripcion -->
    <!-- total -->
    <!-- fecha -->

    <!------------------------------------------------------------------------------------------->

    <b-form >
        <!-- nro_ticket -->
        <b-form-group label="*Numero de Ticket" label-for="nro_ticket" @submit.stop.prevent="handleSubmit">
            <b-form-input
            id="nro_ticket"
            v-model="gastoSaliente.nro_ticket"
            type="number"
            placeholder="Ingrese el numero del ticket"
            :state="validacion.nro_ticket.estado"
            invalid-feedback="Complete este campo"
            required
            >
            </b-form-input>
            <b-form-invalid-feedback
                id="nro_ticket-live-feedback"
              >{{validacion.nro_ticket.mensaje}}
            </b-form-invalid-feedback>
        </b-form-group>

      <!-- descripcion -->
      <b-form-group label="*Descripcion" label-for="descripcion">
        <b-form-input
          id="descripcion"
          v-model="gastoSaliente.descripcion"
          type="text"
          placeholder="*Ingrese la descripcion del gasto"
          :state="validacion.descripcion.estado"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback
                id="descripcion-live-feedback"
              >{{validacion.descripcion.mensaje}}
            </b-form-invalid-feedback>
      </b-form-group>

      <!-- total -->
        <b-form-group label="*Total" label-for="total" @submit.stop.prevent="handleSubmit">
          <b-form-input 
            id="total"
            v-model="gastoSaliente.total"
            type="number"
            :state="validacion.total.estado"
            placeholder="Ingrese el total del gasto"
            invalid-feedback="Complete este campo"
            required>
          </b-form-input>
          <b-form-invalid-feedback id="total-live-feedback">
              {{validacion.total.mensaje}}
          </b-form-invalid-feedback>
        </b-form-group>

      <!-- fecha -->
      <b-form-group label="*Fecha" label-for="fecha">
        <b-form-input
          id="fecha"
          v-model="gastoSaliente.fecha"
          type="date"
          placeholder="Ingrese una fecha"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback id="fecha-live-feedback">
              {{validacion.fecha.mensaje}}
          </b-form-invalid-feedback>
      </b-form-group>

      
    </b-form>
    <b-button class="mt-2" variant="success" block @click="postGastosSalientes()">Guardar</b-button>
  </div>
</template>

<script>
import { APIControler } from "@/store/APIControler";

export default {
  data() {
    return {
      gastoSaliente: {},
      data: {},
      validacion:{
        nro_ticket: {estado:null,mensaje:""},
        descripcion: {estado:null,mensaje:""},
        total: {estado:null,mensaje:""},
        fecha: {estado:null,mensaje:""},
      }
    };
  },
  methods: {
    async getGastosSalientes() {
      let gastoSalienteAPI = new APIControler();
      this.data = await gastoSalienteAPI.getData();
    },
    async postGastosSalientes() {
      let gastoSalienteAPI = new APIControler();
      gastoSalienteAPI.apiUrl.pathname='gastosSalientes/';
      let respuesta = await gastoSalienteAPI.postData(this.gastoSaliente); 
      this.cargarFeedback(respuesta)
    },

    cargarFeedback(respuestaAPI){
      for(let key in this.validacion){
        this.validacion[key].estado=true
      }
      for(let key in respuestaAPI){
        this.validacion[key].estado=false
        this.validacion[key].mensaje=respuestaAPI[key][0]
        
      }
    }
  },
};
</script>

<style>
</style>