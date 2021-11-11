<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Nuevo Venta :</h4>

    <!-- CAMPOS REQUERIDOS -->
    <!-- codigo_seguimiento -->
    <!-- nro de socio-->
  
    
    <!------------------------------------------------------------------------------------------->
    <b-form>
      <b-form-group label="*Codigo Seguimiento" label-for="codigo_seguimiento">
        <!-- codigo_optica -->
        <b-form-input
          id="codigo_seguimiento"
          v-model="ventaOptica.codigo_seguimiento"
          type="text"
          placeholder="Ingrese el código"
          invalid-feedback="Complete este campo"
          :state="validacion.codigo_seguimiento.estado"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback id="codigo_seguimiento-live-feedback"
          >{{ validacion.codigo_seguimiento.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>

      

      <b-form-group label="*Socio" label-for="numero_socio">
        <b-form-select
          id="numero_socio"
          v-model="ventaOptica.numero_socio"
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


    </b-form>
    <b-button class="mt-2" variant="success" block @click="postVentaOptica()"
      >Guardar</b-button
    >
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";

export default {
  data() {
    return {
      list_socios:{},
      ventaOptica: {},
      data: {},
      op_socios: [
        {value: null, text: 'Elija un socio', disabled: true},
      ],

      validacion: {
       
        codigo_seguimiento: { estado: null, mensaje: "" },
        numero_socio: { estado: null, mensaje: "" },
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
    
    async getVentasOptica() {
      let  ventaOpticaAPI = new APIControler();
      this.data = await  ventaOpticaAPI.getData();
    },
    async postVentaOptica() {
      let ventaOpticaAPI = new APIControler();
      ventaOpticaAPI.apiUrl.pathname = "ventasOpticas/";
      this.respuesta = await ventaOpticaAPI.postData(this.ventaOptica);
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
   beforeMount(){
    this.getSocios();
  },
};
</script>

<style>

</style>