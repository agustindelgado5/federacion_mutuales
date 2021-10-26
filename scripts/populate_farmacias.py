import requests
from faker import Faker

def populate_farmacias(
    cantidad: int = 500, url: str = "http://127.0.0.1:8081/"
) -> None:
    url += "farmacias/"
    fake  = Faker(['es-MX', 'es-MX', 'es-MX', 'es-MX', 'es-MX', 'es-MX', 'es-MX', 'es-MX', 'es-MX', 'es-MX'])
    print("Agregando {} farmacias".format(cantidad))
    for i in range(1, cantidad + 1):
        farmacia = {}
        farmacia["cod_farmacia"] = fake.unique.random_int()
        farmacia["cuit"] = fake.unique.random_int()
        farmacia["matricula_farm"] = fake.unique.random_int(min=30000000, max=50000000)
        farmacia["farmacia"] = fake.first_name()
        farmacia["direccion"] = fake.street_address()
        farmacia["localidad"] = fake.city()
        farmacia["cod_postal"] = fake.postcode()
        farmacia["email"] = fake.email()
        farmacia["representante"] = fake.name()
        # farmacia["tel_celular"] = fake.phone_number()

        r = requests.post(url, json=farmacia)
        # print(farmacia)
        print(r.status_code, "farmacia agregado {}".format(i))


if __name__ == "__main__":
    populate_farmacias()
