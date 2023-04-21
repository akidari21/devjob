from typing import Union

from fastapi import FastAPI

from pydantic import BaseModel

from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db

from models import Member, Profile, Category

HOSTNAME = '127.0.0.1'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'skehahffkdy'
DBNAME = 'jobees'
MYSQL_URL = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DBNAME}'

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=MYSQL_URL)

class Item(BaseModel):
  name: str
  price: float
  is_offer: Union[bool, None] = None

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# @app.put("/items/{item_id}")
# def read_item(item_id: int, item: Item):
#     return {"item_price": item.price, "item_id": item_id}


# get MariaDB
@app.get('/member')
async def select_member():
  query = db.session.query(Member)
  return query.all()

@app.get('/profile')
async def select_profile():
  query = db.session.query(Profile)
  return query.all()

@app.get('/category')
async def select_category():
  query = db.session.query(Category)
  return query.all()

# put
@app.put("/join/{item_id}")
def read_item(item_id: int, item: Item):
    return {"item_price": item.price, "item_id": item_id}