from pydantic import BaseModel

class Satellite(BaseModel):
    id: str
    name: str