from fastapi import Depends, Request, HTTPException, status
from jose import jwt, JWTError
from app.config import settings
from datetime import datetime

from app.user.dao import UsersDAO
from app.user.models import Users


def get_token(request: Request):
    token = request.cookies.get("bookings_access_token")
    if not token :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
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
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    expire: str = payload.get("exp")
    if  (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user_id: str = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    return user
