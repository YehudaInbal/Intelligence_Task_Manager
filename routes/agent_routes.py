from fastapi import APIRouter


router = APIRouter()

@router.post("")
def create_agent(data: dict):
    pass



@router.get("")
def get_all_agents():
    pass



@router.get("/{id}")
def get_agent_by_id(id: int):
    pass


@router.put("/{id}")
def update_agent(id: int, data: dict):
    pass


@router.put("/{id}/deactivate")
def deactivate_agent(id: int):
    pass


@router.get("/{id}/performance")
def get_agent_performance(id: int):
    pass