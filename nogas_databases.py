from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func
import random, string
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    dob = Column(Integer)
    mob = Column(Integer)
    yob = Column(Integer)
    email = Column(String)
    password= Column(String)
    phonenumber = Column(Integer)
    gender = Column(String)

class Cats(Base):
    __tablename__ = 'cats'
    id = Column(Integer, primary_key= True)
    name = Column(String)
    dob = Column(String)
    mob = Column(Integer)
    yob = Column(Integer)
    info_about = Column(String)
    photo = Column(String)



    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)



engine = create_engine('sqlite:///fizzBuzz.db')


Base.metadata.create_all(engine)