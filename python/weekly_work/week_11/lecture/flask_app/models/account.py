from flask_app.config.mysqlconnection import connectToMySQL

db = 'bankAccount'

class BankAccount:
    def __init__(self,data):
        self.id = data['id']
        self.type = data['type']
        self.amount = data['amount']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def create_account(cls,data,id):
        query = f"INSERT INTO bankAccounts (type,amount,user_id) VALUES (%type)s,%(amount)s,{id})"
        results = connectToMySQL(db).query_db(query,data)
        return results
