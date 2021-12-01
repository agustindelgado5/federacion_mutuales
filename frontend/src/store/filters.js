// filters.js
import Vue from "vue";
import dayjs from "dayjs";
import swal from "sweetalert"

Vue.filter("FormatStringToDate", value=>{
    return value.split("-")[2] +"/"+ value.split("-")[1] +"/"+
        value.split("-")[0]
})

Vue.filter("Date", value=>{
    return dayjs(value).format('DD/MM/YYYY');
})



Vue.filter("fecha_inicio_range", (value,desde,hasta) => {

    if(desde && hasta){
      if (desde <= hasta) {
          console.log('ENTRO AL IF');
          return value
              .filter(
                  (f) => f.fecha_inicio >= desde && f.fecha_inicio <= hasta
              );
          }
      else{
          swal("¡ERROR!", "Ingrese correctamente las fechas", "error");
          return value;
      }
    }
    else{
        console.log('NO SE PUEDE REALIZAR');
        return value;
    }   
  })

Vue.filter("fecha_ingreso_range", (value,desde,hasta) => {

  if(desde && hasta){
    if (desde <= hasta) {
        console.log('ENTRO AL IF');
        return value
            .filter(
                (f) => f.fecha_ingreso >= desde && f.fecha_ingreso <= hasta
            );
        }
    else{
        swal("¡ERROR!", "Ingrese correctamente las fechas", "error");
        return value;
    }
  }
  else{
      console.log('NO SE PUEDE REALIZAR');
      return value;
  }   
})
