<template>
  <div>
    <v-card>
      <v-form v-on:submit.prevent="onSubmit">
        <v-container>
          <v-text-field
            required
            v-model="user.username"
            name="username"
            label="Nombre de usuario"
            placeholder="XxxElMasC4PO_98xxX"
          >
          </v-text-field>
          <v-text-field
            required
            v-model="user.password"
            name="password"
            label="Contraseña"
            placeholder="mi contraseña"
            :type="show ? 'text' : 'password'"
            :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="show = !show"
          >
          </v-text-field>
          <v-btn class="mr-4" type="submit"> Enviar </v-btn>
        </v-container>
      </v-form>
    </v-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      show: false,
      user: {
        username: "",
        password: "",
      },
    };
  },
};
</script>

<style>
</style>