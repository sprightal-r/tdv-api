from pydantic import BaseModel

class TelemetryPointInfo(BaseModel):
    satelliteId: str
    timestamp: str
    altitude: float
    velocity: float
    status: str

class TelemetryPoint(TelemetryPointInfo):
    id: str