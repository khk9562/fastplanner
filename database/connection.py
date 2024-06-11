from sqlmodel import SQLModel, Session, create_engine
from models.events import Event
# 데이터베이스 초기화
from beanie import init_beanie, PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional, Any, List
from pydantic import BaseSettings, BaseModel

from models.users import User
from models.events import Event

from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    SECRET_KEY: Optional[str] = None
    
    async def initailize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        db = client.get_database("planner")
        await init_beanie(
            database=db,
            document_models=[Event, User]
        )

        class Config:
            env_file = ".env"
    
    async def init_db():
        test_settings = Settings()
        test_settings.DATABASE_URL = "mongodb://localhost:27017/testdb"

        await test_settings.initailize_database()

class Database:
    def __init__(self, model):
        self.model = model
    
    # 생성 처리
    async def save(self, document) -> None:
        await document.create()
        return

    # 조회 처리
    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False

    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all().to_list()
        return docs
    
    # 변경 처리
    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        doc_id = id
        des_body = body.dict()
        des_body = {k:v for k,v in des_body.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}

        doc = await self.get(doc_id)
        if not doc:
            return False
        await doc.update(update_query)
        return doc
    
    # 삭제 처리
    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True
    
# 데이터베이스 생성 p109
# SQLModle에서는 SQLAlchemy 엔진을 사용해서 데이터베이스 연결
# SQLAlchemy엔진은 crete_engine() 메서드를 사용해서 만들며 SQLModel 라이브러리에서 임포트

# create_engine() 메서드는 데이터베이스 URL을 인수로 사용
# 데이터베이스 URL은 sqlite:///dtabase.db 또는 sqlite:///database.sqlite와 같은 형식
# create_engine()은 echo를 선택적 인수로 지정할 수 있고, True로 설정하면 실행된 SQL 명령 출력

database_file = "planner.db"
database_connection_string = f"sqlite:///{database_file}"
connect_args = {"check_same_thread": False}
engine_url = create_engine(database_connection_string, echo=True, connect_args=connect_args)

def conn():
    SQLModel.metadata.create_all(engine_url)

def get_session():
    with Session(engine_url) as session:
        yield session