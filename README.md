# Blacklist Microservice Project

Este repositorio forma parte de una arquitectura basada en microservicios. Actualmente contiene el microservicio de listas negras (`blacklist_service`) y la configuración general del entorno de desarrollo y despliegue. Está diseñado desde el inicio para ser escalable y facilitar la incorporación de nuevos microservicios en el futuro. 

---

## 📁 Estructura del Proyecto

```
.
├── blacklist_service/        # Microservicio para gestionar listas negras de emails 
│   ├── app/                  # Código fuente del microservicio
│   │   ├── __init__.py       # Inicialización de la app Flask y configuración de extensiones
│   │   ├── models.py         # Modelos de base de datos con SQLAlchemy
│   │   ├── routes.py         # Endpoints REST de la API
│   │   ├── schemas.py        # Validaciones y serialización con Marshmallow
│   │   └── utils.py          # Funciones auxiliares
│   ├── config.py             # Configuración de la app (base de datos, JWT, etc.)
│   ├── Dockerfile            # Imagen Docker para el microservicio
│   ├── requirements.txt      # Dependencias del microservicio en Python
│   └── run.py                # Punto de entrada de la app Flask
├── db/                       # Servicio de base de datos (desarrollo local)
│   └── init.sql              # Script opcional para inicializar la base de datos
├── docker-compose.yml        # Orquestador de servicios para entorno local (multi-contenedor)
├── .env                      # Variables de entorno globales (no se incluye por seguridad)
└── Dockerrun.aws.json        # Configuración de despliegue multi-contenedor para AWS Elastic Beanstalk

```

---

## 🚀 Objetivo del Microservicio

El microservicio `blacklist_service` permite gestionar una lista negra global de emails. Provee dos endpoints principales:

- `POST /blacklists`: Agrega un email a la lista negra.
- `GET /blacklists/<email>`: Consulta si un email está en la lista negra.

Ambos endpoints requieren autorización mediante un token JWT estático (por ahora).

---

## 🐳 Despliegue y ejecución

- Para desarrollo local:
    
    `docker-compose up --build`
    
- Para despliegue en AWS Elastic Beanstalk (multi-contenedor):
    
    Se utiliza el archivo `Dockerrun.aws.json` versión 2.
    

---

## 🧱 Tecnologías utilizadas

- **Python 3.8+**
- **Flask 1.1.x**
- **Flask-SQLAlchemy**
- **Flask-RESTful**
- **Flask-Marshmallow**
- **Flask-JWT-Extended**
- **PostgreSQL**
- **Docker / Docker Compose**
- **AWS Elastic Beanstalk**

---

Este proyecto está en desarrollo y se actualizará a medida que se incorporen nuevos servicios y funcionalidades.