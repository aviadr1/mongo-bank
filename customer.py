# https://www.mongodb.com/try/download/community-kubernetes-operator
from mongoengine import (
    Document,
    IntField,
    StringField,
    EmailField,
    DecimalField,
    ReferenceField,
    ListField,
    connect,
)

connect(host="mongodb://localhost:27017/bank")

class Account(Document):
    account_id = IntField(primay_key=True)
    balance = DecimalField()

class Customer(Document):
    email = EmailField(
        required=True,
        primary_key=True,
    )
    name = StringField(max_length=50, required=True)
    accounts = ListField(ReferenceField(Account))

account1 = Account.objects(account_id=1).first()
if not account1:
    account1 = Account(account_id=1, balance=1000)
    account1.save()

account2 = Account.objects(account_id=2).first()
if not account2:
    account2 = Account(account_id=2, balance=9000)
    account2.save()

customer1 = Customer(email='avi@blah.com', name='avi', accounts=[account2, account1])
customer1.save()

email = input('who are you looking for? ')
the_customer = Customer.objects(email=email).first()
if not the_customer:
    print('not found')
else:
    print(the_customer.email, the_customer.name)
    for account in the_customer.accounts:
        print(account.account_id, account.balance)
