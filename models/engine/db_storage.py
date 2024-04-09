#!/usr/bin/python3
"""DB Storage Engine Module"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """DB Storage Engine Class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""
        # Get MySQL configuration from environment variables
        HBNB_MYSQL_USER = os.getenv("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = os.getenv("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = os.getenv("HBNB_MYSQL_HOST")
        HBNB_MYSQL_DB = os.getenv("HBNB_MYSQL_DB")
        HBNB_ENV = os.getenv("HBNB_ENV")

        # Create the database engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(HBNB_MYSQL_USER,
                                              HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST,
                                              HBNB_MYSQL_DB,
                                              pool_pre_ping=True))
        # Drop all tables if environment is 'test'
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query all objects by class name, or all if cls=None"""
        # Define a class map similar to the first snippet
        class_map = {
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }

        list_objects = {}
        if cls:
            if isinstance(cls, str):
                cls = class_map.get(cls, None)
                if cls is None:
                    print("** class doesn't exist **")
                    return list_objects
            self.query_session(cls, list_objects)
        else:
            for cls_obj in class_map.values():
                self.query_session(cls_obj, list_objects)
        return list_objects

    def query_session(self, cls, list_objects):
        """handle the query and populate the dictionary,called by all"""
        query_result = self.__session.query(cls).all()
        for obj in query_result:
            key = "{}.{}".format(cls.__name__, obj.id)
            list_objects[key] = obj

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()

    def close(self):
        """Dispose of current session if active"""
        self.__session.remove()
