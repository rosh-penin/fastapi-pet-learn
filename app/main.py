from fastapi import FastAPI

from engine import Session, engine, Base
import models
from routers import users

app = FastAPI()
app.include_router(users.router)


Base.metadata.create_all(engine)
# @app.get('/{item_id}')
# def read_item(item_id, item: Item):
#     return {'item': item_id, 'name': item.name}


# @app.put("/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}
