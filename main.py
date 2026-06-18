import uvicorn
from fastapi import FastAPI

from database.db_connection import DB_connection

from routes.agent_routes import router as agent_routes
from routes.mission_routes import router as mission_routs
from routes.report_routes import router as report_router


app = FastAPI()
app.include_router(router=agent_routes, prefix="/agents", tags=["agents"])
app.include_router(router=mission_routs, prefix="/missions", tags=["missions"])
app.include_router(router=report_router, prefix="/reports", tags=["reports"])




if __name__ == "__main__":
    DB_connection.create_database()
    DB_connection.create_tables()
    uvicorn.run("main:app", reload=True)








# from database.agent_db import AgentDB
# from database.mission_db import MissionDB

# print(MissionDB.get_top_agent())


# def create_agent(data):
#     if data['agent_rank'] not in {'Junior', 'Senior', 'Commander'}:
#         raise KeyError("rank must be one of those - 'Junior', 'Senior', 'Commander'")
#     return AgentDB.create_agent(data)
    




# print(MissionDB.count_critical_missions())
# print(MissionDB.count_open_missions())
# print(MissionDB.count_by_status('ASSIGNED'))
# print(MissionDB.count_all_missions())
# print(MissionDB.get_open_missions_by_agent(2))
# print(MissionDB.update_mission_status(6, 'CRITICAL'))
# print(MissionDB.assign_mission(7, 3))
# print(MissionDB.get_all_missions())
# data = {'title': 'dto do', 'description':"dooooo", 'location':"evr", 'difficulty': 9, 'importance': 9}
# print(MissionDB.create_mission(data))
# print(AgentDB.count_active_agents())
# print(AgentDB.get_agent_performance(3))
# print(AgentDB.increment_failed(3))
# print(AgentDB.deactivate_agent(1))
# print(AgentDB.get_all_agents())
# data = {'name': 'rexi', 'specialty': 'Bark', 'agent_rank': 'Commander'}
# data = {'name': 'rexi', 'specialty': 'Bark', 'agent_rank': 'Senior'}
# data = {'name': 'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh', 'specialty': 'Bark', 'agent_rank': 'Junior'}
# print(create_agent(data))
# print(AgentDB.update_agent(4, data))