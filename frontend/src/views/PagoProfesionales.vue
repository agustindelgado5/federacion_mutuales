<template>
	<div id="listadoPagos" class="myTable">
		<vue-headful
			title="Listado de Pagos a los Profesionales - Federación Tucumana de Mutuales"
		></vue-headful>
		<b-overlay
			:show="show"
			rounded="sm"
			@shown="onShown"
			@hidden="onHidden"
			variant="dark"
			opacity="0.30"
		>
			<h2>Listado de Pagos a los Profesionales</h2>
			<b-button
				@click="getOrdenes()"
				class="mb-4"
				title="Recargar"
				variant="light"
			>
				<v-icon dark style="color: black">mdi-cached</v-icon>
				Actualizar
			</b-button>

			<!-- ======== Formulario de Busqueda ======== -->
			<b-form-group
				label-for="filter-input"
				label-align-sm="right"
				label-size="sm"
				class="mb-0"
				style="width: 100%; padding-bottom: 1em"
				v-show="rows > 0"
			>
				<b-input-group size="sm">
					<b-form-input
						id="filter-input"
						v-model="filter"
						type="search"
						placeholder="Buscar registros"
					></b-form-input>

					<b-input-group-append>
						<b-button :disabled="!filter" @click="filter = ''"
							>Limpiar</b-button
						>
					</b-input-group-append>
				</b-input-group>
			</b-form-group>
			<!-- ======================================== -->
			<!-- 
    <section class="container">
    {{ tabla_ordenes }}
	-->

			<section>
				<b-table :fields="fields"
						 striped
						 sortable
						 responsive
						 hover
						 :items="tabla_ordenes"
						 show-empty
						 :per-page="perPage"
						 :current-page="currentPage"
						 :sticky-header="true"
						 :no-border-collapse="false"
						 ref="tablaregistros"
						 id="tablaregistros"
						 :filter="filter"
						 @filtered="onFiltered">
					<template #empty="">
						<b>No hay registros para mostrar</b>
					</template>
					<template slot="cell(id_medico)" slot-scope="data">
						<b>{{ data.value }}</b>
					</template>
					<template slot="cell(profesional)" slot-scope="data">
						{{ data.value.toUpperCase() }}
					</template>
					<template slot="cell(diasliquidacion)" slot-scope="data">
						<b>{{ data.value }}</b>
					</template>
					<template slot="cell(action)" slot-scope="row">
						<div class="mt-3">
							<b-button-group>
								<b-button variant="info"
										  id="button-1"
										  title="Mostrar Info"
										  @click="row.toggleDetails">
									{{ row.detailsShowing ? "Ocultar" : "Mostrar" }} detalles
								</b-button>
							</b-button-group>
						</div>
					</template>

					<template #row-details="row">
						<div>
							<b-form-group label-for="filter-input"
										  label-align-sm="right"
										  label-size="sm"
										  class="mb-0"
										  style="width: 100%; padding-bottom: 1em">
								<b-input-group size="sm">
									<b-form-input id="filter-input"
												  v-model="filter"
												  type="search"
												  placeholder="Buscar registros"></b-form-input>

									<b-input-group-append>
										<b-button :disabled="!filter" @click="filter = ''">
											Limpiar
										</b-button>
									</b-input-group-append>
								</b-input-group>
							</b-form-group>
							<b-table hover
									 :items="row.item.ordenes"
									 :fields="fields_ordenes"
									 :sticky-header="true"
									 :no-border-collapse="true"
									 :filter="filter"
									 show-empty>
								<template #empty="">
									<b>No hay registros para mostrar</b>
								</template>
								<template slot="cell(mes)" slot-scope="data">
									<b>{{ data.value }}</b>
								</template>
								<template slot="cell(ListOrdenes)" slot-scope="data">
									<div v-for="orden in data.value"
										 :key="orden.num_orden"
										 @click="auxOrdenesMes(orden)">
										<b-list-group horizontal>
											<b-list-group>
												<b-list-group-item>
													<b>N° Orden: </b>{{ orden.num_orden }} | <b>Fecha: </b>{{ orden.fecha.split("-")[2] }}/{{
														orden.fecha.split("-")[1]
													}}/{{ orden.fecha.split("-")[0] }} | <b>Hora: </b>{{ orden.hora }} | <b>Precio A Pagar: </b>${{ orden.preciomutual }}
												</b-list-group-item>
											</b-list-group>
										</b-list-group>
										&nbsp;
									</div>
								</template>
								<template slot="cell(total)" slot-scope="data">
									<b>$ {{ data.value }}</b>
								</template>
								<template slot="cell(action)" slot-scope="row">
									<b-button-group>
										<b-button variant="warning"
												  id="button-2"
												  title="Editar este registro"
												  v-b-modal.modal-editar
												  @click="editarPago(row.item, row.index)">
											<v-icon class="mr-2"> mdi-pencil </v-icon>
											Editar
										</b-button>

										<b-button @click="generarPDF(row.item)"
												  id="btn_down_pdf"
												  title="Generar PDF"
												  variant="danger"
												  style="color: white">
											<svg xmlns="http://www.w3.org/2000/svg"
												 width="16"
												 height="16"
												 fill="currentColor"
												 class="bi bi-file-pdf-fill"
												 viewBox="0 0 16 16">
												<path d="M5.523 10.424c.14-.082.293-.162.459-.238a7.878 7.878 0 0 1-.45.606c-.28.337-.498.516-.635.572a.266.266 0 0 1-.035.012.282.282 0 0 1-.026-.044c-.056-.11-.054-.216.04-.36.106-.165.319-.354.647-.548zm2.455-1.647c-.119.025-.237.05-.356.078a21.035 21.035 0 0 0 .5-1.05 11.96 11.96 0 0 0 .51.858c-.217.032-.436.07-.654.114zm2.525.939a3.888 3.888 0 0 1-.435-.41c.228.005.434.022.612.054.317.057.466.147.518.209a.095.095 0 0 1 .026.064.436.436 0 0 1-.06.2.307.307 0 0 1-.094.124.107.107 0 0 1-.069.015c-.09-.003-.258-.066-.498-.256zM8.278 4.97c-.04.244-.108.524-.2.829a4.86 4.86 0 0 1-.089-.346c-.076-.353-.087-.63-.046-.822.038-.177.11-.248.196-.283a.517.517 0 0 1 .145-.04c.013.03.028.092.032.198.005.122-.007.277-.038.465z" />
												<path fill-rule="evenodd"
													  d="M4 0h8a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2zm.165 11.668c.09.18.23.343.438.419.207.075.412.04.58-.03.318-.13.635-.436.926-.786.333-.401.683-.927 1.021-1.51a11.64 11.64 0 0 1 1.997-.406c.3.383.61.713.91.95.28.22.603.403.934.417a.856.856 0 0 0 .51-.138c.155-.101.27-.247.354-.416.09-.181.145-.37.138-.563a.844.844 0 0 0-.2-.518c-.226-.27-.596-.4-.96-.465a5.76 5.76 0 0 0-1.335-.05 10.954 10.954 0 0 1-.98-1.686c.25-.66.437-1.284.52-1.794.036-.218.055-.426.048-.614a1.238 1.238 0 0 0-.127-.538.7.7 0 0 0-.477-.365c-.202-.043-.41 0-.601.077-.377.15-.576.47-.651.823-.073.34-.04.736.046 1.136.088.406.238.848.43 1.295a19.707 19.707 0 0 1-1.062 2.227 7.662 7.662 0 0 0-1.482.645c-.37.22-.699.48-.897.787-.21.326-.275.714-.08 1.103z" />
											</svg>
											Generar PDF
										</b-button>
									</b-button-group>
								</template>
							</b-table>
						</div>
					</template>
				</b-table>

				<b-modal id="modal-editar" hide-footer ref="my-modal">
					<template #modal-title>
						<h5 class="modal-title">Editar: {{ editar.mes }}</h5>
					</template>
					<b-form>
						<b-form-group label="Elija la forma de pago">
							<b-form-select
								v-model="selected"
								:options="options"
								class="mb-3"
								type="text"
								required
							></b-form-select>
						</b-form-group>

						<b-button
							class="mt-2"
							variant="success"
							block
							@click="putModoPago(editar.mes)"
						>
							<b>GUARDAR</b>
						</b-button>
					</b-form>
				</b-modal>
				<!-- ==================================CREAR PDF================================== -->

				<vue-html2pdf
					:show-layout="false"
					:float-layout="true"
					:enable-download="false"
					:preview-modal="true"
					:paginate-elements-by-height="1400"
					filename="DetallePago"
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
						<section class="pdf-item">
							<h3>Federación Tucumana de Mutuales</h3>
							<img
								src="../assets/logo.jpg"
								alt="Logo Federación"
								srcset=""
								id="Logo_fed"
							/>
						</section>
						<section class="pdf-item">
							<h3>Comprobante de pago</h3>

							<b-list-group horizontal>
								<b-list-group-item>
									<b>ID: {{ ordenAPDF.ID }}</b>
								</b-list-group-item>
								<b-list-group-item>
									<b>Profesional:</b> {{ ordenAPDF.profesional }}
								</b-list-group-item>
								<b-list-group-item>
									<b>Dias de Liquidacion:</b> {{ ordenAPDF.diasliquidacion }}
								</b-list-group-item>
								<b-list-group-item>
									<b>Total de Pago:</b> {{ ordenAPDF.totalapagar }}
								</b-list-group-item>
							</b-list-group>
							<br>
							<b-list-group>
								<b-list-group-item>
									<b>MES: {{ ordenAPDF.mes }}</b>
								</b-list-group-item>
								<b-list-group-item
									v-for="orden in ordenAPDF.ordenes"
									:key="orden.num_orden"
								>
									{{ orden.num_orden }} - {{ orden.fecha }} -
									{{ orden.hora }} - ${{ orden.preciomutual }}
								</b-list-group-item>
							</b-list-group>
							<br />
							<b-list-group horizontal>
								<b-list-group-item>
									<b>Forma de Pago: {{ ordenAPDF.modo_pago }}</b>
								</b-list-group-item>
								<b-list-group-item>
									<b>TOTAL: ${{ ordenAPDF.total }}</b>
								</b-list-group-item>
							</b-list-group>
						</section>
					</section>
				</vue-html2pdf>

				<b-container fluid>
					<b-col class="my-1">
						<b-pagination
							v-model="currentPage"
							align="center"
							pills
							:total-rows="totalRows"
							:per-page="perPage"
							aria-controls="table_profesionales"
						>
						</b-pagination>
					</b-col>
				</b-container>
			</section>
			<!---
    <aside v-show="rows > 0">
      <div>
        <b-card-group deck>
          <b-card bg-variant="primary" text-variant="white" header="FILTRAR POR AÑO" class="text-center">
            <b-card-text>
             
            </b-card-text>
          </b-card>
        </b-card-group>
      </div>
    </aside>
    -->
			<template #overlay>
				<div class="text-center">
					<v-icon>fas fa-circle-notch fa-spin</v-icon>
					<p id="cancel-label">Espere un momento...</p>
				</div>
			</template>
		</b-overlay>
	</div>
</template>

<script>
	let api = new URL("http://localhost");
	api.pathname = "ordenes";
	//api.port = 8000;
	api.port = 8081;

	import VueHtml2pdf from "vue-html2pdf";
	import { APIControler } from "../store/APIControler";
	import swal from "sweetalert";
	import _ from "lodash";
    import axios from "axios";
	import { mapState, mapActions } from "vuex";

	export default {
		components: { VueHtml2pdf },
		data() {
			return {
				tabla_profesionales: [],
				data: {},
				tabla_ordenes: [],
                list_pagado: {},
				//profesionales:[],
				fields: [
					{
						key: "id_medico",
						label: "ID",
						sortable: true,
					},
					{
						key: "profesional",
						label: "Nombre Completo",
						sortable: true,
					},
                    {
                        key: "diasliquidacion",
                        label: "Dias de Liquidacion",
                        sortable: true,
                    },
                    {
                        key: "totalapagar",
                        label: "Total a Pagar",
                        sortable: true,
                    },
					{ key: "action", label: "Acciones", variant: "secondary" },
				],
				fields_ordenes: [
					{
						key: "mes",
						label: "Mes",
						sortable: true,
					},
					{
						key: "ListOrdenes",
						label: "Ordenes",
						sortable: true,
					},
					{
						key: "total",
						label: "Total",
						sortable: true,
					},
					{
						key: "formaPago",
						label: "Forma de Pago",
						sortable: true,
					},
                    {
                        key: "liquidacionlista",
                        label: "Liquidacion Lista",
                        sortable: true,
					},
                    {
                        key: "pagado",
                        label: "Ya Pagado",
                        sortable: true,
                    },
					{ key: "action", label: "Acciones", variant: "secondary" },
				],
				//buscar: "",
				filter: null,
				editar: {},
				selected: null,
				totalRows: 1, //Total de filas
				currentPage: 1, //Pagina actual
				perPage: 30, // Datos en la tabla por pagina
				ordenAPDF: {},
				pagadardo: 0,
				options: [
					{
						value: null,
						text: "--------ELIJA UNA FORMA DE PAGO--------",
						disabled: true,
					},
					{ value: "Contado", text: "Contado" },
					{ value: "Transferencia", text: "Transferencia" },
				],
				show: false,
				ordenAPDF: {
					ID: 0,
					profesional: null,
					mes: null,
					ordenes: [],
					modo_pago: null,
					total: 0,
				},
				orden_del_mes: [],
			};
		},

		created() {
			this.cargar_pagos();
		},

		computed: {
			...mapState("PagosProf", ["pagos"]),

			rows() {
				return this.tabla_ordenes.length;
			},
			sortOptions() {
				// Create an options list from our fields
				return this.fields
					.filter((f) => f.sortable)
					.map((f) => {
						return { text: f.label, value: f.key };
					});
			},
		},

		methods: {
			//Traigo las funciones para almacenarlas en la session
			...mapActions("PagosProf", ["set_pagos", "cargar_pagos"]),

			//Funcion para obtener los profesionales
			async getProfesional(id) {
				let profesionalAPI = new APIControler();
				profesionalAPI.apiUrl.pathname = "profesionales/" + id;
				let response = await fetch(profesionalAPI.apiUrl);
				let data = await response.json();
				return data;
			},

			//Funcion para sumar el total de las ordenes por mes
			sumaTotal(array) {
				let suma = 0;
				if (array != null)
				{
                    for (let index = 0; index < array.length; index++) {
                        suma += array[index].preciomutual;
                    }
				}
				return suma;
			},
            sumaTotal2(array) {
				let suma = 0;
				if (array != null) {
					for (let index = 0; index < array.length; index++) {
						if (array[index].liquidacionlista == 'Si') {
                            suma += array[index].total - array[index].pagado;
						}
					}
				}
                return suma;
			},
            diasdediff(fecha) {
				var FechaInicio = new Date(fecha).getTime();
                var ahora = Date.now();
                var hoy = new Date(ahora);
				var diff = hoy - FechaInicio;

                console.log(diff / (1000 * 60 * 60 * 24));
				return (diff / (1000 * 60 * 60 * 24));
            },
			//Formateo la fecha
			formatMesAnio(mes, anio) {
				var meses = [
					{ inicial: "ENE", numero: "01" },
					{ inicial: "FEB", numero: "02" },
					{ inicial: "MAR", numero: "03" },
					{ inicial: "ABR", numero: "04" },
					{ inicial: "MAY", numero: "05" },
					{ inicial: "JUN", numero: "06" },
					{ inicial: "JUL", numero: "07" },
					{ inicial: "AGO", numero: "08" },
					{ inicial: "SEP", numero: "09" },
					{ inicial: "OCT", numero: "10" },
					{ inicial: "NOV", numero: "11" },
					{ inicial: "DIC", numero: "12" },
				];
				let mesMM = meses.filter((m) => m.numero == mes);
				console.log("FECHA", mesMM);
				return mesMM[0].inicial + "/" + anio;
			},
			formatoMesAnio(mes, fecha)
			{
				let mesusado = '';
                let anio = fecha.split('-')[0]
				switch (mes)
				{
					case 'Enero':
						mesusado = 'ENE';
						break;
                    case 'Febrero':
                        mesusado = 'FEB';
						break;
                    case 'Marzo':
                        mesusado = 'MAR';
						break;
                    case 'Abril':
                        mesusado = 'ABR';
						break;
                    case 'Mayo':
                        mesusado = 'MAY';
						break;
                    case 'Junio':
                        mesusado = 'JUN';
						break;
                    case 'Julio':
                        mesusado = 'JUL';
						break;
                    case 'Agosto':
                        mesusado = 'AGO';
						break;
                    case 'Septiembre':
                        mesusado = 'SEP';
						break;
                    case 'Octubre':
                        mesusado = 'OCT';
						break;
                    case 'Noviembre':
                        mesusado = 'NOV';
						break;
                    case 'Diciembre':
                        mesusado = 'DIC';
                        break;
				}
				mesusado = mesusado + '/' + anio;
				return mesusado;
			},
			//Funcion para agrupar las ordenes por profesional y mes
			async GroupOrdenes(lista_orden) {
				let pagos = sessionStorage.getItem("pagos");
				if (!pagos) {
					//	Agrupo primero por el profesional

					lista_orden.forEach((element) => {
						let result = {};
						result.id_medico = element.id_medico;
						result.profesional = element.profesional;
						result.diasliquidacion = element.diasliquidacion;
						result.ordenes = [];

						//Controlo las ordenes que posea ese profesional por mes
						lista_orden.forEach((mes) => {
							let mesOrden = {};
							mesOrden.mes = mes.mes;
							mesOrden.ListOrdenes = [];
							mesOrden.formaPago = mes.formaPago;
							mesOrden.total = parseFloat(0);
							mesOrden.liquidacionlista = 'No';
                            mesOrden.pagado = this.GetPagadoDef(parseInt(result.id_medico), mesOrden.mes);
							lista_orden.forEach((orden) => {
								if (
									orden.id_medico == result.id_medico &&
									orden.mes == mesOrden.mes
								) {
									let orden_Prof = {};
									orden_Prof.num_orden = orden.numero_orden;
									orden_Prof.fecha = orden.fecha;
									orden_Prof.hora = orden.hora;
									orden_Prof.preciomutual = parseFloat(orden.preciomutual);
									orden_Prof.realizado = orden.realizado;
									orden_Prof.presentada = orden.presentada;

                                    let liquidacion = this.diasdediff(orden_Prof.fecha)

									if (liquidacion > result.diasliquidacion)
									{
                                        mesOrden.liquidacionlista = 'Si';
									}

                                    if (orden_Prof.realizado == false || orden_Prof.presentada == false) {
										console.log(
											"Orden ",
											orden_Prof.num_orden,
											"no se llevo a cabo aun"
										);
									} else if (
										mesOrden.ListOrdenes.includes(orden_Prof) == false
									) {
										mesOrden.ListOrdenes.push(orden_Prof);
									}
								}
							});
							mesOrden.total = this.sumaTotal(mesOrden.ListOrdenes);
							if (
								result.ordenes.find((t) => t.mes == mesOrden.mes) ||
								mesOrden.ListOrdenes.length == 0
							) {
								console.log("Elemento ", mesOrden, "duplicado o vacio");
							} else {
								result.ordenes.push(mesOrden);
							}
						});
						console.log("Hoal");
                        result.totalapagar = this.sumaTotal2(result.ordenes);
						this.cambioenprof(result.id_medico, result.totalapagar);
						if (
							this.tabla_ordenes.find((x) => x.id_medico == result.id_medico)
						) {
							console.log("Elemento ", result, "duplicado");
						} else {
							this.tabla_ordenes.push(result);
						}
					});
					this.set_pagos(this.tabla_ordenes);
				} else {
					this.tabla_ordenes = JSON.parse(pagos);
				}
			},

			//Obtengo todas las ordenes
			async getOrdenes() {
				try {
					this.show = true;

					const res = await fetch(api);
					const data = await res.json();
					var lista_orden = data.results;
					var modo_pago = null;

					console.log("1");
					for (var i = 0; i < lista_orden.length; i++) {
						var medico = await this.getProfesional(
							lista_orden[i].id_medico.split("/")[4]
						);
						lista_orden[i].id_medico = medico.id_medico;
						lista_orden[i].profesional = medico.apellido + ", " + medico.nombre;
						lista_orden[i].diasliquidacion = medico.diasliquidacion;
						lista_orden[i].dni = medico.dni;
						lista_orden[i].formaPago = modo_pago;
						/*
							lista_orden[i].mes =
								lista_orden[i].fecha.split("-")[1] +
								"/" +
								lista_orden[i].fecha.split("-")[0];
							*/
						lista_orden[i].mes = this.formatMesAnio(
							lista_orden[i].fecha.split("-")[1],
							lista_orden[i].fecha.split("-")[0]
						);
					}
					console.log(lista_orden);

					this.GroupOrdenes(lista_orden);

					//this.btn_down_pdf=false;  //Habilito los botones

					if (this.tabla_ordenes.length == 0) {
						this.msj_tabla = " No se encuentran regitros en esta tabla ";
					}
				} catch (error) {
					console.log(error);
				} finally {
					this.show = false;
				}
			},
            async getPagado() {
				try {
                    let apiPag = new URL("http://localhost");
                    apiPag.pathname = "pagadoprofesionales";
                    //api.port = 8000;
                    apiPag.port = 8081;

                    const res = await fetch(apiPag);
					const data = await res.json();

                    this.lista_pagado = data.results;
                } catch (error) {
                    console.log(error);
                }
			},
			async cambioenprof(id_medico, totalapagarlo)
			{
                const item_prof = await fetch("http://localhost:8081/profesionales/" +
					id_medico);
                const data = await item_prof.json();
				data.totalapagar = totalapagarlo;
				this.respuesta = await axios.put(
					"http://localhost:8081/profesionales/" +
					id_medico +
					"/",
					data
                );
			},
            GetPagadoDef(id_medicardo, mesardo)
			{
                let pagado = 0;

				for (var i = 0; i < this.lista_pagado.length; i++) {
                    if ((parseInt(this.lista_pagado[i].id_medico.split("/")[4]) == id_medicardo) && (this.formatoMesAnio(this.lista_pagado[i].mespagado, this.lista_pagado[i].fecha) == mesardo)) {
						pagado = pagado + parseInt(this.lista_pagado[i].total);
					}
				}
				return pagado;
			},
			//Funcion para mostrar el modal
			showModal() {
				this.$refs["my-modal"].show();
			},

			//Funcion para esconder el modal
			hideModal() {
				this.$refs["my-modal"].hide();
			},

			//Funcion para mostrar el modal de edicion
			editarPago(item, index) {
				this.editar = item;
				console.log("Elemento a modificar: ", this.editar);
				this.showModal();
			},

			//Funcion para modificar la forma de pago
			putModoPago(mes) {
				try {
					this.tabla_ordenes.forEach((x) => {
						for (var i = 0; i < x.ordenes.length; i++) {
							if (x.ordenes[i].mes == mes) {
								x.ordenes[i].formaPago = this.selected;
								break;
							}
						}
					});
					this.hideModal();
					swal("¡ESTADO GUARDADO¡", " ", "success");
					console.log(this.tabla_ordenes);
				} catch (error) {
					this.hideModal();
					swal("¡ERROR¡", "No se pudo guardar los cambios ", "error");
					console.log(error);
				} finally {
					this.set_pagos(this.tabla_ordenes);
				}
			},

			/*
			auxOrdenesMes(orden){
				this.orden_del_mes.push(orden);
			},
			*/

			//Funcion para generar el comprobante
			generarPDF(item) {
				let data_ordenes = {};
				//data_ordenes.ID = item.id_medico;
				//data_ordenes.profesional = item.profesional;
				data_ordenes.mes = item.mes;
				data_ordenes.ordenes = item.ListOrdenes;
				data_ordenes.modo_pago = item.formaPago;
				data_ordenes.total = this.sumaTotal(data_ordenes.ordenes);
				console.log("LISTADO: ", data_ordenes.ordenes);
				this.tabla_ordenes.forEach((data) => {
					if (data.ordenes.find((x) => x.mes == data_ordenes.mes)) {
						data_ordenes.ID = data.id_medico;
						data_ordenes.profesional = data.profesional;
                        data_ordenes.diasliquidacion = data.diasliquidacion;
					}
				});
				//this.ordenAPDF = { ...item };
				this.ordenAPDF = data_ordenes;
				this.$refs.html2Pdf.generatePdf();
			},

			//Funcion para actualizar la paginacion
			onFiltered(filteredItems) {
				// Trigger pagination to update the number of buttons/pages due to filtering
				this.totalRows = filteredItems.length;
				this.currentPage = 1;
			},
			onShown() {
				// Focus the cancel button when the overlay is showing
				//this.$refs.cancel.focus();
			},
			onHidden() {
				// Focus the show button when the overlay is removed
				//this.$refs.show.focus();
			},
		},
		beforeMount() {
			this.show = true;
			this.getOrdenes();
			this.getPagado();
			console.log(this.formatoMesAnio('Febrero', '02-03-2021'));
			//this.saveFile();
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
	/*
.container {
  float: left;
  width: 85%
}
aside{
  float: right;
  width: 15%;
}
*/
</style>
