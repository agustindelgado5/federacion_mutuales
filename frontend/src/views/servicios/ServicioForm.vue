<template>
  <div>
    <v-card>
      <v-card-title> Nuevo Servicio</v-card-title>
      <v-card-text>
        <v-text-field label="Nombre del servicio" v-model="servicio">
        </v-text-field>
      </v-card-text>
      <v-card-actions>
        <v-spacer> </v-spacer>
        <v-btn @click="closeDialog"> Cancelar </v-btn>
        <v-btn @click="save"> Guardar </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      servicio: "",
    };
  },
  methods: {
    save() {
      this.$emit("new", {"servicio": this.servicio})
      this.closeDialog()
    },
    closeDialog() {
      this.servicio = "";
      this.$emit("close");
    },
  },
};
</script>

<style>
</style>