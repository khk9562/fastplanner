import asyncio
# asyncio 모듈은 활성 루프 세션을 만들어서 테스트가 단일 스레드로 실행되도록 함
import httpx
# httpx 테스트는 HTTP CRUD 처리를 실행하기 위한 비동기 클라이언트 역할을 함
import pytest
# pytest 모듈은 픽스처 정의를 위해 사용됨.

from main import app
from database.connection import Settings
from models.events import Event
from models.users import User

# 루프 세션 픽스처 정의
@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

# 기본 클라이언트 픽스처 정의
# 이 픽스처는 httpx를 통해 비동기로 실행되는 애플리케이션 인스턴스를 반환
@pytest.fixture(scope="session")
async def default_client():
    await Settings.init_db()
    async with httpx.AsyncClient(app=app, base_url="http://app") as client:
        yield client
        # 리소스 정리
        await Event.find_all().delete()
        await User.find_all().delete()

