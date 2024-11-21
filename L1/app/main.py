from fastapi import FastAPI
from app.api.end_point_resize_image import router as resize_router  # Ajusta el path según tu estructura

app = FastAPI()

# Incluye el router de redimensionamiento
app.include_router(resize_router, prefix="/images", tags=["Image Processing"])

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
