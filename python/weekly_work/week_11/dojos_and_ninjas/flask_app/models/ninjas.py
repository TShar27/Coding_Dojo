from flask_app.config.mysqlconnection import connectToMySQL

db = 'bankAccount'

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def create_user(cls,data):
        print(f"this data is coming from the data in ninja.py line 33 {data}")
        query = "INSERT INTO ninjas (first_name,last_name,age) values (%(first_name)s, %(last_name)s,%(age)s)"
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        return results

    @classmethod
    def get_all_users(hicls):
        query = "SELECT * FROM ninjas"
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
        query = "SELECT * FROM ninjas where id = %(id)s"
        results = connectToMySQL(db).query_db(query,{'id':data})
        print(results)
        return hicls(results[0]) # only way to return an output on the front end
    
    @classmethod
    def update_user(hicls,data,id):
        query = f"Update ninjas SET first_name = %(first_name)s,last_name = %(last_name)s,age = %(age)s WHERE id = {id}"
        results = connectToMySQL(db).query_db(query,data)
        return results 
    
    @classmethod
    def deletion(hicls,id):
        query = "DELETE FROM ninjas WHERE id = %(id)s)"
        results = connectToMySQL(db).query_db(query,{'id':id})
        return results 