from pydantic import BaseModel

from fastapi import FastAPI
from server.path import cq_profile

app = FastAPI()

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
