from User_DB.User import *
from User_DB.user_database import *
def user_db_test():
    assert User.login_authenticate("golnaz","pacs1golnaz")== True ,"login authenticate does not work"
    assert User.signup_authenticate("golnaz","pacs1golnaz","gmesbahi.gm@gmail.com","golnazmes")==False ,"signup authenticated does not work"

#user_db_test()


