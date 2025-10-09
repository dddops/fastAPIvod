from fastapi import APIRouter

from app.dtos.create_meeting_response import CreateMeetingResponse

mysql_router = APIRouter(prefix="/v1/meetings", tags=["meeting"])


@mysql_router.post("/create-meeting", description="meeting을 생성합니다.")
async def api_create_meeting() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")
