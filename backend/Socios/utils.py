import datetime


# Funcion para calcular la edad de una persona
def calcular_edad(fecha_nac):
    fecha_actual = datetime.datetime.now()

    if fecha_actual.year > fecha_nac.year:
        if fecha_actual.month > fecha_nac.month:
            edad = fecha_actual.year - fecha_nac.year
        elif fecha_actual.month < fecha_nac.month:
            edad = (fecha_actual.year - fecha_nac.year) - 1
        elif fecha_actual.day >= fecha_nac.day:
            edad = fecha_actual.year - fecha_nac.year
        else:
            edad = (fecha_actual.year - fecha_nac.year) - 1
    elif fecha_actual.year == fecha_nac.year:
        edad = 0
    else:
        edad = None
    return edad
