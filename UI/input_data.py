global name_in, id_in, date_in, row_in,column_in, type_in
global email_in,tel_in,username_in,password_in

def get_email(text):
    global email_in
    email_in = text

def get_tel(text):
    global tel_in
    tel_in = text

def get_username(text):
    global username_in
    username_in = text

def get_password(text):
    global password_in
    password_in = text

def get_name(text):
    global name_in
    name_in = text
    print(name_in)

def get_id(text):
    global id_in
    id_in = text
    print(id_in)

def get_date(text):
    global date_in
    date_in = text
    print(date_in)

def get_row(text):
    global row_in
    row_in = text
    print(row_in)

def get_column(text):
    global column_in
    column_in = text
    print(column_in)


def get_type(text):
    global type_in
    type_in = text
    print(type_in)