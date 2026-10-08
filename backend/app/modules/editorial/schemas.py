from pydantic import BaseModel

class Stories(BaseModel):
    title: str
    story: str
