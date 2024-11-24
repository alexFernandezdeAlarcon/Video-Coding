from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
import os

router = APIRouter()

SCRIPTS_DIR = "app/scripts_S1"  # Ruta donde se encuentra el archivo
NOTEBOOK_FILE = "first_seminar.ipynb"  # Nombre del archivo .ipynb


@router.get("/notebook", tags=["Notebook"])
def download_notebook():
    """
    Proporciona el archivo .ipynb para su descarga.
    """
    file_path = os.path.join(SCRIPTS_DIR, NOTEBOOK_FILE)
    if os.path.isfile(file_path):
        return FileResponse(file_path, media_type="application/x-ipynb+json", filename=NOTEBOOK_FILE)
    else:
        raise HTTPException(status_code=404, detail="Notebook no encontrado")


@router.get("/notebook/view", tags=["Notebook"])
def view_notebook():
    """
    Proporciona un enlace para visualizar o descargar el archivo.
    """
    file_path = os.path.join(SCRIPTS_DIR, NOTEBOOK_FILE)
    if os.path.isfile(file_path):
        html_content = f"""
        <html>
            <head>
                <title>Notebook</title>
            </head>
            <body>
                <h1>Notebook de Scripts</h1>
                <p>Puedes descargar el notebook con todos los scripts aquí:</p>
                <a href="/files/notebook">Descargar Notebook</a>
            </body>
        </html>
        """
        return HTMLResponse(content=html_content)
    else:
        raise HTTPException(status_code=404, detail="Notebook no encontrado")
