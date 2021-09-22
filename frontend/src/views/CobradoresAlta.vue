<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Datos </h4>   
    
      
     <b-form-group label="*Socio" label-for="numero_socio"  @submit.stop.prevent="handleSubmit">
        <b-form-select
          id="numero_socio"
          v-model="Cobradores.numero_socio"
          :state="validacion.numero_socio.estado"
          type="text"
          placeholder="Ingrese un Numero"
          invalid-feedback="Complete este campo"
          required
          :options="op_socios"
        >
        </b-form-select>
        <b-form-invalid-feedback
                id="numero_socio-live-feedback"
              >{{validacion.numero_socio.mensaje}}
            </b-form-invalid-feedback>
      </b-form-group>
   
    <b-form >
       <b-form-group label="*ID Cobrador" label-for="id_cobrador" @submit.stop.prevent="handleSubmit">
        <b-form-input
          id="id_cobrador"
          v-model="Cobradores.id_cobrador"
          :state="validacion.id_cobrador.estado"
          type="number"
          placeholder="Ingrese un Numero"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
         <b-form-invalid-feedback
                id="id_cobrador-live-feedback"
              >{{validacion.id_cobrador.mensaje}}
            </b-form-invalid-feedback>
     </b-form-group>

      <b-form-group label="*Nombre/s" label-for="nombre" @submit.stop.prevent="handleSubmit">
        <b-form-input
          id="nombre"
          v-model="Cobradores.nombre"
          type="text"
          placeholder="*Ingrese los Nombre/s"
          :state="validacion.nombre.estado"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback
                id="nombre-live-feedback"
              >{{validacion.nombre.mensaje}}
            </b-form-invalid-feedback>
      </b-form-group>
       <b-form-group label="*Apellido/s" label-for="apellido" @submit.stop.prevent="handleSubmit">
        <b-form-input
          id="apellido"
          v-model="Cobradores.apellido"
          type="text"
          placeholder="*Ingrese los Apellido/s"
          :state="validacion.apellido.estado"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
         <b-form-invalid-feedback
                id="apellido-live-feedback"
              >{{validacion.apellido.mensaje}}
            </b-form-invalid-feedback>
      </b-form-group>
      <b-form-group label="*DNI" label-for="dni" @submit.stop.prevent="handleSubmit">
        <b-form-input
          id="dni"
          v-model="Cobradores.dni"
          type="number"
          placeholder="Ingrese un DNI"
          :state="validacion.dni.estado"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback
            id="dni-live-feedback"
          >{{validacion.dni.mensaje}}
        </b-form-invalid-feedback>
      </b-form-group>

      
       <b-form-group label="*Fecha de cobro" label-for="fecha_cobro" @submit.stop.prevent="handleSubmit">
        <b-form-input
          id="fecha_cobro"
          v-model="Cobradores.fecha_cobro"
          type="date"
          placeholder="Ingrese una fecha"
          :state="validacion.fecha_cobro.estado"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
         <b-form-invalid-feedback
                id="fecha_cobro-live-feedback"
              >{{validacion.fecha_cobro.mensaje}}
          </b-form-invalid-feedback>
      </b-form-group>
    
    </b-form>
    <b-button class="mt-2" variant="success" block @click="postCobrador()">Enviar</b-button>
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";

export default {
  data() {
    return {
      list_socios:{},
      Cobradores: {},
      data: {},
      op_socios: [
        {value: null, text: 'Elija un socio', disabled: true},
      ],
      validacion:{
      numero_socio:{estado:null,mensaje:""},
      id_cobrador: {estado:null,mensaje:""},
      nombre: {estado:null,mensaje:""},
      apellido: {estado:null,mensaje:""},
      dni: {estado:null,mensaje:""},
      fecha_cobro: {estado:null,mensaje:""},
        
      }
    };
  },
  methods: {

    async getSocios() {
      let socioAPI = new APIControler();
      socioAPI.apiUrl.pathname='socios/';
      this.data = await socioAPI.getData(this.list_socios);
      this.data.forEach(element => {   
        let option={}
        option.value='http://localhost:8081/socios/'+ element.numero_socio +'/';
        option.text= element.numero_socio +'-- '+ element.apellido +', '+ element.nombre ;
        console.log(option);
        this.op_socios.push(option);
        
      });
    },

    async getCobrador() {
      let cobradorAPI = new APIControler();
      this.data = await cobradorAPI.getData();
    },
    async postCobrador() {
      let cobradorAPI = new APIControler();
      cobradorAPI.apiUrl.pathname='cobradores/'
      this.data = await cobradorAPI.postData(this.Cobradores);
    },
  },
   beforeMount(){
    this.getSocios();
  },

};

</script>

<style>
</style>