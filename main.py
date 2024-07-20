from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from .models import SubPage
from . import schema
from .database import engine_sql,session_sql
from . import models

models.Base.metadata.create_all(engine_sql)

app = FastAPI()

def sqlitedb():
    db = session_sql()
    try:
        yield db
    finally:
        db.close()

@app.post("/",response_model = schema.Subpage)
async def host(sub:schema.SubPagecreate,db:Session = Depends(sqlitedb)):
    # db_sub = SubPage(heading = sub.heading,description = sub.description,footer=sub.footer,pg_no=sub.pg_no,pg_dim=sub.pg_dim)
    db_sub = SubPage(dict(sub))
    db.add(db_sub)
    db.commit()
    db.refresh(db_sub) 
    return "db_sub result created"

@app.get("/",response_model = schema.Subpage)
async def get_subpage(id:int,db:Session = Depends(sqlitedb)):
     sub = db.query(SubPage).filter(id == SubPage.id)
     return sub
