import requests
from faker import Faker


def populate_profesionales(
    cantidad: int = 500, url: str = "http://127.0.0.1:8000/"
) -> None:
    url += "profesionales/"
    fake = Faker()
    print("Agregando {} profesionales".format(cantidad))
    for i in range(1, cantidad + 1):
        profesional = {}
        profesional["id_medico"] = fake.unique.random_int()
        profesional["nombre"] = fake.first_name()
        profesional["apellido"] = fake.last_name()
        profesional["dni"] = fake.unique.random_int(min=30000000, max=50000000)
        profesional["fecha_nacimiento"] = str(fake.date_of_birth())
        profesional["domicilio"] = fake.street_address()
        profesional["localidad"] = fake.city()
        profesional["provincia"] = "Buenos Aires"
        profesional["email"] = fake.email()
        profesional["especialidad"] = fake.job()
        profesional["matricula"] = fake.unique.random_int(min=30000000, max=50000000)
        profesional["carencia"] = str(fake.future_date())
        profesional["fecha_ingreso"] = str(fake.past_date())
        r = requests.post(url, json=profesional)
        print(r.status_code, "profesional agregado {}".format(i))


if __name__ == "__main__":
    populate_profesionales()
