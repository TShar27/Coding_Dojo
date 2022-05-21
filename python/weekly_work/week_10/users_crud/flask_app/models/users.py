from flask_app.config.mysqlconnection import connectToMySQL

db = 'bankAccount'

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def create_user(cls,data):
        print(f"this data is coming from the data in user.py line 33 {data}")
        query = "INSERT INTO users (first_name,last_name,email) values (%(first_name)s, %(last_name)s,%(email)s)"
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        return results

    @classmethod
    def get_all_users(hicls):
        query = "SELECT * FROM users"
        results = connectToMySQL(db).query_db(query)
        print(results) # Dict
        users = []
        for user in results:
            print(user) # each individual user line by line
            users.append(hicls(user))
        print(users) # array
        return users
    
    @classmethod
    def show_one_user(hicls,data):
        query = "SELECT * FROM users where id = %(id)s"
        results = connectToMySQL(db).query_db(query,{'id':data})
        print(results)
        return hicls(results[0]) # only way to return an output on the front end
    
    @classmethod
    def update_user(hicls,data,id):
        query = f"Update users SET first_name = %(first_name)s,last_name = %(last_name)s,email = %(email)s WHERE id = {id}"
        results = connectToMySQL(db).query_db(query,data)
        return results 
    
    @classmethod
    def deletion(hicls,id):
        query = "DELETE FROM users WHERE id = %(id)s)"
        results = connectToMySQL(db).query_db(query,{'id':id})
        return results 