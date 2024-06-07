from fastapi import FastAPI
from routes.users import user_router
from routes.events import event_router
from database.connection import conn, Settings

import uvicorn


app = FastAPI()
settings = Settings()

# 라우트 등록
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

# 애플리케이션이 시작될 때 데이터베이스 생성
@app.on_event("startup")
async def init_db():
    await settings.initailize_database()
# def on_startup():
#     conn()


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)