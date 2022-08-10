
from turtle import title
from fastapi import FastAPI,Depends
from blog import models
from blog import schemas
from sqlalchemy.orm import Session

from blog.database import  SessionLocal, engine

from blog.schemas import Blog

app=FastAPI()

models.Base.metadata.create_all(engine)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog')
def create(request: schemas.Blog,db:Session=Depends(get_db)):
    new_blog=models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
