import sqlalchemy
from table import ctm
from salt import generate_salt
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash,check_password_hash
from flask import Flask, request

Base = declarative_base()
engine = sqlalchemy.create_engine('sqlite:///ctm.db')
Base.metadata.create_all(engine)
sm = sessionmaker(engine)
session = sm()