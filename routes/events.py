from beanie import PydanticObjectId
from fastapi import APIRouter, Body, HTTPException, status, Depends, Request
from database.connection import get_session, Database

from models.events import Event, EventUpdate
from typing import List
from sqlmodel import select

event_router = APIRouter(
    tags=["Events"]
)

events = []

event_database = Database(Event)

@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    events = await event_database.get_all()
    return events

# @event_router.get("/", response_model=List[Event])
# async def retrieve_all_events(session=Depends(get_session)) -> List[Event]:
#     statement = select(Event)
#     events = session.exec(statement).all()
#     return events


# @event_router.get("/", response_model=List[Event])
# async def retrieve_all_events() -> List[Event]:
#     return events

@event_router.get("/{id}", response_model=Event)
async def retrieve_events(id:PydanticObjectId) -> Event:
    event = await event_database.get(id)
    if not event :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="이벤트를 찾을 수 없습니다." 
        )
    return event

# @event_router.get("/{id}", response_model=Event)
# async def retrieve_events(id:int, session=Depends(get_session)) -> Event:
#     event = session.get(Event, id)
#     if event:
#         return event
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail="이벤트를 찾을 수 없습니다." 
#     )

# @event_router.get("/{id}", response_model=Event)
# async def retrieve_events(id:int) -> Event:
#     for event in events:
#         if event.id == id:
#             return event
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail="이벤트를 찾을 수 없습니다." 
#     )

@event_router.post("/new")
async def create_event(body: Event) -> dict:
    await event_database.save(body)
    return {
        "message": "이벤트가 성공적으로 등록되었습니다."
    }

# @event_router.post("/new")
# async def create_event(new_event: Event, session=Depends(get_session)) -> dict:
#     session.add(new_event)
#     session.commit()
#     session.refresh(new_event)
#     return {
#         "message": "이벤트가 성공적으로 등록되었습니다."
#     }

# @event_router.post("/new")
# async def create_event(body: Event = Body(...)) -> dict:
#     events.append(body)
#     return {
#         "message": "이벤트가 성공적으로 등록되었습니다."
#     }


@event_router.put("/edit/{id}", response_model=Event)
async def update_event(id: PydanticObjectId, body: EventUpdate) -> Event:
    event = await event_database.update(id, body)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="이벤트를 찾을 수 없습니다."
        )
    return event

# @event_router.put("/edit/{id}", response_model=Event)
# async def update_event(id: int, new_data: EventUpdate, session=Depends(get_session)) -> Event:
#     event = session.get(Event, id)
#     if event:
#         event_data = new_data.dict(exclude_unset=True)
#         for key, value in event_data.items():
#             setattr(event, key, value)
#         session.add(event)
#         session.commit()
#         session.refresh(event)

#         return event
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail="이벤트를 찾을 수 없습니다."
#     )

@event_router.delete("/{id}")
async def delete_event(id:PydanticObjectId) -> dict:
    event = await event_database.delete(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="이벤트를 찾을 수 없습니다." 
        )
    return {
        "message": "이벤트가 성공적으로 삭제되었습니다."
    }

# @event_router.delete("/{id}")
# async def delete_event(id:int, session=Depends(get_session)) -> dict:
#     event = session.get(Event, id)
#     if event:
#         session.delete(event)
#         session.commit()
#         return {
#             "message": "이벤트가 성공적으로 삭제되었습니다."
#         }
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail="이벤트를 찾을 수 없습니다." 
#     )

# @event_router.delete("/{id}")
# async def delete_event(id:int) -> dict:
#     for event in events:
#         if event.id == id:
#             events.remove(event)
#             return {
#                 "message": "이벤트가 성공적으로 삭제되었습니다."
#             }
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail="이벤트를 찾을 수 없습니다." 
#     )

@event_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {
        "message": "모든 이벤트가 성공적으로 삭제되었습니다."
    }

