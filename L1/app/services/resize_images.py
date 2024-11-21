import subprocess
import os
from pathlib import Path

def resize_image_ffmpeg(image_path: str, orientation: str) -> str:
    # Define el nombre del archivo de salida
    output_image = Path(image_path).parent / (
        "output_image_480x640.jpg" if orientation == "v" else "output_image_640x480.jpg"
    )
    
    # Define el comando FFmpeg según la orientación
    if orientation == "v":
        command = ['ffmpeg', '-y', '-i', image_path, '-vf', 'scale=480:640', str(output_image)]
    else:
        command = ['ffmpeg', '-y', '-i', image_path, '-vf', 'scale=640:480', str(output_image)]

    # Ejecuta el comando
    subprocess.run(command, check=True)

    return str(output_image)  # Retorna la ruta de la imagen redimensionada
