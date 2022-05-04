from mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all_users(hicls):
        query = "SELECT * FROM users"
        results = connectToMySQL('bankAccount').query_db(query)
        print(results) # Dict
        users = []
        for user in results:
            print(user) # each individual user line by line
            users.append(hicls(user))
        print(users) # array
        return users

    def get_one_user(cls):
        pass
    def create_user(cls,data):
        pass
        