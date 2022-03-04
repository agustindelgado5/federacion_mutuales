<template>
	<div class="accordion" role="tablist">
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
						<!-- 
						<b-form-group label="*N° Socio" label-for="numero_socio">
							<b-form-input
								id="numero_socio"
								v-model="socio.numero_socio"
								:state="validacion.numero_socio.estado"
								type="number"
								placeholder="Ingrese un Numero"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="numero_socio-live-feedback"
								>{{ validacion.numero_socio.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
						-->
						<b-form-group label="*Nombre/s" label-for="nombre">
							<b-form-input
								id="nombre"
								v-model="socio.nombre"
								:state="validacion.nombre.estado"
								type="text"
								placeholder="*Ingrese los Nombre/s"
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
								v-model="socio.apellido"
								:state="validacion.apellido.estado"
								type="text"
								placeholder="*Ingrese los Apellido/s"
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
								v-model="socio.dni"
								:state="validacion.dni.estado"
								type="number"
								placeholder="Ingrese un DNI"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="dni-live-feedback"
								>{{ validacion.dni.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group
							label="*Fecha de nacimiento"
							label-for="fecha_nacimiento"
						>
							<b-form-input
								id="fecha_nacimiento"
								v-model="socio.fecha_nacimiento"
								:state="validacion.fecha_nacimiento.estado"
								type="date"
								placeholder="Ingrese una fecha"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="fecha_nacimiento-live-feedback"
								>{{ validacion.fecha_nacimiento.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group
							label="*Fecha de asociacion"
							label-for="fecha_asociacion"
						>
							<b-form-input
								id="fecha_asociacion"
								v-model="socio.fecha_asociacion"
								:state="validacion.fecha_asociacion.estado"
								type="date"
								placeholder="Ingrese la fecha de asociacion"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="fecha_asociacion-live-feedback"
								>{{ validacion.fecha_asociacion.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="*Mutual de asociación" label-for="id_mutual">
							<b-form-select
								id="id_mutual"
								v-model="socio.mutual"
								type="text"
								:state="validacion.mutual.estado"
								placeholder="Ingrese el ID de la mutual"
								invalid-feedback="Complete este campo"
								required
								:options="op_mutuales"
							>
							</b-form-select>
							<!-- <b-form-invalid-feedback id="id_mutual-live-feedback"
              >{{ validacion.id_mutual.mensaje }}
            </b-form-invalid-feedback> -->
						</b-form-group>

						<b-form-group label="*Método de pago" label-for="metodoPago">
							<b-form-select
								id="metodoPago"
								v-model="socio.metodoPago"
								:state="validacion.metodoPago.estado"
								type="text"
								placeholder="Ingrese un método de pago"
								invalid-feedback="Complete este campo"
								required
								:options="op_metodosPago"
							>
							</b-form-select>
							<b-form-invalid-feedback id="metodoPago-live-feedback"
								>{{ validacion.metodoPago.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
						<b-form-group v-show="socio.metodoPago=='Cobrador'" label="*Cobrador" label-for="id_cobrador">
							<b-form-select
								id="id_cobrador"
								v-model="socio.cobrador"
								type="text"
								:state="validacion.cobrador.estado"
								placeholder="Ingrese el ID del cobrador"
								invalid-feedback="Complete este campo"
								required
								:options="op_cobradores"
							>
							</b-form-select>
						</b-form-group>
						<b-form-group label="*Tiene Obra social" label-for="obra_social">
							<b-form-checkbox
								id="obra_social"
								v-model="socio.tieneObraSocial"
								:state="validacion.tieneObraSocial.estado"
								value="true"
								type="boolean"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-checkbox>
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
						>Domicilio:</b-button
					>
				</b-card-header>
				<b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
					<b-card-body>
						<b-form-group label="*Calle" label-for="calle">
							<b-form-input
								id="calle"
								v-model="socio.calle"
								:state="validacion.calle.estado"
								type="text"
								placeholder="Ingrese una calle"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="calle-live-feedback"
								>{{ validacion.calle.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="*Localidad" label-for="localidad">
							<b-form-select
								id="localidad"
								v-model="socio.localidad"
								:state="validacion.localidad.estado"
								:options="op_localidad"
								type="text"
								placeholder="Ingrese una localidad"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-select>
							<b-form-invalid-feedback id="localidad-live-feedback"
								>{{ validacion.localidad.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="*Departamento" label-for="departamento">
							<b-form-select
								id="departamento"
								v-model="socio.departamento"
								:state="validacion.departamento.estado"
								type="text"
								placeholder="Ingrese un departamento"
								invalid-feedback="Complete este campo"
								required
								:options="options"
							>
							</b-form-select>
							<b-form-invalid-feedback id="departamento-live-feedback"
								>{{ validacion.departamento.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="*Codigo postal" label-for="cod_postal">
							<b-form-input
								id="cod_postal"
								v-model="socio.cod_postal"
								:state="validacion.cod_postal.estado"
								type="number"
								placeholder="Ingrese un numero"
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
				<b-collapse id="accordion-3" accordion="my-accordion" role="tabpanel">
					<b-card-body>
						<b-form-group label="*Email" label-for="email">
							<b-form-input
								:state="validacion.email.estado"
								id="email"
								v-model="socio.email"
								type="email"
								placeholder="Ingrese un email"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="email-live-feedback"
								>{{ validacion.email.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="Telefono fijo" label-for="tel_fijo">
							<b-form-input
								id="tel_fijo"
								v-model="socio.tel_fijo"
								:state="validacion.tel_fijo.estado"
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
								v-model="socio.tel_celular"
								:state="validacion.tel_celular.estado"
								type="number"
								placeholder="Ingrese un numero"
							>
							</b-form-input>
							<b-form-invalid-feedback id="tel_celular-live-feedback"
								>{{ validacion.tel_celular.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
						<b-form-group label="Carencia" label-for="carencia">
							<b-form-input
								id="carencia"
								v-model="socio.carencia"
								:state="validacion.carencia.estado"
								type="date"
								placeholder="Ingrese una fecha"
								invalid-feedback="Complete este campo"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="carencia-live-feedback"
								>{{ validacion.carencia.mensaje }}
							</b-form-invalid-feedback>
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
		<b-button
			class="mt-2"
			variant="primary"
			@click="sumarFliares()"
			style="color: white"
			>¿Agregar adherentes?</b-button
		>
		<div v-show="btn_familiar" v-for="(item, index) in familiar" :key="index">
			<b-form>
				<h4>Datos del Adherente: {{ index + 1 }}</h4>
				<b-form-group label="*Nombre/s" label-for="nombre">
					<b-form-input
						:state="validacionFamiliar[index].nombre.estado"
						id="nombre"
						v-model="item.nombre"
						type="text"
						placeholder="*Ingrese los Nombre/s"
						invalid-feedback="Complete este campo"
						required
					>
					</b-form-input>
					<b-form-invalid-feedback id="nombre-live-feedback"
						>{{ validacionFamiliar[index].nombre.mensaje }}
					</b-form-invalid-feedback>
				</b-form-group>
				<b-form-group label="*Apellido/s" label-for="apellido">
					<b-form-input
						:state="validacionFamiliar[index].apellido.estado"
						id="apellido"
						v-model="item.apellido"
						type="text"
						placeholder="*Ingrese los Apellido/s"
						invalid-feedback="Complete este campo"
						required
					>
					</b-form-input>
					<b-form-invalid-feedback id="apellido-live-feedback"
						>{{ validacionFamiliar[index].apellido.mensaje }}
					</b-form-invalid-feedback>
				</b-form-group>
				<b-form-group label="*DNI" label-for="dni_familiar">
					<b-form-input
						:state="validacionFamiliar[index].dni_familiar.estado"
						id="dni_familiar"
						v-model="item.dni_familiar"
						type="number"
						placeholder="Ingrese un DNI"
						invalid-feedback="Complete este campo"
						required
					>
					</b-form-input>
					<b-form-invalid-feedback id="dni_familiar-live-feedback"
						>{{ validacionFamiliar[index].dni_familiar.mensaje }}
					</b-form-invalid-feedback>
				</b-form-group>

				<b-form-group label="*Fecha de nacimiento" label-for="fecha_nacimiento">
					<b-form-input
						:state="validacionFamiliar[index].fecha_nacimiento.estado"
						id="fecha_nacimiento"
						v-model="item.fecha_nacimiento"
						type="date"
						placeholder="Ingrese una fecha"
						invalid-feedback="Complete este campo"
						required
					>
					</b-form-input>
					<b-form-invalid-feedback id="fecha_nacimiento-live-feedback"
						>{{ validacionFamiliar[index].fecha_nacimiento.mensaje }}
					</b-form-invalid-feedback>
				</b-form-group>

				<b-form-group label="*Fecha de asociación" label-for="fecha_asociacion">
					<b-form-input
						:state="validacionFamiliar[index].fecha_asociacion.estado"
						id="fecha_asociacion"
						v-model="item.fecha_asociacion"
						type="date"
						placeholder="Ingrese una fecha"
						invalid-feedback="Complete este campo"
						required
					>
					</b-form-input>
					<b-form-invalid-feedback id="fecha_asociacion-live-feedback"
						>{{ validacionFamiliar[index].fecha_asociacion.mensaje }}
					</b-form-invalid-feedback>
				</b-form-group>

				<b-form-group label="Carencia" label-for="carencia">
					<b-form-input
						:state="validacionFamiliar[index].carencia.estado"
						id="carencia"
						v-model="item.carencia"
						type="date"
						placeholder="Ingrese una fecha"
						invalid-feedback="Complete este campo"
						required
					>
					</b-form-input>
					<b-form-invalid-feedback id="carencia-live-feedback"
						>{{ validacionFamiliar[index].carencia.mensaje }}
					</b-form-invalid-feedback>
				</b-form-group>

				<b-form-group label="*Tiene Obra social">
					<b-form-checkbox
						v-model="item.tieneObraSocial"
						value="true"
						type="boolean"
						:state="validacionFamiliar[index].tieneObraSocial.estado"
						invalid-feedback="Complete este campo"
						required
						unchecked-value="false"
					>
					</b-form-checkbox>
				</b-form-group>
			</b-form>
			<b-button
				class="mt-2"
				variant="primary"
				@click="sumarFliares()"
				style="color: white"
				>+</b-button
			>
		</div>
		<!-- 
    {{ socio }}
    {{familiar}} -->
		<!-- {{ data }} -->
		<b-button class="mt-2" variant="success" block @click="postSocio()"
			>Guardar</b-button
		>
	</div>
</template>

<script>
	import { APIControler } from "@/store/APIControler";

	export default {
		props: {
			updateTable: Function,
		},
		data() {
			return {
				socio: { tieneObraSocial: false },
				familiar: [],
				data: {},
				plan: [],
				validacion: {
					numero_socio: { estado: null, mensaje: "" },
					nombre: { estado: null, mensaje: "" },
					apellido: { estado: null, mensaje: "" },
					dni: { estado: null, mensaje: "" },
					fecha_nacimiento: { estado: null, mensaje: "" },
					mutual: { estado: null, mensaje: "" },
					tieneObraSocial: { estado: null, mensaje: "" },
					fecha_asociacion: { estado: null, mensaje: "" },
					carencia: { estado: null, mensaje: "" },
					calle: { estado: null, mensaje: "" },
					localidad: { estado: null, mensaje: "" },
					departamento: { estado: null, mensaje: "" },
					cod_postal: { estado: null, mensaje: "" },
					email: { estado: null, mensaje: "" },
					tel_fijo: { estado: null, mensaje: "" },
					tel_celular: { estado: null, mensaje: "" },
					metodoPago: { estado: null, mensaje: "" },
					cobrador: { estado: null, mensaje: "" },
				},
				validacionFamiliar: [],
				list_mutuales: {},
				op_mutuales: [
					{ value: null, text: "Elija una mutual", disabled: true },
				],
				op_cobradores: [
					{ value: null, text: "Elija un cobrador", disabled: true },
				],

				btn_familiar: false,
				cantidad: 0,
				respuesta: {},
				select: null,
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
				op_metodosPago: [
					{ value: "Mercado pago", text: "Mercado pago" },
					{ value: "Transferencia bancaria", text: "Transferencia bancaria" },
					{ value: "Otro", text: "Otro" },
					{ value: "Cobrador", text: "Cobrador" },
				],
				op_localidad: [
					{ value: null, text: "Elija una localidad" },
					{ value: "Acheral", text: " 1 - Acheral " },
					{
						value: "Agua Dulce y La Soledad",
						text: "2 - Agua Dulce y La Soledad",
					},
					{ value: "Aguilares", text: " 3 - Aguilares " },
					{ value: "Alderetes", text: " 4 - Alderetes " },
					{
						value: "Alpachiri y El Molino",
						text: " 5 - Alpachiri y El Molino ",
					},
					{
						value: "Alto Verde y Los Gucheas",
						text: " 6 - Alto Verde y Los Gucheas ",
					},
					{ value: "Amaichá del Valle", text: " 7 - Amaichá del Valle " },
					{ value: "Amberes", text: " 8 - Amberes " },
					{ value: "Anca Juli", text: " 9 - Anca Juli " },
					{ value: "Arcadia", text: " 10 - Arcadia " },
					{ value: "Atahona", text: " 11 - Atahona " },
					{ value: "Banda del Río Salí", text: " 12 - Banda del Río Salí " },
					{ value: "Bella Vista", text: " 13 - Bella Vista " },
					{ value: "Buena Vista", text: " 14 - Buena Vista " },
					{ value: "Burruyacú", text: " 15 - Burruyacú " },
					{ value: "Capitán Cáceres", text: " 16 - Capitán Cáceres " },
					{ value: "Cevil Redondo", text: " 17 - Cevil Redondo " },
					{ value: "Choromoro", text: " 18 - Choromoro " },
					{ value: "Ciudacita", text: " 19 - Ciudacita " },
					{ value: "Colalao del Valle", text: " 20 - Colalao del Valle " },
					{ value: "Colombres", text: " 21 - Colombres " },
					{ value: "Concepción", text: " 22 - Concepción " },
					{
						value: "Delfín Gallo (Ex Ingenio Esperanza)",
						text: " 23 - Delfín Gallo (Ex Ingenio Esperanza) ",
					},
					{
						value: "El Bracho y El Cevilar",
						text: " 24 - El Bracho y El Cevilar ",
					},
					{ value: "El Cadillal", text: " 25 - El Cadillal " },
					{ value: "El Cercado", text: " 26 - El Cercado " },
					{ value: "El Chañar", text: " 27 - El Chañar " },
					{ value: "El Manantial", text: " 28 - El Manantial " },
					{ value: "El Mojón", text: " 29 - El Mojón " },
					{ value: "El Mollar", text: " 30 - El Mollar " },
					{ value: "El Naranjito", text: " 31 - El Naranjito " },
					{
						value: "El Naranjo y El Sunchal",
						text: " 32 - El Naranjo y El Sunchal ",
					},
					{ value: "El Polear", text: " 33 - El Polear " },
					{ value: "El Puestito", text: " 34 - El Puestito " },
					{ value: "El Sacrificio", text: " 35 - El Sacrificio " },
					{ value: "El Timbó", text: " 36 - El Timbó " },
					{ value: "Escaba", text: " 37 - Escaba " },
					{ value: "Esquina y Mancopa", text: " 38 - Esquina y Mancopa " },
					{
						value: "Estación Araox y Tacanas",
						text: " 39 - Estación Araox y Tacanas ",
					},
					{ value: "Famaillá", text: " 40 - Famaillá " },
					{ value: "Gastona y Belicha", text: " 41 - Gastona y Belicha " },
					{
						value: "Gobernador Garmendia",
						text: " 42 - Gobernador Garmendia ",
					},
					{
						value: "Gobernador Piedrabuena",
						text: " 43 - Gobernador Piedrabuena ",
					},
					{ value: "Graneros", text: " 44 - Graneros " },
					{ value: "Huasa Pampa", text: " 45 - Huasa Pampa " },
					{
						value: "Juan Bautista Alberdi",
						text: " 46 - Juan Bautista Alberdi ",
					},
					{ value: "La Cocha", text: " 47 - La Cocha " },
					{ value: "La Esperanza", text: " 48 - La Esperanza " },
					{
						value: "La Florida y Luisiana",
						text: " 49 - La Florida y Luisiana ",
					},
					{
						value: "La Ramada y La Cruz",
						text: " 50 - La Ramada y La Cruz ",
					},
					{ value: "La Trinidad", text: " 51 - La Trinidad " },
					{ value: "Lamadrid", text: " 52 - Lamadrid " },
					{ value: "Las Cejas", text: " 53 - Las Cejas " },
					{ value: "Las Talas", text: " 54 - Las Talas " },
					{ value: "Las Talitas", text: " 55 - Las Talitas " },
					{
						value: "Los Bulacio y Los Villagra",
						text: " 56 - Los Bulacio y Los Villagra ",
					},
					{ value: "Los Gómez", text: " 57 - Los Gómez " },
					{ value: "Los Nogales", text: " 58 - Los Nogales " },
					{ value: "Los Pereyra", text: " 59 - Los Pereyra " },
					{ value: "Los Puestos", text: " 60 - Los Puestos " },
					{ value: "Los Pérez", text: " 61 - Los Pérez " },
					{ value: "Los Ralos", text: " 62 - Los Ralos " },
					{
						value: "Los Sarmientos y La Tipa",
						text: " 63 - Los Sarmientos y La Tipa ",
					},
					{ value: "Los Sosas", text: " 64 - Los Sosas " },
					{ value: "Lules", text: " 65 - Lules " },
					{
						value: "Manuel García Fernández",
						text: " 66 - Manuel García Fernández ",
					},
					{ value: "Manuela Pedraza", text: " 67 - Manuela Pedraza " },
					{ value: "Medinas", text: " 68 - Medinas " },
					{ value: "Monte Bello", text: " 69 - Monte Bello " },
					{ value: "Monteagudo", text: " 70 - Monteagudo " },
					{ value: "Monteros", text: " 71 - Monteros " },
					{ value: "Padre Monti", text: " 72 - Padre Monti " },
					{ value: "Pampa Mayo", text: " 73 - Pampa Mayo " },
					{
						value: "Quilmes y Los Sueldos",
						text: " 74 - Quilmes y Los Sueldos ",
					},
					{ value: "Raco", text: " 75 - Raco " },
					{
						value: "Ranchillos y San Miguel",
						text: " 76 - Ranchillos y San Miguel ",
					},
					{ value: "Rumi Punco", text: " 77 - Rumi Punco " },
					{
						value: "Río Chico y Nueva Trinidad",
						text: " 78 - Río Chico y Nueva Trinidad ",
					},
					{ value: "Río Colorado", text: " 79 - Río Colorado " },
					{ value: "Río Seco", text: " 80 - Río Seco " },
					{ value: "San Andrés", text: " 81 - San Andrés " },
					{
						value: "San Felipe y Santa Bárbara",
						text: " 82 - San Felipe y Santa Bárbara ",
					},
					{ value: "San Ignacio", text: " 83 - San Ignacio " },
					{ value: "San Javier", text: " 84 - San Javier " },
					{
						value: "San José de la Cocha",
						text: " 85 - San José de la Cocha ",
					},
					{
						value: "San Miguel de Tucumán",
						text: " 86 - San Miguel de Tucumán ",
					},
					{
						value: "San Pablo y Villa Nougués",
						text: " 87 - San Pablo y Villa Nougués ",
					},
					{
						value: "San Pedro de Colalao",
						text: " 88 - San Pedro de Colalao ",
					},
					{
						value: "San Pedro y San Antonio",
						text: " 89 - San Pedro y San Antonio ",
					},
					{ value: "Santa Ana", text: " 90 - Santa Ana " },
					{
						value: "Santa Cruz y La Tuna",
						text: " 91 - Santa Cruz y La Tuna ",
					},
					{ value: "Santa Lucía", text: " 92 - Santa Lucía " },
					{
						value: "Santa Rosa de Leales",
						text: " 93 - Santa Rosa de Leales ",
					},
					{
						value: "Santa Rosa y Los Rojo",
						text: " 94 - Santa Rosa y Los Rojo ",
					},
					{ value: "Sargento Moya", text: " 95 - Sargento Moya " },
					{ value: "Siete de Abril", text: " 96 - Siete de Abril " },
					{ value: "Simoca", text: " 97 - Simoca " },
					{ value: "Soldado Maldonado", text: " 98 - Soldado Maldonado " },
					{ value: "Taco Ralo", text: " 99 - Taco Ralo " },
					{ value: "Tafí Viejo", text: " 100 - Tafí Viejo " },
					{ value: "Tafí del Valle", text: " 101 - Tafí del Valle " },
					{ value: "Tapia", text: " 102 - Tapia " },
					{ value: "Teniente Berdina", text: " 103 - Teniente Berdina " },
					{ value: "Trancas", text: " 104 - Trancas " },
					{ value: "Villa Belgrano", text: " 105 - Villa Belgrano " },
					{
						value: "Villa Benjamín Araoz",
						text: " 106 - Villa Benjamín Araoz ",
					},
					{ value: "Villa Chigligasta", text: " 107 - Villa Chigligasta " },
					{ value: "Villa Quinteros", text: " 108 - Villa Quinteros " },
					{ value: "Villa de Leales", text: " 109 - Villa de Leales " },
					{ value: "Yerba Buena", text: " 110 - Yerba Buena " },
					{ value: "Yánima", text: " 111 - Yánima " },
				],
			};
		},

		methods: {
			async getSocios() {
				let socioAPI = new APIControler();
				this.data = await socioAPI.getData();
			},
			async postSocio() {
				let socioAPI = new APIControler();
				this.respuesta = await socioAPI.postData(this.socio);
				if (this.familiar.length > 0) {
					this.postFamiliar();
				}

				//this.resetForm();
				this.cargarFeedback();
				this.updateTable();
			},
			cargarFeedback() {
				let valido;
				if (!this.respuesta) this.respuesta = {};
				for (let key in this.validacion) {
					valido = !this.respuesta.hasOwnProperty(key);
					this.validacion[key].estado = valido;
					//console.log(key);
					if (!valido) this.validacion[key].mensaje = this.respuesta[key][0];
				}
			},
			cargarFeedbackFamiliares(response, index) {
				let valido;
				if (!response) response = {};
				for (let key in this.validacionFamiliar[index]) {
					valido = !response.hasOwnProperty(key);
					this.validacionFamiliar[index][key].estado = valido;
					//console.log(key);
					if (!valido)
						this.validacionFamiliar[index][key].mensaje = response[key][0];
				}
			},

			async sumarFliares() {
				this.btn_familiar = true;
				// this.resetFormAdh();
				// this.cantidad=this.cantidad +1;
				this.familiar.push({
					numero_socio: null,
					apellido: "",
					nombre: "",
					dni_familiar: null,
					fecha_nacimiento: null,
					fecha_asociacion: null,
					carencia: null,
					tieneObraSocial: false,
				});
				this.validacionFamiliar.push({
					numero_socio: { estado: null, mensaje: "" },
					nombre: { estado: null, mensaje: "" },
					apellido: { estado: null, mensaje: "" },
					dni_familiar: { estado: null, mensaje: "" },
					fecha_nacimiento: { estado: null, mensaje: "" },
					fecha_asociacion: { estado: null, mensaje: "" },
					carencia: { estado: null, mensaje: "" },
					tieneObraSocial: { estado: null, mensaje: "" },
				});
			},
			async postFamiliar() {
				let familiarAPI = new APIControler();
				let _nroSocio =
					"http://localhost:8081/socios/" + this.socio.numero_socio + "/";
				familiarAPI.apiUrl.pathname = "familiar/";
				console.log("Mostrando familiar");
				console.log(this.familiar);
				let response;
				for (const [index, adherente] of this.familiar.entries()) {
					console.log("Mostrando adherente");
					console.log(adherente);
					adherente.numero_socio = _nroSocio;
					response = await familiarAPI.postData(adherente);
					this.cargarFeedbackFamiliares(response, index);
				}

				// this.resetFormAdh();
			},
			async getMutuales() {
				let mutualesAPI = new APIControler();
				mutualesAPI.apiUrl.pathname = "mutuales/";
				this.data = await mutualesAPI.getData(this.list_mutuales);
				this.data.forEach((element) => {
					let option = {};
					option.value =
						"http://localhost:8081/mutuales/" + element.id_mutual + "/";
					option.text =
						element.id_mutual +
						"-- " +
						element.nombre +
						", " +
						element.sucursal;
					console.log(option);
					this.op_mutuales.push(option);
				});
			},
			async getCobradores() {
				let cobradoresAPI = new APIControler();
				cobradoresAPI.apiUrl.pathname = "cobradores/";
				this.data = await cobradoresAPI.getData();
				this.data.forEach((element) => {
					let option = {};
					option.value =
						"http://localhost:8081/cobradores/" + element.id_cobrador + "/";
					option.text =
						element.id_cobrador +
						"-- " +
						element.apellido+
						", " +
						element.nombre;

					this.op_cobradores.push(option);
				});
			},
			async resetForm() {
				this.socio.numero_socio = null;
				this.socio.apellido = "";
				this.socio.nombre = "";
				this.socio.dni = null;
				this.socio.fecha_nacimiento = null;
				this.socio.fecha_asociacion = null;
				this.socio.calle = "";
				this.socio.localidad = "";
				this.socio.departamento = "";
				this.socio.cod_postal = null;
				this.socio.tel_fijo = null;
				this.socio.tel_celular = null;
				this.socio.carencia = null;
			},
			async resetFormAdh() {
				/*
        this.familiar.apellido = "";
        this.familiar.nombre = "";
        this.familiar.dni_familiar = null;
        this.familiar.fecha_nacimiento=null;
        this.familiar.carencia= null;
        */
			},
		},
		beforeMount() {
			this.getMutuales();
			this.getCobradores();
		},
	};
</script>

<style></style>
