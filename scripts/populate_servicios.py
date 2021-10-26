import requests
#rom faker import Faker

_servicios = sorted([
    'Salud',
    'Farmacia', 
   'Odontología', 
    'Sepelio',
    'Óptica',
    'Cultura',
    'Deporte',
    'Turismo',
    'Proveeduría'
    'Órdenes de Compra',
    'Educación'
])


def populate_servicios(
    cantidad: int = len(_servicios), url: str = "http://127.0.0.1:8081/"
) -> None:
    url += "servicios/"
    
    print("Agregando {} servicios".format(cantidad))
    for i in range(0, cantidad):
        servicios = {}
        servicios["servicio"] = _servicios[i]
        
        r = requests.post(url, json=servicios)
        # print(farmacia)
        print(r.status_code, "servicio agregado {}".format(i))


if __name__ == "__main__":
    populate_servicios()
