from flask_app.config.mysqlconnection import connectToMySQL

db = 'mydb'

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.type = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['ninjas_id']

    @classmethod
    def create_dojo(cls,data,id):
        query = f"INSERT INTO dojo (name,ninjas_id) VALUES (%name)s,%(ninjas_id)s,{id})"
        results = connectToMySQL(db).query_db(query,data)
        return results
