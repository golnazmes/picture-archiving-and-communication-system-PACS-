# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_page.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1130, 878)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.menu_line = QtWidgets.QFrame(self.centralwidget)
        self.menu_line.setGeometry(QtCore.QRect(200, 90, 20, 771))
        self.menu_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.menu_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.menu_line.setObjectName("menu_line")
        self.add_patient_data_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_patient_data_button.setGeometry(QtCore.QRect(20, 130, 161, 41))
        self.add_patient_data_button.setObjectName("add_patient_data_button")
        self.convert_patient_data_button = QtWidgets.QPushButton(self.centralwidget)
        self.convert_patient_data_button.setGeometry(QtCore.QRect(20, 400, 161, 41))
        self.convert_patient_data_button.setObjectName("convert_patient_data_button")
        self.send_patient_data_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_patient_data_button.setGeometry(QtCore.QRect(20, 330, 161, 41))
        self.send_patient_data_button.setObjectName("send_patient_data_button")
        self.convert_project_data_button = QtWidgets.QPushButton(self.centralwidget)
        self.convert_project_data_button.setGeometry(QtCore.QRect(20, 460, 161, 41))
        self.convert_project_data_button.setObjectName("convert_project_data_button")
        self.view_patient_data_button = QtWidgets.QPushButton(self.centralwidget)
        self.view_patient_data_button.setGeometry(QtCore.QRect(20, 270, 161, 41))
        self.view_patient_data_button.setObjectName("view_patient_data_button")
        self.edit_patient_data_button = QtWidgets.QPushButton(self.centralwidget)
        self.edit_patient_data_button.setGeometry(QtCore.QRect(20, 200, 161, 41))
        self.edit_patient_data_button.setObjectName("edit_patient_data_button")
        self.header_line = QtWidgets.QFrame(self.centralwidget)
        self.header_line.setGeometry(QtCore.QRect(0, 80, 1131, 20))
        self.header_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.header_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.header_line.setObjectName("header_line")
        self.image_container = QtWidgets.QLabel(self.centralwidget)
        self.image_container.setGeometry(QtCore.QRect(540, 160, 531, 401))
        self.image_container.setObjectName("image_container")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 200, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 230, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 260, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 290, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 320, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(270, 200, 141, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(270, 290, 141, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(270, 230, 141, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(270, 260, 141, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(270, 320, 141, 16))
        self.label_10.setObjectName("label_10")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(340, 200, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 230, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(340, 260, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(340, 290, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(340, 320, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1000, 580, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1000, 610, 81, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 10, 151, 71))
        self.label_11.setObjectName("label_11")
        self.dicom_widget = QtWidgets.QWidget(self.centralwidget)
        self.dicom_widget.setGeometry(QtCore.QRect(500, 140, 601, 391))
        self.dicom_widget.setObjectName("dicom_widget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1130, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_patient_data_button.setText(_translate("MainWindow", "add a patient data"))
        self.convert_patient_data_button.setText(_translate("MainWindow", "convert a patient data(jpg)"))
        self.send_patient_data_button.setText(_translate("MainWindow", "send a patient data"))
        self.convert_project_data_button.setText(_translate("MainWindow", " convert a project data for ML"))
        self.view_patient_data_button.setText(_translate("MainWindow", "view a patient data"))
        self.edit_patient_data_button.setText(_translate("MainWindow", "edit a patient data"))
        self.image_container.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.label_2.setText(_translate("MainWindow", "ID:"))
        self.label_3.setText(_translate("MainWindow", "Date:"))
        self.label_4.setText(_translate("MainWindow", "size:"))
        self.label_5.setText(_translate("MainWindow", "type:"))
        self.label_6.setText(_translate("MainWindow", "name_label"))
        self.label_7.setText(_translate("MainWindow", "size_label"))
        self.label_8.setText(_translate("MainWindow", "id_label"))
        self.label_9.setText(_translate("MainWindow", "date_label"))
        self.label_10.setText(_translate("MainWindow", "type_label"))
        self.pushButton.setText(_translate("MainWindow", "extract mp4"))
        self.pushButton_2.setText(_translate("MainWindow", "view scroll bar"))
        self.label_11.setText(_translate("MainWindow", "logo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

