from populate_farmacias import populate_farmacias
from populate_socios import populate_socios
from populate_profesionales import populate_profesionales
from populate_servicios import populate_servicios
from populate_mutuales import populate_mutuales


if __name__ == "__main__":

    api_url = "http://localhost:8081/"

    #populate_socios(url=api_url)
    #populate_profesionales(url=api_url)
    #populate_farmacias(url=api_url)
    #populate_servicios(url=api_url)
    populate_mutuales(url=api_url)
    