<template>
	<div>
		<h6>Los campos en (*) son obligatorios</h6>
		<h4>Datos</h4>

		<b-form>
			<b-card no-body class="mb-1">
				<b-card-header header-tag="header" class="p-1" role="tab">
					<b-button
						block
						v-b-toggle.accordion-1
						style="background-color: darkorange"
						>Datos Principales:</b-button
					>
				</b-card-header>
				<b-collapse
					id="accordion-1"
					visible
					accordion="my-accordion"
					role="tabpanel"
				>
					<b-card-body>
						<!-- matricula_farm -->
						<b-form-group
							label="*Matricula Farmacia"
							label-for="matricula_farm"
							@submit.stop.prevent="handleSubmit"
						>
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
							<b-form-invalid-feedback id="matricula_farm-live-feedback"
								>{{ validacion.matricula_farm.mensaje }}
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
							<b-form-invalid-feedback id="farmacia-live-feedback"
								>{{ validacion.farmacia.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<!-- cuit -->
						<b-form-group
							label="*CUIT Farmacia"
							label-for="cuit"
							@submit.stop.prevent="handleSubmit"
						>
							<b-form-input
								id="cuit"
								v-model="farmacia.cuit"
								type="text"
								placeholder="Ingrese el CUIT de la farmacia"
								:state="validacion.cuit.estado"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="cuit-live-feedback"
								>{{ validacion.cuit.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
					</b-card-body>
				</b-collapse>
			</b-card>
			<b-card no-body class="mb-1">
				<b-card-header header-tag="header" class="p-1" role="tab">
					<b-button
						block
						v-b-toggle.accordion-2
						style="background-color: darkorange"
						>Direccion:</b-button
					>
				</b-card-header>
				<b-collapse
					id="accordion-2"
					visible
					accordion="my-accordion"
					role="tabpanel"
				>
					<b-card-body>
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
							<b-form-invalid-feedback id="localidad-live-feedback"
								>{{ validacion.localidad.mensaje }}
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
							<b-form-invalid-feedback id="direccion-live-feedback"
								>{{ validacion.direccion.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<!-- cod_postal -->
						<b-form-group
							label="*Codigo postal"
							label-for="cod_postal"
							@submit.stop.prevent="handleSubmit"
						>
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
							<b-form-invalid-feedback id="cod_postal-live-feedback"
								>{{ validacion.cod_postal.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
					</b-card-body>
				</b-collapse>
			</b-card>
			<b-card no-body class="mb-1">
				<b-card-header header-tag="header" class="p-1" role="tab">
					<b-button
						block
						v-b-toggle.accordion-3
						style="background-color: darkorange"
						>Contacto:</b-button
					>
				</b-card-header>
				<b-collapse
					id="accordion-3"
					visible
					accordion="my-accordion"
					role="tabpanel"
				>
					<b-card-body>
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
							<b-form-invalid-feedback id="email-live-feedback"
								>{{ validacion.email.mensaje }}
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
							<b-form-invalid-feedback id="tel_fijo-live-feedback"
								>{{ validacion.tel_fijo.mensaje }}
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
							<b-form-invalid-feedback id="tel_celular-live-feedback"
								>{{ validacion.tel_celular.mensaje }}
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
							<b-form-invalid-feedback id="representante-live-feedback"
								>{{ validacion.representante.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
					</b-card-body>
				</b-collapse>
			</b-card>
			<b-card no-body class="mb-1">
				<b-card-header header-tag="header" class="p-1" role="tab">
					<b-button
						block
						v-b-toggle.accordion-4
						style="background-color: darkorange"
						>Datos De Pago:</b-button
					>
				</b-card-header>
				<b-collapse
					id="accordion-4"
					visible
					accordion="my-accordion"
					role="tabpanel"
				>
					<b-card-body>
						<!-- cbu -->
						<b-form-group label="*CBU" label-for="cbu">
							<b-form-input
								id="cbu"
								v-model="farmacia.cbu"
								type="number"
								placeholder="*Ingrese el cbu"
								:state="validacion.cbu.estado"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="cbu-live-feedback"
								>{{ validacion.cbu.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<!-- entidad_bancaria -->
						<b-form-group
							label="*Entidad Bancaria"
							label-for="entidad_bancaria"
						>
							<!--
							<b-form-input
								id="entidad_bancaria"
								v-model="farmacia.entidad_bancaria"
								type="text"
								placeholder="*Ingrese la entidad bancaria"
								:state="validacion.entidad_bancaria.estado"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							-->
							<v-autocomplete
								id="entidad_bancaria"
								v-model="farmacia.entidad_bancaria"
								:items="options_banco"
								type="text"
								solo
								filled
							></v-autocomplete>
							<b-form-invalid-feedback id="entidad_bancaria-live-feedback"
								>{{ validacion.entidad_bancaria.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<!-- nro_cuenta -->
						<b-form-group
							label="*Numero De Cuenta"
							label-for="nro_cuenta"
							@submit.stop.prevent="handleSubmit"
						>
							<b-form-input
								id="nro_cuenta"
								v-model="farmacia.nro_cuenta"
								type="number"
								placeholder="Ingrese el número de cuenta"
								:state="validacion.nro_cuenta.estado"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="nro_cuenta-live-feedback"
								>{{ validacion.nro_cuenta.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
						<!--tipo_cuenta-->
						<b-form-group label="*Tipo de cuenta" label-for="tipo_cuenta">
							<b-form-select
								id="tipo_cuenta"
								v-model="farmacia.tipo_cuenta"
								:state="validacion.tipo_cuenta.estado"
								type="text"
								placeholder="Ingrese un tipo de cuenta"
								invalid-feedback="Complete este campo"
								required
								:options="options1"
							>
							</b-form-select>
						</b-form-group>
						<!--modalidad_pago-->
						<b-form-group label="*Modalidad De Pago" label-for="modalidad_pago">
							<b-form-select
								id="modalidad_pago"
								v-model="farmacia.modalidad_pago"
								:state="validacion.modalidad_pago.estado"
								type="text"
								placeholder="Ingrese la modalidad de pago"
								invalid-feedback="Complete este campo"
								required
								:options="options2"
							>
							</b-form-select>
						</b-form-group>
					</b-card-body>
				</b-collapse>
			</b-card>
		</b-form>

		<b-button class="mt-2" variant="success" block @click="putFarmacia()"
			>Modificar</b-button
		>
	</div>
</template>

<script>
	import { APIControler } from "@/store/APIControler";
	import axios from "axios";

	export default {
		props: {
			farmacia: {},
			updateTable: Function,
		},
		data() {
			return {
				farmacias: {},
				data: {},
				options: [{ value: null, text: "Elija una farmacia", disabled: true }],

				validacion: {
					//cod_farmacia: { estado: null, mensaje: "" },
					cuit: { estado: null, mensaje: "" },
					farmacia: { estado: null, mensaje: "" },
					direccion: { estado: null, mensaje: "" },
					localidad: { estado: null, mensaje: "" },
					email: { estado: null, mensaje: "" },
					cod_postal: { estado: null, mensaje: "" },
					tel_fijo: { estado: null, mensaje: "" },
					tel_celular: { estado: null, mensaje: "" },
					matricula_farm: { estado: null, mensaje: "" },
					representante: { estado: null, mensaje: "" },
					cbu: { estado: null, mensaje: "" },
					entidad_bancaria: { estado: null, mensaje: "" },
					nro_cuenta: { estado: null, mensaje: "" },
					tipo_cuenta: { estado: null, mensaje: "" },
					modalidad_pago: { estado: null, mensaje: "" },
				},
				options1: [
					{ value: "Cuenta Corriente", text: "1- Cuenta Corriente" },
					{ value: "Caja de ahorros", text: "2- Caja de ahorros" },
				],

				options2: [
					{ value: "Efectivo", text: "1- Efectivo" },
					{ value: "Transferencia", text: "2- Transferencia" },
				],
				options_banco: [
					{
						value: "00007-BANCO DE GALICIA Y BUENOS AIRES S.A.U.",
						text: "00007-BANCO DE GALICIA Y BUENOS AIRES S.A.U.",
					},
					{
						value: "00011-BANCO DE LA NACION ARGENTINA",
						text: "00011-BANCO DE LA NACION ARGENTINA",
					},
					{
						value: "00014-BANCO DE LA PROVINCIA DE BUENOS AIRES",
						text: "00014-BANCO DE LA PROVINCIA DE BUENOS AIRES",
					},
					{
						value: "00015-INDUSTRIAL AND COMMERCIAL BANK OF CHINA",
						text: "00015-INDUSTRIAL AND COMMERCIAL BANK OF CHINA",
					},
					{ value: "00016-CITIBANK N.A.", text: "00016-CITIBANK N.A." },
					{
						value: "00017-BANCO BBVA ARGENTINA S.A.",
						text: "00017-BANCO BBVA ARGENTINA S.A.",
					},
					{
						value: "00020-BANCO DE LA PROVINCIA DE CORDOBA S.A.",
						text: "00020-BANCO DE LA PROVINCIA DE CORDOBA S.A.",
					},
					{
						value: "00027-BANCO SUPERVIELLE S.A.",
						text: "00027-BANCO SUPERVIELLE S.A.",
					},
					{
						value: "00029-BANCO DE LA CIUDAD DE BUENOS AIRES",
						text: "00029-BANCO DE LA CIUDAD DE BUENOS AIRES",
					},
					{
						value: "00034-BANCO PATAGONIA S.A.",
						text: "00034-BANCO PATAGONIA S.A.",
					},
					{
						value: "00044-BANCO HIPOTECARIO S.A.",
						text: "00044-BANCO HIPOTECARIO S.A.",
					},
					{
						value: "00045-BANCO DE SAN JUAN S.A.",
						text: "00045-BANCO DE SAN JUAN S.A.",
					},
					{
						value: "00065-BANCO MUNICIPAL DE ROSARIO",
						text: "00065-BANCO MUNICIPAL DE ROSARIO",
					},
					{
						value: "00072-BANCO SANTANDER RIO S.A.text: ",
						text: "00072-BANCO SANTANDER RIO S.A.",
					},
					{
						value: "00083-BANCO DEL CHUBUT S.A.",
						text: "00083-BANCO DEL CHUBUT S.A.",
					},
					{
						value: "00086-BANCO DE SANTA CRUZ S.A.",
						text: "00086-BANCO DE SANTA CRUZ S.A.",
					},
					{
						value: "00093-BANCO DE LA PAMPA SOCIEDAD DE ECONOMÍA M",
						text: "00093-BANCO DE LA PAMPA SOCIEDAD DE ECONOMÍA M",
					},
					{
						value: "00094-BANCO DE CORRIENTES S.A.",
						text: "00094-BANCO DE CORRIENTES S.A.",
					},
					{ value: "00143-BRUBANK S.A.U.", text: "00143-BRUBANK S.A.U." },
					{
						value: "00097-BANCO PROVINCIA DEL NEUQUÉN SOCIEDAD ANÓ",
						text: "00097-BANCO PROVINCIA DEL NEUQUÉN SOCIEDAD ANÓ",
					},
					{
						value: "00147-BANCO INTERFINANZAS S.A.",
						text: "00147-BANCO INTERFINANZAS S.A.",
					},
					{
						value: "00150-HSBC BANK ARGENTINA S.A.",
						text: "00150-HSBC BANK ARGENTINA S.A.",
					},
					{
						value: "00158-OPEN BANK ARGENTINA S.A.",
						text: "00158-OPEN BANK ARGENTINA S.A.",
					},
					{
						value: "00165-JPMORGAN CHASE BANK, NATIONAL ASSOCIATION",
						text: "00165-JPMORGAN CHASE BANK, NATIONAL ASSOCIATION",
					},
					{
						value: "00191-BANCO CREDICOOP COOPERATIVO LIMITADO",
						text: "00191-BANCO CREDICOOP COOPERATIVO LIMITADO",
					},
					{
						value: "00198-BANCO DE VALORES S.A.",
						text: "00198-BANCO DE VALORES S.A.",
					},
					{ value: "00247-BANCO ROELA S.A.", text: "00247-BANCO ROELA S.A." },
					{ value: "00254-BANCO MARIVA S.A.", text: "00254-BANCO MARIVA S.A." },
					{
						value: "00259-BANCO ITAU ARGENTINA S.A.",
						text: "00259-BANCO ITAU ARGENTINA S.A.",
					},
					{
						value: "00262-BANK OF AMERICA, NATIONAL ASSOCIATION",
						text: "00262-BANK OF AMERICA, NATIONAL ASSOCIATION",
					},
					{ value: "00266-BNP PARIBAS", text: "00266-BNP PARIBAS" },
					{
						value: "00268-BANCO PROVINCIA DE TIERRA DEL FUEGO",
						text: "00268-BANCO PROVINCIA DE TIERRA DEL FUEGO",
					},
					{
						value: "00269-BANCO DE LA REPUBLICA ORIENTAL DEL URUGUAY",
						text: "00269-BANCO DE LA REPUBLICA ORIENTAL DEL URUGUAY",
					},
					{ value: "00277-BANCO SAENZ S.A.", text: "00277-BANCO SAENZ S.A." },
					{
						value: "00281-BANCO MERIDIAN S.A.",
						text: "00281-BANCO MERIDIAN S.A.",
					},
					{ value: "00285-BANCO MACRO S.A.", text: "00285-BANCO MACRO S.A." },
					{
						value: "00299-BANCO COMAFI SOCIEDAD ANONIMA",
						text: "00299-BANCO COMAFI SOCIEDAD ANONIMA",
					},
					{
						value: "00300-BANCO DE INVERSION Y COMERCIO EXTERIOR S",
						text: "00300-BANCO DE INVERSION Y COMERCIO EXTERIOR S",
					},
					{ value: "00301-BANCO PIANO S.A.", text: "00301-BANCO PIANO S.A." },
					{
						value: "00305-BANCO JULIO SOCIEDAD ANONIMA",
						text: "00305-BANCO JULIO SOCIEDAD ANONIMA",
					},
					{
						value: "00309-BANCO RIOJA SOCIEDAD ANONIMA UNIPERSONAL",
						text: "00309-BANCO RIOJA SOCIEDAD ANONIMA UNIPERSONAL",
					},
					{
						value: "00310-BANCO DEL SOL S.A.",
						text: "00310-BANCO DEL SOL S.A.",
					},
					{
						value: "00311-NUEVO BANCO DEL CHACO S. A.",
						text: "00311-NUEVO BANCO DEL CHACO S. A.",
					},
					{ value: "00312-BANCO VOII S.A.", text: "00312-BANCO VOII S.A." },
					{
						value: "00315-BANCO DE FORMOSA S.A.",
						text: "00315-BANCO DE FORMOSA S.A.",
					},
					{ value: "00319-BANCO CMF S.A.", text: "00319-BANCO CMF S.A." },
					{
						value: "00321-BANCO DE SANTIAGO DEL ESTERO S.A.",
						text: "00321-BANCO DE SANTIAGO DEL ESTERO S.A.",
					},
					{
						value: "00322-BANCO INDUSTRIAL S.A.",
						text: "00322-BANCO INDUSTRIAL S.A.",
					},
					{
						value: "00330-NUEVO BANCO DE SANTA FE SOCIEDAD ANONIMA",
						text: "00330-NUEVO BANCO DE SANTA FE SOCIEDAD ANONIMA",
					},
					{
						value: "00331-BANCO CETELEM ARGENTINA S.A.",
						text: "00331-BANCO CETELEM ARGENTINA S.A.",
					},
					{
						value: "00332-BANCO DE SERVICIOS FINANCIEROS S.A.",
						text: "00332-BANCO DE SERVICIOS FINANCIEROS S.A.",
					},
					{
						value: "00336-BANCO BRADESCO ARGENTINA S.A.U.",
						text: "00336-BANCO BRADESCO ARGENTINA S.A.U.",
					},
					{
						value: "00338-BANCO DE SERVICIOS Y TRANSACCIONES S.A.",
						text: "00338-BANCO DE SERVICIOS Y TRANSACCIONES S.A.",
					},
					{ value: "00339-RCI BANQUE S.A.", text: "00339-RCI BANQUE S.A." },
					{
						value: "00340-BACS BANCO DE CREDITO Y SECURITIZACION S",
						text: "00340-BACS BANCO DE CREDITO Y SECURITIZACION S",
					},
					{
						value: "00341-BANCO MASVENTAS S.A.",
						text: "00341-BANCO MASVENTAS S.A.",
					},
					{ value: "00384-WILOBANK S.A.", text: "00384-WILOBANK S.A." },
					{
						value: "00386-NUEVO BANCO DE ENTRE RÍOS S.A.",
						text: "00386-NUEVO BANCO DE ENTRE RÍOS S.A.",
					},
					{
						value: "00389-BANCO COLUMBIA S.A.",
						text: "00389-BANCO COLUMBIA S.A.",
					},
					{ value: "00426-BANCO BICA S.A.", text: "00426-BANCO BICA S.A." },
					{ value: "00431-BANCO COINAG S.A.", text: "00431-BANCO COINAG S.A." },
					{
						value: "00432-BANCO DE COMERCIO S.A.",
						text: "00432-BANCO DE COMERCIO S.A.",
					},
					{
						value: "00435-BANCO SUCREDITO REGIONAL S.A.U.",
						text: "00435-BANCO SUCREDITO REGIONAL S.A.U.",
					},
					{ value: "00448-BANCO DINO S.A.", text: "00448-BANCO DINO S.A." },
					{
						value: "00515-BANK OF CHINA LIMITED SUCURSAL BUENOS AI",
						text: "00515-BANK OF CHINA LIMITED SUCURSAL BUENOS AI",
					},
					{
						value: "44059-FORD CREDIT COMPAÑIA FINANCIERA S.A.",
						text: "44059-FORD CREDIT COMPAÑIA FINANCIERA S.A.",
					},
					{
						value: "44077-COMPAÑIA FINANCIERA ARGENTINA S.A.",
						text: "44077-COMPAÑIA FINANCIERA ARGENTINA S.A.",
					},
					{
						value: "44088-VOLKSWAGEN FINANCIAL SERVICES COMPAÑIA F",
						text: "44088-VOLKSWAGEN FINANCIAL SERVICES COMPAÑIA F",
					},
					{
						value: "44090-CORDIAL COMPAÑÍA FINANCIERA S.A.",
						text: "44090-CORDIAL COMPAÑÍA FINANCIERA S.A.",
					},
					{
						value: "44092-FCA COMPAÑIA FINANCIERA S.A.",
						text: "44092-FCA COMPAÑIA FINANCIERA S.A.",
					},
					{
						value: "44093-GPAT COMPAÑIA FINANCIERA S.A.U.",
						text: "44093-GPAT COMPAÑIA FINANCIERA S.A.U.",
					},
					{
						value: "44095-ROMBO COMPAÑÍA FINANCIERA S.A.",
						text: "44095-ROMBO COMPAÑÍA FINANCIERA S.A.",
					},
					{
						value: "44096-JOHN DEERE CREDIT COMPAÑÍA FINANCIERA S.",
						text: "44096-JOHN DEERE CREDIT COMPAÑÍA FINANCIERA S.",
					},
					{
						value: "44098-PSA FINANCE ARGENTINA COMPAÑÍA FINANCIER",
						text: "44098-PSA FINANCE ARGENTINA COMPAÑÍA FINANCIER",
					},
					{
						value: "44099-TOYOTA COMPAÑÍA FINANCIERA DE ARGENTINA",
						text: "44099-TOYOTA COMPAÑÍA FINANCIERA DE ARGENTINA",
					},
					{
						value: "45030-NARANJA DIGITAL COMPAÑÍA FINANCIERA S.A.",
						text: "45030-NARANJA DIGITAL COMPAÑÍA FINANCIERA S.A.",
					},
					{
						value: "45056-MONTEMAR COMPAÑIA FINANCIERA S.A.",
						text: "45056-MONTEMAR COMPAÑIA FINANCIERA S.A.",
					},
					{
						value: "45072-TRANSATLANTICA COMPAÑIA FINANCIERA S.A.",
						text: "45072-TRANSATLANTICA COMPAÑIA FINANCIERA S.A.",
					},
					{
						value: "65203-CREDITO REGIONAL COMPAÑIA FINANCIERA S.A",
						text: "65203-CREDITO REGIONAL COMPAÑIA FINANCIERA S.A",
					},
				],
			};
		},
		created: function () {
			//console.log('Funcion realizada');
			this.getFarmacias();
		},
		methods: {
			async getFarmacias() {
				let farmaciaAPI = new APIControler();
				farmaciaAPI.apiUrl.pathname = "farmacias/";
				this.data = await farmaciaAPI.getData(this.farmacias);
				this.data.forEach((element) => {
					let option = {};
					option.value =
						"http://localhost:8081/farmacias/" + element.cod_farmacia + "/";
					option.text = element.farmacia;
					console.log(option);
					this.options.push(option);
				});
			},

			async putFarmacia() {
				let respuesta = "vacio";
				// try{
				await axios
					.put(
						"http://localhost:8081/farmacias/" +
							this.farmacia.cod_farmacia +
							"/",
						this.farmacia
					)
					.then(function (data) {
						swal("Operación Exitosa", " ", "success");
					})
					.catch(function (error) {
						const mje =
							error.response.status < 500
								? "Los datos no son válidos"
								: "Se ha detectado un problema ";
						swal("¡ERROR!", mje, "error");
						respuesta = error.response.data;
					});
				this.cargarFeedback(respuesta);
				this.updateTable();
			},

			cargarFeedback(respuestaAPI) {
				let valido;
				for (let key in this.validacion) {
					valido = !respuestaAPI.hasOwnProperty(key);
					this.validacion[key].estado = valido;
					if (!valido) this.validacion[key].mensaje = respuestaAPI[key][0];
				}
			},
		},
	};
</script>

<style></style>
