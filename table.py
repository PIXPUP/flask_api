import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash,check_password_hash

Base = declarative_base()

class ctm(Base):
    __tablename__ = 'member'
    Username = sqlalchemy.Column(sqlalchemy.String,primary_key=True)
    Password = sqlalchemy.Column(sqlalchemy.String)
    Email = sqlalchemy.Column(sqlalchemy.String)
    Salt = sqlalchemy.Column(sqlalchemy.String)

    def __repr__(self):
        return f' Username {self.Username} \n password {self.Password} \n Email {self.Email} \n {self.Salt}'
    
engine = sqlalchemy.create_engine('sqlite:///ctm.db')
Base.metadata.create_all(engine)
sm = sessionmaker(engine)
session = sm()