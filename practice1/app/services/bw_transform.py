import subprocess
import os
from pathlib import Path
from fastapi import HTTPException

def transform_to_bw(image_path: str, compression_rate: str = "28") -> str:
    """
    Convierte una imagen a blanco y negro y la comprime utilizando FFmpeg.

    Args:
    - image_path: Ruta completa del archivo de imagen.
    - compression_rate: Tasa de compresión (1-31).

    Returns:
    - str: Ruta del archivo transformado.
    """
    try:
        # Ruta de salida
        output_image = Path(image_path).parent / "output_gray_compressed.jpg"

        # Comando para convertir a blanco y negro
        command = [
            "ffmpeg", "-y", "-i", image_path,
            "-vf", "format=gray", "-q:v", compression_rate,
            str(output_image)
        ]

        # Ejecutar el comando
        subprocess.run(command, check=True)

        # Verificar que la imagen de salida se haya creado
        if not output_image.exists():
            raise HTTPException(status_code=500, detail="Error al generar la imagen transformada.")

        return str(output_image)  # Retorna la ruta de la imagen transformada
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Error en FFmpeg: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inesperado: {e}")
