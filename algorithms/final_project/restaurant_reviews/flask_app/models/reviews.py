from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import pprint

db = 'foodie_test'

class Reviews:
    def __init__(self,data):
        self.id = data['id']
        self.rating = data['rating']
        self.analysis = data['analysis']
        self.users_id = data ['users_id']
        self.restaurants_id = data['restaurants_id']


    @classmethod
    def reviewed_restauarnts(cls,data):
        query = "SELECT rest.name,rev.rating,rev.analysis FROM restaurants rest LEFT JOIN reviews rev ON rest.id = rev.restaurants_id WHERE rev.rating IS NOT NULL"
        results = connectToMySQL(db).query_db(query,data)
        print(results)
        pprint.pprint(results,sort_dicts=False)
        return results

    @classmethod
    def single_restaurant_reviews(cls,data):
        query = "SELECT rs.name, u.first_name, r. rating,r.analysis FROM reviews r JOIN users u ON r.users_id = u.id JOIN restaurants rs ON r.restaurants_id = rs.id WHERE restaurants_id = %(restaurants_id)s"
        results = connectToMySQL(db).query_db(query,data)
        print(results)
        return results
