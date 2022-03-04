<template>
  <div id="socios" class="myTable">
    <!--HEAD DE LA PAGINA -->
    <vue-headful
      title="Cobrador / Socios - Federación Tucumana de Mutuales"
    ></vue-headful>

    <h2>Cobrador: {{cobrador.nombre}} {{cobrador.apellido}}</h2>
    <h3>Listado de Socios, monto total: ${{montoTotal}}</h3> 
    <b-button @click="testFetch" class="mb-4" title="Recargar" variant="light">
      <v-icon dark style="color: black">mdi-cached</v-icon>
      Actualizar
    </b-button>

    <!-- ======== Formulario de Busqueda ======== -->
    <div>
      <b-input-group size="sm" class="mb-2">
        <b-input-group-prepend is-text>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            class="bi bi-search"
            viewBox="0 0 16 16"
          >
            <path
              d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"
            />
          </svg>
        </b-input-group-prepend>
        <b-form-input
          v-model="buscar"
          type="text"
          placeholder="Busque un registro"
          v-on:keyup="buscarnow()"
          ref="buscadorlista"
        ></b-form-input>
      </b-input-group>
    </div>
    <!-- ======================================== -->
    <!-- ======== Tabla con los registros ======= -->

    <b-table
      :fields="fields"
      striped
      sortable
      responsive
      hover
      :items="tabla_socios"
      show-empty
      :per-page="perPage"
      :current-page="currentPage"
      
      :no-border-collapse="false"
      ref="tablaregistros"
      id="tablaregistros"
    >
      <template #empty="">
        <b>No hay registros para mostrar</b>
      </template>
      
     
      <template slot="cell(id_mutual)" slot-scope="data">
        {{ data.value.split("/")[4] }}
      </template>

      <template slot="cell(monto)" slot-scope="data">
        ${{ data.value||0 }}
      </template>

      <template slot="cell(action)" slot-scope="row">
        <div class="mt-3">
          <b-button-group>
            <b-button
              variant="info"
              id="button-1"
              title="Mostrar Info"
              @click="row.toggleDetails"
            >
              {{ row.detailsShowing ? "Ocultar" : "Mostrar" }} detalles
            </b-button>
<!--             FUNCION NO HABILITADA AÚN
            <b-button
              variant="success"
              id="button-1"
              title="Mostrar Info"
              @click="noop"
            >
              <v-icon class="mr-1"> mdi-cash </v-icon>
              Pagar
            </b-button>
             -->
            
          </b-button-group>
        </div>
      </template>
      <template #row-details="row">
					<b-card title="Datos del socio: ">
						<div>
							<b-list-group horizontal>
								<b-list-group class="col-4">
											<b-list-group-item
												><b>Nombre Completo:</b>
												{{ row.item.apellido.toUpperCase() }},
												{{ row.item.nombre.toUpperCase() }}</b-list-group-item
											>
											<b-list-group-item
												><b>DNI:</b> {{ row.item.dni }}</b-list-group-item
											>
											<b-list-group-item
												><b>Fecha de Nacimiento:</b>
												{{
													row.item.fecha_nacimiento | FormatStringToDate
												}}</b-list-group-item
											>
											<b-list-group-item
												><b>Fecha de Asociacion:</b>
												{{
													row.item.fecha_asociacion | FormatStringToDate
												}}</b-list-group-item
											>
											<b-list-group-item
												><b>Edad:</b> {{ row.item.edad }}</b-list-group-item
											>
										</b-list-group>
										&nbsp;
										<b-list-group class="col-4">
											<b-list-group-item
												><b>Domicilio:</b> {{ row.item.calle.toUpperCase() }} -
												{{ row.item.localidad.toUpperCase() }}
											</b-list-group-item>
											<b-list-group-item
												><b>Departamento:</b>
												{{
													row.item.departamento.toUpperCase()
												}}</b-list-group-item
											>
											<b-list-group-item
												><b>Codigo Postal:</b>
												{{ row.item.cod_postal }}</b-list-group-item
											>
											<b-list-group-item
												><b>Correo:</b> {{ row.item.email }}
											</b-list-group-item>
											<!--
											<b-list-group-item
											
												><b>Mutual:</b> {{ row.item.id_mutual.split("/")[4] }}
											</b-list-group-item>
											-->
										<b-list-group-item
												><b>Plan:</b>
												{{
													row.item.plan != null
														? row.item.plan
														: "No disponible"
												}}
											</b-list-group-item>
                    </b-list-group>

										&nbsp;
										<b-list-group class="col-4">
											<b-list-group-item
												><b>Telefono Fijo:</b>
												{{ row.item.tel_fijo }}</b-list-group-item
											>
											<b-list-group-item
												><b>Celular:</b>
												{{ row.item.tel_celular }}</b-list-group-item
											>
											<!-- <b-list-group-item
												><b>Carencia:</b>
												{{ row.item.carencia | FormatStringToDate }}
											</b-list-group-item> -->
											<b-list-group-item
												><b>Tiene Obra social:</b>
												{{ row.item.tieneObraSocial ? "Si" : "No" }}
											</b-list-group-item>
											<b-list-group-item>
                        <b>Filial:</b>
												{{ row.item.id_mutual.split('/')[4] }}
											</b-list-group-item>
									<b-list-group-item>
                        <b>Monto adeudado:</b>
												${{
													row.item.monto
												}}
											</b-list-group-item>
								</b-list-group>
							</b-list-group>
						</div>
					</b-card>
				</template>
    </b-table>
    

    <!-- ==================================CREAR PDF================================== -->
    <vue-html2pdf
      :show-layout="false"
      :float-layout="true"
      :enable-download="false"
      :preview-modal="true"
      :paginate-elements-by-height="1400"
      filename="DetalleSocio"
      :pdf-quality="2"
      :manual-pagination="false"
      pdf-format="a4"
      pdf-orientation="portrait"
      pdf-content-width="80%"
      @progress="onProgress($event)"
      @startPagination="startPagination()"
      @hasPaginated="hasPaginated()"
      @beforeDownload="beforeDownload($event)"
      @hasDownloaded="hasDownloaded($event)"
      ref="html2Pdf"
    >
      <section slot="pdf-content">
        <!-- PDF Content Here -->
        <section class="pdf-item">
          <h3>Federación Tucumana de Mutuales</h3>
          
          <img
            src="@/assets/logo.jpg"
            alt="Logo Federación"
            srcset=""
            id="Logo_fed"
          />
        </section>
        <section class="pdf-item">
          <h3>Socio Médica</h3>
          <b-list-group>
            <b-list-group-item
              v-for="value in fields.slice(0, -1)"
              :key="value.key"
              >{{ value.label }}: {{ socioAPDF[value.key] }}</b-list-group-item
            >
          </b-list-group>
        </section>
      </section>
    </vue-html2pdf>
    <!-- ============================================================================== -->
  </div>
</template>

<script>

import VueHtml2pdf from "vue-html2pdf";

import axios from "axios";
import { APIControler } from "@/store/APIControler";

export default {
  components: { VueHtml2pdf },
  
  data() {
    return {
      tabla_socios: [],
      list_mutuales: [],
      cobrador: {},
      fields: [
					{ key: "selected", label: "", sortable: true },
					{ key: "numero_socio", label: "N° Socio", sortable: true },
					{ key: "apellido", label: "Apellido/s", sortable: true },
					{ key: "nombre", label: "Nombre/s", sortable: true },
					{ key: "dni", label: "DNI", sortable: true },
					//{ key: "edad", label: "Edad", sortable: true },
					{ key: "monto", label: "Monto", sortable: true },
					/*{
						key: "fecha_nacimiento",
						label: "Fecha de Nacimiento",
						sortable: true,
					},*/
					//{ key: "fecha_asociacion", label: "Fecha de Asociacion", sortable: true,},
					{key: 'calle' ,label: 'Direccion', sortable: true,},
					// {key:'localidad' ,label: 'Localidad', sortable: true,},
					// { key: "departamento", label: "Departamento", sortable: true },
					//{key:'cod_postal' ,label: 'Codigo Postal', sortable: true,},
					//{key: 'email' ,label: 'Mail', sortable: true,},
					//{key: 'tel_fijo',label: 'Telefono Fijo', sortable: true,},
					{key:'tel_celular' ,label: 'Telefono Celular', sortable: true,},
					// { key: "carencia", label: "Carencia", sortable: true },
					// { key: "aldia", label: "Al Día", sortable: true },
					// { key: "id_mutual", label: "Mutual", sortable: true },
					{ key: "action", label: "Acciones", variant: "secondary" },
      ],
      totalRows: 1, //Total de filas
      currentPage: 1, //Pagina actual
      perPage: 10, // Datos en la tabla por pagina
      buscar: "",
      
      socioAPDF: {}, //Se carga cuando se hace clic en exportar a pdf, con la socio a exportar
    };
  },
  computed: {
    montoTotal(){
      const initialValue = 0;
      const sumWithInitial = this.tabla_socios.reduce(
        (previousValue, currentValue) => parseInt(previousValue) + (parseInt(currentValue.monto)||0),
        initialValue
      );
      return sumWithInitial
    },
    rows() {
      return this.tabla_socios.length;
    },
    id() {
      return this.tabla_socios.numero_socio;
    },
    items() {
      return tabla_socios.filter((item) => {
        return item.numero_socio
          .toLowerCase()
          .includes(this.buscar.toLowerCase());
      });
    },
  },
  methods: {
    async testFetch() {
      //Si se viene desde Cobradores, se le manda el objeto completo, sino solo el id
      try { 
        let cobrador=this.$route.params.cobrador
        let id;
        console.log("param",cobrador)
        
        const baseURL="http://localhost:8081";
        if(cobrador == null ){
          id=this.$route.query.id
          console.log("Cobrador vacio")
          const response = await axios.get(baseURL+"/cobradores/"+id+"/")
          this.cobrador=response.data
        }
        else{
          this.cobrador=cobrador
          id=cobrador.id_cobrador
        }
        const pathname = "/socios/?cobrador="+id;
        const res = await axios.get(baseURL+pathname)
        const data = await res.data

        this.tabla_socios = data.results;
      } catch (error) {
        console.log(error);
      }
    },
    
    //Funcion para mostrar el modal
    showModal() {
      this.$refs["my-modal"].show();
    },
    showModalinfo(item, index) {
      
      //this.showModal();
    },
    //Funcion para esconder el modal
    hideModal() {
      this.$refs["my-modal"].hide();
    },
  
    async getMutuales() {
				let mutualAPI = new APIControler();
				mutualAPI.apiUrl.pathname = "mutuales/";
				this.list_mutuales = await mutualAPI.getData();
				
			},

    async buscarnow() {
      // Declare variables
      var input,
        filter,
        table,
        tr,
        td,
        i,
        txtValue,
        p1, //nro de socio
        p2, //nro de socio
        p3, //servicio
        p4, //id medico
        p5; //fecha
      input = this.$refs.buscadorlista;
      filter = input.value.toUpperCase();
      table = document.getElementById("tablaregistros");
      tr = table.getElementsByTagName("tr");

      // Loop through all list items, and hide those who don't match the search query
      for (i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td");
        p1 = td[0].textContent || td[0].innerText;
        p2 = td[1].textContent || td[1].innerText;
        p3 = td[3].textContent || td[3].innerText;
        p4 = td[4].textContent || td[4].innerText;
        p5 = td[6].textContent || td[6].innerText;
        txtValue = p1 + p2 + p3 + p4 + p5;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    },
  
  },
  beforeMount() {
    this.cobrador=this.$route.params.cobrador || {}
    this.testFetch();
    this.getMutuales();
  },
};
</script>

<style scoped>
.myTable {
  position: absolute;
  left: 0;
  padding: 1.5em;
  margin-top: 4rem;
  overflow: auto;
  transition: 0.5s;
  width: 100%;
}
</style>
