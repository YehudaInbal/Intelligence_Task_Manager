from fastapi import APIRouter


router = APIRouter()


@router.post("")
def create_mission(data: dict):
    pass

@router.get("")
def get_all_missions():
    pass

@router.get("/{id}")
def get_mission_by_id(id: int):
    pass

@router.put("/{id}/assign/{agent_id}")
def assign_mission(id: int, agent_id: int):
    pass

@router.put("/{id}/start")
def start_mission(id: int):
    pass


@router.put("/{id}/complete")
def complete_mission(id: int):
    pass

@router.put("/{id}/fail")
def faile_mission(id: int):
    pass

@router.put("/{id}/cancel")
def cancel_mission(id: int):
    pass
