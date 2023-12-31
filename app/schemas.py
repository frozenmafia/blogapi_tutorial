from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

class PostBase(BaseModel):
    title:str
    content:str
    published:bool = True 

class  PostCreate(PostBase):
    pass

class Post(PostBase):
    id:int
    created_st:datetime

class UserCreate(BaseModel):
    email:EmailStr
    password:str
    name:str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at:datetime
     
class UserLogin(BaseModel):
    email : EmailStr
    password:str

class Token(BaseModel):
    access_token :str
    token_type :str

class TokenData(BaseModel):
    id:Optional[str] = None