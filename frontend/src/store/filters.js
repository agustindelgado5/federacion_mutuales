// filters.js
import Vue from "vue";
import dayjs from "dayjs";
import swal from "sweetalert";

Vue.filter("FormatStringToDate", (value) => {
	return (
		value.split("-")[2] + "/" + value.split("-")[1] + "/" + value.split("-")[0]
	);
});

Vue.filter("FormatStringToTime", (value) => {
	return value.split(":")[0] + ":" + value.split(":")[1];
});


Vue.filter("Date", (value) => {
	return dayjs(value).format("DD/MM/YYYY");
});

Vue.filter("fecha_asociacion_range", (value, desde, hasta) => {
	if (desde && hasta) {
		if (desde <= hasta) {
			console.log("ENTRO AL IF");
			return value.filter(
				(f) => f.fecha_asociacion >= desde && f.fecha_asociacion <= hasta
			);
		} else {
			swal("¡ERROR!", "Ingrese correctamente las fechas", "error");
			return value;
		}
	} else {
		console.log("NO SE PUEDE REALIZAR");
		return value;
	}
});

//Filtros en Mutuales
Vue.filter("fecha_inicio_range", (value, desde, hasta) => {
	if (desde && hasta) {
		if (desde <= hasta) {
			console.log("ENTRO AL IF");
			return value.filter(
				(f) => f.fecha_inicio >= desde && f.fecha_inicio <= hasta
			);
		} else {
			swal("¡ERROR!", "Ingrese correctamente las fechas", "error");
			return value;
		}
	} else {
		console.log("NO SE PUEDE REALIZAR");
		return value;
	}
});

Vue.filter("fecha_ingreso_range", (value, desde, hasta) => {
	if (desde && hasta) {
		if (desde <= hasta) {
			console.log("ENTRO AL IF");
			return value.filter(
				(f) => f.fecha_ingreso >= desde && f.fecha_ingreso <= hasta
			);
		} else {
			swal("¡ERROR!", "Ingrese correctamente las fechas", "error");
			return value;
		}
	} else {
		console.log("NO SE PUEDE REALIZAR");
		return value;
	}
});

Vue.filter("Representante", (value, option) => {
	if (option != null) {
		return value.filter((f) => f.representante == option);
	} else {
		return value;
	}
});

Vue.filter("Localidad", (value, option) => {
	if (option != null) {
		return value.filter((f) => f.localidad == option);
	} else {
		return value;
	}
});

Vue.filter("Sucursal", (value, option) => {
	if (option != null) {
		return value.filter((f) => f.sucursal == option);
	} else {
		return value;
	}
});

Vue.filter("Correo", (value, option) => {
	if (option != null) {
		return value.filter((f) => f.email == option);
	} else {
		return value;
	}
});

//Filtros en Profesionales
Vue.filter("Especialidad", (value, option) => {
	if (option != null) {
		return value.filter((f) => f.especialidad == option);
	} else {
		return value;
	}
});

//Filtros en Medicamentos
Vue.filter("Laboratorio", (value, option) => {
	if (option != null) {
		return value.filter((f) => f.laboratorio == option);
	} else {
		return value;
	}
});

Vue.filter("Farmacia", (value, option) => {
	if (option != null) {
		return value.filter((f) => f.cod_farmacia == option);
	} else {
		return value;
	}
});

//Filtros en ordenes
Vue.filter("FechaRange", (value, desde, hasta) => {
	if (desde && hasta) {
		if (desde <= hasta) {
			console.log("ENTRO AL IF");
			return value.filter((f) => f.fecha >= desde && f.fecha <= hasta);
		} else {
			swal("¡ERROR!", "Ingrese correctamente las fechas", "error");
			return value;
		}
	} else {
		console.log("NO SE PUEDE REALIZAR");
		return value;
	}
});

Vue.filter("Servicio", (value, option) => {
	if (option != null) {
		return value.filter((f) => f.servicio == option);
	} else {
		return value;
	}
});

Vue.filter("Realizado", (value, option) => {
	if (option != null) {
		let Bool = false
		if(option ==0) Bool = true
		return value.filter((f) => f.realizado == Bool);
	} else {
		return value;
	}
});

//Filtros en Socios
Vue.filter("Departamento", (value, option) => {
	if (option != null) {
		return value.filter((f) => f.departamento == option);
	} else {
		return value;
	}
});

Vue.filter("AlDia", (value, option) => {
	if (option != null) {
		return value.filter((f) => f.aldia == option);
	} else {
		return value;
	}
});

Vue.filter("FechaPagoRange", (value, desde, hasta) => {
	if (desde && hasta) {
		if (desde <= hasta) {
			console.log("ENTRO AL IF");
			return value.filter(
				(f) => f.fecharealizacion >= desde && f.fecharealizacion <= hasta
			);
		} else {
			swal("¡ERROR!", "Ingrese correctamente las fechas", "error");
			return value;
		}
	} else {
		console.log("NO SE PUEDE REALIZAR");
		return value;
	}
});

//Filtro en Estudios
Vue.filter("Tipo", (value, option) => {
	if (option != null) {
		return value.filter((f) => f.tipo == option);
	} else {
		return value;
	}
});

Vue.filter("Proveedor", (value, option) => {
	if (option != null) {
		return value.filter((f) => f.proveedor == option);
	} else {
		return value;
	}
});

Vue.filter("FechaRealizacionRange", (value, desde, hasta) => {
	if (desde && hasta) {
		if (desde <= hasta) {
			console.log("ENTRO AL IF");
			return value.filter(
				(f) => f.fecha >= desde && f.fecha <= hasta
			);
		} else {
			swal("¡ERROR!", "Ingrese correctamente las fechas", "error");
			return value;
		}
	} else {
		console.log("NO SE PUEDE REALIZAR");
		return value;
	}
});

//Filtros en Institutos

Vue.filter("Responsable", (value, option) => {
	if (option != null) {
		return value.filter((f) => f.responsable == option);
	} else {
		return value;
	}
});

Vue.filter("Provincia", (value, option) => {
	if (option != null) {
		return value.filter((f) => f.provincia == option);
	} else {
		return value;
	}
});

Vue.filter("Consultorio", (value, option) => {
	if (option != null) {
		return value.filter((f) => f.nombre == option);
	} else {
		return value;
	}
});

//Filtros en Gastos Salientes

Vue.filter("ModoPago", (value, option) => {
	if (option != null) {
		return value.filter((f) => f.modo_pago == option);
	} else {
		return value;
	}
});


Vue.filter("Split", (value) => {
	const v=value?value.split("/")[4]:value
	return v
});
