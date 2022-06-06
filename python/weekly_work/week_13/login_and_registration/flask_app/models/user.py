import email
from operator import is_
from flask_app.config.mysqlconnection import connectToMySQL
import pprint
from flask import flash
import re 

db = 'mydb'

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    

    @classmethod
    def save(cls,data):
        query = 'INSERT into log_reg_users (first_naem,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);'  
        
        return connectToMySQL(db).query_db(query,data)



    @classmethod 
    def get_by_email(cls,data):
        query = "SELECT * FROM log_reg_users where email  = %(email)s "
        results = connectToMySQL(db).query_db(query,data)
        if results:
            return cls(results[0])
        else:
            return False 

    @staticmethod
    def validate(data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        is_valid = True 
        if len(data['first_name']) <= 2:
            is_valid = False
            flash('First name must be greater than 2 characters')  
        if len(data['last_name']) <= 2:
            is_valid = False
            flash('Last name must be greater than 2 characters') 
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash('Email is not valid') 
        elif not User.get_by_email({'email': data['email']}):
            is_valid = False
            flash('Email is already in use')
        if data['password'] != data['confirm']:
            is_valid = False
            flash('Password does not match current password')
            


            