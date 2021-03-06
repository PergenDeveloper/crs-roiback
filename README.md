# CRS API

Este proyecto implementa la prueba backend de Roiback

## Guía de instalación

### Instalar y activar un entorno virtual
> `python3 -m venv crsvenv` 
>
> `source  crsvenv/bin/activate`

### Clonar el proyecto
> `git clone https://github.com/PergenDeveloper/crs-roiback.git`
> 
> `cd crs-roiback`

### Entorno local
#### Instalar dependencias del proyecto
> `pip install -r requirements/local.txt`

#### Aplicar las migraciones
> `python manage.py migrate`

#### Lanzamos los tests
> `pytest`

#### Ejecutar el proyecto
> `python manage.py runserver`


### Entorno de producción
#### Instalar dependencias del proyecto
> `pip install -r requirements/production.txt`


Antes de ejecutar el proyecto en producción es necesario configurar las siguientes 
variables de entorno:

`SECRET_KEY`: Es la clave secreta que usa Django para 
la encriptación

`ALLOWED_HOSTS`: Los hosts o dominios están separados por comas. 
Eg: dominio.es,mi.dominio.com

`SQLITE3_FILEPATH`: En este caso sería el path del fichero *.sqlite3

También es necesario tener especial atención a las configuraciones de seguridad
que se encuentran en el fichero `config/settings/production.py`


## API REST

Se ha habilitado la documentación de la API mediante `Swagger` en 
entornos de desarrollo, en la siguiente dirección:
> `127.0.0.1:8000`


Por otra parte, el paquete `djangorestframework` nos ofrece una interfaz cómoda para gestionar los datos
mediante el navegador.

A continuación vamos a especificar los diferentes servicios:

### HOTELES

Introducir en el navegador `127.0.0.1:8000/api/hotels/`

| Endpoint      | HTTP METHOD | Descripción | Campos
| ----------- | ----------- | -----------| -----------
| `/api/hotels/`      | `POST`       |  Crear un nuevo hotel | code, name
| `/api/hotels/`   | `GET`        |  Obtener lista de códigos de hotel |
| `/api/hotels/<hotel_code>/`   | `GET`        |  Obtener los detalles del hotel |
| `/api/hotels/<hotel_code>/`   | `PUT / PATCH`       |  Modificar datos del hotel | code, name
| `/api/hotels/<hotel_code>/`   | `DELETE`        |  Eliminar el hotel |


### HABITACIONES

Introducir en el navegador `127.0.0.1:8000/api/rooms/`

| Endpoint      | HTTP METHOD | Descripción | Campos
| ----------- | ----------- | ----------- | -----------
| `/api/rooms/`      | `POST`       |  Crear una habitación | hotel, code, name
| `/api/rooms/`   | `GET`        |  Obtener lista de habitaciones |
| `/api/rooms/<room_code>/`   | `GET`        |  Obtener los detalles de una habitación |
| `/api/rooms/<room_code>/`   | `PUT / PATCH`       |  Modificar datos de la habitación | hotel, code, name
| `/api/rooms/<room_code>/`   | `DELETE`        |  Eliminar la habitación |

- NOTA: Al campo hotel se le pasa el código del hotel


### TARIFA

Introducir en el navegador `127.0.0.1:8000/api/rates/`

| Endpoint      | HTTP METHOD | Descripción | Campos
| ----------- | ----------- | ----------- | -----------
| `/api/rates/`      | `POST`       |  Crear una tarifa | room, code, name
| `/api/rates/`   | `GET`        |  Obtener lista de tarifas |
| `/api/rates/<rate_code>/`   | `GET`        |  Obtener los detalles de una tarifa |
| `/api/rates/<rate_code>/`   | `PUT / PATCH`       |  Modificar datos de la tarifa | room, code, name
| `/api/rates/<rate_code>/`   | `DELETE`        |  Eliminar una tarifa |

- NOTA: Al campo room se le pasa el código de la habitación

### INVENTARIO

Introducir en el navegador `127.0.0.1:8000/api/inventories/`

| Endpoint      | HTTP METHOD | Descripción | Campos
| ----------- | ----------- | ----------- | -----------
| `/api/inventories/`      | `POST`       |  Crear un inventario | rate, date, price, allotment
| `/api/inventories/`   | `GET`        |  Obtener lista de inventarios |
| `/api/inventories/<inventory_id>/`   | `GET`        |  Obtener los detalles de un inventario |
| `/api/inventories/<inventory_id>/` | `PUT / PATCH` | Modificar datos del inventario | rate, date, price, allotment
| `/api/inventories/<inventory_id>/`   | `DELETE`        |  Eliminar un inventario |

- NOTA: Al campo rate se le pasa el código de la tarifa

### CONSULTAR DISPONIBILIDAD
| Endpoint      | HTTP METHOD | Descripción | 
| ----------- | ----------- | ----------- | 
| `/api/availability/<hotel_code>/<checkin_date>/<checkout_date>` | `GET`  |  Consultar disponibilidad en hotel

## ACCIONES PRE-COMMIT

Antes realizar cualquier commit en el código es necesario ejecutar los siguientes comandos, y asegurarnos
que ninguno genera WARNINGS o ERRORS

> `flake8`: Nos aseguramos que nuestro código está limpio
> 
> `pytest`: Ejecutamos todos los tests implementados