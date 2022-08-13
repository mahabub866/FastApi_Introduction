
from datetime import timedelta
from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from fastapi.security import  OAuth2PasswordRequestForm
from blog import models, schemas
from blog.database import get_db
from ..jwt_token import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from blog.hashing import Hash
router=APIRouter(tags=['Authentication'])


@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Credintials Invalid ')
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Password Invalid ')
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}