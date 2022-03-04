export default {
  namespaced: true,
  state: {
      pagos: {},
  },
  mutations: {
      SET_PAGOS(state, payload){
        state.pagos=payload;    
      }
  },
  actions: {
      set_pagos({commit}, payload){
          commit("SET_PAGOS", payload);
          sessionStorage.setItem("pagos", JSON.stringify(payload));
      },

      cargar_pagos({commit}){
          const _pagos = sessionStorage.getItem("pagos");
          if (_pagos) {
            commit("SET_PAGOS", _pagos); 
          }
      }
  },
  //modules: {},
};
