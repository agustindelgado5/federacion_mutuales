#!/bin/bash

echo "tirando un makemigrations"

while ! python manage.py makemigrations Socios Profesionales Ordenes Mutuales Medicamentos Farmacias 2>&1; do
    echo "makemigrations corriendo :V"
    sleep 2
done

echo "tirando un migrate"

while ! python manage.py migrate 2>&1; do
    echo "migrate corriendo :V"
    sleep 2
done


echo "Iniciando server de backend"

python manage.py runserver 0.0.0.0:8081
# bash

echo "El backend esta listo para que explotar"

exec "$@"