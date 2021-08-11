import "@babel/polyfill";
import "mutationobserver-shim";
import Vue from "vue";
import "./plugins/bootstrap-vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import VueSidebarMenu from 'vue-sidebar-menu'

Vue.use(VueSidebarMenu)

Vue.config.productionTip = false;

export default {
    install(Vue, options) {
        Vue.component('vue-nested-menu', App);
    },
};

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");


