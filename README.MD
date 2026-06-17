# Intelligence Task Manager 
------------------------

This system manages missions using a mission table and a agents table in a database.
----
The system contains a table of agents, knows their name, rank, expertise, the number of missions completed and the number of missions failed, and whether they are active.

There is also a task table, which contains information by id:
Title, description, location, importance level,
Status, risk level and who the agent is associated with, if any.

-----

The system can create tasks and agents, assign tasks to agents, access them, change or update the tasks' status and the agents themselves, and access data and statistics.

------





## Folder structure

```
intelligence-task-manager/
├── database/
│   ├── db_connection.py
│   ├── agent_db.py
│   └── mission_db.py
├── README.md
├── requirements.txt
└── .gitignore
```





## Description of the tables

### agents


| field | type | Notes |
| :--   | :--  | :--   |
|id     |  INT, AUTO_INCREMENT, PK | Unique identifier |
|name   | VARCHAR(50) | Agent name |
|specialty | VARCHAR(50) | Field of specialization |
|is_active | BOOLEAN | default = TRUE |
|completed_missions | INT | default = 0 |
|failed_missions | INT | default = 0 |
|agent_rank | ENUM | ENUM(Junior / Senior / Commander) |

----

### missions
| field | type | Notes |
| :--   | :--  | :--   |
|id     |  INT, AUTO_INCREMENT, PK | Unique identifier |
|title  | VARCHAR(50) |  mission title |
|description | TEXT | detailed description |
|location | VARCHAR(50) | mission location |
|difficulty | INT | only 1 - 10 |
|importance | INT | only 1 - 10 |
|status | VARCHAR(25) | default = NEW |
|risk_level | VARCHAR(25) | Automatically calculated — not from the user input |
|assigned_agent_id | INT | default = NULL (Until assigned to a specific agent) |









## Explanation of classes and methods in the code

### DB_connection
--- Responsible for initializing the database and tables, and creating connection to the database---


|method | role |
|:--    | :--  |
get_connection() | Returns an active connection to MySQL |
create_database() | Creates Intelligence_db if it does not exist (activated at system startup) |
create_tables() | Creates both tables if they do not exist (activated at system startup)|


### AgentDB
---Responsible for all SQL operations on the agents table---

|method | role |
|:--    | :--  |
|create_agent(data) | Creates a new agent and returns the agent object|
|get_all_agents() | Returns a list of all agents|
|update_agent(id, data) | UPDATE for the entire row (cannot change id) |
|deactivate_agent(id) | Changes agent status to inactive |
|increment_completed(id) | Updates the number of tasks completed |
|increment_failed(id) | Updates the number of failed tasks |
| get_agent_performance(id) | Returns a dictionary with this keys completed, failed, total, success_rate |
|count_active_agents() | Returns the number of active agents |


### MissionDB
---Responsible for all SQL operations on the missions table---

|method | role |
|:--    | :--  |
|create_mission(data) | Creates a new task (returns the object)
|get_all_missions() | Returns a list of all missions|
|get_mission_by_id(id) | Returns task by ID (None if not found) |
|assign_mission(m_id, a_id) | Assigning a task to an agent |
|update_mission_status(id, status) | Used for any status change |
get_open_missions_by_agent(id)| Returns agent ASSIGNED/IN_PROGRESS tasks |
|count_all_missions() | Total tasks |
|count_by_status(status) | Counting by a specific status |
|count_open_missions() | Open task counter |
|count_critical_missions() | CRITICAL task counter |
|get_top_agent() | Returns the agent with the highest completed_missions |






## System rules

|id     | role |
|:--    | :--  |
|1      | rank must be Junior / Senior / Commander |
|2      | Difficulty and importance must be between 1 and 10 |
|3      |risk_level is calculated automatically when a task |is created |
|4      | An agent with is_active=False cannot accept tasks |
|5      | An agent cannot have more than 3 open tasks (ASSIGNED / IN_PROGRESS) at the same time |
|6      | If risk_level=CRITICAL — only an agent with the rank of Commander can accept the task |
| 7     | Only a task with a status of NEW can be assigned. After assignment: status=ASSIGNED |
|8      | Only a task with the status ASSIGNED can be started. After: status=IN_PROGRESS |
|9      | Only a task will be allowed to finish. IN_PROGRESS and change the status to failed or completed |
|10     | Only a task with a status of NEW or ASSIGNED can be canceled |







## Running instructions

 1.  Open terminal and run this command:
```
docker run -d --name intelligence-mysql -e MYSQL_ROOT_PASSWORD=1234
-e MYSQL_DATABASE=Intelligence_db -p 3306:3306 mysql:8.0
```

2. Open the terminal on the project folder and run this command:
```
python -m venv venv
```

3. now run this on the same location:
```
venv\Scripts\activate
```

4. now you can install the requirements:
```
pip install -r requirements.txt
```

5. 5. the project is ready, now run it with
```
python main.py
```

