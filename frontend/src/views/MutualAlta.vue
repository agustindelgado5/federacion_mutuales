<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Registrar nueva Mutual:</h4>

    <!-- CAMPOS REQUERIDOS -->
    <!-- nombre -->
    <!-- sucursal -->
    <!-- id_servicio -->

    <!------------------------------------------------------------------------------------------->

    <!-- nombre -->
    <b-form>
      <b-form-group label="*Nombre de la mutual" label-for="nombre">
        <b-form-input
          id="nombre"
          v-model="mutuales.nombre"
          type="text"
          placeholder="*Ingrese el Nombre"
          invalid-feedback="Complete este campo"
          required
          :state="validacion.nombre.estado"
        >
        </b-form-input>
        <b-form-invalid-feedback id="nombre-live-feedback"
          >{{ validacion.nombre.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>
      <!-- sucursal -->

      <b-form-group label="*Sucursal" label-for="sucursal">
        <b-form-select
          id="sucursal"
          v-model="mutuales.sucursal"
          type="text"
          placeholder="Ingrese una sucursal"
          invalid-feedback="Complete este campo"
          :state="validacion.sucursal.estado"
          :options="options"
          required
        >
        </b-form-select>
        <b-form-invalid-feedback id="sucursal-live-feedback"
          >{{ validacion.sucursal.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>
      
      <b-form-group
        label="*Servicio" label-for="servicio"
        v-slot="{ ariaDescribedby }"
      >
        <b-form-checkbox-group
          v-model="selected"
          :options="op_servicios"
          :aria-describedby="ariaDescribedby"
          name="flavour-2a"
          stacked
        ></b-form-checkbox-group>
    </b-form-group>
    </b-form>
    
    <b-button class="mt-2" variant="success" block @click="postMutual()"><b>GUARDAR</b></b-button
    >
  </div>
</template>

<script>
import axios from 'axios';
import { APIControler } from "../store/APIControler";

export default {

  data() {
    return {
      mutuales: {},
      mutuales_anteriores: {},
      index:[],
      maximo: 0,
      data: {},
      list_servicios: {},
      op_servicios: [
        { value: null, text: "Elija los servicios", disabled: true },
      ],
      selected: [],
      validacion: {
        nombre: { estado: null, mensaje: "" },
        sucursal: { estado: null, mensaje: "" },
        id_servicio: { estado: null, mensaje: "" },
      },
      respuesta: null,
      options: [
        { value: null, text: "Elija un departamento" },
        { value: "Burruyacú", text: "1- Burruyacú" },
        { value: "Capital", text: "2- Capital" },
        { value: "Chicligasta", text: "3- Chicligasta" },
        { value: "Cruz Alta", text: "4- Cruz Alta" },
        { value: "Famaillá", text: "5- Famaillá" },
        { value: "Graneros", text: "6- Graneros" },
        { value: "Juan Bautista Alberdi", text: "7- Juan Bautista Alberdi" },
        { value: "La Cocha", text: "8- La Cocha" },
        { value: "Leales", text: "9- Leales" },
        { value: "Lules", text: "10- Lules" },
        { value: "Monteros", text: "11- Monteros" },
        { value: "Río Chico", text: "12- Río Chico" },
        { value: "Simoca", text: "13- Simoca" },
        { value: "Tafí del Valle", text: "14- Tafí del Valle" },
        { value: "Tafí Viejo", text: "15- Tafí Viejo" },
        { value: "Trancas", text: "16- Trancas" },
        { value: "Yerba Buena", text: "17- Yerba Buena" },
      ],
      /*
      servers_mutual: {
        id_mutual : '',
        id_servicio : '',
      }
      */
    };
  },
  methods: {
    //Obtengo la mutual
    
    async getMutuales() {
      let mutualesAPI = new APIControler();
      mutualesAPI.apiUrl.pathname = "mutuales/";
      this.data = await mutualesAPI.getData(this.mutuales_anteriores);
      
      this.data.forEach((element) => {
        this.index.push(element.id_mutual)
        
      });
      
    },
    

    //Post de la mutual
    async postMutual() {
      let mutualAPI = new APIControler();
      mutualAPI.apiUrl.pathname = "mutuales/";
      if (this.selected.length>0) {
        this.respuesta = await mutualAPI.postData(this.mutuales);
        this.postServicios();
        this.cargarFeedback();
        this.testFetch();
      }
      else{
        swal("¡ERROR!", "Debe seleccionar al menos un servicio", "error");
      }
    },

    //Obtengo los servicios
    async getServicios() {
      let serviciosAPI = new APIControler();
      serviciosAPI.apiUrl.pathname = "servicios/";
      this.data = await serviciosAPI.getData(this.list_servicios);
      this.data.forEach((element) => {
        let option = {};
        option.value = "http://localhost:8081/servicios/" + element.id_servicio + "/";
        option.text = element.servicio;
        console.log(option);
        this.op_servicios.push(option);
      });
    },
  

    //Cargo los servicios de las mutuales
    async postServicios(){
      var id=1
      this.maximo = this.index.length-1 
      if (this.index[this.maximo]!=null) {
        id = this.index[this.maximo]+1; 
      }
      console.log('ID:', id);

      for(var i=0; i<this.selected.length; i++){
        
        axios
        .post('http://localhost:8081/servicio_mutual/', {
          id_mutual : "http://localhost:8081/mutuales/" + id + "/",
          id_servicio : this.selected[i]
        })
        .then(data=>{
          console.log(data)
          console.log('¡Servicios cargados con exito!')
        })
        .catch(error=>{
          console.log(error)
        })   
      }
      
    },
    //Validacion de los campos
    cargarFeedback() {
      let valido;
      for (let key in this.validacion) {
        valido = !this.respuesta.hasOwnProperty(key);
        this.validacion[key].estado = valido;
        if (!valido) this.validacion[key].mensaje = this.respuesta[key][0];
      }
    },
  },
  beforeMount() {
    this.getServicios();
  },
  created(){
    this.getMutuales();
    this.postServicios();
  },
  computed: {
    
  }

};
</script>

<style>
</style>