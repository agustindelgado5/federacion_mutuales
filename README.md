# Federación de Mutuales

## Lista de tareas pa hacer


## Levantar sistema Localmente

### Paso 0 - Clonar el repo
	git clone https://Dariiio@bitbucket.org/EstebanSaborido/2021-federacionmutuales.git

	cd 2021-federacionmutuales
	

### Opción 1 - Docker y node (para el front nomas)

1. 
	Nos movemos a la raíz del repo y ponemos:

		docker-compose -f "docker-compose.yml" up -d --build

	**Importante:** bajá los contenedores que tengas levantado con:

		docker-compose down

	Si lo mismo tira algún problema de que *ya existe x cosa o del estilo*, probá con un system prune antes de rebuildear todo

		docker system prune
	Para saber que está todo ok tirá para ver que los dos contenedores estén levantados
	
		docker ps


2. Una vez levantado los contenedores, debemos hacer las migraciones por si hubo cambios en los modelos de la base de datos, para esto tiramos:

		docker exec backend python manage.py makemigrations Socios Profesionales Ordenes Mutuales Medicamentos Farmacias Administracion

	y después:

		docker exec backend python manage.py migrate


3. Nos movemos a frontend

		cd frontend

4. Instalamos las dependencias con npm

		npm install

5. Levantamos el servidor

		npm run serve


#### Los links deberían ser:

back:

	http://localhost:8081/

front:

	http://localhost:8082/

y postgres corriendo en: 
	
	http://localhost:5430/

Listooo... Si no explotó nada ya está todo ok!


### Opción 2 - Localmente (Django, PostgreSQL y Node-js)


