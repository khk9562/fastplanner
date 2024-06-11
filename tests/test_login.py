import httpx
import pytest

@pytest.mark.asyncio
async def test_sign_new_user(default_client: httpx.AsyncClient) -> None:
    payload = {
        "email" : "testuser@packt.com",
        "password" : "testpassword"
    }
    headers = {
        "accept" : "application/json",
        "Content-type" : "application/json"
    }
    test_response = {
        "message" : "User created successfully."
    }
        # 사전에 해당 사용자가 존재하는 경우 삭제
    await default_client.delete("/user/testuser@packt.com")

    response = await default_client.post("/user/signup", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json() == test_response

        # 추가로, 테스트 후 해당 사용자를 삭제
    await default_client.delete("/user/testuser@packt.com")
