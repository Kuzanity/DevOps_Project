from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db=SQLAlchemy(app)
marsh=Marshmallow(app)

class Users(db.Model):
    __tbname__="Users_table"
    __table_args__ = {'sqlite_autoincrement': True}
    user_ID=db.Column(db.Integer,primary_key=True, nullable=False)
    user_name= db.Column(db.String(50))
    user_email= db.Column(db.String(50))
    user_pass = db.Column(db.String(50))

    def __init__(self,user_ID,user_name,user_email,user_pass):
        self.user_ID=user_ID
        self.user_name=user_name
        self.user_email=user_email
        self.user_pass= user_pass

class UsersSchema(marsh.Schema):
    class Meta:
        fields=("user_id","user_name","user_email","user_pass")

userSchema=UsersSchema()
usersSchema=UsersSchema(many=True)

@app.route('/users',methods=['POST'])
def insert_user():
    user_ID=request.json.get('user_id')
    user_name=request.json.get('user_name')
    user_email=request.json.get('user_email')
    user_pass=request.json.get('user_pass')
    add_user=Users(user_ID,user_name,user_email,user_pass)
    db.session.add(add_user)
    db.session.commit()
    return userSchema.jsonify(add_user)

@app.route('/users', methods=['GET'])
def get_users():
    user=Users.query.all()
    result=usersSchema.dump(user)
    return usersSchema.jsonify(result).data

@app.route('/users/<user_id>',methods=['PUT'])
def update_user(user_ID):
    user=Users.query.get(user_ID)
    user_ID=request.json.get('user_id')
    user_name=request.json.get('user_name')
    user_email=request.json.get('user_email')
    user_pass=request.json.get('user_pass')

    user.user_name=user_name
    user.user_email=user_email
    user.user_pass=user_pass
    db.session.commit()
    return userSchema.jsonify(user)

@app.route('/users/<user_id>',methods=['DELETE'])
def delete_user(user_ID):
    user=Users.query.get(user_ID)
    db.session.delete(user_ID)
    db.session.commit()
    return userSchema.jsonify(user)

if __name__=='__main__':
    app.run(host='0.0.0.0', port= 8000,debug=True)