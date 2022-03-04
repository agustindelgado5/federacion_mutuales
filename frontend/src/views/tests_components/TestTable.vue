<template>
  <div>
    <h1>HI, WELCOME TO TEST TABLE</h1>
    <b-button @click="createServicios"> Nuevo Servicio </b-button>
    <BaseForm :fields="formFields" :createFunction="createServicios"/>
    <BaseTable
      :fields="fields"
      :items="items"
      :deleteFunction="deleteServicio"
      :updateFunction="updateServicio"
    />
  </div>
</template>

<script>
import BaseTable from "../../components/BaseTable.vue";

import { Fetcher } from "@/store/utils/Fetcher";
import FormServ from "./FormServ.vue";
import BaseForm from "../../components/BaseForm.vue";

export default {
  components: { BaseTable, FormServ, BaseForm },
  data() {
    return {
      fields: [
        { key: "servicio", label: "Servicios", sortable: true },
        { key: "action", label: "Acciones", variant: "secondary" },
      ],
      formFields: [
        {
          form_input: "input",
          id: "servicio",
          name: "servicio",
          value: "",
          type: "text",
          label: "Servicio",
          placeholder: "Ej: Odontología",
          invalid_feedback: "Ingrese un nombre de servicio valido",
          required: true,
        },
      ],
      items: [],
      fetcher: new Fetcher("servicios/"),
    };
  },
  methods: {
    async getServicios() {
      this.items = await this.fetcher.getList();
    },
    async createServicios(payload) {
      let res = await this.fetcher.post(payload);
      if (res.status === 201) {alert("Servicio creado: " + payload.servicio);this.getServicios()}
      else alert("No se pudo crear el servicio: " + payload.servicio);
    },
    async updateServicio(row, payload) {
      let res = await this.fetcher.update(row.item.id_servicio, payload);
      if (res.status === 200) {alert("Servicio modificado: " + payload.servicio);this.getServicios()}
      else alert("No se pudo modificar el servicio: " + payload.servicio);
    },
    async deleteServicio(row) {
      let res = await this.fetcher.delete(row.item.id_servicio);
      if (res.status === 204) {alert("Servicio Eliminado: " + row.item.servicio);this.getServicios()}
      else alert("No se pudo elminar el servicio");
    },
  },
  created() {
    this.getServicios();
  },
};
</script>

<style>
</style>