import sqlite3
from sqlite3 import Connection, Cursor

class SingletonDatabase():
    '''
    Singleton class that establishes connection to database.
    Use get_connection to 

    '''
    
    _instance = None
    _cursor: Cursor = None
    _connection: Connection = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonDatabase, cls).__new__(cls)
            cls._connection = sqlite3.connect('jarp.db')
            cls._cursor = cls._connection.cursor()
            cls.create_tables()
        return cls._instance

    def create_tables(self) -> None:
        create_tables_file = "create.sql"
        with open(create_tables_file, 'r') as f:
            self.cur.execute(f.read())

    def get_connection(self) -> Connection:
        return self._connection
    
    def close_connection(self) -> None:
        if self._connection:
            self._connection.close()
            SingletonDatabase._instance = None
            SingletonDatabase._connection = None
            SingletonDatabase._cursor = None