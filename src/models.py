import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

    
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    title = Column(String(250))
    description = Column(String(250))
    media_source = Column(String(250))


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    follower_id = Column(Integer, ForeignKey('user.id'))
    

class Comment (Base): 
    __tablename__ = 'comment'
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    commentText_id = Column(String(250))

class PostType(Base):
    __tablename__ = 'postType'
    id = Column(Integer,primary_key=True)
    story_id = Column(Integer, unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    reel_id = Column(Integer, unique=True, nullable=False)   


class Like(Base):
    __tablename__ = 'like'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, unique=True, nullable=False)
    comment_id = Column(Integer, unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    
class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    # id = Column(Integer, primary_key=True)
    # name = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250))
    password = Column(String(250))
    like = relationship(Like)
    follower = relationship(Follower)
    postType = relationship(PostType)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e