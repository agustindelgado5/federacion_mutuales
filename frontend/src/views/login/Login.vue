<template>
  <div style="width:24rem; margin:0 auto;">
    <h1>Federación de Mutuales</h1>
    <img src="@/assets/logo.jpg" alt="Logo Federación" srcset="" id="Logo_fed" style="margin-top:1em;margin-bottom:1em;">
    <v-card max-width="500">
      <v-card-title>
        Iniciar Sesión
      </v-card-title>
      <v-form v-on:submit.prevent="logIn">
        <v-container>
          <v-text-field
            required
            v-model="user.username"
            name="username"
            label="Nombre de usuario"
            placeholder="usuario"
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
import { Fetcher } from "@/store/utils/Fetcher";

export default {
  data() {
    return {
      fetcher: new Fetcher(),
      show: false,
      user: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    async logIn() {
      await this.fetcher.login(this.user)
      location.reload()
    }
  },
};
</script>

<style>
</style>