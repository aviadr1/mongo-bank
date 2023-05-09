# https://www.mongodb.com/try/download/community-kubernetes-operator
from mongoengine import Document, StringField, connect

connect(host="mongodb://localhost:27017/bank")


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


