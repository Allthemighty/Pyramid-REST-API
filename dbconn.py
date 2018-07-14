from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import configparser

config = configparser.ConfigParser()
config.read("config.txt")
login_string = config.get("configuration", "password")
conn = engine.connect()
Session = sessionmaker(bind=engine)
Base = declarative_base()
