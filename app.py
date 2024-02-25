import sqlalchemy
from table import ctm
from salt import generate_salt
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash,check_password_hash
from flask import Flask, request

app = Flask(__name__)
books=[]

Base = declarative_base()
engine = sqlalchemy.create_engine('sqlite:///ctm.db')
Base.metadata.create_all(engine)
sm = sessionmaker(engine)
session = sm()

@app.route("/register",methods=['POST'])
def register():
    try:
        if request.method =='POST':
            j_req = request.json
            username = j_req['Username']
            password = j_req['Password']
            email = j_req['Email']
            salt = generate_salt.saltting()
            prehash = salt+password
            pass_hash = generate_password_hash(prehash)
            member1 = ctm(Username=username,Password=pass_hash,Email=email,Salt=salt)
            session.add(member1)
            session.commit()
        return f'Wellcome {username}'
    except:
        return 'username is already taken'

@app.route("/login",methods=['POST'])
def login():
        if request.method =='POST':
            try:
                j_req = request.json
                username = j_req['Username']
                password = j_req['Password']
                user = session.query(ctm).filter(ctm.Username == username).first()
                if check_password_hash(user.Password,user.Salt+password):
                    return f'Hello, {username}'
                else:
                    return 'Password is incorrect'
            except:
                return 'username is not found'

@app.route("/ChangePassword",methods=['PUT'])
def ChangePassword():
    if request.method == 'PUT':
        try:
            j_req = request.json
            username = j_req['Username']
            old_password = j_req['Old Password']
            user = session.query(ctm).filter(ctm.Username == username).first()
            new_password = generate_password_hash(user.Salt+j_req['New Password'])
            new_user={"Username":user.Username, "Password":new_password, "Email":user.Email}
            j_req = request.get_json()
            if check_password_hash(user.Password,user.Salt+old_password):
                session.query(ctm).filter(ctm.Username==username).update(new_user)
                session.commit()
                return 'change password succeed'
            else:
                return 'password is incorrect'
        except:
            return 'username is not found'

@app.route("/DeleteAccount",methods=['DELETE'])
def delete_account():
    try:
        if request.method == 'DELETE':
            j_req = request.json
            username = j_req['Username']
            password = j_req['Password']
            user = session.query(ctm).filter(ctm.Username == username).first()
            if check_password_hash(user.Password,user.Salt+password):
                del_user = session.query(ctm).filter(ctm.Username==username).first()
                session.delete(del_user)
                session.commit()
                return 'Delete Success'
            else:
                return 'Password is incorrect'
    except:
        return 'username is not found'
if __name__ == '__main__':
    app.run(debug=True)
