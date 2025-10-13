from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from app.dtos.create_meeting_response import CreateMeetingResponse
from app.dtos.get_meeting_response import GetMeetingResponse
from app.services.meeting_service import service_create_meeting
from app.tortoise_models import meeting

mysql_router = APIRouter(prefix="/v1/meetings", tags=["meeting"])


@mysql_router.post("/v1/meetings", description="meeting을 생성합니다.")
async def api_create_meeting() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code=(await service_create_meeting()).url_code)


@mysql_router.get("/{meeting_url_code}", description="meeting을 조회합니다.")
async def api_get_meeting_mysql(meeting_url_code: str, service_get_meetting_mysql=None) -> GetMeetingResponse:
    meeting_model = await service_get_meetting_mysql(meeting_url_code)
    if meeting is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f"meeting with url_code: {meeting_url_code} not found")
    return GetMeetingResponse(url_code=meeting_url_code)
