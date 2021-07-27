from timedelta import Timedelta

from flask import Flask,jsonify
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate,identity
from user import UserRegister
from item import Item,ItemList

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

app.config['JWT_EXPIRATION_DELTA'] = Timedelta(seconds=1800)

jwt = JWT(app,authenticate,identity)

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')

@jwt.auth_response_handler
def customized_response_handler(access_token, identity):
 return jsonify({
 'access_token': access_token.decode('utf-8'),
 'user_id': identity.id
 })


if __name__ == '__main__':
    app.run(port=5000, debug=True)



