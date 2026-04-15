import os

from dotenv import load_dotenv
from openai import OpenAI



load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def create_simple_tasks(description):
    
    if not client.api_key:
        return ("Error: La API key de OpenAi no está configurada.")
    
    try:
        
        prompt = f"""Desglosa la siguiente tarea compleja en una lista de 3 a 5 subtareas simples y accionables.
        
    tarea: {description}
    formato de respuesta:
    - subtarea 1
    - subtarea 2
    - subtarea 3
    - etc.
    
    Responde solo con la lista de subtareas, una por linea empezando cada linea, empezando cada linea con un guión.
    """
    #!!! TODO ESTA PUESTO EN LA DOCUMENTACIÓN. REVISAR
    
        params = {
            "model" : "gpt-5", #indicamos modelo gpt
            "messages": [ #indicamos el role y contexto a chat gpt
                {"role": "system", "content": "Eres un asistente experto en gestión de tareas que ayuda a dividir tareas complejas en pasos simples y accionables"},
                
                {"role": "user", "content": prompt},
            ],
            #mas parametros a gpt como el máximo de tokens a gastar, la verbosidad en la contestación o el razonamiento y lo que va a tardar en contestar.
            "max_completion_tokens": 300,
            "verbosity": "medium",
            "reasoning_effort": "minimal"
        }
        #lanzamos consulta, llamando al cliente configurado, chat y su capacidad para completar y creamos la peticion, con los dos asteriscos desempaquetamos el contenido del diccionario y lo guardxamos en una variable llamada response
        response = client.chat.completions.create(**params)
        
        content = response.choices[0].message.content.strip() #Accedemos a la primera respuesta al mensaje, contenido y le hacemos un strip para quitar espacios en blanco, este contenido es cada una de las substareas.
        
        subtasks = [] #creamos una lista de subtareas.
    
    #esto es para recorrer el contenido para encontrar cada una de las lineas, si esta empieza con guion entonces la subtarea existe y se añade en el listado de substareas que hemos creado arriba.
        for line in content.split("\n"):
            line = line.strip()
            if line and line.startswith("-"):
                subtask = line[1:].strip()#empezamos del caracter uno saltandonos el primer guion
                if subtask:
                    subtasks.append(subtask)
    #retornamos el listado si no esta vacio.
        return subtasks if subtasks else ("Error:No se han podido generar las subtareas.")
        
    except Exception:
        return ("Error: No se ha podido realizar la conexión a OpenAI")