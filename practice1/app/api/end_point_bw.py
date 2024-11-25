from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import os
import tempfile
from app.services.bw_transform import transform_to_bw

router = APIRouter()

@router.post("/transform_bw/")
async def transform_image_to_bw(file: UploadFile = File(...), compression_rate: str = "28"):
    """
    Converts an uploaded image to black and white and returns it compressed.
    
    Args:
    - `file`: Image provided by the user.
    - `compression_rate`: Compression level (1-31). Default is 28.
    """
    try:
        # Crear un archivo temporal para la imagen subida
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[-1]) as temp_file:
            temp_file.write(await file.read())
            temp_file_path = temp_file.name

        # Procesar la imagen con la función transform_to_bw
        output_path = transform_to_bw(temp_file_path, compression_rate)

        # Retornar la imagen transformada como respuesta
        return FileResponse(output_path, media_type="image/jpeg", filename="output_gray_compressed.jpg")
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
    finally:
        # Eliminar el archivo temporal
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
