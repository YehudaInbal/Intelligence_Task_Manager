from database.agent_db import AgentDB

allowed_ranks = {"Commander", "Senior", "Junior"}


def create_agent(data: dict):
    if not data.get("agent_rank"): #While in the table's schema (in the first part) the key appears as "agent_rank",
        data["agent_rank"] = data.get("rank")#in the system rules in the same part, the key appears as "rank".
    if data.get("agent_rank") not in allowed_ranks:
        raise ValueError("Invalid rank")
    return AgentDB.create_agent(data)


def get_all_agents():
    return AgentDB.get_all_agents()

def get_agent_by_id(id: int):
    """return soldier/ key Error if not exist"""
    agent = AgentDB.get_agent_by_id(id)
    if not agent:
        raise KeyError("Agent not found")
    else:
        return agent
    

def update_agent(id:int, data: dict):
    if data.get("agent_rank") not in allowed_ranks and data.get("agent_rank") != None:
        raise ValueError("Invalid rank")
    return AgentDB.update_agent(id, data)


def deactivate_agent(id: int):
    get_agent_by_id(id)
    return AgentDB.deactivate_agent(id)


def get_agent_performance(id):
    get_agent_by_id(id)
    return AgentDB.get_agent_performance(id)



def increment_completed(id):
    return AgentDB.increment_completed(id)

def increment_failed(id):
    return AgentDB.increment_failed(id)