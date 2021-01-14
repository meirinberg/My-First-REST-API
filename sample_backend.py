from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/users', methods=['GET', 'POST'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      if search_username and search_job:
         return findUserByNameAndJob(search_username, search_job)
      elif search_username:
         return findUserByName(search_username)
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True)
      #resp.status_code = 200 #optionally, you can always set a response code. 
      #200 is the default code for a normal response
      return resp

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
   if id :
      for user in users['users_list']:
         if user['id'] == id:
            if request.method == 'GET':
               return user
            elif request.method == 'DELETE':
               users['users_list'].remove(user)
               #resp = jsonify(success=True)
               #resp.status_code = 204
               resp = jsonify(), 204
               return resp
      resp = jsonify({"Msg": "User not found with provided id."}), 404
      return resp
   return users

def findUserByNameAndJob(name, job):
  sub = {'users_list' : []}
  for user in users['users_list']:
    if user['name'] == name and user['job'] == job:
      sub['users_list'].append(user)
  return sub

def findUserByName(name):
  sub = {'users_list' : []}
  for user in users['users_list']:
    if user['name'] == name:
      sub['users_list'].append(user)
  return sub

