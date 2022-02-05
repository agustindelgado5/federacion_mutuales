<template>
	<div>
		<h6>Los campos en (*) son obligatorios</h6>

		<b-form>
			<b-card no-body class="mb-1">
				<b-card-header header-tag="header" class="p-1" role="tab">
					<b-button
						block
						v-b-toggle.accordion-1
						style="background-color: darkorange"
						>Datos Personales:</b-button
					>
				</b-card-header>
				<b-collapse
					id="accordion-1"
					visible
					accordion="my-accordion"
					role="tabpanel"
				>
					<b-card-body>
						<b-form-group label="*Id Medico" label-for="id_medico">
							<b-form-input
								id="id_medico"
								v-model="item_prof.id_medico"
								type="number"
								placeholder="Ingrese un Numero"
								invalid-feedback="Complete este campo"
								:state="validacion.id_medico.estado"
								required
								:disabled="true"
							>
							</b-form-input>
							<b-form-invalid-feedback id="id_medico-live-feedback"
								>{{ validacion.id_medico.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
						<b-form-group label="*Matricula" label-for="matricula">
							<b-form-input
								id="matricula"
								v-model="item_prof.matricula"
								type="number"
								placeholder="Ingrese un Numero"
								invalid-feedback="Complete este campo"
								:state="validacion.matricula.estado"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="matricula-live-feedback"
								>{{ validacion.matricula.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
						<b-form-group label="*Nombre/s" label-for="nombre">
							<b-form-input
								id="nombre"
								v-model="item_prof.nombre"
								type="text"
								placeholder="*Ingrese los Nombre/s"
								:state="validacion.nombre.estado"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="nombre-live-feedback"
								>{{ validacion.nombre.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
						<b-form-group label="*Apellido/s" label-for="apellido">
							<b-form-input
								id="apellido"
								v-model="item_prof.apellido"
								type="text"
								placeholder="*Ingrese los Apellido/s"
								:state="validacion.apellido.estado"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="apellido-live-feedback"
								>{{ validacion.apellido.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
						<b-form-group label="*DNI" label-for="dni">
							<b-form-input
								id="dni"
								v-model="item_prof.dni"
								type="number"
								placeholder="Ingrese un DNI"
								:state="validacion.dni.estado"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="dni-live-feedback"
								>{{ validacion.dni.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="*Fecha de ingreso" label-for="fecha_ingreso">
							<b-form-input
								id="fecha_ingreso"
								v-model="item_prof.fecha_ingreso"
								type="date"
								:state="validacion.fecha_ingreso.estado"
								placeholder="Ingrese una fecha"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="fecha_ingreso-live-feedback"
								>{{ validacion.fecha_ingreso.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
						<b-form-group label="Especialidad" label-for="especialidad">
							<b-form-input
								id="especialidad"
								:state="validacion.especialidad.estado"
								v-model="item_prof.especialidad"
								type="text"
								placeholder="*Ingrese la Especialidad"
								invalid-feedback="Complete este campo"
							>
							</b-form-input>
							<b-form-invalid-feedback id="especialidad-live-feedback"
								>{{ validacion.especialidad.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
					</b-card-body>
				</b-collapse>
			</b-card>
			<!-- <h4>Domicilio:</h4> -->
			<b-card no-body class="mb-1">
				<b-card-header header-tag="header" class="p-1" role="tab">
					<b-button
						block
						v-b-toggle.accordion-2
						style="background-color: darkorange"
						>Domicilio:</b-button
					>
				</b-card-header>
				<b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
					<b-card-body>
						<b-form-group label="*Calle" label-for="domicilio">
							<b-form-input
								id="domicilio"
								v-model="item_prof.domicilio"
								:state="validacion.domicilio.estado"
								type="text"
								placeholder="Ingrese una calle"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="domicilio-live-feedback"
								>{{ validacion.domicilio.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="*Localidad" label-for="localidad">
							<b-form-input
								id="localidad"
								v-model="item_prof.localidad"
								:state="validacion.localidad.estado"
								type="text"
								placeholder="Ingrese una localidad"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="localidad-live-feedback"
								>{{ validacion.localidad.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
						<b-form-group label="*Provincia" label-for="provincia">
							<b-form-select
								id="provincia"
								v-model="item_prof.provincia"
								type="text"
								:state="validacion.provincia.estado"
								placeholder="Ingrese una provincia"
								invalid-feedback="Complete este campo"
								required
								:options="options"
							>
							</b-form-select>
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
				<b-collapse id="accordion-3" accordion="my-accordion" role="tabpanel">
					<b-card-body>
						<b-form-group label="Email" label-for="email">
							<b-form-input
								id="email"
								v-model="item_prof.email"
								:state="validacion.email.estado"
								type="email"
								placeholder="Ingrese un email"
								invalid-feedback="Complete este campo"
							>
							</b-form-input>
							<b-form-invalid-feedback id="email-live-feedback"
								>{{ validacion.email.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="Telefono fijo" label-for="tel_fijo">
							<b-form-input
								id="tel_fijo"
								:state="validacion.tel_fijo.estado"
								v-model="item_prof.tel_fijo"
								type="number"
								placeholder="Ingrese un numero"
							>
							</b-form-input>
							<b-form-invalid-feedback id="tel_fijo-live-feedback"
								>{{ validacion.tel_fijo.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="Celular" label-for="tel_celular">
							<b-form-input
								id="tel_celular"
								v-model="item_prof.tel_celular"
								:state="validacion.tel_celular.estado"
								type="number"
								placeholder="Ingrese un numero"
							>
							</b-form-input>
							<b-form-invalid-feedback id="tel_celular-live-feedback"
								>{{ validacion.tel_celular.mensaje }}
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
						>Datos Bancarios:</b-button
					>
				</b-card-header>
				<b-collapse id="accordion-4" accordion="my-accordion" role="tabpanel">
					<b-card-body>
						<b-form-group label="*Banco" label-for="banco">
							<v-autocomplete
								id="banco"
								v-model="item_prof.banco"
								:items="options_banco"
								type="text"
								solo
								filled
							></v-autocomplete>
							
							<b-form-invalid-feedback id="banco-live-feedback"
								>{{ validacion.banco.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="*CBU" label-for="cbu">
							<b-form-input
								id="cbu"
								v-model="item_prof.cbu"
								:state="validacion.cbu.estado"
								type="text"
								placeholder="Ingrese un cbu"
							>
							</b-form-input>
							<b-form-invalid-feedback id="cbu-live-feedback"
								>{{ validacion.cbu.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="*Alias CBU" label-for="alias_cbu">
							<b-form-input
								id="alias_cbu"
								v-model="item_prof.alias_cbu"
								:state="validacion.alias_cbu.estado"
								type="text"
								placeholder="Ingrese un alias"
							>
							</b-form-input>
							<b-form-invalid-feedback id="alias_cbu-live-feedback"
								>{{ validacion.alias_cbu.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group
							label="Titular de la cuenta"
							label-for="titular_cuenta"
						>
							<b-form-input
								id="titular_cuenta"
								v-model="item_prof.titular_cuenta"
								:state="validacion.titular_cuenta.estado"
								type="text"
								placeholder="Ingrese un titular"
							>
							</b-form-input>
							<b-form-invalid-feedback id="titular_cuenta-live-feedback"
								>{{ validacion.titular_cuenta.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="Tipo de cuenta" label-for="tipo_cuenta">
							<b-form-select
								id="tipo_cuenta"
								v-model="item_prof.tipo_cuenta"
								:state="validacion.tipo_cuenta.estado"
								type="text"
								placeholder="Ingrese un tipo"
								:options="tipo_cuenta_options"
							>
							</b-form-select>
							<b-form-invalid-feedback id="tipo_cuenta-live-feedback"
								>{{ validacion.tipo_cuenta.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
					</b-card-body>
				</b-collapse>
			</b-card>
		</b-form>
		<!-- {{item_med}}
        <br>
        <br>
        {{ data }} -->
		<b-button class="mt-2" variant="success" block @click="putProfesional()"
			>Modificar</b-button
		>
	</div>
</template>

<script>
	import { APIControler } from "@/store/APIControler";
	import axios from "axios";

	export default {
		props: {
			item_prof: {},

			updateTable: Function,
		},
		data() {
			return {
				profesional: {},
				respuesta: {},
				validarError: {
					validateStatus: function (status) {
						return status < 500; // Resolve only if the status code is less than 500
					},
				},
				validacion: {
					id_medico: { estado: null, mensaje: "" },
					matricula: { estado: null, mensaje: "" },
					nombre: { estado: null, mensaje: "" },
					apellido: { estado: null, mensaje: "" },
					dni: { estado: null, mensaje: "" },
					fecha_ingreso: { estado: null, mensaje: "" },
					especialidad: { estado: null, mensaje: "" },
					domicilio: { estado: null, mensaje: "" },
					provincia: { estado: null, mensaje: "" },
					localidad: { estado: null, mensaje: "" },
					email: { estado: null, mensaje: "" },
					tel_fijo: { estado: null, mensaje: "" },
					tel_celular: { estado: null, mensaje: "" },
					cbu: { estado: null, mensaje: "" },
					alias_cbu: { estado: null, mensaje: "" },
					titular_cuenta: { estado: null, mensaje: "" },
					tipo_cuenta: { estado: null, mensaje: "" },
					banco: { estado: null, mensaje: "" },
				},
				options: [
					{ value: "Buenos Aires", text: "1- Buenos Aires" },
					{ value: "Catamarca", text: "2- Catamarca" },
					{ value: "Chaco", text: "3- Chaco" },
					{ value: "Chubut", text: "4- Chubut" },
					{ value: "Córdoba", text: "5- Córdoba" },
					{ value: "Corrientes", text: "6- Corrientes" },
					{ value: "Entre Ríos", text: "7- Entre Ríos" },
					{ value: "Formosa", text: "8- Formosa" },
					{ value: "Jujuy", text: "9- Jujuy" },
					{ value: "La Pampa", text: "10- La Pampa" },
					{ value: "La Rioja", text: "11- La Rioja" },
					{ value: "Mendoza", text: "12- Mendoza" },
					{ value: "Misiones", text: "13- Misiones" },
					{ value: "Neuquén", text: "14- Neuquén" },
					{ value: "Río Negro", text: "15- Río Negro" },
					{ value: "Salta", text: "16- Salta" },
					{ value: "San Juan", text: "17- San Juan" },
					{ value: "San Luis", text: "18- San Luis" },
					{ value: "Santa Cruz", text: "19- Santa Cruz" },
					{ value: "Santa Fe", text: "20- Santa Fe" },
					{ value: "Santiago del Estero", text: "21- Santiago del Estero" },
					{ value: "Tierra del Fuego", text: "22- Tierra del Fuego" },
					{ value: "Tucumán", text: "23- Tucumán" },
				],
				tipo_cuenta_options: [
					{ value: "Caja de Ahorro", text: "Caja de Ahorro" },
					{ value: "Cuenta Corriente", text: "Cuenta Corriente" },
					{ value: "Otro", text: "Otro" },
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
		methods: {
			async getProfesionales() {
				let profesionalAPI = new APIControler();
				profesionalAPI.apiUrl.pathname = "profesionales/";
				this.data = await profesionalAPI.getData(this.profesional);
				this.data.forEach((element) => {
					let option = {};
					option.value =
						"http://localhost:8081/profesionales/" + element.id_medico + "/";
					option.text = element.profesional;
					console.log(option);
					this.options.push(option);
				});
			},
			async putProfesional() {
				try {
					this.respuesta = await axios.put(
						"http://localhost:8081/profesionales/" +
							this.item_prof.id_medico +
							"/",
						this.item_prof,
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
					console.log(error.toJSON());
				}
				this.cargarFeedback();
				this.updateTable();
			},

			cargarFeedback() {
				let valido;
				for (let key in this.validacion) {
					valido = !this.respuesta.hasOwnProperty(key);
					this.validacion[key].estado = valido;
					//console.log(key);
					if (!valido) this.validacion[key].mensaje = this.respuesta[key][0];
				}
			},
		},
	};
</script>

<style></style>
