#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import Base
from models.state import State
from models.city import City
from models.place import Place

classes = {"State": State, "City": City, "Place": Place}

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(f"mysql+mysqldb://{user}:{pwd}@{host}/{db}", pool_pre_ping=True)

    def all(self, cls=None):
        objs = {}
        if cls:
            if type(cls) == str:
                cls = classes.get(cls)
            if cls:
                for obj in self.__session.query(cls).all():
                    objs[f"{obj.__class__.__name__}.{obj.id}"] = obj
        else:
            for c in classes.values():
                for obj in self.__session.query(c).all():
                    objs[f"{obj.__class__.__name__}.{obj.id}"] = obj
        return objs

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        self.__session.close()
