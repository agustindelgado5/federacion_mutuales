import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
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
    component: () =>
      import(
        /* webpackChunkName: "profesionales" */ "../views/profesionales/Profesionales.vue"
      ),
    meta: { title: 'Profesionales - Federación Tucumana de Mutuales' }
  },
  {
    path: "/profesionales/list_pagos",
    name: "Listado_de_Pagos",
    component: () => import("../views/PagoProfesionales.vue"),
  },
  {
    path: "/socios",
    name: "Socios",
    component: () => import("../views/Socios.vue"),
  },
  {
    path: "/mutuales",
    name: "Mutuales",
    component: () => import("../views/mutuales/Mutuales.vue"),
  },
  {
    path: "/farmacias",
    name: "Farmacias",
    component: () => import("../views/farmacias/Farmacias.vue"),
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
    component: () => import("../views/servicios/Servicios.vue"),
    meta: { title: 'Servicios - Federación Tucumana de Mutuales' }
  },
  {
    path: "/cobradores",
    name: "Cobradores",
    component: () => import("../views/cobradores/Cobradores.vue"),
    meta: { title: 'Cobradores - Federación Tucumana de Mutuales' }
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("../views/login/Login.vue"),
    meta: { title: 'Iniciar Sessión - Federación Tucumana de Mutuales' }
  },
  {
    path: '/cuotas',
    name: 'cuotas',
    component: () => import('../views/cuotas/Cuotas.vue')
  },
  {
    path: '/estudios',
    name: 'estudios',
    component: () => import('../views/estudios/Estudios.vue')
  },
  {
    path: '/ordenesProf',
    name: 'ordenesProf',
    component: () => import('../views/Ordenes_Profesional.vue')
  },
  {
    path: "/gastosSalientes",
    name: "GastosSalientes",
    component: () => import("../views/GastosSalientes.vue"),
    meta: { title: 'Gastos Salientes - Federación Tucumana de Mutuales' }
  },
  {
    path: '/cirugias',
    name: 'cirugias',
    component: () => import('../views/cirugias/Cirugias.vue')
  },
  {
    path: '/institutos',
    name: 'institutos',
    component: () => import('../views/institutos/Institutos.vue')
  },
  {
    path: '/lentes',
    name: 'lentes',
    component: () => import('../views/Lentes.vue')
  },
  {
    path: '/ventasOpticas',
    name: 'VentasOpticas',
    component: () => import('../views/VentasOpticas.vue'),
    meta: { title: '"Ventas Opticas - Federación Tucumana de Mutuales"' }
  },
  {
    path: '/baja_mora',
    name: 'baja_mora',
    component: () => import('../views/SociosBajaMora.vue')
  },

];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
