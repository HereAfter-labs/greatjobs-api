
from flask import Flask, redirect, url_for, request,render_template
from flask import jsonify, request

from ..models import db,User
from ..schemas import loginSchema,UserSchema
from ..app import app

@app.route('/')
def notmain():
    return {'welcome to greatjobs':'wait for updates please'}



@app.route('/main')
def main():
    return {'welcome to greatjobs 2':'stay tuned for updates '}




@app.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        print(request.json)
        (data, error) = loginSchema().load(request.json)
        print(data)
        if error:
            return jsonify(error), 400

        search = User.query.filter_by(email=data['email']).first()
        if search.password == data['password']:
            print('Yes')

            return {'id':search.id,'email':data['email'],'name':search.name,'surname':search.surname}

        return {'not found':404}




@app.route('/signup', methods=['POST', 'GET'])
def signup():

    # print (request.json , "\n-----------------------------\n")

    (data, error) = UserSchema().load(request.json)
    if error:
        return jsonify(error), 400
    print(data)
    if User.query.filter_by(email=data.email).first():
        print('email in use')
        return jsonify({'email': ['this email in use']}), 400

    db.session.add(data)
    db.session.commit()

    return ''
