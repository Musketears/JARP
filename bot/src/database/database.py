import sqlite3, os
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
            database_file = 'jarp.db'
            database_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), database_file)
            cls._connection = sqlite3.connect(database_path)
            cls._cursor = cls._connection.cursor()
            cls._instance.create_tables()
        return cls._instance

    def create_tables(self) -> None:
        '''
        Create the sql tables if they dont exist
        
        '''
        create_tables_file = "create.sql"
        create_tables_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), create_tables_file)
        with open(create_tables_path, 'r') as f:
            self._instance._cursor.execute(f.read())

    def get_cursor(self) -> Cursor:
        '''
        Return the current cursor for querying the database
        
        '''
        return self._instance._cursor
    
    def get_connection(self) -> Connection:
        '''
        Return the current connection for querying the database
        
        '''
        return self._instance._connection
    
    def close_connection(self) -> None:
        '''
        Close the database connection
        
        '''
        if self._instance._connection:
            self._instance._connection.close()
            SingletonDatabase._instance = None
            SingletonDatabase._connection = None
            SingletonDatabase._cursor = None
            
    def fetch(self, query: str, values: any = (), many: bool = False) -> any:
        '''
        Fetch results from the database. Can return many or one result. Used for selects
        
        '''
        self._instance._cursor.execute(query, values)
        result = self._instance._cursor.fetchmany()
        
        if many:
            return result
        if len(result) > 0:
            return result[0]
        return None
    
    def commit(self, query: str, values: any = ()) -> None:
        '''
        Commit something to the database. Used for inserts and updates
        
        '''
        self._instance._cursor.execute(query, values)
        self._instance._connection.commit()