<template>
  <div>
  
    <h6>Los campos en (*) son obligatorios</h6>
    <h4>Nueva Orden: </h4>

    <!-- CAMPOS REQUERIDOS -->
    <!-- N° Orden -->
    <!-- N° Socio -->
    <!-- Paciente -->
    <!-- Servicio -->
    <!-- Id Medico -->
    <!-- Id Mutual -->
    <!-- Fecha -->
    <!-- Precio -->
    <!-- Realizado -->

    <!------------------------------------------------------------------------------------------->
    <b-form >
        <b-form-group label="*N° Orden" label-for="numero_orden">
            <!-- Numero de Orden -->
            <b-form-input
            id="numero_orden"
            v-model="orden.numero_orden"
            type="number"
            placeholder="Ingrese un Numero"
            invalid-feedback="Complete este campo"
            required
            >
            </b-form-input>
        </b-form-group>

        <b-form-group label="*N° Socio" label-for="numero_socio">
            <!-- Numero de Socio -->
            <b-form-input
            id="numero_socio"
            v-model="orden.numero_socio"
            type="number"
            placeholder="Ingrese un Numero"
            invalid-feedback="Complete este campo"
            required
            >
            </b-form-input>
        </b-form-group>

      <!-- Paciente para el cual se emite la receta -->
      <b-form-group label="*Paciente" label-for="paciente">
        <b-form-input
          id="paciente"
          v-model="orden.paciente"
          type="number"
          placeholder="*Ingrese el nombre completo del paciente"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>

      <!-- Servicio -->
      <b-form-group label="*Servicio" label-for="servicio">
        <b-form-input
          id="servicio"
          v-model="orden.servicio"
          type="text"
          placeholder="*Ingrese el tipo de servicio"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>
      
      <!-- Id del medico -->
      <b-form-group label="*ID Medico" label-for="id_medico">
        <b-form-input
          id="id_medico"
          v-model="orden.id_medico"
          type="number"
          placeholder="Ingrese el ID del medico"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>

      <!-- Id de la mutual -->
      <b-form-group label="*ID Mutual" label-for="id_mutual">
        <b-form-input
          id="id_mutual"
          v-model="orden.id_mutual"
          type="number"
          placeholder="Ingrese el ID de la mutual"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>

      <!-- Fecha de emision -->
      <b-form-group label="*Fecha" label-for="fecha">
        <b-form-input
          id="fecha"
          v-model="orden.fecha"
          type="date"
          placeholder="Ingrese una fecha"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>

      <!-- Hora -->
      <b-form-group label="*Hora" label-for="hora">
        <b-form-input
          id="hora"
          v-model="orden.hora"
          type="time"
          placeholder="Ingrese una hora"
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>

      <!-- Precio -->
      <b-form-group label="*Precio" label-for="precio">
        <b-form-input
          id="precio"
          v-model="orden.precio"
          type="decimal"
          placeholder="Ingrese el precio correspondiente a la orden "
          invalid-feedback="Complete este campo"
          required
        >
        </b-form-input>
      </b-form-group>

      <!-- Realizado -->
      <b-form-group label="*Realizado" label-for="realizado">
        <b-form-checkbox
          id="realizado"
          v-model="orden.realizado"
          value="true"
          type="boolean"
          invalid-feedback="Complete este campo"
          required
          unchecked-value="false"
        >
        </b-form-checkbox>
      </b-form-group>

    </b-form>
    {{ orden }}
    {{ data }}
    <b-button class="mt-2" variant="success" block @click="postOrden()">POST TEST</b-button>
  </div>
</template>

<script>
import { APIControler } from "../store/APIControler";

export default {
  data() {
    return {
      orden: {},
      data: {},
      options: [
        { value: true, text: 'SI' },
        { value: false, text: 'NO' },
      ]
    };
  },
  methods: {
    async getOrdenes() {
      let ordenAPI = new APIControler();
      this.data = await ordenAPI.getData();
    },
    async postOrden() {
      let ordenAPI = new APIControler();
      ordenAPI.apiUrl.pathname='ordenes/';
      this.data = await ordenAPI.postData(this.orden);
    },
  },
};
</script>

<style>
</style>