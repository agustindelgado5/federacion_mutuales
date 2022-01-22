<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Nuevo Venta Optica:</h4>

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
          :disabled="true"
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
    <b-button class="mt-2" variant="success" block @click="putVentaOptica()"
      >Guardar</b-button
    >
  </div>
</template>

<script>
import { APIControler } from "@/store/APIControler";
import axios from "axios";
export default {
  props: {
			ventaOptica: {},
			updateTable: Function,
		},
  data() {
    return {
      list_socios:{},
      data: {},
      respuesta: {},
      validarError: {
					validateStatus: function (status) {
						return status < 500; // Resolve only if the status code is less than 500
					},
				},
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
    
    async putVentaOptica() {
				try {
					this.respuesta = await axios.put(
						"http://localhost:8081/ventasOpticas/" +
							this.ventaOptica.codigo_seguimiento +
							"/",
						this.ventaOptica,
						this.validarError
					);
					const content = this.respuesta.request;
					if (content.statusText == "OK") {
						this.respuesta = "";
						swal("Carga Exitosa", " ", "success");
					} else {
						//console.log(content.response);
						this.respuesta = JSON.parse(content.response);
						swal("¡ERROR!", "Los datos no son válidos", "error");
					}
				} catch (error) {
					swal("¡ERROR!", "Se ha detectado un problema ", "error");
					console.log(error);
				}
				this.cargarFeedback();
				this.updateTable();
			},


    cargarFeedback() {
      let valido; 
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