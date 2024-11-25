from fastapi import FastAPI
from app.api.end_point_resize_image import router as resize_router 
from app.api.end_point_scripts import router as scripts_router 
from fastapi.responses import HTMLResponse
from app.api.end_point_bw import router as bw_router
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI(
    title="Image & Video Processing Lab1 API",
    description=""" 
    We implemented the resize to SD method image and convert to B&W one.
    Developed by: Miquel Ferreiro Rojas & Alex Fernandez de Alarcon. All the API structure is contained in: https://github.com/alexFernandezdeAlarcon/Video-Coding
    """,
    version="1.0.0",
    contact={
        "Developed by": "Miquel Ferreiro Rojas & Alex Fernandez de Alarcon",
        "url": "https://github.com/alexFernandezdeAlarcon/Video-Coding",
    },
)

app.include_router(resize_router, prefix="/images", tags=["Image Processing"])
app.include_router(scripts_router, prefix="/files", tags=["Notebook"])
app.include_router(bw_router, prefix="/images", tags=["Image Processing"])

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <html>
        <head>
            <title>Practice 1 API by Miquel and Alex</title>
            <style>
                body {
                    font-family: 'Arial', sans-serif;
                    background-color: #f4f4f4;
                    color: #333;
                }
                h1 {
                    color: #007bff;
                }
                h2 {
                    color: #555;
                }
                ul {
                    list-style-type: none;
                }
                li {
                    margin: 10px 0;
                }
                a {
                    color: #007bff;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <h1>Practice 1 API by Miquel and Alex</h1>
            <h2>Links:</h2>
            <ul>
                <li><a href="/docs">Main page with two functional endpoints</a></li>
                <li><a href="/files/notebook">Download Notebook (.ipynb) with all S1 tasks</a></li>
            </ul>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
