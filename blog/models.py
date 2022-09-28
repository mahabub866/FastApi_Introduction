
from datetime import datetime
from email.policy import default
from enum import unique
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
import sqlalchemy as sa
from blog.database import Base

class Blog(Base):
    __tablename__ = 'blogs'

    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    body=Column(String)
    user_id=Column(Integer,ForeignKey('users.id'))

    creator = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__ = 'users'

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)

    blogs = relationship("Blog", back_populates="creator")

class UserExamp(Base):
    __tablename__ = 'usersex'

    id=sa.Column(sa.Integer,primary_key=True,index=True)
    name=sa.Column(sa.String)
    email=sa.Column(sa.String,unique=True)
    create_date=sa.Column(sa.DateTime,default=datetime.now,index=True)
    last_login=sa.Column(sa.DateTime,default=datetime.now,index=True)
    password=sa.Column(sa.String)

    blogs = relationship("Blog", back_populates="creator")
