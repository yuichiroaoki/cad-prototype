from pydantic import BaseModel

from fastapi import FastAPI
from fastapi.responses import FileResponse
from server.path import cq_profile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
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

@app.post("/gcode/profile")
async def use_profile(conf: PathConfig):
    cq_profile.run_cq_profile(conf.diameter)
    return {"status": "ok"}

@app.get("/load/model/{model_id}")
async def load_model(model_id: str):
    return FileResponse(f"data/{model_id}.stl")