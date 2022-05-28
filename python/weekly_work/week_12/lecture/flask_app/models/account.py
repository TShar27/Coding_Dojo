from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


db = 'mydb'

class BankAccount:
    def __init__(self,data):
        self.id = data['id']
        self.type = data['type']
        self.amount = data['amount']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
    
    @staticmethod
    def validate_account(account_data):
        is_valid = True
        if int(account_data['amount']) < 100:
            flash("Amount deposited must be greater than $100") 
            is_valid = False
        return is_valid





    @classmethod
    def create_account(cls,data,id):
        query = f"INSERT INTO bankAccounts (type,amount,user_id) VALUES (%type)s,%(amount)s,{id})"
        results = connectToMySQL(db).query_db(query,data)
        return results
