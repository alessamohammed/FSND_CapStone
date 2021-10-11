from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth.auth import requires_auth

from models import setup_db, Movie, Actor
#from .auth.auth import AuthError, requires_auth

MOVIE_PER_PAGE =10

def paginate_movies(request,selection):
  page = request.args.get('page',1,type=int)
  start = (page-1)* MOVIE_PER_PAGE
  end = start+MOVIE_PER_PAGE

  movies = [movie.format() for movie in selection]
  current_movies = movies[start:end]
  return current_movies

def create_app(test_config=None):
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response
    
  @app.route('/actors')
  @requires_auth('get:actors')
  def actor_detail(payload):
    selection = Actor.query.order_by(Actor.id).all()
    
    total_actors = [actor.format() for actor in selection]
    return jsonify({
      'success': True,
      'actors': total_actors
    })

  @app.route('/movies')
  @requires_auth('get:movies')
  def movie_detail(payload):
    selection = Movie.query.order_by(Movie.id).all()
    current_movies = paginate_movies(request,selection)
    if len(current_movies) == 0:
      abort(404)
    return jsonify({
      'success':True,
      'movies':current_movies,
      'total_movies':len(Movie.query.all())
    })
  

  @app.route('/actors', methods=['post'])
  @requires_auth('post:actors')
  def create_actor(payload):
    body = request.get_json()
    new_name =body.get('name', None)
    new_age = body.get('age', None)
    new_gender = body.get('gender', None)

    try:
      actor =Actor(name=new_name,age=new_age,gender=new_gender)
      actor.insert()
      selection = Actor.query.all()

      total_actors = [actors.format() for actors in selection]
      
      return jsonify({
        'success': True,
        'actors': total_actors,
        'created': actor.format()
      
      })
    except:
      abort(422)

  @app.route('/movies', methods=['POST'])
  @requires_auth('post:movies')
  def movie_post(payload):
    body = request.get_json()
    new_title =body.get('title', None)
    new_date = body.get('date', None)
    try:
      movie =Movie(title=new_title,date=new_date)
      print(movie)
      movie.insert()
      selection = Movie.query.all()

      total_movies = [movie.format() for movie in selection]
      
      return jsonify({
        'success': True,
        'movies': total_movies,
        'created': movie.format()
      
      })
    except:
      abort(422)

  @app.route('/actors/<int:actor_id>', methods=['delete'])
  @requires_auth('delete:actors')
  def actor_delete(payload,actor_id):
    try:
      actor =Actor.query.filter(Actor.id==actor_id).one_or_none()
      deleted_actor=actor
      if actor is None:
        abort(404)
      actor.delete()

      return jsonify({
        'success': True,
        'delete': deleted_actor.format()
      
      })
    
    except:
      abort(422)

  @app.route('/movies/<int:movie_id>', methods=['delete'])
  @requires_auth('delete:movies')
  def movie_delete(payload,movie_id):
    try:
      movie = Movie.query.filter(Movie.id==movie_id).one_or_none()
      deleted_movie=movie
      if movie is None:
        abort(404)
      movie.delete()

      return jsonify({
        'success': True,
        'delete': deleted_movie.format()
      })
    
    except:
      abort(422)


  @app.route('/actors/<int:actor_id>', methods=['patch'])
  @requires_auth('modify:actors')
  def actor_edit(payload,actor_id):
    body = request.get_json()

    try:
      actor = Actor.query.filter(Actor.id==actor_id).one_or_none()
      if actor is None:
        abort(404)
      if 'name' in body:
        actor.name=body.get('name')
      if 'age' in body:
        actor.age=body.get('age')
      if 'gender' in body:
        actor.gender=body.get('gender')
      
      actor.update()

      return jsonify({
        'success': True,
        'actors': actor.format()
      
      })
    
    except:
      abort(400)

  @app.route('/movies/<int:movie_id>', methods=['patch'])
  @requires_auth('modify:movies')
  def movie_edit(payload,movie_id):
    body = request.get_json()

    try:
      movie = Movie.query.filter(Movie.id==movie_id).one_or_none()
      if movie is None:
        abort(404)
      if 'title' in body:
        movie.title=body.get('title')
      if 'date' in body:
        movie.date=body.get('date')
      movie.update()
    except:
      abort(400)
    
    return jsonify({
      'success': True,
      'movies': movie.format()
    })

   


  return app



app = create_app()

if __name__ == '__main__':
    app.run()


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        'success': False,
        'error': 422,
        'message': 'unprocessable'
    }), 422
    

@app.errorhandler(400)
def bad_request(error):
    return jsonify ({
      "success": False,
      "error": 400,
      "message": "bad request"
    })
  
@app.errorhandler(405)
def not_allowed(error):
    return jsonify({
      "success": False,
      "message": "method not allowed"
    })



@app.errorhandler(404)
def resource_not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"})


""" @app.errorhandler("AuthError")
def auth_error(AuthError):
    return jsonify({
        "success": False,
        "error": AuthError.status_code,
        "message": "Authentication error"
        
    }) """