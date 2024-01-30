from fastapi import Depends, Request 
from jose import jwt, JWTError
from app.config import settings
from datetime import datetime
from app.exeptions import TokenExpiredExcexption, TokenAbsentException, IncorrectTokenFormatException, UserIsNotPresentException

from app.user.dao import UsersDAO
from app.user.models import Users


def get_token(request: Request):
    token = request.cookies.get("bookings_access_token")
    if not token :
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        print(f"Token: {token}")
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITNM
        )
        print(f"Decoded Payload: {payload}")
    except JWTError as e:
        print(f"Error decoding token: {e}")
        raise IncorrectTokenFormatException
    expire: str = payload.get("exp")
    if  (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredExcexption
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserIsNotPresentException
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise UserIsNotPresentException
    
    return user
