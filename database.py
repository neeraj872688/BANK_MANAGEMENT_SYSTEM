#database management banking
import mysql.connector as sql
mydb=sql.connect(
    host="localhost",
    user="root",
    passwd="suraj@4Mysql",
    database="BANK_MANAGEMENT_SYSTEM"
)
cursor=mydb.cursor()

def db_query(str):
    cursor.execute(str)
    result=cursor.fetchall()
    return result
def  createcustomertable():
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers
                (username VARCHAR(20),
                password VARCHAR(20),
                name varchar(20),
                age INTEGER,
                city VARCHAR(20),
                balance integer not null,
                account_number integer not null,
                status BOOLEAN)

    ''')
mydb.commit()
if __name__ == "__main__":
    createcustomertable()