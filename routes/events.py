from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlmodel import select

from database.connection import get_session
from models.events import Event, EventUpdate
from typing import List

event_router = APIRouter(tags=["Events"])




@event_router.get("events/", response_model=List[Event])
async def retrieve_all_events(session=Depends(get_session)) -> List[Event]:
    statement = select(Event)
    events = session.exec(statement).all()
    return events


@event_router.get("event/{id}", response_model=Event)
async def retrieve_event(id: int, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)

    if event is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Такой задачи нет в списке')

    return event


@event_router.put("/edit/{id}", response_model=Event)
async def update_event(id: int, new_data: EventUpdate, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)

    if event:
        event_data = new_data.dict(exclude_unset=True)
        for key, value in event_data.items():
            setattr(event, key, value)
        session.add(event)
        session.commit()
        session.refresh(event)
        return event

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Событие не найдено")


@event_router.post('new/')
async def create_event(new_event: Event, session=Depends(get_session)) -> dict:
    existing_event = session.query(Event).filter(Event.title == new_event.title).first()

    if existing_event:
        return {
            'message': 'Такая задача уже есть'}
    else:
        session.add(new_event)
        session.commit()
        session.refresh(new_event)

        return {
            'message': 'Задача создана'
        }


@event_router.delete('delete/{id}')
async def delete_event(id: int, session=Depends(get_session)) -> dict:
    event = session.get(Event, id)
    if event:
        session.delete(event)
        session.commit()
        return {'message': 'Задача удалена'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Такая задачи не найдена')


@event_router.delete('delete/')
async def delete_all_events(session=Depends(get_session)) -> dict:
    session.query(Event).delete()
    session.commit()
    return {
        'message': 'Весь список дел был удален'
    }
