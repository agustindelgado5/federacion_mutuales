<template>
  <div class="accordion" role="tablist">
    
    <h6>Los campos en (*) son obligatorios</h6>
    
    <b-form>
      <b-card no-body class="mb-1">
        <b-card-header header-tag="header" class="p-1" role="tab">
          <b-button block v-b-toggle.accordion-1 style="background-color:darkorange;">Datos Personales:</b-button>
        </b-card-header>
        <b-collapse id="accordion-1" visible accordion="my-accordion" role="tabpanel">
          <b-card-body>
            <b-form-group label="*N° Socio" label-for="numero_socio">
              <b-form-input
              id="numero_socio"
              :disabled=true
              v-model="socio.numero_socio"
              type="number"
              placeholder="Ingrese un Numero"
              invalid-feedback="Complete este campo"
              required
              >
              </b-form-input>
            </b-form-group>
            <b-form-group label="*Nombre/s" label-for="nombre">
              <b-form-input
                id="nombre"
                v-model="socio.nombre"
                type="text"
                placeholder="*Ingrese los Nombre/s"
                invalid-feedback="Complete este campo"
                required
              >
              </b-form-input>
            </b-form-group>
            <b-form-group label="*Apellido/s" label-for="apellido">
              <b-form-input
                id="apellido"
                v-model="socio.apellido"
                type="text"
                placeholder="*Ingrese los Apellido/s"
                invalid-feedback="Complete este campo"
                required
              >
              </b-form-input>
          </b-form-group>
          <b-form-group label="*DNI" label-for="dni">
            <b-form-input
              id="dni"
              v-model="socio.dni"
              type="number"
              placeholder="Ingrese un DNI"
              invalid-feedback="Complete este campo"
              required
            >
            </b-form-input>
          </b-form-group>

          <b-form-group label="*Fecha de nacimiento" label-for="fecha_nacimiento">
            <b-form-input
              id="fecha_nacimiento"
              v-model="socio.fecha_nacimiento"
              type="date"
              placeholder="Ingrese una fecha"
              invalid-feedback="Complete este campo"
              required
            >
            </b-form-input>
          </b-form-group>
            
        </b-card-body>
      </b-collapse>
    </b-card>

    <b-card no-body class="mb-1">
        <b-card-header header-tag="header" class="p-1" role="tab">
          <b-button block v-b-toggle.accordion-2 style="background-color:darkorange;">Domicilio:</b-button>
        </b-card-header>
        <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
          <b-card-body>
            <b-form-group label="*Calle" label-for="calle">
              <b-form-input
                id="calle"
                v-model="socio.calle"
                type="text"
                placeholder="Ingrese una calle"
                invalid-feedback="Complete este campo"
                required
              >
              </b-form-input>
            </b-form-group>

            <b-form-group label="*Localidad" label-for="localidad">
              <b-form-input
                id="localidad"
                v-model="socio.localidad"
                type="text"
                placeholder="Ingrese una localidad"
                invalid-feedback="Complete este campo"
                required
              >
              </b-form-input>
            </b-form-group>
      

            <b-form-group label="*Departamento" label-for="departamento">
              <b-form-select
                id="departamento"
                v-model="socio.departamento"
                type="text"
                placeholder="Ingrese un departamento"
                invalid-feedback="Complete este campo"
                required
                :options="options"
              >
              </b-form-select>
            </b-form-group>


            <b-form-group label="*Codigo postal" label-for="cod_postal">
              <b-form-input
                id="cod_postal"
                v-model="socio.cod_postal"
                type="number"
                placeholder="Ingrese un numero"
                invalid-feedback="Complete este campo"
                required
              >
              </b-form-input>
            </b-form-group>
          </b-card-body>
      </b-collapse>
    </b-card>

    <b-card no-body class="mb-1">
        <b-card-header header-tag="header" class="p-1" role="tab">
          <b-button block v-b-toggle.accordion-3 style="background-color:darkorange;">Contacto:</b-button>
        </b-card-header>
        <b-collapse id="accordion-3" accordion="my-accordion" role="tabpanel">
          <b-card-body>
            <b-form-group label="*Email" label-for="email">
             <b-form-input
              id="email"
              v-model="socio.email"
              type="email"
              placeholder="Ingrese un email"
              invalid-feedback="Complete este campo"
              required
            >
            </b-form-input>
          </b-form-group>

          <b-form-group label="Telefono fijo" label-for="tel_fijo">
            <b-form-input
              id="tel_fijo"
              v-model="socio.tel_fijo"
              type="number"
              placeholder="Ingrese un numero"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group label="Celular" label-for="tel_celular">
            <b-form-input
              id="tel_celular"
              v-model="socio.tel_celular"
              type="number"
              placeholder="Ingrese un numero"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group label="Carencia" label-for="carencia">
            <b-form-input
              id="carencia"
              v-model="socio.carencia"
              type="date"
              placeholder="Ingrese una fecha"
              invalid-feedback="Complete este campo"
              required
            >
            </b-form-input>
          </b-form-group>
        </b-card-body>
      </b-collapse>
    </b-card>

          
          
      
      
      
      
      
      
      
      <!--
      <h4>Servicios: </h4>
      <b-form-group label="*Servicios" label-for="servicios">
        <div id='plan_servicios'>
          <input type="checkbox" id="salud" value="Salud" v-model="plan">
          <label for="salud">Salud</label>
          <input type="checkbox" id="sepelio" value="Sepelio" v-model="plan">
          <label for="sepelio">Sepelio</label>
          <input type="checkbox" id="optica" value="Optica" v-model="plan">
          <label for="optica">Optica</label>
          <input type="checkbox" id="odontologia" value="Odontologia" v-model="plan">
          <label for="odontologia">Odontologia</label>
          <br>
          <span>Plan de servicios: {{ plan }}</span>
        </div>
      </b-form-group>
    -->
    </b-form>
    

    <!---------------- FAMILIARES ---------------------------->
    <b-button class="mt-2" variant="primary"  @click="sumarFliares()" style="color:white;">¿Agregar adherentes?</b-button>
    <div v-show="btn_familiar" v-for="(item,index) in familiar" :key="item.dni_familiar">
      <b-form>
        <h4>Datos del Adherente: {{index+1}}</h4>
        <!--
        <b-form-group label="*N° Socio">
          <b-form-input
            id="numero_socio"
            v-model="socio.numero_socio"
            type="number"
            placeholder="Ingrese un Numero"
            invalid-feedback="Complete este campo"
            required
          >
          </b-form-input>
        </b-form-group>
        -->
        <b-form-group label="*Nombre/s" label-for="nombre">
          <b-form-input
            id="nombre"
            v-model="item.nombre"
            type="text"
            placeholder="*Ingrese los Nombre/s"
            invalid-feedback="Complete este campo"
            required
          >
          </b-form-input>
        </b-form-group>
        <b-form-group label="*Apellido/s" label-for="apellido">
          <b-form-input
            id="apellido"
            v-model="item.apellido"
            type="text"
            placeholder="*Ingrese los Apellido/s"
            invalid-feedback="Complete este campo"
            required
          >
          </b-form-input>
        </b-form-group>
        <b-form-group label="*DNI" label-for="dni_familiar">
          <b-form-input
            id="dni_familiar"
            v-model="item.dni_familiar"
            type="number"
            placeholder="Ingrese un DNI"
            invalid-feedback="Complete este campo"
            required
          >
          </b-form-input>
        </b-form-group>

      
        <b-form-group label="*Fecha de nacimiento" label-for="fecha_nacimiento">
          <b-form-input
            id="fecha_nacimiento"
            v-model="item.fecha_nacimiento"
            type="date"
            placeholder="Ingrese una fecha"
            invalid-feedback="Complete este campo"
            required
          >
          </b-form-input>
        </b-form-group>
  

        <b-form-group label="Carencia" label-for="carencia">
          <b-form-input
            id="carencia"
            v-model="item.carencia"
            type="date"
            placeholder="Ingrese una fecha"
            invalid-feedback="Complete este campo"
            required
          >
          </b-form-input>
      </b-form-group>
    </b-form>
    <b-button class="mt-2" variant="primary" @click="sumarFliares()" style="color:white;">+</b-button>
    
  </div>
<!-- 
    {{ socio }}
    {{familiar}} -->
    <!-- {{ data }} -->
    <b-button class="mt-2" variant="success" block @click="putSocio()">Cambiar</b-button>
    
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";
import axios from "axios";


export default {
  props: {
    socio: {},
  },
  data() {
    return {
      // socio: {},
      familiar:[
        
      ],
      data: {},
      plan: [],
      btn_familiar: false,
      cantidad: 0,
      select: null,
      options: [
        {value: null, text: 'Elija un departamento'},
        {value: 'Burruyacú', text: '1- Burruyacú'},
        {value: 'Capital', text: '2- Capital'},
        {value: 'Chicligasta', text: '3- Chicligasta'},
        {value: 'Cruz Alta', text: '4- Cruz Alta'},
        {value: 'Famaillá', text: '5- Famaillá'},
        {value: 'Graneros', text: '6- Graneros'},
        {value: 'Juan Bautista Alberdi', text: '7- Juan Bautista Alberdi'},
        {value: 'La Cocha', text: '8- La Cocha'},
        {value: 'Leales', text: '9- Leales'},
        {value: 'Lules', text: '10- Lules'},
        {value: 'Monteros', text: '11- Monteros'},
        {value: 'Río Chico', text: '12- Río Chico'},
        {value: 'Simoca', text: '13- Simoca'},
        {value: 'Tafí del Valle', text: '14- Tafí del Valle'},
        {value: 'Tafí Viejo', text: '15- Tafí Viejo'},
        {value: 'Trancas', text: '16- Trancas'},
        {value: 'Yerba Buena', text: '17- Yerba Buena'},
      ]
    };
  },

  methods: {
    async getSocios() {
      let socioAPI = new APIControler();
      this.data = await socioAPI.getData();
    },
    async putSocio() {
      let respuesta ="vacio"
      // try{
      await axios.put('http://localhost:8081/socios/'+this.socio.numero_socio+ '/', this.socio)
      .then(function (data){
        console.log("Data")
        console.log(data)
        swal("Operación Exitosa", " ", "success");
      })
      .then(this.putFamiliar)
      .catch(function (error) {
        swal("¡ERROR!", "Se ha detectado un problema ", "error");
        console.log(error)
        // respuesta=error.response.data;
        //console.log(error.response.data);
      })

      
      //this.resetForm();
    },
    async sumarFliares(){
      this.btn_familiar=true;
      // this.resetFormAdh();
      // this.cantidad=this.cantidad +1;
      this.familiar.push({
          numero_socio:null, 
          apellido : "",
          nombre : "",
          dni_familiar : null,
          fecha_nacimiento:null,
          carencia: null,
        })
    },
    async putFamiliar() {
      let familiarAPI = new APIControler();
      let _nroSocio='http://localhost:8081/socios/'+ this.socio.numero_socio +'/';
      familiarAPI.apiUrl.pathname='familiar/';

      // console.log("Mostrando nro socio")
      // console.log(_nroSocio)
      for (const adherente of this.familiar) {
        console.log("Mostrando adherente")
        console.log(adherente)
        if(adherente.numero_socio){
          console.log("Modificando familiar")
          axios.put('http://localhost:8081/familiar/'+adherente.dni_familiar+ '/', adherente)
          .catch(function (error) {
            swal("¡ERROR!", "Se ha detectado un problema al actualizar un familiar", "error");
            console.log(error)
          })

        }
        else{
          console.log("Agregando familiar")
          adherente.numero_socio=_nroSocio          
          axios.post('http://localhost:8081/familiar/', adherente)

        }


      //   .then(function (data){
      //     swal("Operación Exitosa", " ", "success");
      // })
      // .catch(function (error) {
      //   swal("¡ERROR!", "Se ha detectado un problema ", "error");
        // respuesta=error.response.data;
        
        //console.log(error.response.data);
      }
      // )
        // await familiarAPI.putData(adherente);
      // }
      
      // this.resetFormAdh();
    },
    async getPaciente() {
      let familiarAPI = new APIControler();
      familiarAPI.apiUrl.pathname = "familiar/";
      this.data = await familiarAPI.getData();
      this.data.forEach((element) => {
        if (element.numero_socio.split('/')[4] == this.socio.numero_socio) {
          this.familiar.push(element)
          this.btn_familiar=true
        }
          console.log(this.familiar)
      });
    },
    async resetForm() {
        this.socio.numero_socio = null;
        this.socio.apellido = "";
        this.socio.nombre = "";
        this.socio.dni = null;
        this.socio.fecha_nacimiento=null;
        this.socio.calle = "";
        this.socio.localidad = "";
        this.socio.departamento = "";
        this.socio.cod_postal = null;
        this.socio.tel_fijo = null;
        this.socio.tel_celular = null;
        this.socio.carencia= null;
    },
    async resetFormAdh() {
      
        this.familiar.apellido = "";
        this.familiar.nombre = "";
        this.familiar.dni_familiar = null;
        this.familiar.fecha_nacimiento=null;
        this.familiar.carencia= null;
        
    },
  },
  beforeMount() {
    this.getPaciente();
  },
};
</script>

<style>
</style>