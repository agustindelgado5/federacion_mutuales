import "@babel/polyfill";
import "mutationobserver-shim";
import Vue from "vue";
import "./plugins/bootstrap-vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import VueSidebarMenu from 'vue-sidebar-menu'
import vuetify from './plugins/vuetify'
import '@babel/polyfill'
import 'roboto-fontface/css/roboto/roboto-fontface.css'
import '@mdi/font/css/materialdesignicons.css'
import VueCookies from 'vue-cookies'

Vue.use(VueCookies)

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
    vuetify,
    render: (h) => h(App)
}).$mount("#app");


