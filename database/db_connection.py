import mysql.connector

CREATE_AGENTS = """
CREATE TABLE IF NOT EXISTS agents (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    specialty VARCHAR(50),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    completed_missions INT DEFAULT 0,
    failed_missions INT DEFAULT 0,
    agent_rank ENUM('Junior', 'Senior',  'Commander')
)"""


CREATE_MISSIONS = """
CREATE TABLE IF NOT EXISTS missions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    description TEXT,
    location VARCHAR(50),
    difficulty INT,
    importance INT,
    status VARCHAR(50),
    risk_level VARCHAR(50),
    assigned_agent_id INT DEFAULT NULL
    )"""

class DB_connection:

    @staticmethod
    def get_connection():
        """Returns an active connection to MySQL"""
        conn = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="1234",
            database="Intelligence_db"
        )
        return conn
    
    @staticmethod
    def create_database():
        conn = None
        try:
            conn = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="1234",
            )
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS Intelligence_db")
            conn.commit()
        finally:
            if conn:
                cursor.close()
                conn.close()
    
    
    @staticmethod
    def create_tables():
        """Creates both tables if they do not exist"""
        conn = None
        try:
            conn = DB_connection.get_connection()
            cursor = conn.cursor()
            cursor.execute(CREATE_MISSIONS)
            cursor.execute(CREATE_AGENTS)
            
            conn.commit()
        finally:
            if conn:
                cursor.close()
                conn.close()

if __name__ == '__main__':
    DB_connection.create_database()
    DB_connection.create_tables()
