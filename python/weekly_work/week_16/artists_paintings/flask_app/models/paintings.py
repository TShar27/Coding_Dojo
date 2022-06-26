from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import pprint

db = 'artists_paintings'


class Paintings:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.price = data['price']
        self.artists_id = data['artists_id']


    @staticmethod
    def validate_painting(painting):
        is_valid = True
        if len(painting['title']) ==0:
            is_valid = False
            flash("Title must have an entry")
        elif len(painting['title']) < 3:
            is_valid = False
            flash("Title must be greater than 2 charachters")
        if len(painting['description']) ==0:
            is_valid = False
            flash("Description must have an entry")
        elif len(painting['description']) < 10:
            is_valid = False
            flash("Description must be greater than 10 charachters")
        if len(painting['price']) ==0:
            is_valid = False
            flash("Price must have an entry")
        elif int(painting['price']) < 1:
            is_valid = False
            flash("Price must be greater than $0")
        return is_valid



    @classmethod
    def artists_paintings(cls,data):
        query = "SELECT p.id, p.title,p.description,p.price,a.first_name,a.last_name FROM paintings p LEFT JOIN artists a ON p.artists_id = a.id"
        results = connectToMySQL(db).query_db(query,data)
        print(results)
        pprint.pprint(results,sort_dicts=False)
        return results
    

    @classmethod
    def show_one(cls,data):
        query = "SELECT * FROM paintings WHERE id = %(id)s"
        results = connectToMySQL(db).query_db(query,{'id':data})
        print(results)
        return cls(results[0])
    
    @classmethod
    def update(cls,data,id):
        query = f"UPDATE paintings SET title = %(title)s,description = %(description)s,price = %(price)s WHERE id = {id}"
        results = connectToMySQL(db).query_db(query,data)
        print(results)
        return results 

    @classmethod
    def create(cls,data):
        query = "INSERT INTO paintings (title,description,price,artists_id) VALUES (%(title)s,%(description)s,%(price)s, %(artists_id)s)"
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        return results

    @classmethod
    def deletion(cls,data):
        query = "DELETE FROM paintings WHERE id = %(id)s"
        results = connectToMySQL(db).query_db(query,data)
        return results 


