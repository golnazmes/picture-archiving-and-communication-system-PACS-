from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

from UI.main_window import Ui_MainWindow
from User_DB.user_database import *

global email_in, tel_in, username_in, password_in


def get_email(text):
    global email_in
    email_in = text
    # print(email_in)


def get_tel(text):
    global tel_in
    tel_in = text
    # print(tel_in)


def get_username(text):
    global username_in
    username_in = text
    # print(username_in)


def get_password(text):
    global password_in
    password_in = text
    # print(password_in)


class Signup(object):
    global name_in, id_in, date_in, row_in, column_in, type_in
    global email_in, tel_in, username_in, password_in

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Begin with PACS")
        MainWindow.resize(421, 503)
        MainWindow.setWindowIcon(QtGui.QIcon(r"C:\Users\Golnaz\Desktop\final\UI\images and logos\logo.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(110, 230, 61, 16))
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(110, 260, 61, 16))
        self.password_label.setObjectName("password_label")
        self.user_name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.user_name_edit.setGeometry(QtCore.QRect(180, 230, 101, 20))
        self.user_name_edit.setObjectName("user_name_edit")
        self.pasword_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.pasword_edit.setGeometry(QtCore.QRect(180, 260, 101, 20))
        self.pasword_edit.setObjectName("pasword_edit")
        self.first_page_logo_container = QtWidgets.QLabel(self.centralwidget)
        self.first_page_logo_container.setGeometry(QtCore.QRect(120, 60, 161, 151))
        self.first_page_logo_container.setObjectName("first_page_logo_container")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(100, 340, 181, 31))
        self.login_button.setObjectName("login_button")
        self.sign_up_button = QtWidgets.QPushButton(self.centralwidget)
        self.sign_up_button.setGeometry(QtCore.QRect(100, 380, 181, 31))
        self.sign_up_button.setObjectName("sign_up_button")
        self.guest_button = QtWidgets.QPushButton(self.centralwidget)
        self.guest_button.setGeometry(QtCore.QRect(100, 420, 181, 31))
        self.guest_button.setObjectName("sign_up_button")
        self.telegram_id_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.telegram_id_edit.setGeometry(QtCore.QRect(180, 200, 101, 20))
        self.telegram_id_edit.setObjectName("telegram_id_edit")
        self.telegram_id_label = QtWidgets.QLabel(self.centralwidget)
        self.telegram_id_label.setGeometry(QtCore.QRect(110, 200, 61, 16))
        self.telegram_id_label.setObjectName("telegram_id_label")
        self.email_label = QtWidgets.QLabel(self.centralwidget)
        self.email_label.setGeometry(QtCore.QRect(110, 170, 61, 16))
        self.email_label.setObjectName("email_label")
        self.email_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.email_edit.setGeometry(QtCore.QRect(180, 170, 101, 20))
        self.email_edit.setObjectName("email_edit")
        self.sign_up_logo_container = QtWidgets.QLabel(self.centralwidget)
        self.sign_up_logo_container.setGeometry(QtCore.QRect(150, 80, 91, 61))
        self.sign_up_logo_container.setObjectName("sign_up_logo_container")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(150, 310, 75, 23))
        self.start_button.setObjectName("start_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 421, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.initial_hidden_elements()
        self.set_initial_logo_background()
        self.text_inputs()
        self.set_buttons()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username_label.setText(_translate("MainWindow", "username"))
        self.password_label.setText(_translate("MainWindow", "password"))
        self.first_page_logo_container.setText(_translate("MainWindow", "first_page_logo_container"))
        self.login_button.setText(_translate("MainWindow", "log in"))
        self.sign_up_button.setText(_translate("MainWindow", "not a member? sign up"))
        self.guest_button.setText(_translate("MainWindow", "enter as guest"))
        self.telegram_id_label.setText(_translate("MainWindow", "telegram id"))
        self.email_label.setText(_translate("MainWindow", "email"))
        self.sign_up_logo_container.setText(_translate("MainWindow", "sign_up_logo_container"))
        self.start_button.setText(_translate("MainWindow", "start "))

    def initial_hidden_elements(self):
        self.email_edit.setHidden(True)
        self.email_label.setHidden(True)
        self.telegram_id_edit.setHidden(True)
        self.telegram_id_label.setHidden(True)
        self.start_button.setHidden(True)
        self.sign_up_logo_container.setHidden(True)


    def set_initial_logo_background(self):
        # image loads
        logo = QPixmap(
            r"C:\Users\Golnaz\Desktop\final\UI\images and logos\background.png")

        self.first_page_logo_container.setScaledContents(True)
        self.first_page_logo_container.setPixmap(logo)

    def text_inputs(self):
        self.email_edit.textChanged.connect(get_email)
        self.telegram_id_edit.textChanged.connect(get_tel)
        self.user_name_edit.textChanged.connect(get_username)
        self.pasword_edit.textChanged.connect(get_password)

    def set_buttons(self):
        self.login_button.clicked.connect(self.login)
        self.sign_up_button.clicked.connect(self.signup)
        self.start_button.clicked.connect(self.enter)
        self.guest_button.clicked.connect(self.guest)

    def guest(self):
        main_page.setupUi(MainWindow)
        MainWindow.show()
    def login(self):
        print("here")
        print(username_in, password_in)
        print(User.login_authenticate(username_in, password_in))
        if User.login_authenticate(username_in, password_in):
            main_page.setupUi(MainWindow)
            MainWindow.show()
        else:
            print("login failed")

    def signup(self):
        self.email_edit.setHidden(False)
        self.email_label.setHidden(False)
        self.telegram_id_edit.setHidden(False)
        self.telegram_id_label.setHidden(False)
        self.start_button.setHidden(False)
        self.sign_up_logo_container.setHidden(False)
        self.login_button.setHidden(True)
        self.sign_up_button.setHidden(True)
        self.guest_button.setHidden(True)
        self.first_page_logo_container.setHidden(True)
        logo = QPixmap(
            r"C:\Users\Golnaz\Desktop\final\UI\images and logos\background.png")

        self.sign_up_logo_container.setScaledContents(True)
        self.sign_up_logo_container.setPixmap(logo)
        MainWindow.setWindowIcon(QtGui.QIcon(r"C:\Users\Golnaz\Desktop\final\UI\images and logos\logo.png"))

    def enter(self):
        if User.signup_authenticate(username_in, password_in, email_in, tel_in) == True:
            new_user = User(username_in, password_in, email_in, tel_in)
            new_user.insert_record()
            self.login()
        else:
            print("signup not valid")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    signup_ui = Signup()
    main_page = Ui_MainWindow()
    signup_ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
