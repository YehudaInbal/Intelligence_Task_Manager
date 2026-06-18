from fastapi import APIRouter


router = APIRouter()

@router.get("/summary")
def report_summary():
    pass

@router.get("/missions-by-status")
def get_mission_by_status():
    pass

@router.get("/top-agent")
def get_top_agent():
    pass