from fastapi import APIRouter
from database.agent_db import AgentDB
from database.mission_db import MissionDB

router = APIRouter()

@router.get("/summary")
def report_summary():
    return {
        "active_agents_count": AgentDB.count_active_agents(),
        "total_missions": MissionDB.count_all_missions(),
        "open_missions": MissionDB.count_open_missions(),
        "completed_missions": MissionDB.count_by_status("COMPLETED"),
        "failed_missions": MissionDB.count_by_status("FAILED"),
        "critical_missions": MissionDB.count_critical_missions()
    }

@router.get("/missions-by-status")
def get_mission_by_status():
    return {
        "new": MissionDB.count_by_status("NEW"),
        "assigned": MissionDB.count_by_status("ASSIGNED"),
        "in_progress": MissionDB.count_by_status("IN_PROGRESS"),
        "completed": MissionDB.count_by_status("COMPLETED"),
        "failed": MissionDB.count_by_status("FAILED"),
        "cancelled": MissionDB.count_by_status("CANCELLED")
    }

@router.get("/top-agent")
def get_top_agent():
    return MissionDB.get_top_agent()