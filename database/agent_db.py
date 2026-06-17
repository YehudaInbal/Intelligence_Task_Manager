from db_connection import DB_connection


class AgentDB:


    def create_agent(data: dict) -> dict:
        """Creates a new agent and returns the agent object"""
        conn = None
        try:
            conn = DB_connection.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""INSERT INTO agents(name, specialty, agent_rank)
                           VALUES(%(name)s, %(specialty)s, %(agent_rank)s)""", data)
            conn.commit()
            agent_id = cursor.lastrowid
            return AgentDB.get_agent_by_id(agent_id)
        finally:
            if conn:
                cursor.close()
                conn.close()
        
    @staticmethod
    def get_agent_by_id(id) -> dict | None:
        """Returns one agent bu id"""
        conn = None
        try:
            conn = DB_connection.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""SELECT * FROM agents WHERE id = %s""", (id,))
            return cursor.fetchone()
        finally:
            if conn:
                cursor.close()
                conn.close()

    @staticmethod
    def get_all_agents() -> list | list[dict]:
        """Returns a list of all agents"""
        conn = None
        try:
            conn = DB_connection.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM agents")
            return cursor.fetchall()
        finally:
            if conn:
                cursor.close()
                conn.close()


    @staticmethod
    def update_agent(id: int, data: dict) -> bool:
        """UPDATE for the entire row (cannot change id)"""
        conn = None
        try:
            conn = DB_connection.get_connection()
            cursor = conn.cursor()
            for k, v in data.items():
                cursor.execute(f"UPDATE agents SET {k} = %s WHERE id = %s", (v, id))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            if conn:
                cursor.close()
                conn.close()

    @staticmethod
    def deactivate_agent(id) -> bool:
        """Changes agent status to inactive"""
        conn = None
        try:
            conn = DB_connection.get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE agents SET is_active = FALSE WHERE id = %s", (id,))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            if conn:
                cursor.close()
                conn.close()

    @staticmethod
    def increment_completed(id):
        """Updates the number of missions completed (Add 1 more)"""
        conn = None
        updated_missions_count = AgentDB.get_agent_by_id(id)["completed_missions"] + 1
        try:
            conn = DB_connection.get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE agents SET completed_missions = %s WHERE id = %s", (updated_missions_count, id))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            if conn:
                cursor.close()
                conn.close()


    @staticmethod
    def increment_failed(id) -> bool:
        """Updates the number of failed tasks"""
        conn = None
        updated_failed_missions = AgentDB.get_agent_by_id(id)["failed_missions"] + 1
        try:
            conn = DB_connection.get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE agents SET failed_missions = %s WHERE id = %s", (updated_failed_missions, id))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            if conn:
                cursor.close()
                conn.close()

    @staticmethod
    def get_agent_performance(id) -> dict:
        """Returns a dictionary with this keys completed, failed, total, success_rate"""
        agent = AgentDB.get_agent_by_id(id)
        completed = agent["completed_missions"]
        failed = agent["failed_missions"]
        total = completed + failed
        success_rate = (completed / total) * 100
        return {
            'completed': completed,
            'failed': failed,
            'total': total,
            'success_rate': success_rate
        }
    

    @staticmethod
    def count_active_agents() -> int:
        """Returns the number of active agents"""
        agents = AgentDB.get_all_agents()
        sum_active = 0
        for agent in agents:
            if agent["is_active"] == True:
                sum_active += 1
        return sum_active




# print(AgentDB.count_active_agents())

# print(AgentDB.get_agent_performance(3))


# print(AgentDB.increment_failed(3))
# print(AgentDB.deactivate_agent(1))
# print(AgentDB.get_all_agents())
# data = {'name': 'rexi', 'specialty': 'Bark', 'agent_rank': 'Commander'}
# data = {'name': 'rexi', 'specialty': 'Bark', 'agent_rank': 'Senior'}
# data = {'name': 'rexi', 'specialty': 'Bark', 'agent_rank': 'Junior'}
# print(AgentDB.create_agent(data))
# print(AgentDB.update_agent(4, data))