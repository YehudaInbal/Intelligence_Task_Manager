from database.agent_db import AgentDB
from database.mission_db import MissionDB



def create_agent(data):
    if data['agent_rank'] not in {'Junior', 'Senior', 'Commander'}:
        raise KeyError("rank must be one of those - 'Junior', 'Senior', 'Commander'")
    return AgentDB.create_agent(data)
    



