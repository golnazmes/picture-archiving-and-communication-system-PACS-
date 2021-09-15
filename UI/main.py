# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_page.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import random

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QWidget, QVBoxLayout
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_template import FigureCanvas

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from dicom_manipulator.dicom_handler import *
from UI.input_data import *
from dicom_manipulator.images_to_video import convert_pictures_to_video


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
        # self.add_patient_data_button = QtWidgets.QPushButton(self.centralwidget)
        # self.add_patient_data_button.setGeometry(QtCore.QRect(20, 130, 161, 41))
        # self.add_patient_data_button.setObjectName("add_patient_data_button")
        self.apply_edit_button = QtWidgets.QPushButton(self.centralwidget)
        self.apply_edit_button.setGeometry(QtCore.QRect(240,360,75,23))
        self.apply_edit_button.setObjectName("apply_edit_data_button")
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
        self.name_tag = QtWidgets.QLabel(self.centralwidget)
        self.name_tag.setGeometry(QtCore.QRect(230, 200, 47, 13))
        self.name_tag.setObjectName("label")
        self.id_tag = QtWidgets.QLabel(self.centralwidget)
        self.id_tag.setGeometry(QtCore.QRect(230, 230, 47, 13))
        self.id_tag.setObjectName("label_2")
        self.date_tag = QtWidgets.QLabel(self.centralwidget)
        self.date_tag.setGeometry(QtCore.QRect(230, 260, 47, 13))
        self.date_tag.setObjectName("label_3")
        self.size_tag = QtWidgets.QLabel(self.centralwidget)
        self.size_tag.setGeometry(QtCore.QRect(230, 290, 47, 13))
        self.size_tag.setObjectName("label_4")
        self.type_tag = QtWidgets.QLabel(self.centralwidget)
        self.type_tag.setGeometry(QtCore.QRect(230, 320, 47, 13))
        self.type_tag.setObjectName("label_5")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(270, 200, 141, 16))
        self.name_label.setObjectName("label_6")
        self.size_label = QtWidgets.QLabel(self.centralwidget)
        self.size_label.setGeometry(QtCore.QRect(270, 290, 141, 16))
        self.size_label.setObjectName("label_7")
        self.id_label = QtWidgets.QLabel(self.centralwidget)
        self.id_label.setGeometry(QtCore.QRect(270, 230, 141, 16))
        self.id_label.setObjectName("label_8")
        self.date_label = QtWidgets.QLabel(self.centralwidget)
        self.date_label.setGeometry(QtCore.QRect(270, 260, 141, 16))
        self.date_label.setObjectName("label_9")
        self.type_label = QtWidgets.QLabel(self.centralwidget)
        self.type_label.setGeometry(QtCore.QRect(270, 320, 141, 16))
        self.type_label.setObjectName("label_10")
        self.logo_container = QtWidgets.QLabel(self.centralwidget)
        self.logo_container.setGeometry(QtCore.QRect(30, 10, 100, 70))
        self.logo_container.setObjectName("label_11")
        self.name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_edit.setGeometry(QtCore.QRect(340, 200, 113, 20))
        self.name_edit.setObjectName("lineEdit")
        self.id_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.id_edit.setGeometry(QtCore.QRect(340, 230, 113, 20))
        self.id_edit.setObjectName("lineEdit_2")
        self.date_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.date_edit.setGeometry(QtCore.QRect(340, 260, 113, 20))
        self.date_edit.setObjectName("lineEdit_3")
        self.size_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.size_edit.setGeometry(QtCore.QRect(340, 290, 113, 20))
        self.size_edit.setObjectName("lineEdit_4")
        self.type_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.type_edit.setGeometry(QtCore.QRect(340, 320, 113, 20))
        self.type_edit.setObjectName("lineEdit_5")
        self.extract_video_button = QtWidgets.QPushButton(self.centralwidget)
        self.extract_video_button.setGeometry(QtCore.QRect(20, 520, 161, 41))
        self.extract_video_button.setObjectName("pushButton")
        self.scroll_button = QtWidgets.QPushButton(self.centralwidget)
        self.scroll_button.setGeometry(QtCore.QRect(1000, 610, 81, 23))
        self.scroll_button.setObjectName("pushButton_2")
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
        # my code
        # buttons and clicks
        self.convert_project_data_button.clicked.connect(
            self.convert_project_data)  # TODO: age taraf pashimoon she chizi entekhab nakone ro handle konam
        self.view_patient_data_button.clicked.connect(self.view_dcm_data)
        self.extract_video_button.clicked.connect(self.extract_video)
        self.edit_patient_data_button.clicked.connect(self.edit_dcm_data)
        self.apply_edit_button.clicked.connect(self.apply_edit)

        # hidden elements
        self.name_edit.setHidden(True)
        self.name_label.setHidden(True)
        self.name_tag.setHidden(True)

        self.id_edit.setHidden(True)
        self.id_label.setHidden(True)
        self.id_tag.setHidden(True)

        self.date_edit.setHidden(True)
        self.date_label.setHidden(True)
        self.date_tag.setHidden(True)

        self.size_edit.setHidden(True)
        self.size_label.setHidden(True)
        self.size_tag.setHidden(True)

        self.type_edit.setHidden(True)
        self.type_label.setHidden(True)
        self.type_tag.setHidden(True)
        self.scroll_button.setHidden(True)
        self.apply_edit_button.setHidden(True)

        # image loads
        logo = QPixmap(
            r"C:\Users\Golnaz\Desktop\system design and analysis\picture-archiving-and-communication-system-PACS-\UI\images and logos\logo.png")

        self.logo_container.setScaledContents(True)
        self.logo_container.setPixmap(logo)
        background = QPixmap(
            r"C:\Users\Golnaz\Desktop\system design and analysis\picture-archiving-and-communication-system-PACS-\UI\images and logos\background.png")
        self.image_container.setScaledContents(True)
        self.image_container.setPixmap(background)
        # text inputs
        self.name_edit.textChanged.connect(get_name)
        self.id_edit.textChanged.connect(get_id)
        self.date_edit.textChanged.connect(get_date)
        self.type_edit.textChanged.connect(get_type)
        self.size_edit.textChanged.connect(get_size)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.add_patient_data_button.setText(_translate("MainWindow", "add a patient data"))
        self.apply_edit_button.setText((_translate("MainWindow","apply")))
        self.convert_patient_data_button.setText(_translate("MainWindow", "convert a patient data(jpg)"))
        self.send_patient_data_button.setText(_translate("MainWindow", "send a patient data"))
        self.convert_project_data_button.setText(_translate("MainWindow", " convert a project data for ML"))
        self.view_patient_data_button.setText(_translate("MainWindow", "view a patient data"))
        self.edit_patient_data_button.setText(_translate("MainWindow", "edit a patient data"))
        self.image_container.setText(_translate("MainWindow", "TextLabel"))
        self.name_tag.setText(_translate("MainWindow", "Name:"))
        self.id_tag.setText(_translate("MainWindow", "ID:"))
        self.date_tag.setText(_translate("MainWindow", "Date:"))
        self.size_tag.setText(_translate("MainWindow", "size:"))
        self.type_tag.setText(_translate("MainWindow", "type:"))
        self.name_label.setText(_translate("MainWindow", "name_label"))
        self.size_label.setText(_translate("MainWindow", "size_label"))
        self.id_label.setText(_translate("MainWindow", "id_label"))
        self.date_label.setText(_translate("MainWindow", "date_label"))
        self.type_label.setText(_translate("MainWindow", "type_label"))
        self.logo_container.setText(_translate("MainWindow", "logo"))
        self.extract_video_button.setText(_translate("MainWindow", "extract mp4"))
        self.scroll_button.setText(_translate("MainWindow", "view scroll bar"))

    # my functions
    def convert_project_data(self):
        response = QFileDialog.getExistingDirectory(
            QWidget(),
            caption='Select a folder'
        )
        convert_dicom_directory_to_jpg(response)
        convert_dicom_directory_to_csv(response)

    def view_dcm_data(self):
        response = QFileDialog.getOpenFileName(
            QWidget(),
            caption='Select a file to view'
        )
        print(response)
        file_path = response[0]
        ds = make_ds(file_path)
        name, id, date, row, column, type = print_patient_image_data(ds, file_path)
        print(name, id, date, row, column, type)
        self.name_label.setHidden(False)
        self.name_tag.setHidden(False)
        self.name_label.setText(name)

        self.id_label.setHidden(False)
        self.id_tag.setHidden(False)
        self.id_label.setText(id)

        self.date_label.setHidden(False)
        self.date_tag.setHidden(False)
        self.date_label.setText(str(date))

        self.size_label.setHidden(False)
        self.size_tag.setHidden(False)
        self.size_label.setText(str(row) + "*" + str(column))

        self.type_label.setHidden(False)
        self.type_tag.setHidden(False)
        self.type_label.setText(str(type[0]) if type is not None else " ")

        self.extract_video_button.setHidden(False)

        show_image(ds)
        image_path = make_image_path_based_on_file_path(file_path)
        save_image_as_jpg(ds, image_path)

    def edit_dcm_data(self):
        response = QFileDialog.getOpenFileName(
            QWidget(),
            caption='Select a file to edit'
        )
        print(response)
        file_path = response[0]
        ds = make_ds(file_path)
        name, id, date, row, column, type = print_patient_image_data(ds, file_path)
        print(name, id, date, row, column, type)

        self.name_edit.setText(name)
        self.name_tag.setHidden(False)
        self.name_edit.setHidden(False)

        self.id_edit.setText(id)
        self.id_tag.setHidden(False)
        self.id_edit.setHidden(False)

        self.date_tag.setHidden(False)
        self.date_edit.setText(str(date))
        self.date_edit.setHidden(False)

        self.size_tag.setHidden(False)
        self.size_edit.setText(str(row) + "*" + str(column))
        self.size_edit.setHidden(False)

        self.type_tag.setHidden(False)
        self.type_edit.setText(str(type[0]) if type is not None else " ")
        self.type_edit.setHidden(False)

        show_image(ds)
        image_path = make_image_path_based_on_file_path(file_path)
        save_image_as_jpg(ds, image_path)
        print_patient_image_data(ds, file_path)

    def apply_edit(self):
        file_path = f"D:\MedicalData\liver\^245652_20210825\FILE10.dcm"
        ds = make_ds(file_path)
        print_patient_image_data(ds, file_path)
        edit_dicom(ds, file_path, name_in, id_in, date_in, size_in, type_in)
        print_patient_image_data(ds, file_path)

    def extract_video(self):
        response = QFileDialog.getExistingDirectory(
            QWidget(),
            caption='Select a folder'
        )
        print(response)
        folder_path = response
        first, second = path.split(folder_path)
        second = second + "_MP4"
        mp4_folder_path = path.join(first, second)  # TODO:error handling
        if not path.exists(mp4_folder_path):
            mkdir(mp4_folder_path)
        video_path = mp4_folder_path + r"\video.mp4"
        frames_per_sec = 10
        time = 1
        convert_pictures_to_video(folder_path, video_path, frames_per_sec, time)


import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
