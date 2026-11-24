# Rutas Puebla — Sprint 1 (CRUD en Python + Redis Cloud + Mapa Leaflet)

API REST y aplicación web para la administración de paradas de transporte público de la ciudad de Puebla mediante operaciones CRUD, almacenando los registros como documentos JSON en **Redis Cloud** y visualizándolos en un mapa interactivo con **Leaflet**.

## Estructura del proyecto

```text
rutas-puebla/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── routes.py
├── static/
│   ├── index.html
│   ├── styles.css
│   └── app.js
├── .env
├── .env.example
├── requirements.txt
└── README.md
```

## Instalación

1. Crear y activar entorno virtual:
   ```bash
   python -m venv venv
   # En Linux/macOS:
   source venv/bin/activate
   # En Windows:
   venv\Scripts\activate
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configurar Redis Cloud:
   Edita el archivo `.env` con tu cadena de conexión real de Redis Cloud:
   ```env
   REDIS_URL=rediss://default:TU_PASSWORD@TU_HOST:PUERTO
   ```

## Ejecución

Inicia el servidor con Uvicorn:

```bash
uvicorn app.main:app --reload
```

- **Aplicación Web y Mapa:** http://127.0.0.1:8000/
- **Documentación Swagger API:** http://127.0.0.1:8000/docs
- **Estado de conexión Redis:** http://127.0.0.1:8000/estado

## Endpoints del CRUD

| Método | Ruta | Acción |
| :--- | :--- | :--- |
| `POST` | `/paradas/` | Crear parada |
| `GET` | `/paradas/` | Listar paradas |
| `GET` | `/paradas/{id}` | Obtener una parada |
| `PUT` | `/paradas/{id}` | Actualizar parada |
| `DELETE` | `/paradas/{id}` | Eliminar parada |
