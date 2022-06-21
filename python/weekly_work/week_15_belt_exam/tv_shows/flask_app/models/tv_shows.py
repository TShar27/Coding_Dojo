from flask_app.config.mysqlconnection import connectToMySQL
import pprint

db = 'tv_shows_2'


class TvShow:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.description = data['description']
        self.users_id = data['users_id']



    @classmethod
    def user_tv_shows(cls,data):
        query = "SELECT * FROM tv_shows WHERE users_id = %(id)s"
        results = connectToMySQL(db).query_db(query,data)
        print(results)
        pprint.pprint(results,sort_dicts=False)
        return results
    

    @classmethod
    def show_one_tv_show(cls,data):
        query = "SELECT * FROM tv_shows WHERE id = %(id)s"
        results = connectToMySQL(db).query_db(query,{'id':data})
        print(results)
        return cls(results[0])
    
    @classmethod
    def update_tv_show(hicls,data,id):
        query = f"Update tv_shows SET title = %(title)s,network = %(network)s,release_date = %(release_date)s, description = %(description)s WHERE id = {id}"
        results = connectToMySQL(db).query_db(query,data)
        return results 

    @classmethod
    def create_tv_show(cls,data):
        query = "INSERT INTO tv_shows (title,network,release_date,description,users_id) VALUES (%(title)s, %(network)s,%(release_date)s,%(description)s)"
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        return results

    @classmethod
    def deletion(cls,data):
        query = "DELETE FROM tv_shows WHERE id = %(id)s"
        results = connectToMySQL(db).query_db(query,data)
        return results 


