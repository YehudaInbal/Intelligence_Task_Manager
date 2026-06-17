from db_connection import DB_connection


class AgentDB:


    def create_agent(data: dict):
        """Creates a new agent and returns the agent object"""
        conn = None
        try:
            conn = DB_connection.get_connection()
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO agents(name, specialty, agent_rank)
                           VALUES(%(name)s, %(specialty)s %(agent_rank)s)""", data)
            conn.commit()
            return cursor.fetchone()
        finally:
            if conn:
                cursor.close()
                conn.close()