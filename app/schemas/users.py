from pydantic import BaseModel


class UserScheme(BaseModel):
    first_name: str
    last_name: str
