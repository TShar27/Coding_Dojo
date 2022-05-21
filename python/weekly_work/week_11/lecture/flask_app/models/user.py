from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.account import BankAccount
import pprint

db = 'mydb'

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.account = []
    
    @classmethod
    def get_all_users_with_accounts(cls,id):
        query = f"SELECT * FROM users u LEFT JOIN bankAccounts ba ON u.id = ba.user_id WHERE u.id = {id}"
        results = connectToMySQL(db).query_db(query)
        pprint.pprint(results,sort_dicts=False)
        user = cls(results[0])
        for row in results:
            account = {
                "id": row['ba.id'],
                "type": row['type'],
                "amount": row['amount'],
                "created_at": row['ba.created_at'],
                "updated_at": row['ba.updated_at'],
                "user_id": row['user_id']
            }
            user.account.append(BankAccount(account))
        return user

# row = [{'id': 1,
#   'first_name': 'timmy',
#   'last_name': 'shar',
#   'email': 'timshar27@gmail.com',
#   'password': '12345678',
#   'created_at': datetime.datetime(2022, 5, 18, 22, 17, 38),
#   'updated_at': datetime.datetime(2022, 5, 18, 22, 17, 38),
#   'ba.id': 1,
#   'type': 'savings',
#   'amount': 500.0,
#   'ba.created_at': datetime.datetime(2022, 5, 18, 22, 17, 41),
#   'ba.updated_at': datetime.datetime(2022, 5, 18, 22, 17, 41),
#   'user_id': 1},

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL(db).query_db(query)
        print(results) # Dict
        users = []
        for user in results:
            print(user) # each individual user line by line
            users.append(cls(user))
        print(users) # array
        return users

    @classmethod
    def get_one_user(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(db).query_db(query, {'id': data})
        # print(results)
        return cls(results[0])

    @classmethod
    def create_user(cls,data):
        print(f"this data is coming from the data in user.py line 33 {data}")
        query = "INSERT INTO users (first_name,last_name,email) values (%(first_name)s, %(last_name)s,%(email)s)"
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        return results
    
    @classmethod
    def update_user(cls,data,id,):
        query = f"Update users SET first_name = %(first_name)s,last_name = %(last_name)s,email = %(email)s WHERE id = {id}"
        results = connectToMySQL(db).query_db(query,data)
        return results

    @classmethod
    def delete_user(cls,id):
        query = f"DELETE FROM users WHERE id = {id}"
        results = connectToMySQL(db).query_db(query)
        return results
