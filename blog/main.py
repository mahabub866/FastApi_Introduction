

from turtle import title
from fastapi import FastAPI,Depends,status,Response,HTTPException
from blog import models
from blog import schemas
from sqlalchemy.orm import Session
from typing import List
from blog.database import  get_db, engine
from blog.routers import authentication

from .routers import blog,user
from blog.schemas import Blog, ShowBlog,User,ShowBlogDetails
from blog.hashing import Hash

app=FastAPI()

models.Base.metadata.create_all(engine)
# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

# @app.post('/create',status_code=status.HTTP_201_CREATED,tags=["Blogs"])
# def create(request: schemas.Blog,db:Session=Depends(get_db)):
#     new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.get('/blog',response_model=List[schemas.ShowBlogDetails],tags=["Blogs"])
# def all(db:Session=Depends(get_db)):
#     blogs=db.query(models.Blog).all()
#     return blogs

# @app.delete('/delete/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=["Blogs"])
# def destroy(id,response:Response,db:Session=Depends(get_db)):
    
#     blog=db.query(models.Blog).filter(models.Blog.id==id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog is not found {id}')
#     blog.delete(synchronize_session=False)
#     db.commit()
    
#     return {'Deleted Sucessufly'}

# @app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=["Blogs"])
# def update(id,request:schemas.Blog,db:Session=Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id==id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog is not found {id}')
#     blog.update(request.dict())
#     # blog.update({'title': request.title, 'body': request.body})
#     db.commit()
#     return  {'Updated Sucessufly'}

# @app.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog,tags=["Blogs"])
# def show(id,db:Session=Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id==id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} is not availabe')
#         # response.status_code=status.HTTP_404_NOT_FOUND
#         # return {'details': f'Blog with id {id} is not availabe'}
#     return blog



# @app.post('/user',response_model=schemas.ShowUser,tags=["users"])
# def create_user(request:schemas.User,db:Session=Depends(get_db)):
    
#     new_user=models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user



# @app.get('/user/{id}',status_code=200,response_model=schemas.ShowUser,tags=["users"])
# def get_user(id:int,db:Session=Depends(get_db)):
#     user=db.query(models.User).filter(models.User.id==id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user with id {id} is not availabe')
       
#     return user
