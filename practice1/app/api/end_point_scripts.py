from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
import os

router = APIRouter()

SCRIPTS_DIR = "app/scripts_S1"  # Ruta donde se encuentra el archivo
NOTEBOOK_FILE = "first_seminar.ipynb"  # Nombre del archivo .ipynb


@router.get("/notebook", tags=["Notebook"])
def download_notebook():
    """
    Download the first_seminar.ipynb file.
    """
    file_path = os.path.join(SCRIPTS_DIR, NOTEBOOK_FILE)
    if os.path.isfile(file_path):
        return FileResponse(file_path, media_type="application/x-ipynb+json", filename=NOTEBOOK_FILE)
    else:
        raise HTTPException(status_code=404, detail="Notebook no encontrado")
