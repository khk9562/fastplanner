from fastapi import APIRouter, Depends, HTTPException, status
from models.users import User, UserSignIn
from database.connection import Database
from auth.hash_password import HashPassword

user_router = APIRouter(
    tags=["User"]
)

user_database = Database(User)
hash_password = HashPassword()

users = {}

# 사용자 모델(User)을 함수에 전달해 email 필드 추출

@user_router.post("/signup")
async def sign_new_user(data: User) -> dict:
    user_exist = await User.find_one(User.email == data.email)
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="이미 존재하는 사용자입니다."
        )
    hashed_password = hash_password.create_hash(data.password)
    data.password = hashed_password
    # users[data.email] = data
    await user_database.save(data)
    return {"message": "사용자 등록 성공"}

@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    print("로그인한 이메일",user.email)
    print("user_exist",user_exist)
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 사용자입니다."
        )
    if user_exist.password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="잚못된 비밀번호입니다."
        )
    return {"message": "로그인 성공"}