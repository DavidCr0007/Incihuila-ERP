# ERP Multisede

Base de proyecto ERP multisede para Incihuila con soporte para las sedes de Neiva, Florencia y Villavicencio. El entorno está preparado para desarrollo local con Docker, VS Code y Dev Containers.

## Requisitos
- Docker y Docker Compose
- Make

## Puesta en marcha
```bash
cp .env.example .env
make up
```

La aplicación estará disponible en `http://localhost:8000` y la documentación de la API en `http://localhost:8000/api/docs/`.

## Estructura principal
- `src/`: Código fuente de Django y aplicaciones internas.
- `deploy/`: Configuración de despliegue (Gunicorn, Nginx).
- `requirements/`: Dependencias separadas para desarrollo y producción.
- `.vscode/` y `.devcontainer/`: Configuraciones para Visual Studio Code.

## Apps incluidas
- `core`: utilidades y configuración base.
- `accounts`: gestión de usuarios y roles.
- `logistics`: procesos logísticos y de inventario.
- `adminflow`: automatización administrativa.
- `hr`: recursos humanos.

## Comandos útiles
- `make up`: levanta los servicios en segundo plano.
- `make down`: detiene y elimina los contenedores.
- `make logs`: muestra los logs del servicio web.
- `make migrate`: ejecuta las migraciones de Django.
- `make createsuperuser`: crea un usuario administrador.
