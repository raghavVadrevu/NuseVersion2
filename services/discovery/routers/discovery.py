from fastapi import APIRouter


router = APIRouter()


@router.post("/discover")
def discover() -> dict:
    return {
        "total_feeds_checked": 0,
        "total_entries_seen": 0,
        "total_events_published": 0,
        "category_filter": None,
    }
