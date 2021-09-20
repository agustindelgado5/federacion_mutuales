import requests
from faker import Faker

fake = Faker()

url = "http://localhost:8081/socios/"

# Populate socios
for i in range(20):
    socio = {}
    
    socio['numero_socio'] = fake.unique.random_int()
    socio['nombre'] = fake.first_name()
    socio['apellido'] = fake.last_name()
    socio['dni'] = fake.unique.random_int(min=30000000, max=50000000)
    socio['fecha_nacimiento'] = str(fake.date_of_birth())
    socio['calle'] = fake.street_address()
    socio['localidad'] = fake.city()
    socio['cod_postal'] = fake.postcode()
    socio['email'] = fake.email()
    # socio['tel_fijo'] = fake.phone_number()
    socio['carencia'] = str(fake.future_date())
    socio['departamento'] = "Burruyacú"

    r = requests.post(url, json=socio)
    print(r.status_code)


