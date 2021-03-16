#defines the auth module, which provides the ability to validate and sign JWTS based on any object.
from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

import ENV
from auth_models import Auth, Token
AUTH = Auth()
from ..DB.database_service import query

def checkPassWord(plainPassword:str, hashPassword:str):
        return AUTH.pwd_context.verify(plainPassword,hashPassword)

def getHash( plainItem:str):
    return AUTH.pwd_context.hash(plainItem)

async def getUser(jwt:Token):
    # gets user from MySQL using the jwt's user id.
    
    cursor = query("SELECT * from USER where id = {}")