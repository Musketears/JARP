import sqlite3
from sqlite3 import Connection, Cursor

class SingletonDatabase():
    '''
    Singleton class that establishes connection to database.
    Use get_cursor to get database cursor

    '''
    
    _instance = None
    _cursor: Cursor = None
    _connection: Connection = None
    
    def __new__(cls):
        '''
        Instantiate the singleton if it hasnt been accessed yet, otherwise return the singleton
        
        '''
        if cls._instance is None:
            cls._instance = super(SingletonDatabase, cls).__new__(cls)
            cls._connection = sqlite3.connect('jarp.db')
            cls._cursor = cls._connection.cursor()
            cls.create_tables(cls)
        return cls._instance

    def create_tables(self) -> None:
        '''
        Create the sql tables if they dont exist
        
        '''
        create_tables_file = "create.sql"
        with open(create_tables_file, 'r') as f:
            self._cursor.execute(f.read())

    def get_cursor(self) -> Cursor:
        '''
        Return the current cursor for querying the database
        
        '''
        return self._cursor
    
    def get_connection(self) -> Connection:
        '''
        Return the current connection for querying the database
        
        '''
        return self._connection
    
    def close_connection(self) -> None:
        '''
        Close the database connection
        
        '''
        if self._connection:
            self._connection.close()
            SingletonDatabase._instance = None
            SingletonDatabase._connection = None
            SingletonDatabase._cursor = None