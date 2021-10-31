import requests
from faker import Faker


def populate_medicamentos(
    cantidad: int = 500, url: str = "http://127.0.0.1:8000/"
) -> None:
    url += "medicamentos/"
    fake  = Faker(['es-MX', 'es-ES', 'es-MX', 'es-MX', 'es-MX'])
    print("Agregando {} medicamentos".format(cantidad))
    for i in range(1, cantidad + 1):
        remedio = {}
        remedio["id_medicamento"] = i #fake.unique.random_int()
        remedio["nombre"] = fake.cryptocurrency_name()
        
        remedio["presentacion"] = fake.catch_phrase()
        remedio["laboratorio"] = fake.company()
        remedio["cod_farmacia"] = "http://localhost:8081/farmacias/2/"
        r = requests.post(url, json=remedio)
        print(r.status_code, "medicamento agregado {}".format(i))


if __name__ == "__main__":
    populate_medicamentos()
