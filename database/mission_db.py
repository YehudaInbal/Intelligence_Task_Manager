from database.db_connection import DB_connection
from database.agent_db import AgentDB

class MissionDB:


    @staticmethod
    def create_mission(data: dict) -> dict:
        """Creates a new task (returns the object)"""
        conn = None
        try:
            conn = DB_connection.get_connection()
            cursor = conn.cursor()
            cursor.execute(f"""INSERT INTO missions(title, description, location, difficulty, importance, risk_level) 
                           VALUES(%(title)s, %(description)s, %(location)s, %(difficulty)s, %(importance)s, %(risk_level)s)""", data)
            mission_id = cursor.lastrowid
            conn.commit()
            return MissionDB.get_mission_by_id(mission_id)
        finally:
            if conn:
                cursor.close()
                conn.close()


    @staticmethod
    def get_all_missions() -> list[dict] | list:
        """Returns a list of all missions"""
        conn = None
        try:
            conn = DB_connection.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM missions")
            return cursor.fetchall()
        finally:
            if conn:
                cursor.close()
                conn.close()


    @staticmethod
    def get_mission_by_id(id):
        """"Returns mission by ID (None if not found)"""
        conn = None
        try:
            conn = DB_connection.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""SELECT * FROM missions WHERE id = %s""", (id,))
            return cursor.fetchone()
        finally:
            if conn:
                cursor.close()
                conn.close()


    @staticmethod
    def assign_mission(m_id, a_id) -> bool:
        "Assigning a mission to an agent"
        conn = None
        try:
            conn = DB_connection.get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE missions SET assigned_agent_id = %s WHERE id = %s", (a_id, m_id))
            cursor.execute("UPDATE missions SET status = 'ASSIGNED' WHERE id = %s", (m_id,))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            if conn:
                cursor.close()
                conn.close()
        
    @staticmethod
    def update_mission_status(id: int, status: str) -> bool:
        """Used for any status change"""
        conn = None
        try:
            conn = DB_connection.get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE missions SET status = %s WHERE id = %s", (status, id))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            if conn:
                cursor.close()
                conn.close()
        
        
    @staticmethod
    def get_open_missions_by_agent(id) -> list | list[dict]:
        """Returns agent ASSIGNED/IN_PROGRESS tasks"""
        missions = MissionDB.get_all_missions()
        open_missions = []
        for m in missions:
            if (m["assigned_agent_id"] == id) and (m["status"] == 'ASSIGNED' or m["status"] == 'IN_PROGRESS'):
                open_missions.append(m)
        return open_missions


    @staticmethod
    def count_all_missions():
        """Total tasks"""
        return len(MissionDB.get_all_missions())

    
    @staticmethod
    def count_by_status(status) -> int:
        """Counting by a specific status"""
        conn = None
        try:
            conn = DB_connection.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM missions WHERE status = %s", (status,))
            return cursor.fetchone()[0]
        finally:
            if conn:
                cursor.close()
                conn.close()


    @staticmethod
    def count_open_missions():
        """Open task counter"""
        missions = MissionDB.get_all_missions()
        open_missions = 0
        open_status ={'IN_PROGRESS', 'NEW', 'ASSIGNED'}
        for m in missions:
            if m['status'] in open_status:
                open_missions += 1
        return open_missions
    
    @staticmethod
    def count_critical_missions():
        """"CRITICAL task counter"""
        conn = None
        try:
            conn = DB_connection.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM missions WHERE risk_level = 'CRITICAL'")
            return cursor.fetchone()[0]
        finally:
            if conn:
                cursor.close()
                conn.close()



    @staticmethod
    def get_top_agent():
        """Returns the agent with the highest completed_missions"""
        conn = None
        try:
            conn = DB_connection.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
            SELECT
                assigned_agent_id,
                COUNT(*) AS completed_count
            FROM missions
            WHERE status = 'COMPLETED'
            GROUP BY assigned_agent_id
            ORDER BY completed_count DESC
            LIMIT 1
            """)
            return cursor.fetchone()
        finally:
            if conn:
                conn.close()



