import Vue from "vue";
import Vuex from "vuex";
import PagosProf from "../store/PagosProf"
import "../store/filters";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {PagosProf},
});
