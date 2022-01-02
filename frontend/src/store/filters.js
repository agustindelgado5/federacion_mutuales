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





Vue.filter("fecha_asociacion_range", (value,desde,hasta) => {

    if(desde && hasta){
      if (desde <= hasta) {
          console.log('ENTRO AL IF');
          return value
              .filter(
                  (f) => f.fecha_asociacion >= desde && f.fecha_asociacion <= hasta
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

//Filtros en Mutuales
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

Vue.filter("Representante", (value, option)=>{
    if(option != null){
        return value
        .filter((f) => f.representante==option);
    }
    else{
        return value;
    }
})

Vue.filter("Localidad", (value, option)=>{
    if(option != null){
        return value
        .filter((f) => f.localidad==option);
    }
    else{
        return value;
    }
})

Vue.filter("Sucursal", (value, option)=>{
    if(option != null){
        return value
        .filter((f) => f.sucursal==option);
    }
    else{
        return value;
    }
})

Vue.filter("Correo", (value, option)=>{
    if(option != null){
        return value
        .filter((f) => f.email==option);
    }
    else{
        return value;
    }
})


//Filtros en Profesionales
Vue.filter("Especialidad", (value, option)=>{
    if(option != null){
        return value
        .filter((f) => f.especialidad==option);
    }
    else{
        return value;
    }
})

//Filtros en Medicamentos
Vue.filter("Laboratorio", (value, option)=>{
    if(option != null){
        return value
        .filter((f) => f.laboratorio==option);
    }
    else{
        return value;
    }
})

Vue.filter("Farmacia", (value, option)=>{
    if(option != null){
        return value
        .filter((f) => f.cod_farmacia==option);
    }
    else{
        return value;
    }
})