// filters.js
import Vue from "vue";

Vue.filter("fecha_pagos_range", (array,desde,hasta) => {

  if(desde && hasta){
    if (desde <= hasta) {
        console.log('ENTRO AL IF');
        return array
            .filter(
                (f) => f.fecharealizacion >= desde && f.fecharealizacion <= hasta
            )
            .map((f) => {
                return { text: f.label, value: f.key };
            });
        }
  }
  else{
      console.log('NO SE PUEDE REALIZAR');
  }   
})