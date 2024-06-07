import time
from datetime import datetime

from fastapi import HTTPException, status
from jose import jwt, JWTError
from database.connection import Settings

settings = Settings()

# 토큰 생성
def create_access_token(user:str):
    payload = {
        "user" : user,
        # 만료 시간은 생성 시점에서 한시간 후로 설정
        "expires" : time.time() + 3600
    }

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token


# 토큰 검증
def verify_access_token(token:str):
    try:
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        expire = data.get("expires")

        if expire is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="토큰이 유효하지 않습니다."
            )
        if datetime.utcnow() > datetime.utcfromtimestamp(expire):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="토큰이 만료되었습니다."
            )
        return data

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="토큰이 유효하지 않습니다."
        )