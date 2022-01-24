<template>
	<div>
		<h6>Los campos en (*) son obligatorios</h6>

		<!------------------------------------------------------------------------------------------->

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
						<b-form-group label="*Matricula" label-for="matricula">
							<b-form-input
								id="matricula"
								v-model="mutuales.matricula"
								type="text"
								placeholder="Ingrese una sucursal"
								invalid-feedback="Complete este campo"
								:state="validacion.matricula.estado"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="matricula-live-feedback"
								>{{ validacion.matricula.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

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

						<b-form-group label="*CUIT" label-for="cuit">
							<b-form-input
								id="cuit"
								v-model="mutuales.cuit"
								type="text"
								placeholder="Ingrese una sucursal"
								invalid-feedback="Complete este campo"
								:state="validacion.cuit.estado"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="cuit-live-feedback"
								>{{ validacion.cuit.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="*Fecha Inicio" label-for="fecha_inicio">
							<b-form-input
								id="fecha_inicio"
								v-model="mutuales.fecha_inicio"
								type="date"
								placeholder="Ingrese una sucursal"
								invalid-feedback="Complete este campo"
								:state="validacion.fecha_inicio.estado"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="fecha_inicio-live-feedback"
								>{{ validacion.fecha_inicio.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="*Fecha Ingreso" label-for="fecha_ingreso">
							<b-form-input
								id="fecha_ingreso"
								v-model="mutuales.fecha_ingreso"
								type="date"
								placeholder="Ingrese una sucursal"
								invalid-feedback="Complete este campo"
								:state="validacion.fecha_ingreso.estado"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="fecha_ingreso-live-feedback"
								>{{ validacion.fecha_ingreso.mensaje }}
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
						<b-form-group label="*Direccion" label-for="direccion">
							<b-form-input
								id="direccion"
								v-model="mutuales.direccion"
								type="text"
								placeholder="Ingrese una direccion"
								invalid-feedback="Complete este campo"
								:state="validacion.direccion.estado"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="direccion-live-feedback"
								>{{ validacion.direccion.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="*Localidad" label-for="localidad">
							<b-form-select
								id="localidad"
								v-model="mutuales.localidad"
								type="text"
								placeholder="Ingrese una sucursal"
								invalid-feedback="Complete este campo"
								:state="validacion.localidad.estado"
								:options="op_localidad"
								required
							>
							</b-form-select>
							<b-form-invalid-feedback id="localidad-live-feedback"
								>{{ validacion.localidad.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

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
						<b-form-group label="Email" label-for="email">
							<b-form-input
								id="email"
								v-model="mutuales.email"
								type="text"
								placeholder="Ingrese una sucursal"
								invalid-feedback="Complete este campo"
								:state="validacion.email.estado"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="email-live-feedback"
								>{{ validacion.email.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="Telefono" label-for="Telefono">
							<b-form-input
								id="telefono"
								v-model="mutuales.telefono"
								type="text"
								placeholder="Ingrese una sucursal"
								invalid-feedback="Complete este campo"
								:state="validacion.telefono.estado"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="telefono-live-feedback"
								>{{ validacion.telefono.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>

						<b-form-group label="*Representante" label-for="representante">
							<b-form-input
								id="representante"
								v-model="mutuales.representante"
								type="text"
								placeholder="Ingrese una sucursal"
								invalid-feedback="Complete este campo"
								:state="validacion.representante.estado"
								required
							>
							</b-form-input>
							<b-form-invalid-feedback id="representante-live-feedback"
								>{{ validacion.sucursal.mensaje }}
							</b-form-invalid-feedback>
						</b-form-group>
					</b-card-body>
				</b-collapse>
			</b-card>

			<b-form-group
				label="*Servicio"
				label-for="servicio"
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

		<b-button class="mt-2" variant="success" block @click="postMutual()"
			><b>GUARDAR</b></b-button
		>
	</div>
</template>

<script>
	import axios from "axios";
	import { APIControler } from "@/store/APIControler";

	export default {
		props: {
			updateTable: Function,
		},
		data() {
			return {
				mutuales: {},
				mutuales_anteriores: {},
				index: [],
				maximo: 0,
				data: {},
				list_servicios: {},
				op_servicios: [
					{ value: null, text: "Elija los servicios", disabled: true },
				],
				selected: [],
				validacion: {
					nombre: { estado: null, mensaje: "" },
					matricula: { estado: null, mensaje: "" },
					cuit: { estado: null, mensaje: "" },
					localidad: { estado: null, mensaje: "" },
					email: { estado: null, mensaje: "" },
					telefono: { estado: null, mensaje: "" },
					representante: { estado: null, mensaje: "" },
					fecha_inicio: { estado: null, mensaje: "" },
					fecha_ingreso: { estado: null, mensaje: "" },
					direccion: { estado: null, mensaje: "" },
					sucursal: { estado: null, mensaje: "" },
					id_servicio: { estado: null, mensaje: "" },
				},
				respuesta: {},
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
					this.index.push(element.id_mutual);
				});
			},

			//Post de la mutual
			async postMutual() {
				let mutualAPI = new APIControler();
				mutualAPI.apiUrl.pathname = "mutuales/";
				if (this.selected.length > 0) {
					this.respuesta = await mutualAPI.postData(this.mutuales);
					this.postServicios();
					this.cargarFeedback();
					this.updateTable();
				} else {
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
					option.value =
						"http://localhost:8081/servicios/" + element.id_servicio + "/";
					option.text = element.servicio;
					console.log(option);
					this.op_servicios.push(option);
				});
			},

			//Cargo los servicios de las mutuales
			async postServicios() {
				var id = 1;
				this.maximo = this.index.length - 1;
				if (this.index[this.maximo] != null) {
					id = this.index[this.maximo] + 1;
				}
				console.log("ID:", id);

				for (var i = 0; i < this.selected.length; i++) {
					axios
						.post("http://localhost:8081/servicio_mutual/", {
							id_mutual: "http://localhost:8081/mutuales/" + id + "/",
							id_servicio: this.selected[i],
						})
						.then((data) => {
							console.log(data);
							console.log("¡Servicios cargados con exito!");
						})
						.catch((error) => {
							console.log(error);
						});
				}
			},
			//Validacion de los campos
			cargarFeedback() {
				let valido;
				if (!this.respuesta) this.respuesta = {};
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
		created() {
			this.getMutuales();
			this.postServicios();
		},
		computed: {},
	};
</script>

<style></style>
