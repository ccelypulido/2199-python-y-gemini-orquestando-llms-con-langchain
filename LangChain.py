from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from my_models import GEMINI_FLASH
from my_keys import GEMINI_API_KEY
from my_helper import encode_image
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain.globals import set_debug
from pydantic import BaseModel, Field  # <-- Importamos Pydantic para estructurar el JSON

set_debug(True)

# ==========================================
# 1. DEFINICIÓN DEL FORMATO JSON ESPERADO
# ==========================================
class ResumenEjecutivo(BaseModel):
    resumen_sencillo: str = Field(description="Un resumen muy claro, objetivo y amigable para el público colombiano.")
    palabras_clave: list[str] = Field(description="Lista de 3 a 5 palabras clave del análisis para búsquedas posteriores.")
    categoria_principal: str = Field(description="Categoría o área principal a la que pertenece el gráfico analizado.")

# Instanciamos el parser_json con la estructura definida
parser_json = JsonOutputParser(pydantic_object=ResumenEjecutivo)


# ==========================================
# 2. CONFIGURACIÓN DEL LLM Y LA IMAGEN
# ==========================================
llm = ChatGoogleGenerativeAI(
    api_key=GEMINI_API_KEY,
    model=GEMINI_FLASH
)

imagen = encode_image("datos/ejemplo_grafico.jpg")


# ==========================================
# 3. PRIMERA CADENA (ANÁLISIS DE IMAGEN)
# ==========================================
template_analisis = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Asume que eres un analista de imágenes. Tu tarea principal
            consiste en: analizar una imagen y extraer información importante
            de forma objetiva.

            # FORMATO DE SALIDA
            Descripción de la Imagen: 'Coloca aquí tu descripción de la imagen'
            Etiquetas: 'Coloca una lista con tres términos clave separados por coma'
            """
        ),
        (
            "user",
            [
                {
                    "type" : "text", 
                    "text" : "Describe la imagen: "
                },
                {
                    "type" : "image_url",
                    "image_url" : {"url":"data:image/jpeg;base64,{imagen_informada}"}
                }
            ]
        )
    ]
)

cadena_analisis = template_analisis | llm | StrOutputParser()


# ==========================================
# 4. SEGUNDA CADENA (ESTRUCTURACIÓN EN JSON)
# ==========================================
template_respuesta = PromptTemplate(
    template="""
    Genera un resumen, utilizando un lenguaje claro y objetivo, enfocado en el público colombiano. 
    La idea es que la comunicación del resultado sea lo más sencilla posible, priorizando los registros
    para consultas posteriores.

    #RESULTADO DE LA IMAGEN
    {respuesta_analisis_imagen}
    
    #FORMATO DE SALIDA REQUERIDO
    {formato_salida}
    """,
    input_variables=["respuesta_analisis_imagen"],
    partial_variables={
        # Ahora que parser_json está definido arriba, esto funcionará sin errores
        "formato_salida": parser_json.get_format_instructions()
    }
)

# Cambiamos el último StrOutputParser() por parser_json para recibir un diccionario
cadena_compuesta = (cadena_analisis | template_respuesta | llm | parser_json)


# ==========================================
# 5. EJECUCIÓN
# ==========================================
respuesta = cadena_compuesta.invoke({"imagen_informada": imagen})

# La respuesta ahora será un diccionario nativo de Python gracias al parser_json
print("\n--- RESULTADO EN FORMATO DICT (JSON) ---")
print(respuesta)
print(f"Tipo de dato devuelto: {type(respuesta)}")