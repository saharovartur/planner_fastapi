from fastapi import APIRouter, Body, HTTPException, status
from models.events import Event
from typing import List

event_router = APIRouter(tags=["Events"])

events = []


@event_router.get("events/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    return events


@event_router.get("event/{id}", response_model=Event)
async def retrieve_event(id: int) -> Event:
    try:
        for event in events:
            if event.id == id:
                return event
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Такой задачи нет в списке')


@event_router.post('new/')
async def create_event(body: Event = Body(...)) -> dict:
    events.append(body)
    return {
        'message': 'Задача создана'
    }


@event_router.delete('delete/{id}')
async def delete_event(id: int) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return {'message': 'Задача удалена'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Такая задачи не найдена')


@event_router.delete('delete/')
async def delete_all_events() -> dict:
    if len(events) == 0:
        return {
            'message': 'Список дел  пуст'
        }
    else:
        (
            events.clear())
    return {
        'message': 'Весь список дел был удален'
    }
