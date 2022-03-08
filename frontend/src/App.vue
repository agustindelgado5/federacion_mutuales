<template>
  <v-app>
    <v-main>
      <v-container fluid>
        <Login v-show="!isLogged"/>
        <MainView v-show="isLogged"/>
      </v-container>
    </v-main>
  </v-app>
</template>
<script>
import { Fetcher } from "@/store/utils/Fetcher";

import MainView from "./MainView.vue";
import Login from "./views/login/Login.vue";
export default {
  components: { MainView, Login },
  data() {
    return {
      fetcher: new Fetcher(),
      isLogged: false,
    }
  },
  created() {
    this.isLogged = this.fetcher.isLogged()
  }
};
</script>
<style>
</style>