from fastapi import APIRouter, HTTPException

from service import agent_service

router = APIRouter()

@router.post("", status_code=201)
def create_agent(data: dict):
    try:
        return agent_service.create_agent(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"{e}")



@router.get("")
def get_all_agents():
    return agent_service.get_all_agents()



@router.get("/{id}")
def get_agent_by_id(id: int):
    try:
        return agent_service.get_agent_by_id(id)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=f"{e}")


@router.put("/{id}")
def update_agent(id: int, data: dict):
    try:
        return agent_service.update_agent(id, data)
    except KeyError as e:
        raise HTTPException(status_code=422, detail=f"{e}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"{e}")


@router.put("/{id}/deactivate")
def deactivate_agent(id: int):
    try:
        return agent_service.deactivate_agent(id)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=f"{e}")



@router.get("/{id}/performance")
def get_agent_performance(id: int):
    try:
        return agent_service.get_agent_performance(id)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=f"{e}")