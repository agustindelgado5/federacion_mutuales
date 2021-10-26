<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Datos </h4>
 
    <b-form>
      <b-form-group label="*ID" >
        <b-form-input
            id="id_medicamento"
            :disabled="true"
            v-model="item_med.id_medicamento"
            type="number"
            placeholder="Ingrese un Numero"
            invalid-feedback="Complete este campo"
            required
        >
        </b-form-input>
      </b-form-group>
      <b-form-group label="*Nombre" >
        <b-form-input
            id="nombre"
            v-model="item_med.nombre"
            type="text"
            placeholder="Ingrese el nombre"
            invalid-feedback="Complete este campo"
            required
        >
        </b-form-input>
      </b-form-group>
      
      <b-form-group label="*Presentacion" >
        <b-form-textarea
          id="presentacion"
          v-model="item_med.presentacion"
          type="text"
          placeholder="Describa la presentacion"
          invalid-feedback="Complete este campo"
          required
          rows="3"
          max-rows="6"
        >
        </b-form-textarea>
      </b-form-group>
      <b-form-group label="*Laboratorio">
        <b-form-input
            id="laboratorio"
            v-model="item_med.laboratorio"
            type="text"
            placeholder="Ingrese el nombre"
            invalid-feedback="Complete este campo"
            required
        >
        </b-form-input>
      </b-form-group>
      
      <b-form-group label="*Farmacia">
        <b-form-select
            id="cod_farmacia"
            v-model="item_med.cod_farmacia"
            type="text"
            placeholder="Ingrese un Numero"
            invalid-feedback="Complete este campo"
            required
            :options="options"
        >
        </b-form-select>
      </b-form-group>
    </b-form>
    
    <b-button class="mt-2" variant="success" block @click="putMedicamento()">Guardar</b-button>
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";
import axios from "axios";

export default {
  props: {
    item_med: {},
  },
  data() {
    return {
      //medicamentos: {},
      farmacias:{},
      data: {},
      options: [
        {value: null, text: 'Elija una farmacia', disabled: true},
      ]
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
    
    async putMedicamento() {
      try{
        this.item_med= await axios.put('http://localhost:8081/medicamentos/'+this.item_med.id_medicamento+ '/', this.item_med)
        swal("Operación Exitosa", " ", "success");
        console.log(this.item_med);
      }
      catch(error) {
          swal("¡ERROR!", "Se ha detectado un problema ", "error");
          console.log(error);
      }
      finally{location.href = '/medicamentos'} ;
    },
  },
};
</script>

<style>
</style>