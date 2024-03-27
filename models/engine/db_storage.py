#!/usr/bin/python3
"""DB Storage Engine Module"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
import sqlalchemy


class DBStorage:
    """DB Storage Engine Class"""
    __engine = None
    __session = None
    all_classes = {'User': User, 'State': State, 'City': City,
                   'Amenity': Amenity, 'Place': Place, 'Review': Review}

    def __init__(self):
        """Initialize DBStorage"""
        # Get MySQL configuration from environment variables
        HBNB_MYSQL_USER = getenv("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = getenv("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = getenv("HBNB_MYSQL_HOST")
        HBNB_MYSQL_DB = getenv("HBNB_MYSQL_DB")
        HBNB_ENV = getenv("HBNB_ENV")

        # Create the database engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(HBNB_MYSQL_USER,
                                              HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST,
                                              HBNB_MYSQL_DB),
                                      pool_pre_ping=True)
        # Drop all tables if environment is 'test'
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        objects = {}
        try:
            if cls:
                query = self.__session.query(cls).all()
            else:
                # Query all types of objects if cls is not specified
                for cls in self.all_classes.values():
                    query = self.__session.query(cls).all()
                    for obj in query:
                        key = "{}.{}".format(type(obj).__name__, obj.id)
                        objects[key] = obj
            return objects
        except SQLAlchemyError as e:
            print("Error querying the database: {}".format(e))
            return {}

    def new(self, obj):
        """Add the object to the current database session"""
        try:
            self.__session.add(obj)
        except SQLAlchemyError as e:
            print("Error adding object to session: {}".format(e))

    def save(self):
        """Commit all changes of the current database session"""
        try:
            self.__session.commit()
        except SQLAlchemyError as e:
            print("Error committing changes: {}".format(e))

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            try:
                self.__session.delete(obj)
            except SQLAlchemyError as e:
                print("Error deleting object: {}".format(e))

    def reload(self):
        """Create all tables in the database and initialize a new session"""
        try:
            # Create tables based on metadata
            Base.metadata.create_all(self.__engine)
            # Create a new database session
            session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
            Session = scoped_session(session_factory)
            self.__session = Session()
        except SQLAlchemyError as e:
            print("Error reloading the database: {}".format(e))
