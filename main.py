from fastapi import FastAPI
from routers import telemetry, satellites

app = FastAPI()

app.include_router(telemetry.router)
app.include_router(satellites.router)

@app.get("/")
def ping():
    return {"message": "Hello, World!"}