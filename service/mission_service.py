from database.mission_db import MissionDB
from service import agent_service

def create_mission(data: dict):
    print(data.get("difficulty"), data.get("importance"))

    if  data.get("difficulty") > 10  or data.get("difficulty") < 1 or data.get("importance") > 10 or data.get("importance") < 1:
        raise KeyError("Difficulty and importance must be between one and ten.")
    risk_level = data["difficulty"] * 2 + data["importance"]
    if 0 <= risk_level <= 9:
        risk_level = 'LOW'
    elif risk_level <= 17:
        risk_level = 'MEDIUM'
    elif risk_level <= 24:
        risk_level = 'HIGH'
    elif risk_level > 24:
        risk_level = 'CRITICAL'
    data["risk_level"] = risk_level
    return MissionDB.create_mission(data)

def get_all_missions():
    return MissionDB.get_all_missions()

def get_mission_by_id(id):
    mission = MissionDB.get_mission_by_id(id)
    if not mission:
        raise KeyError("Mission not found")
    return MissionDB.get_mission_by_id(id)

def assign_mission(mission_id: int, agent_id: int):
    mission = get_mission_by_id(mission_id)
    agent = agent_service.get_agent_by_id(agent_id)
    if mission.get("status") != 'NEW':
        raise ValueError("Mission not available")
    if not agent.get("is_active"):
        raise ValueError("Agent is not active")
    if len(MissionDB.get_open_missions_by_agent(agent_id)) >= 3:
        raise ValueError("Agent has reached maximum missions")
    if mission.get("risk_level") == "CRITICAL" and agent.get("agent_rank") != "Commander":
        raise ValueError("Only Commander can handle critical missions")
    return MissionDB.assign_mission(mission_id, agent_id)

