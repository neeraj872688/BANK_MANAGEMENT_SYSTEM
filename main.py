from register import *
from bank import *
print("Welcome to Bank Management System")
status=False
while True:
    try:
        register=int(input("1. sign up\n"
                           "2. sign in"))
        if register==1 or register==2:
            if register==1:
                SignUp()
            if register==2:
                user=SignIn()
                status=True
                break
        else:
            print("Please Enter Valid Input from Options")
    except ValueError:
        print("Invalid Input Try Again with Number")
account_number=db_query(f"SELECT account_number FROM customers where username='{user}';")

while status:
    print(f"Welcome {user.capitalize()} Choose Your Banking Service\n")
    try:
        facility=int(input("1. balance Enquiry\n"
                           "2. Cash Deposit\n"
                           "3. Cash Withral\n"
                           "4. fund transfer\n"))
        if facility>=1 and facility<=4:
            if facility==1:
                bobj = Bank(user, account_number[0][0])
                bobj.balanceenquiry()
            elif facility==2:
                while True:
                    try:
                        amount = int(input("Enter amount to deposit"))
                        bobj = Bank(user, account_number[0][0])
                        bobj.deposit(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie Number")
                        continue
            elif facility==3:
                while True:
                    try:
                        amount=int(input("Enter amount to withdraw"))
                        bobj = Bank(user, account_number[0][0])
                        bobj.withdraw(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie Number")
                        continue
            elif facility==4:
                while True:
                    try:
                        receive=int(input("Enter Receiver Account Number"))
                        amount=int(input("Enter Money to Transfer"))
                        bobj = Bank(user, account_number[0][0])
                        bobj.fundtransfer(receive,amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie Number")
                        continue

        else:
            print("Please Enter Valid Input from Options")
            continue
    except ValueError:
        print("Invalid Input Try Again with Number")
        continue