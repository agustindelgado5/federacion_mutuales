import "@babel/polyfill";
import "mutationobserver-shim";
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faUserSecret, faSpinner } from '@fortawesome/free-solid-svg-icons';
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
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'
import './assets/main.css';
import './assets/all.css';

library.add(faUserSecret, faSpinner)
Vue.use(VueCookies)
Vue.component('fa-icon', FontAwesomeIcon)
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


