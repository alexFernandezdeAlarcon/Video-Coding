from fastapi import FastAPI
from app.api.end_point_resize_image import router as resize_router 
from app.api.end_point_scripts import router as scripts_router 
from fastapi.responses import HTMLResponse


app = FastAPI(
    title="Image & Video Processing Lab1 API",
    description="""
    We implemented the resize to SD method image and convert to B&W one.
    Developed by": "Miquel Ferreiro Rojas & Alex Fernandez de Alarcon
    """,
    version="1.0.0",
    contact={
        "Developed by": "Miquel Ferreiro Rojas & Alex Fernandez de Alarcon",
        "url": "https://github.com/alexFernandezdeAlarcon/Video-Coding",
    },
)



app.include_router(resize_router, prefix="/images", tags=["Image Processing"])
app.include_router(scripts_router, prefix="/files", tags=["Notebook"])

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <html>
        <head>
            <title>API de Procesamiento de Imágenes</title>
        </head>
        <body>
            <h1>Bienvenido a la API</h1>
            <h2>Endpoints disponibles</h2>
            <ul>
                <li><a href="/docs">Documentación interactiva (Swagger UI)</a></li>
                <li><a href="/images/resize_images/">Redimensionar imagen</a></li>
                <li><a href="/images/serpentine/">Lectura en serpiente</a></li>
                <li><a href="/files/notebook/view">Notebook con scripts</a></li>
            </ul>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
