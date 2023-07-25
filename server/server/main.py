from pydantic import BaseModel
import uvicorn
import os
from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse 
from server.measure import process
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:4173",
    "https://cad-prototype.pages.dev",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PathConfig(BaseModel):
    diameter: int

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/healthcheck")
def health_check():
    return {"status": "ok"}

@app.get("/load/model/{model_id}")
async def load_model(model_id: str):
    return FileResponse(f"data/{model_id}.stl")

@app.post("/upload/image")
async def upload_image(file: UploadFile, vertical: float, area_threshold: int):
    # save image
    img_path = f"images/{file.filename}"
    with open(img_path, "wb") as buffer:
        buffer.write(await file.read())

    process.process_image(img_path, vertical, area_threshold)
    return {"status": "ok"}

@app.post("/upload/image/pixel")
async def upload_image_with_pixel_per_mm(
    file: UploadFile, 
    pixel_per_mm: float, 
    area_threshold: int):
    # save image
    img_path = f"images/{file.filename}"
    with open(img_path, "wb") as buffer:
        buffer.write(await file.read())

    process.process_image_with_pixel_per_mm(img_path, pixel_per_mm, area_threshold)
    return {"status": "ok"}


@app.get("/load/image")
async def load_image():
    return FileResponse("images/result.jpg")

@app.get("/load/image/pixel")
async def load_image_with_pixel_per_mm():
    return FileResponse("images/result_with_pixel.jpg")

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("server.main:app", host="0.0.0.0", port=8000, reload=False)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))