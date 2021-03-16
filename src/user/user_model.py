
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int #id field is required when instantiating now
    jwt: Optional[str]
    name: str
    email: str