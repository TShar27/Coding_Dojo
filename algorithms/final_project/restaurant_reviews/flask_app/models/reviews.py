from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import pprint

db = 'foodie_real'

class Reviews:
    def __init__(self,data):
        self.users_id = data ['users_id']
        self.restaurants_id = data['restaurants_id']
        self.rating = data['rating']
        self.analysis = data['analysis']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        


    @classmethod
    def reviewed_restauarnts(cls,data):
        query = "SELECT * FROM restaurants rest LEFT JOIN users_has_restaurants rev ON rest.id = rev.restaurants_id WHERE rev.rating IS NOT NULL and users_id = %(id)s"
        results = connectToMySQL(db).query_db(query,data)
        print(results)
        pprint.pprint(results,sort_dicts=False)
        return results

    @classmethod
    def single_restaurant_reviews(cls,unicorn):
        query = "SELECT * FROM users_has_restaurants r JOIN users u ON r.users_id = u.id JOIN restaurants rs ON r.restaurants_id = rs.id WHERE restaurants_id = %(id)s"
        results = connectToMySQL(db).query_db(query,{'id':unicorn}) # the second parameter has to be a dictionary. The paramter within the query between the % s must match the key name in the query db function 
        print(results)
        return results
    
    @classmethod
    def create(cls,data):
        query = "INSERT INTO reviews (rating,analysis,users_id,restaurants_id,created_at,updated_at) VALUES (%(rating)s,%(analysis)s,%(users_id)s, %(restaurants_id)s,NOW(),NOW())"
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        return results
