#user reigistration sign in sign up
from database import *
from customer import *
from bank import Bank
import random
def SignUp():
    username=input("Create Username: ")
    temp=db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        print("Username Already Exists")
    else:
        print("User is Available Please proceed")
        password=input("Enter Your Password: ")
        name=input("Enter Your Name: ")
        age=input("Enter Your Age: ")
        city=input("Enter Your city: ")
        while True:
            account_number=random.randint(10000000,99999999)
            temp=db_query(f"SELECT account_number from customers where account_number=' {account_number}';")
            if temp:
                continue
            else:
                print("Your Account Number",account_number)
                break
    cobj=Customer(username,password,name,age,city,account_number)
    cobj.createuser()
    bobj=Bank(username,account_number)
    bobj.create_transaction_table()
def SignIn():
    username=input("Enter username :")
    temp=db_query(f"SELECT username FROM customers where username='{username}';")
    if temp:
        while True:
            password=input(f"welcome {username.capitalize()} Enter Password: ")
            temp=db_query(f"SELECT password FROM customers where username='{username}';")
            #print(temp[0][0])
            if temp[0][0]==password:
                print("Sign IN successfully")
                return username
            else:
                print("wron Password try again")
                continue
    else:
        print("Enter correct username")
        SignIn()
