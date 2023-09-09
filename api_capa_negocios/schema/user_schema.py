from pydantic import BaseModel
from typing import Optional

class Userschema(BaseModel):
    id: Optional[str]
    nombres: str
    apellidos: str
    password : str
    fecha: str
    
class DataUser(BaseModel):
    nombres : str
    password: str