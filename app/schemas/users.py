from pydantic import BaseModel


class UserScheme(BaseModel):
    first_name: str
    last_name: str

    def create(self):
        return {'first_name': self.first_name, 'last_name': self.last_name}
