import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
//import Socios from "../components/Socios/Socios.vue";
import vueHeadful from 'vue-headful';

Vue.component('vue-headful', vueHeadful);

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: { title: 'Home - Federación Tucumana de Mutuales' },
    webpackChunkName: "Home",  
  },
  {
    path: "/profesionales",
    name: "Profesionales",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(
        /* webpackChunkName: "profesionales" */ "../views/Profesionales.vue"
      ),
      meta: { title: 'Profesionales - Federación Tucumana de Mutuales' } 
  },
  {
    path: "/socios",
    name: "Socios",
    //component: Socios,

    component: () => import("../views/Socios.vue"),
  },
  {
    path: "/mutuales",
    name: "Mutuales",

    component: () => import("../views/Mutuales.vue"),
  },
  {
    path: "/farmacias",
    name: "Farmacias",

    component: () => import("../views/Farmacias.vue"),
    meta: { title: 'Farmacias - Federación Tucumana de Mutuales' } 
  },
  {
    path: "/ordenes",
    name: "Ordenes",

    component: () => import("../views/Ordenes.vue"),
    meta: { title: 'Ordenes - Federación Tucumana de Mutuales' } 
  },
  {
    path: "/medicamentos",
    name: "Medicamentos",

    component: () => import("../views/Medicamentos.vue"),
    meta: { title: 'Medicamentos - Federación Tucumana de Mutuales' } 
  },
  {
    path: "/Recetas",
    name: "Recetas",

    component: () => import("../views/Recetas.vue"),
    meta: { title: 'Recetas - Federación Tucumana de Mutuales' } 
  },
  {
    path: "/Servicios",
    name: "Servicios",

    component: () => import("../views/Servicios.vue"),
    meta: { title: 'Servicios - Federación Tucumana de Mutuales' } 
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
