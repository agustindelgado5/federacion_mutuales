import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
//import Socios from "../components/Socios/Socios.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
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
  },
  {
    path: "/ordenes",
    name: "Ordenes",

    component: () => import("../views/Ordenes.vue"),
  },
  {
    path: "/medicamentos",
    name: "Medicamentos",

    component: () => import("../views/Medicamentos.vue"),
  },
  {
    path: "/Recetas",
    name: "Recetas",

    component: () => import("../views/Recetas.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
