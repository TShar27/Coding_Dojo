from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo
import pprint

db = 'mydb'

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo = []

    @classmethod
    def get_all_ninjas_with_dojo(hicls,id):
        query = f"SELECT * FROM ninjas n LEFT JOIN dojo d ON n.id = d.ninjas_id WHERE n.id = {id}"
        results = connectToMySQL(db).query_db(query)
        pprint.pprint(results,sort_dicts=False)
        ninja = hicls(results[0])
        for row in results:
            dojo = {
                "id": row['d.id'],
                "name": row['name'],
                "created_at": row['d.created_at'],
                "updated_at": row['d.updated_at'],
                "ninjas_id": row['ninjas_id']
            }
            ninja.dojo.append(Dojo(dojo))

# row = [{'id': 1,
#   'first_name': 'Timmy',
#   'last_name': 'Shar',
#   'age': 25,
#   'created_at': datetime.datetime(2022, 5, 24, 16, 21, 23),
#   'updated_at': datetime.datetime(2022, 5, 25, 17, 10, 3),
#   'd.id': 2,
#   'name': 'Los Angeles',
#   'd.created_at': datetime.datetime(2022, 5, 24, 16, 25, 25),
#   'd.updated_at': datetime.datetime(2022, 5, 24, 16, 25, 25),
#   'ninjas_id': 1}]




    @classmethod
    def create_ninja(cls,data):
        print(f"this data is coming from the data in ninja.py line 33 {data}")
        query = "INSERT INTO ninjas (first_name,last_name,age) values (%(first_name)s, %(last_name)s,%(age)s)"
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        return results

    @classmethod
    def get_all_ninjas(hicls):
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
    def show_one_ninja(hicls,data):
        query = "SELECT * FROM ninjas where id = %(id)s"
        results = connectToMySQL(db).query_db(query,{'id':data})
        print(results)
        return hicls(results[0]) # only way to return an output on the front end
    
    @classmethod
    def update_ninjas(hicls,data,id):
        query = f"Update ninjas SET first_name = %(first_name)s,last_name = %(last_name)s,age = %(age)s WHERE id = {id}"
        results = connectToMySQL(db).query_db(query,data)
        return results 
    
    @classmethod
    def deletion(hicls,id):
        query = "DELETE FROM ninjas WHERE id = %(id)s"
        results = connectToMySQL(db).query_db(query,{'id':id})
        return results 
    