import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
import requests
import sys

from app import create_app
from models import setup_db, Actor, Movie




class CastingTestCase(unittest.TestCase):
    """This class represents the casting test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ.get('DATABASE_URL')
        if self.database_path and self.database_path.startswith("postgres://"):
            self.database_path = self.database_path.replace("postgres://", "postgresql://", 1)
        else:
            self.database_path =os.environ.get('Test_database_name')
        setup_db(self.app, self.database_path)

        self.new_actor = {
            'name': 'mohammed',
            'age': '25',
            'gender': 'male'
        }

        self.new_movie = {
            "title": "catch me",
            "date": "03/25/2006"
        }
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

# @TODO: Write at least two tests for each endpoint - one each for success and error behavior.
#        You can feel free to write additional tests for nuanced functionality,
#        Such as adding a book without a rating, etc.
#        Since there are four routes currently, you should have at least eight tests.
# Optional: Update the book information in setUp to make the test database your own!
    def test_retrieve_actors_success(self):
        """test retreaving all actors"""
        res = self.client().get('/actors', headers={"Authorization": os.environ.get('EXECUTIVE')})
        self.assertEqual(res.status_code,200)
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_retrieve_actors_fail(self):
        """test retriving actor using not allowed method"""
        res = self.client().get('/actors/5')
        self.assertEqual(res.status_code,405)
        
     
    def test_edit_actor_success(self):
        """test if name and age was changed"""
        res = self.client().patch('/actors/3', json={"name":"nasser", "age":"22"}, headers={"Authorization": os.environ.get('EXECUTIVE')})
        self.assertEqual(res.status_code,200)
        actor = Actor.query.filter(Actor.id == 3).one_or_none()
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(actor.format()['age'], '22')
        self.assertEqual(actor.format()['name'], 'nasser')
        



    def test_edit_actor_fail(self):
        """test if actor was not found"""
        res = self.client().patch('/actors/100000',json={"name":"nasser", "age":"22"}, headers={"Authorization": os.environ.get('EXECUTIVE')} )
        self.assertEqual(res.status_code,400)
  

    
    def test_create_actor_success(self):
        """test if actor can be created"""
        res = self.client().post('/actors', json=self.new_actor, headers={"Authorization": os.environ.get('EXECUTIVE')})
        self.assertEqual(res.status_code,200)
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(data['created'])
        

    def test_create_actor_fail(self):
        """test if actor creation method is failed"""
        res = self.client().post('/actors/45', json=self.new_actor, headers={"Authorization": os.environ.get('EXECUTIVE')})
        self.assertEqual(res.status_code,405)
      
    def test_delete_actor_success(self):
        """test if actor was deleted"""
        res = self.client().delete('/actors/4', headers={"Authorization": os.environ.get('EXECUTIVE')})
        self.assertEqual(res.status_code,200)
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
           
    def test_delete_actor_fail(self):
        """test if actor deletion if actor was not found"""
        res = self.client().delete('/actors/100000', headers={"Authorization": os.environ.get('EXECUTIVE')})

        self.assertEqual(res.status_code,422)
        

    def test_retrieve_movies_success(self):
        """test retreaving all movies"""
        res = self.client().get('/movies', headers={"Authorization": os.environ.get('EXECUTIVE')})
        self.assertEqual(res.status_code,200)
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
      
    def test_retrieve_movies_fail(self):
        """test retriving movie using not allowed method"""
        res = self.client().get('/movies?page=1000', headers={"Authorization": os.environ.get('EXECUTIVE')})
        self.assertEqual(res.status_code,404)
        
    def test_edit_movie_success(self):
        """test if title and date was changed"""
        res = self.client().patch('/movies/3', json={"title": "catch me if you can", "date": "03/25/2006"}, headers={"Authorization": os.environ.get('EXECUTIVE')})
        self.assertEqual(res.status_code,200)
        data = json.loads(res.data)  
        movie = Movie.query.filter(Movie.id == 3).one_or_none()

        self.assertEqual(data['success'], True)
        self.assertEqual(movie.format()['date'], '03/25/2006')
        self.assertEqual(movie.format()['title'], 'catch me if you can')


    def test_edit_movie_fail(self):
        """test if movie was not found"""
        res = self.client().patch('/movies/100000', headers={"Authorization": os.environ.get('EXECUTIVE')})
        
        self.assertEqual(res.status_code,400)
         
    def test_create_movie_success(self):
        """test if movie can be created"""
        res = self.client().post('/movies', json=self.new_movie, headers={"Authorization": os.environ.get('EXECUTIVE')})
        self.assertEqual(res.status_code,200)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(data['created'])
        
    def test_create_movie_fail(self):
        """test if movie creation method is failed"""
        res = self.client().post('/movies/45', json=self.new_movie, headers={"Authorization": os.environ.get('EXECUTIVE')})

        self.assertEqual(res.status_code,405)
        
    def test_delete_movie_success(self):
        """test if movie was deleted"""
        res = self.client().delete('/movies/2', headers={"Authorization": os.environ.get('EXECUTIVE')})
        self.assertEqual(res.status_code,200)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        
    def test_delete_movie_fail(self):
        """test if movie deletion if movie was not found"""
        res = self.client().delete('/movies/100000', headers={"Authorization": os.environ.get('EXECUTIVE')})
        self.assertEqual(res.status_code,422)
       
    def test_executive_create_movie_success(self):
        """test if executive can create movie"""
        res = self.client().post('/movies', json=self.new_movie, headers={"Authorization": os.environ.get('EXECUTIVE')})
        self.assertEqual(res.status_code,200)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(data['created'])

    def test_executive_delete_movie_success(self):
        """test if movie was deleted"""
        res = self.client().delete('/movies/2', headers={"Authorization": os.environ.get('EXECUTIVE')})
        self.assertEqual(res.status_code,200)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
    
    def test_assistant_retrieve_actors_success(self):
        """test assistant retreaving all actors"""
        res = self.client().get('/actors', headers={"Authorization": os.environ.get('ASSISTANT')})
        self.assertEqual(res.status_code,200)
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_assistant_create_actor_fail(self):
        """test if assistant can create actor"""
        res = self.client().post('/actors', json=self.new_actor, headers={"Authorization": os.environ.get('ASSISTANT')})
        self.assertEqual(res.status_code,500)
       

    def test_director_create_actor_success(self):
        """test if director can create actor"""
        res = self.client().post('/actors', json=self.new_actor, headers={"Authorization": os.environ.get('DIRECTOR')})
        self.assertEqual(res.status_code,200)
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue(data['created'])   

    def test_director_create_movie_fail(self):
        """test if director can create movie"""
        res = self.client().post('/movies', json=self.new_movie, headers={"Authorization": os.environ.get('DIRECTOR')})
        self.assertEqual(res.status_code,500)


    
 




    

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
