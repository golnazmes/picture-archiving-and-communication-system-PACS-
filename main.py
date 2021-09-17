from PyQt5 import QtWidgets
from UI.main_window import Ui_MainWindow
from UI.signup_login_page import Signup

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    signup_ui = Signup()
    main_page = Ui_MainWindow()
    signup_ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())