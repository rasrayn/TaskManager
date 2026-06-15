
**Gestor de Tareas Inteligente**

Descripción:
- Este proyecto proporciona una pequeña aplicación de consola en Python para gestionar tareas simples y para descomponer tareas complejas en subtareas usando la API de OpenAI.

Características principales:
- Añadir tareas manualmente.
- Generar subtareas desde una descripción compleja mediante IA.
- Listar, completar y borrar tareas.

Requisitos:
- Python 3.8+
- Dependencias listadas en [requirements.txt](requirements.txt)

Instalación:
1. Clona o descarga este repositorio.
2. Crea y activa un entorno virtual (recomendado):

```bash
python -m venv .venv
source .venv/Scripts/activate    # Windows PowerShell: .venv\Scripts\Activate.ps1
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

Configuración de la API de OpenAI:
- El servicio de IA está en [ia_service.py](ia_service.py). Para que funcione, crea un archivo `.env` en la raíz con la variable:

```
OPENAI_API_KEY=tu_api_key_aqui
```

- Si no configuras la clave, la función `create_simple_tasks()` devolverá un mensaje de error y no realizará llamadas.

Ejecución:
- Lanza la aplicación desde la raíz del proyecto:

```bash
python main.py
```

Uso (menú):
- Al ejecutar `main.py` verás el menú con las opciones:
	- `1. Añadir tarea.`: Añade una tarea simple introduciendo su descripción.
	- `2. Añadir tarea compleja.(IA)`: Pide una descripción larga; la app solicitará a la IA que devuelva entre 3 y 5 subtareas y las añadirá automáticamente.
	- `3. Listar tarea.`: Muestra las tareas actuales con sus IDs y estado.
	- `4. Completar tarea.`: Marca una tarea como completada por su ID.
	- `5. Borrar tarea.`: Elimina una tarea por su ID.
	- `6. Salir`: Sale de la aplicación.

Notas sobre el servicio IA:
- La lógica de la petición y el parsing de la respuesta está en [ia_service.py](ia_service.py). El servicio crea un prompt en español y espera respuestas con líneas que empiecen por guion (`- subtarea`).
- Manejo de errores: Si la respuesta no contiene subtareas válidas, el servicio devuelve un mensaje de error que `main.py` imprimirá y no añadirá tareas.

Estructura de archivos relevantes:
- [main.py](main.py): Interfaz de consola y bucle principal.
- [taskManager.py](taskManager.py): Lógica para añadir/listar/completar/borrar tareas.
- [ia_service.py](ia_service.py): Cliente y funciones para generar subtareas usando OpenAI.
- [requirements.txt](requirements.txt): Dependencias del proyecto.

Ejemplo rápido:
1. Ejecuta `python main.py`.
2. Elige `2` y escribe: "Preparar presentación final del curso".
3. Si la API devuelve subtareas, se añadirán automáticamente y podrás listarlas con la opción `3`.

Buenas prácticas y seguridad:
- No comites tu `.env` con la clave de OpenAI a repositorios públicos.
- Controla el uso de la API para evitar costes inesperados.

Contacto y licencia:
- Proyecto de ejemplo sin licencia explícita. Adapta según tu necesidad.
