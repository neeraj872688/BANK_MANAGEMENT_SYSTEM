#bank servicess
from database import *
import datetime
class Bank:
    def __init__(self,username,account_number):
        self.__username=username
        self.__account_number=account_number

    def create_transaction_table(self):
        db_query(f"CREATE TABLE IF NOT EXISTS {self.__username}_transaction"
                 f"(timedate VARCHAR(30),"
                 f"account_number INTEGER,"
                 f"remarks VARCHAR(30),"
                 f"amount INTEGER)")
    def balanceenquiry(self):
        temp=db_query(f"SELECT balance FROM customers where username='{self.__username}'")
        print(f"{self.__username} Balance is {temp[0][0]}")

    def deposit(self,amount):
        temp=db_query(f"SELECT balance FROM customers where username='{self.__username}'")
        test=amount+temp[0][0]
        db_query(f"UPDATE customers SET balance='{test}' where username='{self.__username}';")
        self.balanceenquiry()
        db_query(f"INSERT INTO {self.__username}_transaction VALUES("
                 f"'{datetime.datetime.now()}',"
                 f"'{self.__account_number}',"
                 f"'Amount Deposit',"
                 f"'{amount}'"
                 f")")
        print(f"{self.__username} Amount is Successfully Depositted into Your Account {self.__account_number}")

    def withdraw(self,amount):
        temp=db_query(f"SELECT balance FROM customers where username='{self.__username}';")
        if amount>temp[0][0]:
            print("Insufficient Balance Please Deposit Money")
        else:
            test=temp[0][0]-amount
            db_query(f"UPDATE customers SET balance='{test}' where username='{self.__username}';")
            self.balanceenquiry()
            db_query(f"INSERT INTO {self.__username}_transaction VALUES("
                    f"'{datetime.datetime.now()}',"
                    f"'{self.__account_number}',"
                    f"'Amount Withdraw',"
                    f"'{amount}'"
                    f")")
        print(f"{self.__username} Amount is Successfully Withdraw from Your Account {self.__account_number}")

    def fundtransfer(self, receive,amount):
        temp = db_query(f"SELECT balance FROM customers where username='{self.__username}';")
        if amount > temp[0][0]:
            print("Insufficient Balance Please Deposit Money")
        else:
            temp2 = db_query(f"SELECT balance FROM customers where account_number='{receive}';")
            test1=temp[0][0]-amount
            test2=amount+temp[0][0]
            db_query(f"UPDATE customers SET balance='{test1}' where username='{self.__username}';")
            db_query(f"UPDATE customers SET balance='{test2}' where account_number='{receive}';")
            self.balanceenquiry()
            db_query(f"INSERT INTO {self.__username}_transaction VALUES("
                     f"'{datetime.datetime.now()}',"
                     f"'{self.__account_number}',"
                     f"'Fund Transfer-> {receive}',"
                     f"'{amount}'"
                     f")")
        print(f"{self.__username} Amount is Successfully Transaction from Your Account {self.__account_number}")