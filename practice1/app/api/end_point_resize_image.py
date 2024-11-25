from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
import os
import subprocess

router = APIRouter()

@router.post("/resize_images/")
async def resize_image(file: UploadFile = File(...), orientation: str = Form(..., 
        description="Image orientation: Type 'h' for horizontal, 'v' for vertical",
        example="h"
    )):
    """
    Resize a given image to SD (480x640/640x480).
    - `file`: Image provided by the user.
    - `orientation`: Image orientation: Type 'h' for horizontal, 'v' for vertical.
    """

    # Verifica la orientación
    if orientation not in ["h", "v"]:
        raise HTTPException(status_code=400, detail="Orientation must be 'h' or 'v'.")

    # Guarda el archivo subido temporalmente
    input_path = f"/tmp/{file.filename}"
    output_path = f"/tmp/resized_{file.filename}"
    with open(input_path, "wb") as f:
        f.write(await file.read())

    # Determina el comando de redimensionamiento
    if orientation == "v":
        command = ['ffmpeg', '-y', '-i', input_path, '-vf', 'scale=480:640', output_path]
    else:
        command = ['ffmpeg', '-y', '-i', input_path, '-vf', 'scale=640:480', output_path]

    # Ejecuta el comando
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail="Error resizing the image.")

    # Devuelve la imagen procesada al usuario
    return FileResponse(output_path, media_type="image/jpeg", filename=f"resized_{file.filename}")
