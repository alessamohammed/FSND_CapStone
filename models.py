import os
from flask.json import jsonify
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy


database_path = os.environ.get('DATABASE_URL')
if database_path and database_path.startswith("postgres://"):
    database_path = database_path.replace("postgres://", "postgresql://", 1)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Movie

'''
class Movie(db.Model):  
  __tablename__ = 'movie'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  date = Column(String)
  

  def __init__(self, title, date):
    self.title = title
    self.date = date
  

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'date': self.date
    }

'''
Actor

'''
class Actor(db.Model):  
  __tablename__ = 'actor'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  age = Column(String)
  gender = Column(String)

  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender
    }
