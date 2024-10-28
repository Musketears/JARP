from .database import SingletonDatabase

class Wallet():
    
    def get(self, user_id: str) -> int:
        query = '''
        SELECT balance
        FROM wallet
        WHERE user_id = ?
        '''
        amount = SingletonDatabase().fetch(query, (user_id,))
        
        if amount:
            return amount[0]
        else:
            query = '''
            INSERT INTO wallet VALUES (?, ?)
            '''
            SingletonDatabase().commit(query, (user_id, 100))
            return 100
            
    
    def add(self, user_id: str, amount: int) -> int:
        original_balance = self.get(user_id)
        query = '''
        UPDATE wallet
        SET balance = ?
        WHERE user_id = ?
        '''
        SingletonDatabase().commit(query, (original_balance + amount, user_id))
        
        return original_balance + amount