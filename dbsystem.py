import sqlalchemy
from table import ctm
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = sqlalchemy.create_engine('sqlite:///ctm.db')
Base.metadata.create_all(engine)
sm = sessionmaker(engine)
session = sm()

class database_system:
    def savedata(username,passoword,email,salt):
        member1 = ctm(Username=username,Password=passoword,Email=email,Salt=salt)
        session.add(member1)
        session.commit()
    def find_data(username):
        username = session.query(ctm).filter(ctm.Username == username).first()
        return username
    def updata_data(username,new_user):
        session.query(ctm).filter(ctm.Username==username).update(new_user)
        session.commit()
    def delete_data(username):
        del_user = session.query(ctm).filter(ctm.Username==username).first()
        session.delete(del_user)
        session.commit()