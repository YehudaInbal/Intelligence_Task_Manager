from fastapi import APIRouter, HTTPException

from service import mission_service

router = APIRouter()


@router.post("", status_code=201)
def create_mission(data: dict):
    try:
        return mission_service.create_mission(data) 
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"{e}")

@router.get("")
def get_all_missions():
    return mission_service.get_all_missions()

@router.get("/{id}")
def get_mission_by_id(id: int):
    try:
        return mission_service.get_mission_by_id(id)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=f"{e}")

@router.put("/{id}/assign/{agent_id}")
def assign_mission(id: int, agent_id: int):
    try:
        return mission_service.assign_mission(id, agent_id)
    except KeyError as e:
        raise HTTPException(status_code= 404, detail=f"{e}")
    except ValueError as e:
        raise HTTPException(status_code= 400, detail=f"{e}")

@router.put("/{id}/start")
def start_mission(id: int):
    try:
        return mission_service.start_mission(id)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=f"{e}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"{e}") 

@router.put("/{id}/complete")
def complete_mission(id: int):
    pass

@router.put("/{id}/fail")
def faile_mission(id: int):
    pass

@router.put("/{id}/cancel")
def cancel_mission(id: int):
    pass
