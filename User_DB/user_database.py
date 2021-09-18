from User_DB.User import *
from sqlite3 import connect
from sqlite3 import Error

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_tables():
    database = r"C:\Users\Golnaz\Desktop\final\project.db"
    create_user_table = """ CREATE TABLE IF NOT EXISTS user (
                                username text PRIMARY KEY,
                                password text, 
                                email text,
                                telegram_id text
                                ); """

    conn = connect(database)
    if conn is not None:
        create_table(conn, create_user_table)
    else:
        print("Error! cannot create the database connection.")


def insert_main_user():
    golnaz = User("golnaz","pacs1golnaz","gmesbahi.gm@gmail.com","golnazmes")
    golnaz.insert_record()


#create_tables()
#insert_main_user()

