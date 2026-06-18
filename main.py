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