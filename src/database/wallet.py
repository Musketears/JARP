from database import SingletonDatabase

class Wallet():
    
    def get(self, user_id: str) -> int:
        query = '''
        SELECT balance
        FROM wallet
        WHERE user_id = ?
        '''
        cursor = SingletonDatabase().get_cursor()
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        
        print(f"Query result for user_id '{user_id}': {result}")
        
        return result
    
    def add(self, user_id: str, amount: int) -> None:
        original_balance = self.get(user_id)
        if original_balance is None:
            query = '''
            INSERT INTO wallet VALUES (?, ?)
            '''
            original_balance = 100
        else:
            query = '''
            UPDATE wallet
            SET balance = ?
            WHERE user_id = ?
            '''
        SingletonDatabase().get_cursor().execute(query, (original_balance + amount, user_id))
        SingletonDatabase().get_connection().commit()