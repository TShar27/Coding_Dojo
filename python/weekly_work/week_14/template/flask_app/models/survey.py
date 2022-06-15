from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = 'mydb'

class Survey:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comments = data['comments']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def required_fields(survey_data):
        is_valid = True
        if len(survey_data['name']) == 0:
            is_valid = False
            flash("Name must have an entry")
        elif len(survey_data['name']) < 3:
            is_valid = False
            flash("Name must be greater than 2 charachters")
        if len(survey_data['location']) == 0:
            is_valid = False
            flash("Location must have an entry")
        if len(survey_data['language']) == 0:
            is_valid = False
            flash("Language must have an entry")
        if len(survey_data['comments']) == 0:
            is_valid = False
            flash("Comments must have an entry")
        return is_valid


    
    @classmethod
    def save(cls,data):
        query = "INSERT into survey (name,location,language,comments) VALUES (%(name)s,%(location)s,%(language)s,%(comments)s)"
        return connectToMySQL(db).query_db(query,data)


    @classmethod
    def see_results(cls):
        query = "SELECT * FROM survey ORDER BY id DESC LIMIT 1"
        results = connectToMySQL(db).query_db(query)
        return Survey(results[0])


        