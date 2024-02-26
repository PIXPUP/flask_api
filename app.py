from salt import gen_pass
from dbsystem import database_system
from werkzeug.security import generate_password_hash,check_password_hash
from flask import Flask, request

app = Flask(__name__)
books=[]

@app.route("/register",methods=['POST'])
def register():
    try:
        j_req = request.json
        username = j_req['Username']
        password = j_req['Password']
        email = j_req['Email']
        salt,pass_hash = gen_pass.saltting(password)
        database_system.savedata(username,pass_hash,email,salt)
        return f'Wellcome {username}'
    except:
         return 'username was taken'
    
@app.route("/login",methods=['POST'])
def login():
    try:
        j_req = request.json
        username = j_req['Username']
        password = j_req['Password']
        user = database_system.find_data(username)
        if check_password_hash(user.Password,user.Salt+password):
            return f'Hello, {username}'
        else:
            return 'Password is incorrect'
    except:
        return 'username is not found'

@app.route("/ChangePassword",methods=['PUT'])
def ChangePassword():
    try:
        j_req = request.json
        username = j_req['Username']
        old_password = j_req['Old Password']
        user = database_system.find_data(username)
        new_password = generate_password_hash(user.Salt+j_req['New Password'])
        new_user={"Username":user.Username, "Password":new_password, "Email":user.Email}
        j_req = request.get_json()
        if check_password_hash(user.Password,user.Salt+old_password):
            database_system.updata_data(username,new_user)
            return 'change password success'
        else:
            return 'password is incorrect'
    except:
        return 'username is not found'

@app.route("/DeleteAccount",methods=['DELETE'])
def delete_account():
    try:
        j_req = request.json
        username = j_req['Username']
        password = j_req['Password']
        user = database_system.find_data(username)
        if check_password_hash(user.Password,user.Salt+password):
            database_system.delete_data(username)
            return 'Delete Success'
        else:
            return 'Password is incorrect'
    except:
        return 'username is not found'
if __name__ == '__main__':
    app.run(debug=True)
