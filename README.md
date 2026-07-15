# 2199 - Python y Gemini: Orquestando LLMs con LangChain

Este proyecto demuestra cómo usar LangChain y la API de Gemini para analizar imágenes con IA multimodal y convertir la respuesta en un formato estructurado en JSON.

## Objetivo

El flujo del proyecto permite:

- enviar una imagen al modelo de Gemini,
- extraer una descripción relevante de la imagen,
- generar un resumen claro y objetivo,
- devolver el resultado en un esquema definido mediante Pydantic.

## Funcionalidades

- Análisis de imágenes con modelos de lenguaje multimodales.
- Generación de descripciones, etiquetas y títulos.
- Transformación de respuestas en estructuras JSON organizadas.
- Uso de prompts y cadenas de procesamiento con LangChain.

## Tecnologías utilizadas

- Python
- LangChain
- Gemini API
- Pydantic
- python-dotenv
- Cohere (opcional en el proyecto)

## Estructura del proyecto

- `LangChain.py`: flujo principal de procesamiento con LangChain.
- `detalles_imagen.py`: definición del modelo de salida con Pydantic.
- `my_helper.py`: utilitario para codificar imágenes en Base64.
- `my_keys.py`: carga de claves API desde variables de entorno.
- `my_models.py`: configuración de modelos disponibles de Gemini.
- `datos/`: carpeta con imágenes de ejemplo.
- `requirements.txt`: dependencias del proyecto.

## Requisitos previos

- Python 3.9 o superior
- Una cuenta activa en Google AI Studio para obtener la API key de Gemini
- (Opcional) una clave de Cohere si se habilita esa parte del flujo

## Instalación

### 1. Crear y activar un entorno virtual

En Windows:

```bash
python -m venv .venv-gemini-3
.\.venv-gemini-3\Scripts\activate
```

En Linux o macOS:

```bash
python3 -m venv .venv-gemini-3
source .venv-gemini-3/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Configuración de variables de entorno

Crea un archivo llamado `.env` en la raíz del proyecto con el siguiente contenido:

```env
GEMINI_API_KEY=tu_api_key_aqui
COHERE_API_KEY=tu_api_key_aqui
```

> Si no vas a usar Cohere, puedes dejar la variable vacía o comentar la parte relacionada en el código.

## Ejecución

Ejecuta el archivo principal:

```bash
python3 LangChain.py
```

El programa analizará la imagen ubicada en `datos/ejemplo_grafico.jpg` y mostrará una respuesta generada por el modelo.

## Ejemplo de salida

El resultado esperado se estructura en campos como:

```json
{
  "titulo": "Descripción del contenido visual",
  "descripcion": "Resumen del análisis de la imagen",
  "etiquetas": ["palabra1", "palabra2", "palabra3"]
}
```

## Notas importantes

- Asegúrate de que la imagen que deseas analizar exista en la ruta indicada.
- Puedes cambiar el modelo usado desde `my_models.py`.
- Si el proyecto presenta errores de importación, revisa que el entorno virtual esté activado.

## Siguiente paso

Puedes ampliar este proyecto para trabajar con múltiples imágenes, agregar una interfaz web o integrar la salida con una base de datos o una API propia.
