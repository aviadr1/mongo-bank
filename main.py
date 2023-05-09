print('starting')

# https://www.mongodb.com/try/download/community-kubernetes-operator
from mongoengine import Document, StringField, connect

print('connecting to mongo')
import os
url = "mongodb://localhost:27017/bank"
if "MONGO_URL" in os.environ:
    url = os.environ['MONGO_URL']

connect(host=url, db='bank')

print('mongo connected')

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

user = User(email='aviad@naya.com', first_name='aviad', last_name='R')
existing_user = User.objects(email=user.email, first_name=user.first_name).first()
if not existing_user:
    user.save()  # add this document to the DB
else:
    user = existing_user

print(user.id, user.email, type(user))

# exercise: create a class for Dog or Account and create one object
print('done!')


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.run()