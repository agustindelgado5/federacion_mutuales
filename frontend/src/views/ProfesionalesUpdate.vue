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
                required
                :disabled="true"
              >
              </b-form-input>
            </b-form-group>
            <b-form-group label="*Matricula" label-for="matricula">
              <b-form-input
                id="matricula"
                v-model="item_prof.matricula"
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
                v-model="item_prof.nombre"
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
                v-model="item_prof.apellido"
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
                v-model="item_prof.dni"
                type="number"
                placeholder="Ingrese un DNI"
                invalid-feedback="Complete este campo"
                required
              >
              </b-form-input>
            </b-form-group>

            <b-form-group label="*Fecha de ingreso" label-for="fecha_ingreso">
              <b-form-input
                id="fecha_ingreso"
                v-model="item_prof.fecha_ingreso"
                type="date"
                placeholder="Ingrese una fecha"
                invalid-feedback="Complete este campo"
                required
              >
              </b-form-input>
            </b-form-group>
            <b-form-group label="*Especialidad" label-for="especialidad">
              <b-form-input
                id="especialidad"
                v-model="item_prof.especialidad"
                type="text"
                placeholder="*Ingrese la Especialidad"
                invalid-feedback="Complete este campo"
                required
              >
              </b-form-input>
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
                v-model="item_prof.localidad"
                type="text"
                placeholder="Ingrese una localidad"
                invalid-feedback="Complete este campo"
                required
              >
              </b-form-input>
            </b-form-group>
            <b-form-group label="*Provincia" label-for="provincia">
              <b-form-select
                id="provincia"
                v-model="item_prof.provincia"
                type="text"
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
            <b-form-group label="*Email" label-for="email">
              <b-form-input
                id="email"
                v-model="item_prof.email"
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
                v-model="item_prof.tel_fijo"
                type="number"
                placeholder="Ingrese un numero"
              >
              </b-form-input>
            </b-form-group>

            <b-form-group label="Celular" label-for="tel_celular">
              <b-form-input
                id="tel_celular"
                v-model="item_prof.tel_celular"
                type="number"
                placeholder="Ingrese un numero"
              >
              </b-form-input>
            </b-form-group>
          </b-card-body>
        </b-collapse>
      </b-card>
    </b-form>
    <!-- {{item_med}}
        <br>
        <br>
        {{ data }} -->
    <b-button
      class="mt-2"
      variant="success"
      block
      @click="putProfesional()"
      >Modificar</b-button
    >
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";
import axios from "axios";

export default {
  props: {
    item_prof: {},
  },
  data() {
    return {
      profesional: {},
      data: {},
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
        this.item_prof = await axios.put(
          "http://localhost:8081/profesionales/" +
            this.item_prof.id_medico +
            "/",
          this.item_prof
        );
        swal("Operación Exitosa", " ", "success");
        console.log(this.item_prof);
      } catch (error) {
        swal("¡ERROR!", "Se ha detectado un problema ", "error");
        console.log(error);
      } finally {
        // location.href = "/profesionales";
      }
    },
  },
};
</script>

<style>
</style>