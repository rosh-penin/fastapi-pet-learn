from fastapi import FastAPI, Depends
from typing import Annotated

from .auth import oauth2_scheme
from .engine import Base, engine
from .models.users import *
from .routers import users

api = FastAPI()
api.include_router(users.router)

# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


@api.post('/auth/')
def get_token(token: Annotated[str, Depends(oauth2_scheme)]):
    return {'Token': token}
# @app.get('/{item_id}')
# def read_item(item_id, item: Item):
#     return {'item': item_id, 'name': item.name}


# @app.put("/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}
