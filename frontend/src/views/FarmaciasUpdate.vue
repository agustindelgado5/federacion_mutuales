<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Datos </h4>
 
    <b-form>
      <b-form-group label="*ID Farmacia" label-for="cod_farmacia" @submit.stop.prevent="handleSubmit">
            <b-form-input
            id="cod_farmacia"
            v-model="farmacia.cod_farmacia"
            :state="validacion.cod_farmacia.estado"
            :disabled="true"
            type="number"
            placeholder="Ingrese el ID de la farmacia"
            invalid-feedback="Complete este campo"
            required
            >
            </b-form-input>
            <b-form-invalid-feedback
                id="cod_farmacia-live-feedback"
              >{{validacion.cod_farmacia.mensaje}}
            </b-form-invalid-feedback>
        </b-form-group>

        <!-- matricula_farm -->
        <b-form-group label="*Matricula Farmacia" label-for="matricula_farm" @submit.stop.prevent="handleSubmit">
            <b-form-input
            id="matricula_farm"
            v-model="farmacia.matricula_farm"
            type="number"
            placeholder="Ingrese la matricula de la farmacia"
            :state="validacion.matricula_farm.estado"
            invalid-feedback="Complete este campo"
            required
            >
            </b-form-input>
            <b-form-invalid-feedback
                id="matricula_farm-live-feedback"
              >{{validacion.matricula_farm.mensaje}}
            </b-form-invalid-feedback>
        </b-form-group>

      <!-- farmacia -->
      <b-form-group label="*Farmacia" label-for="farmacia">
        <b-form-input
          id="farmacia"
          v-model="farmacia.farmacia"
          type="text"
          placeholder="*Ingrese el nombre de la farmacia"
          :state="validacion.farmacia.estado"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback
                id="farmacia-live-feedback"
              >{{validacion.farmacia.mensaje}}
            </b-form-invalid-feedback>
      </b-form-group>

      <!-- cuit -->
        <b-form-group label="*CUIT Farmacia" label-for="cuit" @submit.stop.prevent="handleSubmit">
            <b-form-input
            id="cuit"
            v-model="farmacia.cuit"
            type="number"
            placeholder="Ingrese el CUIT de la farmacia"
            :state="validacion.cuit.estado"
            invalid-feedback="Complete este campo"
            required
            >
            </b-form-input>
          <b-form-invalid-feedback
                id="cuit-live-feedback"
              >{{validacion.cuit.mensaje}}
          </b-form-invalid-feedback>
        </b-form-group>

      <!-- localidad -->
      <b-form-group label="*Localidad" label-for="localidad">
        <b-form-input
          id="localidad"
          v-model="farmacia.localidad"
          type="text"
          placeholder="*Ingrese la localidad"
          :state="validacion.localidad.estado"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback
                id="localidad-live-feedback"
              >{{validacion.localidad.mensaje}}
          </b-form-invalid-feedback>
      </b-form-group>

      <!-- direccion -->
      <b-form-group label="*Direccion" label-for="direccion">
        <b-form-input
          id="direccion"
          v-model="farmacia.direccion"
          type="text"
          placeholder="*Ingrese la direccion"
          :state="validacion.direccion.estado"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback
                id="direccion-live-feedback"
              >{{validacion.direccion.mensaje}}
          </b-form-invalid-feedback>
      </b-form-group>

      <!-- cod_postal -->
        <b-form-group label="*Codigo postal" label-for="cod_postal" @submit.stop.prevent="handleSubmit">
            <b-form-input
            id="cod_postal"
            v-model="farmacia.cod_postal"
            type="number"
            placeholder="Ingrese el codigo postal"
            :state="validacion.cod_postal.estado"
            invalid-feedback="Complete este campo"
            required
            >
            </b-form-input>
            <b-form-invalid-feedback
                id="cod_postal-live-feedback"
              >{{validacion.cod_postal.mensaje}}
          </b-form-invalid-feedback>
        </b-form-group>

     <!-- email -->
     <b-form-group label="*Email" label-for="email">
        <b-form-input
          id="email"
          v-model="farmacia.email"
          type="email"
          placeholder="Ingrese un email"
          :state="validacion.email.estado"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback
                id="email-live-feedback"
              >{{validacion.email.mensaje}}
          </b-form-invalid-feedback>
      </b-form-group> 

    <!-- tel_fijo -->
    <b-form-group label="Telefono fijo" label-for="tel_fijo">
        <b-form-input
          id="tel_fijo"
          v-model="farmacia.tel_fijo"
          type="number"
          placeholder="Ingrese un numero de telefono fijo"
          :state="validacion.tel_fijo.estado"
        >
        </b-form-input>
        <b-form-invalid-feedback
                id="tel_fijo-live-feedback"
              >{{validacion.tel_fijo.mensaje}}
          </b-form-invalid-feedback>
    </b-form-group>

    <!-- tel_celular -->
    <b-form-group label="Telefono Celular" label-for="tel_celular">
        <b-form-input
          id="tel_celular"
          v-model="farmacia.tel_celular"
          type="number"
          placeholder="Ingrese un numero de telefono celular"
          :state="validacion.tel_celular.estado"
        >
        </b-form-input>
        <b-form-invalid-feedback
                id="tel_celular-live-feedback"
              >{{validacion.tel_celular.mensaje}}
          </b-form-invalid-feedback>
      </b-form-group>

    <!-- representante -->
    <b-form-group label="*Representante" label-for="representante">
        <b-form-input
          id="representante"
          v-model="farmacia.representante"
          type="text"
          placeholder="*Ingrese el nombre del representante"
          invalid-feedback="Complete este campo"
          :state="validacion.representante.estado"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback
                id="representante-live-feedback"
              >{{validacion.representante.mensaje}}
          </b-form-invalid-feedback>
    </b-form-group>
    </b-form>
    
    
    <!-- {{farmacia}}
    <br>
    <br>
    {{ data }} -->
    
    <b-button class="mt-2" variant="success" block @click="putFarmacia()">Modificar</b-button>
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";
import axios from "axios";

export default {
  props: {
    farmacia: {},
  },
  data() {
    return {
      farmacias:{},
      data: {},
      options: [
        {value: null, text: 'Elija una farmacia', disabled: true},
      ],

      validacion:{
        cod_farmacia: {estado:null,mensaje:""},
        cuit: {estado:null,mensaje:""},
        farmacia: {estado:null,mensaje:""},
        direccion: {estado:null,mensaje:""},
        localidad: {estado:null,mensaje:""},
        email: {estado:null,mensaje:""},
        cod_postal: {estado:null,mensaje:""},
        tel_fijo: {estado:null,mensaje:""},
        tel_celular: {estado:null,mensaje:""},
        matricula_farm: {estado:null,mensaje:""},
        representante: {estado:null,mensaje:""},
      }
    };
  },
  created: function() {
    //console.log('Funcion realizada');
    this.getFarmacias();
  }
  ,
  methods: {
    async getFarmacias() {
      let farmaciaAPI = new APIControler();
      farmaciaAPI.apiUrl.pathname='farmacias/'
      this.data = await farmaciaAPI.getData(this.farmacias);
      this.data.forEach(element => {   
        let option={}
        option.value='http://localhost:8081/farmacias/'+ element.cod_farmacia +'/';
        option.text=element.farmacia;
        console.log(option);
        this.options.push(option);
      });
    },
    
    async putFarmacia() {
      let respuesta ="vacio"
      // try{
      await axios.put('http://localhost:8081/farmacias/'+this.farmacia.cod_farmacia+ '/', this.farmacia)
      .then(function (data){
        
        swal("Operación Exitosa", " ", "success");
      })
      .catch(function (error) {
        swal("¡ERROR!", "Se ha detectado un problema ", "error");
        respuesta=error.response.data;
        
        //console.log(error.response.data);
      })
      this.cargarFeedback(respuesta)
      //this.farmacia= await axios.put('http://localhost:8081/farmacias/'+this.farmacia.cod_farmacia+ '/', this.farmacia)
      console.log("respuesta:");
      console.log(respuesta);
        
      // }
      // catch(error) {
          
      //     console.log("error:");
      //     console.log(error.response);
      // }
      //finally{location.href = '/farmacias'} ;
    },
    cargarFeedback(respuestaAPI){
      console.log("respuestaAPI")
      console.log(respuestaAPI)
      let valido;
      for(let key in this.validacion){
        valido=!(respuestaAPI.hasOwnProperty(key))
        this.validacion[key].estado=valido
        console.log(key)

        if (!valido)
          this.validacion[key].mensaje=respuestaAPI[key][0]
      }
    }
  },
};
</script>

<style>
</style>