
from typing import List
from fastapi import APIRouter,Depends,status,Response,HTTPException
from sqlalchemy.orm import Session
from blog import models, schemas
from blog.database import get_db
from ..oauth2 import get_current_user
from ..repository.blog import create, destory, get, get_all, update

router=APIRouter(prefix="/blog",tags=["Blogs"]
)

@router.get('/',response_model=List[schemas.ShowBlog])
def all(db:Session=Depends(get_db),current_user:schemas.User=Depends(get_current_user)):
   return get_all(db)

@router.post('/create',status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User=Depends(get_current_user)):
    return create(request,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog(id,request:schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User=Depends(get_current_user)):
    return update(id,db,request)
   

@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id,db:Session=Depends(get_db),current_user:schemas.User=Depends(get_current_user)):
    return get(id,db)

@router.delete('/delete/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session=Depends(get_db),current_user:schemas.User=Depends(get_current_user)):
    
   return destory(id,db)

