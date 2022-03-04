<template>
  <div>
    <h1>Listado de Servicios</h1>
    <v-data-table
      :headers="headers"
      :items="tabla_servicios"
      :items-per-page="10"
      class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Servicios</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog">
            <template v-slot:activator="{ on, attrs }">
              <v-btn class="mb-2" v-bind="attrs" v-on="on"> Nuevo </v-btn>
            </template>
            <servicio-form v-on:close="closeDialog()" v-on:new="saveNewItem" />
          </v-dialog>
          <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
              <v-card-title class="text-h5"
                >¿Seguro que quieres elminar?</v-card-title
              >
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="closeDelete"
                  >Cancelar</v-btn
                >
                <v-btn color="blue darken-1" text @click="deleteItemConfirm"
                  >Eliminar</v-btn
                >
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)"> mdi-pencil </v-icon>
        <v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import { Fetcher } from "@/store/utils/Fetcher";
import ServicioForm from "./ServicioForm.vue";

export default {
  components: { ServicioForm },
  data() {
    return {
      headers: [
        { text: "servicio", value: "servicio", sortable: true },
        { text: "Acciones", value: "actions", sortable: false },
      ],
      tabla_servicios: [],
      itemSelected: {},
      dialog: false,
      dialogDelete: false,
      fetcher: new Fetcher("servicios/"),
    };
  },
  methods: {
    async llenar_tabla() {
      let res = await this.fetcher.get();
      let items = await res.json();
      this.tabla_servicios = items.results;
    },
    async saveNewItem(item) {
      let res = await this.fetcher.post(item);
      res.status === 201
        ? this.tabla_servicios.push(item)
        : console.error("No se pudo agregar");
    },
    editItem(item) {},
    deleteItem(item) {
      this.itemSelected = item;
      this.dialogDelete = true;
    },
    closeDialog() {
      this.dialog = false;
    },
    closeDelete() {
      this.dialogDelete = false;
    },
    async deleteItemConfirm() {
      let res = await this.fetcher.delete(this.itemSelected.id_servicio);
      res.status === 204
        ? this.llenar_tabla()
        : console.error("No se pudo eliminar");

      this.closeDelete();
    },
  },
  created() {
    this.llenar_tabla();
  },
};
</script>

<style>
</style>