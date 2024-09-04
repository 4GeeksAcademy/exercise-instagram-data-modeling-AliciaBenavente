import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    fullname = Column(String(250), nullable=False)
    username = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)
    followers = Column(Integer, nullable=False)
    following = Column(Integer, nullable=False)

class DirectMessages(Base):
    __tablename__ = 'direct messages'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    text = Column(String(500), nullable=False)
    userID_from = Column(Integer, ForeignKey("user.id"))
    userID_to = Column(Integer, ForeignKey("user.id"))
    followerID_to = Column(Integer, ForeignKey("followers.id"))
    user = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    # image = Column(image, nullable=False)
    text = Column(String(350), nullable=False)
    likes = Column(Integer, nullable=False)
    tags = Column(Integer, nullable=False)
    userId = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)

class Comments(Base):
    __tablename__ = 'comments'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    text = Column(String(300), nullable=False)
    userId = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Followers(Base):
    __tablename__= "followers"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    follower_id = Column(Integer, ForeignKey("user.id"))





class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
