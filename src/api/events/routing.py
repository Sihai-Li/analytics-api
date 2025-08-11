import os
from fastapi import APIRouter
from .models import (
    EventModel, 
    EventListSchema, 
    EventCreateSchema,
    EventUpdateSchema
)


router = APIRouter()
from api.db.config import DATABASE_URL

# GET DATA HERE
# List View
# GET /api/events/
@router.get("/")
def read_events() -> EventListSchema:
    # a bunch of items in a table
    print(os.environ.get("DATABASE_URL"), DATABASE_URL)
    return {
        "results":[
            {"id": 1},{"id": 2}, {"id": 3}
            ],
            "count": 3
    }

# SEND DATA HERE
# create view
# POST /api/events/
@router.post("/")
def create_events(payload:EventCreateSchema) -> EventModel:
    # a bunch of items in a table
    print(payload.page)
    data = payload.model_dump() # payload -> dict -> pydantic
    return {"id": 123, **data}

# GET /api/events/12
@router.get("/{event_id}")
def get_event(event_id: int) -> EventModel:
    # a single row
    return {
        "id": event_id
    }

# UPDATE THIS DATA
# PUT /api/events/12
@router.put("/{event_id}")
def update_event(event_id: int, payload: EventUpdateSchema) -> EventModel:
    # a single row
    data = payload.model_dump()
    return {"id": event_id, **data}