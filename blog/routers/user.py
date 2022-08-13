
from typing import List
from fastapi import APIRouter,Depends,status,Response,HTTPException
from sqlalchemy.orm import Session
from blog import models, schemas
from blog.database import get_db
from ..repository.user import add_user, show
from blog.hashing import Hash

router=APIRouter(prefix="/user",
    tags=["users"])

@router.post('/create',response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    return add_user(request,db)



@router.get('/{id}',status_code=200,response_model=schemas.ShowUser)
def get_user(id,db:Session=Depends(get_db)):
    return show(id,db)
