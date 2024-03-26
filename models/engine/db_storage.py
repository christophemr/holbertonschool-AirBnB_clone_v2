#!/usr/bin/python3
"""DB Storage Engine Module"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
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
    all_classes = {'User': User, 'State': State, 'City': City,
                   'Amenity': Amenity, 'Place': Place, 'Review': Review}

    def __init__(self):
        """Initialize DBStorage"""
        # Get MySQL configuration from environment variables
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        # Create the database engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)
        # Drop all tables if environment is 'test'
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

        self.reload()

    def all(self, cls=None):
        """Query on the current database session"""
        objects = {}
        # Query objects based on the class
        if cls:
            query = self.__session.query(cls).all()
        else:
            # Query all types of objects if cls is not specified
            for cls in self.all_classes.values():
                query = self.__session.query(cls).all()
                # Format objects as dictionary
                for obj in query:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objects[key] = obj
        return objects

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
        """Create all tables in the database"""
        # Create tables based on metadata
        Base.metadata.create_all(self.__engine)
        # Create a new database session
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
