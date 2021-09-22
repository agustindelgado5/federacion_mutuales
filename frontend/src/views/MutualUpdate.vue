<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    

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
          v-model="mutual.nombre"
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
          v-model="mutual.sucursal"
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

    <b-button class="mt-2" variant="success" block @click="putMutual()">Modificar</b-button
    >
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";
import axios from "axios";

export default {
  props: {
    mutual: {},
  },
  data() {
    return {
      mutuales: {},
      data: {},
      key_mutual: this.mutual.id_mutual,
      key_serv_mutual:[],
      
      selected:[],
      selected_anterior:[],
      new_selected: [],
      list_servicios: {},
      op_servicios: [
        { value: null, text: "Elija un servicio", disabled: true },
      ],
      
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
      validacion: {
        nombre: { estado: null, mensaje: "" },
        sucursal: { estado: null, mensaje: "" },
        id_servicio: { estado: null, mensaje: "" },
      },
    };
  },
  

  methods: {
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

    //Obtengo los servicios
    async getOpcionesSelected() {
      let opcionesAPI = new APIControler();
      opcionesAPI.apiUrl.pathname = "servicio_mutual/";
      this.data = await opcionesAPI.getData(this.list_servicios);
      this.data.forEach((element) => {
        
        if(element.id_mutual == 'http://localhost:8081/mutuales/'+this.mutual.id_mutual+'/')
          this.key_serv_mutual.push(element.id_serv_mut);
          this.selected.push(element.id_servicio);
          
      });
      this.selected_anterior = this.selected;
      
      //this.new_selected=  this.selected + this.selected_anterior;
    },

    async putMutual() {
      let respuesta ="vacio"
      var id = this.mutual.id_mutual
      try{ 
        this.mutual=await axios.put('http://localhost:8081/mutuales/'+id+ '/', this.mutual)
        swal("Operación Exitosa", " ", "success");
        console.log(this.mutual);
        this.putServicios();
      }
      catch(error) {
        swal("¡ERROR!", "Se ha detectado un problema ", "error");
        console.log(error);
        //respuesta=error.response.data;
        
      }
      //this.cargarFeedback(respuesta)
      console.log("respuesta:");
      console.log(respuesta);
    },

    async putServicios(){
      this.new_selected = this.selected.filter(x => !this.selected_anterior[x]);
      console.log(this.new_selected)
      console.log('****ID: ', this.key_mutual)
      for(var i=0; i<this.selected.length; i++){
        
        if(this.estaCargado(i)!=false){
          this.PostServicio(i);
        }
        else{
          this.DeleteServicio(i);
        } 
      }
    },
    //Me fijo si el servicio ya esta cargado
    async estaCargado(i) {
      let valor=false
      try{
        axios
        .get('http://localhost:8081/servicio_mutual/', {
          id_mutual : "http://localhost:8081/mutuales/" + this.key_mutual + "/",
          id_servicio : this.new_selected[i]
        })
        .then(datos=>{
          console.log('¡El Servicio ya se encuentra cargado!')
          valor = true;
        })
      }
      catch(error){
        console.log(error)
        valor=false
      }
      return valor;
    },
    //Hago un post de un nuevo servicio
    async PostServicio(i) {
      try{
        axios
        .post('http://localhost:8081/servicio_mutual/', {
          id_mutual : "http://localhost:8081/mutuales/" + this.key_mutual + "/",
          id_servicio : this.new_selected[i]
        })
       
        console.log('¡Servicios cargados con exito!')
      }
      catch(error){
        console.log(error)
      } 
    },
    //Hago una eliminacion de un registro
    async DeleteServicio(i) {
      try{
        axios
        .delete('http://localhost:8081/servicio_mutual/'+this.key_serv_mutual[i]+'/')
        console.log(data)
        console.log('¡Servicio eliminado con exito!')
      }
      catch(error){
        console.log(error)
      } 
    },

    cargarFeedback() {
      let valido;
      for(let key in this.validacion){
        valido=!(respuestaAPI.hasOwnProperty(key))
        this.validacion[key].estado=valido
        console.log(key)

      if (!valido)
          this.validacion[key].mensaje=respuestaAPI[key][0]
      }
    },

  },
  beforeMount() {
    //this.getID();
    this.getServicios();
    this.getOpcionesSelected();
  },
  
  created(){
    this.putServicios();
  },
};
</script>

<style>
</style>