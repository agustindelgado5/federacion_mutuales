import requests
#rom faker import Faker

_mutuales = sorted([
    'MUTUAL DE TRABAJADORES DEL NORTE ARGENTINO',
    'CENTRO SOCIAL DON BOSCO DE PROTECCION RECIPROCA', 
    'MUTUAL TRIBUNAL DE FALTAS', 
    'MUTUAL NUEVO TIEMPO',
    'MUTUAL MUNICIPALES COMUNAS RURALES DE TUCUMÁN',
    'MUTUAL PERSONAL NORWINCO',
    'MUTUAL INDEPENDENCIA TUCUMÁN',
    'MUTUAL PROVINCIAL DE EMPLEADOS MUNICIPALES',
    'MUTUAL DE LA SANIDAD'
])


def populate_mutuales(
    cantidad: int = len(_mutuales), url: str = "http://127.0.0.1:8000/"
) -> None:
    url += "mutuales/"
    
    print("Agregando {} mutuales".format(cantidad))
    for i in range(0, cantidad):
        mutuales = {}
        mutuales["nombre"] = _mutuales[i]
        mutuales["direccion"] = '---'
        mutuales["sucursal"] = 'Capital'
        
        r = requests.post(url, json=mutuales)
        
        print(r.status_code, "mutual agregado {}".format(i))


if __name__ == "__main__":
    populate_mutuales()
