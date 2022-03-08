<template>
  <div>
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Nuevo Venta Optica:</h4>

    <!-- CAMPOS REQUERIDOS -->
    <!-- codigo_seguimiento -->
    <!-- nro de socio-->
  
    
    <!------------------------------------------------------------------------------------------->
    <b-form>
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
      <b-form-group label="*Lente" label-for="lente">
          <b-form-select
            id="lente"
            v-model="ventaOptica.lente"
            :state="validacion.lente.estado"
            type="text"
            placeholder="Ingrese un Numero"
            invalid-feedback="Complete este campo"
            required
            :options="op_lentes"
          >
          </b-form-select>
          <b-form-invalid-feedback
                  id="lente-live-feedback"
                >{{validacion.lente.mensaje}}
              </b-form-invalid-feedback>
        </b-form-group>
      <b-form-group label="*Cristal Derecho" label-for="cristal_derecho">
        <b-form-select
          id="cristal_derecho"
          v-model="ventaOptica.cristal_derecho"
          :state="validacion.cristal_derecho.estado"
          type="text"
          placeholder="Ingrese un Numero"
          invalid-feedback="Complete este campo"
          required
          :options="op_cristales"
        >
        </b-form-select>
        <b-form-invalid-feedback
                id="cristal-live-feedback"
              >{{validacion.cristal_derecho.mensaje}}
            </b-form-invalid-feedback>
        </b-form-group>

      <b-form-group label="*Cristal izquierdo" label-for="cristal_izquierdo">
        <b-form-select
          id="cristal_izquierdo"
          v-model="ventaOptica.cristal_izquierdo"
          :state="validacion.cristal_izquierdo.estado"
          type="text"
          placeholder="Ingrese un Numero"
          invalid-feedback="Complete este campo"
          required
          :options="op_cristales"
        >
        </b-form-select>
        <b-form-invalid-feedback
            id="cristal-live-feedback"
          >{{validacion.cristal_izquierdo.mensaje}}
        </b-form-invalid-feedback>
      </b-form-group>

      <b-form-group label="*Fecha Receta" label-for="fecha_receta">
        <b-form-input
          id="fecha_receta"
          v-model="ventaOptica.fecha_receta"
          type="date"
          placeholder="Ingrese una fecha"
          invalid-feedback="Complete este campo"
          :state="validacion.fecha_receta.estado"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback id="fecha_receta-live-feedback"
          >{{ validacion.fecha_receta.mensaje }}
        </b-form-invalid-feedback>
      </b-form-group>

      <b-form-group label="*Fecha de Venta" label-for="fecha_venta">
        <b-form-input
          id="fecha_venta"
          v-model="ventaOptica.fecha_venta"
          type="date"
          placeholder="Ingrese una fecha"
          invalid-feedback="Complete este campo"
          :state="validacion.fecha_venta.estado"
          required
        >
        </b-form-input>
        <b-form-invalid-feedback id="fecha_venta-live-feedback"
          >{{ validacion.fecha_venta.mensaje }}
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
      op_lentes: [
        {value: null, text: 'Elija una lente', disabled: true},
      ],
      op_cristales: [
        {value: null, text: 'Elija un cristal', disabled: true},
      ],

      validacion: {
        id_venta: { estado: null, mensaje: "" },
        numero_socio: { estado: null, mensaje: "" },
        lente: { estado: null, mensaje: "" },
        cristal_derecho: { estado: null, mensaje: "" },
        cristal_izquierdo: { estado: null, mensaje: "" },
        fecha_receta: { estado: null, mensaje: "" },
        fecha_venta: { estado: null, mensaje: "" },
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
    async getLentes() {
      let lenteAPI = new APIControler();
      lenteAPI.apiUrl.pathname='lentes/';
      this.data = await lenteAPI.getData(this.list_lentes);
      this.data.forEach(element => {   
        let option={}
        option.value='http://localhost:8081/lentes/'+ element.id_lente +'/';
        option.text= element.marca +'-- '+ element.material +', '+ element.color+', '+ element.precio_mutual ;
        console.log(option);
        this.op_lentes.push(option);
        
      });
    },
    async getCristales() {
      let cristalAPI = new APIControler();
      cristalAPI.apiUrl.pathname='cristales/';
      this.data = await cristalAPI.getData(this.list_cristales);
      this.data.forEach(element => {   
        let option={}
        option.value='http://localhost:8081/cristales/'+ element.id_cristal +'/';
        option.text= element.material +'-- esf: '+ element.esfera +', cil: '+ element.cilindro+', eje: '+ element.eje +', $'+ element.precio_mutual;
        console.log(option);
        this.op_cristales.push(option);
        
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
    this.getLentes();
    this.getCristales();
  },
};
</script>

<style>

</style>