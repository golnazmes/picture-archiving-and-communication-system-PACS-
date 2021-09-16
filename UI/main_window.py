# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_page.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import random
from os import system, startfile

from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog, QWidget

from dicom_manipulator.single_dicom_handler import *

from UI.input_data import *



class Ui_MainWindow(object):
    @property
    def classFilePath(self):
        return self.__FilePathName

    @classFilePath.setter
    def classFilePath(self, value):
        self.__FilePathName = value
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1130, 878)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.menu_line = QtWidgets.QFrame(self.centralwidget)
        self.menu_line.setGeometry(QtCore.QRect(200, 150, 20, 711))
        self.menu_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.menu_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.menu_line.setObjectName("menu_line")
        self.batch_button = QtWidgets.QPushButton(self.centralwidget)
        self.batch_button.setGeometry(QtCore.QRect(20, 220, 161, 41))
        self.batch_button.setObjectName("batch_button")
        self.one_patient_button = QtWidgets.QPushButton(self.centralwidget)
        self.one_patient_button.setGeometry(QtCore.QRect(20, 170, 161, 41))
        self.one_patient_button.setObjectName("one_patient_button")
        self.header_line = QtWidgets.QFrame(self.centralwidget)
        self.header_line.setGeometry(QtCore.QRect(0, 130, 1131, 20))
        self.header_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.header_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.header_line.setObjectName("header_line")
        self.dicom_image_container = QtWidgets.QLabel(self.centralwidget)
        self.dicom_image_container.setGeometry(QtCore.QRect(690, 160, 381, 401))
        self.dicom_image_container.setObjectName("dicom_image_container")
        self.name_tag = QtWidgets.QLabel(self.centralwidget)
        self.name_tag.setGeometry(QtCore.QRect(260, 190, 47, 13))
        self.name_tag.setObjectName("name_tag")
        self.id_tag = QtWidgets.QLabel(self.centralwidget)
        self.id_tag.setGeometry(QtCore.QRect(260, 220, 47, 13))
        self.id_tag.setObjectName("id_tag")
        self.date_tag = QtWidgets.QLabel(self.centralwidget)
        self.date_tag.setGeometry(QtCore.QRect(260, 250, 47, 13))
        self.date_tag.setObjectName("date_tag")
        self.size_tag = QtWidgets.QLabel(self.centralwidget)
        self.size_tag.setGeometry(QtCore.QRect(260, 280, 47, 13))
        self.size_tag.setObjectName("size_tag")
        self.type_tag = QtWidgets.QLabel(self.centralwidget)
        self.type_tag.setGeometry(QtCore.QRect(260, 310, 47, 13))
        self.type_tag.setObjectName("type_tag")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(300, 190, 141, 16))
        self.name_label.setObjectName("name_label")
        self.size_label = QtWidgets.QLabel(self.centralwidget)
        self.size_label.setGeometry(QtCore.QRect(300, 280, 141, 16))
        self.size_label.setObjectName("size_label")
        self.id_label = QtWidgets.QLabel(self.centralwidget)
        self.id_label.setGeometry(QtCore.QRect(300, 220, 141, 16))
        self.id_label.setObjectName("id_label")
        self.date_label = QtWidgets.QLabel(self.centralwidget)
        self.date_label.setGeometry(QtCore.QRect(300, 250, 141, 16))
        self.date_label.setObjectName("date_label")
        self.type_label = QtWidgets.QLabel(self.centralwidget)
        self.type_label.setGeometry(QtCore.QRect(300, 310, 141, 16))
        self.type_label.setObjectName("type_label")
        self.name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_edit.setGeometry(QtCore.QRect(370, 190, 261, 20))
        self.name_edit.setObjectName("name_edit")
        self.id_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.id_edit.setGeometry(QtCore.QRect(370, 220, 261, 20))
        self.id_edit.setObjectName("id_edit")
        self.date_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.date_edit.setGeometry(QtCore.QRect(370, 250, 261, 20))
        self.date_edit.setObjectName("date_edit")
        self.row_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.row_edit.setGeometry(QtCore.QRect(370, 280, 31, 20))
        self.row_edit.setObjectName("row_edit")
        self.type_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.type_edit.setGeometry(QtCore.QRect(370, 310, 261, 20))
        self.type_edit.setObjectName("type_edit")
        self.view_in_plot_button = QtWidgets.QPushButton(self.centralwidget)
        self.view_in_plot_button.setGeometry(QtCore.QRect(270, 380, 81, 23))
        self.view_in_plot_button.setObjectName("view_in_plot_button")
        self.save_as_jpg_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_as_jpg_button.setGeometry(QtCore.QRect(270, 410, 81, 23))
        self.save_as_jpg_button.setObjectName("save_as_jpg_button")
        self.logo_container = QtWidgets.QLabel(self.centralwidget)
        self.logo_container.setGeometry(QtCore.QRect(30, 10, 121, 121))
        self.logo_container.setObjectName("logo_container")
        self.apply_edit_button = QtWidgets.QPushButton(self.centralwidget)
        self.apply_edit_button.setGeometry(QtCore.QRect(270, 350, 81, 23))
        self.apply_edit_button.setObjectName("apply_edit_button")
        self.send_data_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_data_button.setGeometry(QtCore.QRect(270, 440, 81, 23))
        self.send_data_button.setObjectName("send_data_button")
        self.column_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.column_edit.setGeometry(QtCore.QRect(450, 280, 31, 20))
        self.column_edit.setObjectName("column_edit")
        self.multiply_edit = QtWidgets.QLabel(self.centralwidget)
        self.multiply_edit.setGeometry(QtCore.QRect(420, 280, 21, 16))
        self.multiply_edit.setObjectName("multiply_edit")
        self.extract_csv_file_button = QtWidgets.QPushButton(self.centralwidget)
        self.extract_csv_file_button.setGeometry(QtCore.QRect(420, 590, 411, 41))
        self.extract_csv_file_button.setObjectName("extract_csv_file_button")
        self.extract_jpg_file_button = QtWidgets.QPushButton(self.centralwidget)
        self.extract_jpg_file_button.setGeometry(QtCore.QRect(420, 650, 411, 41))
        self.extract_jpg_file_button.setObjectName("extract_jpg_file_button")
        self.extract_mp4_file_button = QtWidgets.QPushButton(self.centralwidget)
        self.extract_mp4_file_button.setGeometry(QtCore.QRect(420, 710, 411, 41))
        self.extract_mp4_file_button.setObjectName("extract_mp4_file_button")
        self.batch_message_container = QtWidgets.QLabel(self.centralwidget)
        self.batch_message_container.setGeometry(QtCore.QRect(430, 170, 361, 91))
        self.batch_message_container.setObjectName("batch_message_container")
        self.main_background_container = QtWidgets.QLabel(self.centralwidget)
        self.main_background_container.setGeometry(QtCore.QRect(450, 300, 381, 401))
        self.main_background_container.setObjectName("main_background_container")
        self.batch_background_container = QtWidgets.QLabel(self.centralwidget)
        self.batch_background_container.setGeometry(QtCore.QRect(440, 260, 371, 301))
        self.batch_background_container.setObjectName("batch_background_container")
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
        self.initial_hidden_elements()
        self.set_initial_logo_background()
        self.set_text_inputs()
        self.set_buttons()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("Picture Archiving Communication System")
        MainWindow.setWindowIcon(QtGui.QIcon(r"C:\Users\Golnaz\Desktop\final\UI\images and logos\logo.png"))
        self.batch_button.setText(_translate("MainWindow", "work with batch data"))
        self.one_patient_button.setText(_translate("MainWindow", "work with one patient data"))
        self.dicom_image_container.setText(_translate("MainWindow", "TextLabel"))
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
        self.view_in_plot_button.setText(_translate("MainWindow", "view in plot "))
        self.save_as_jpg_button.setText(_translate("MainWindow", "save as jpg"))
        self.logo_container.setText(_translate("MainWindow", "logo"))
        self.apply_edit_button.setText(_translate("MainWindow", "apply edit"))
        self.send_data_button.setText(_translate("MainWindow", "send data"))
        self.multiply_edit.setText(_translate("MainWindow", "*"))
        self.extract_csv_file_button.setText(_translate("MainWindow", "extract csv file"))
        self.extract_jpg_file_button.setText(_translate("MainWindow", "extract jpg files"))
        self.extract_mp4_file_button.setText(_translate("MainWindow", "extract mp4"))
        self.batch_message_container.setText(_translate("MainWindow", "message container"))
        self.main_background_container.setText(_translate("MainWindow", "main_background"))
        self.batch_background_container.setText(_translate("MainWindow", "batch_background"))

    def initial_hidden_elements(self):
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

        self.row_edit.setHidden(True)
        self.column_edit.setHidden(True)
        self.size_label.setHidden(True)
        self.size_tag.setHidden(True)
        self.multiply_edit.setHidden(True)

        self.type_edit.setHidden(True)
        self.type_label.setHidden(True)
        self.type_tag.setHidden(True)

        self.view_in_plot_button.setHidden(True)
        self.apply_edit_button.setHidden(True)
        self.save_as_jpg_button.setHidden(True)
        self.send_data_button.setHidden(True)

        self.extract_csv_file_button.setHidden(True)
        self.extract_jpg_file_button.setHidden(True)
        self.extract_mp4_file_button.setHidden(True)

        self.batch_background_container.setHidden(True)
        self.dicom_image_container.setHidden(True)
        self.batch_message_container.setHidden(True)

    def set_initial_logo_background(self):
        # image loads
        logo = QPixmap(
            r"C:\Users\Golnaz\Desktop\final\UI\images and logos\logo.png")

        self.logo_container.setScaledContents(True)
        self.logo_container.setPixmap(logo)
        background = QPixmap(
            r"C:\Users\Golnaz\Desktop\final\UI\images and logos\background.png")
        self.main_background_container.setScaledContents(True)
        self.main_background_container.setPixmap(background)

    def set_text_inputs(self):
        # text inputs
        self.name_edit.textChanged.connect(get_name)
        self.id_edit.textChanged.connect(get_id)
        self.date_edit.textChanged.connect(get_date)
        self.type_edit.textChanged.connect(get_type)
        self.row_edit.textChanged.connect(get_row)
        self.column_edit.textChanged.connect(get_column)


    def set_buttons(self):
        self.one_patient_button.clicked.connect(self.view_dcm_data)
        self.view_in_plot_button.clicked.connect(self.view_in_plot)
        self.save_as_jpg_button.clicked.connect(self.save_as_jpg)
        self.apply_edit_button.clicked.connect(self.apply_edit)
        self.batch_button.clicked.connect(self.get_UI_ready_for_ML)
        self.extract_csv_file_button.clicked.connect(self.extract_csv_file)
        self.extract_jpg_file_button.clicked.connect(self.extract_jpg_files)
        self.extract_mp4_file_button.clicked.connect(self.extract_mp4)
    def view_dcm_data(self):
        self.initial_hidden_elements()
        response = QFileDialog.getOpenFileName(
            QWidget(),
            caption='Select a dicom file to view'
        )
        if not response[0]:
            return
        print(response)
        file_path = response[0]
        self.classFilePath = file_path
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

        self.view_in_plot_button.setHidden(False)
        self.apply_edit_button.setHidden(False)
        self.save_as_jpg_button.setHidden(False)
        self.send_data_button.setHidden(False)

        image_path = make_image_path_based_on_file_path(file_path)
        save_image_as_jpg(ds, image_path)
        dicom_image = QPixmap(image_path)
        self.main_background_container.setHidden(True)
        self.dicom_image_container.setHidden(False)
        self.dicom_image_container.setScaledContents(True)
        self.dicom_image_container.setPixmap(dicom_image)

    def view_in_plot(self):
        show_image(make_ds(self.classFilePath))

    def save_as_jpg(self):
        response = QFileDialog.getExistingDirectory(
            QWidget(),
            caption='Select a folder in which you want to save jpg'
        )
        #print(response)
        if not response:
            return
        #print(response)
        image_path = path.join(response,"figure.png")
        save_image_as_jpg(make_ds(self.classFilePath),image_path)

    def apply_edit(self):
        ds = make_ds(self.classFilePath)
        name, id, date, row, column, type = print_patient_image_data(ds, self.classFilePath)
        print(name, id, date, row, column, type)

        self.name_edit.setText(name)
        self.name_label.setHidden(True)
        self.name_tag.setHidden(False)
        self.name_edit.setHidden(False)

        self.id_edit.setText(id)
        self.id_label.setHidden(True)
        self.id_tag.setHidden(False)
        self.id_edit.setHidden(False)

        self.date_tag.setHidden(False)
        self.date_label.setHidden(True)
        self.date_edit.setText(str(date))
        self.date_edit.setHidden(False)

        self.size_tag.setHidden(False)
        self.size_label.setHidden(True)
        self.row_edit.setText(str(row))
        self.column_edit.setText(str(column))
        self.row_edit.setHidden(False)
        self.column_edit.setHidden(False)

        self.type_label.setHidden(True)
        self.type_tag.setHidden(False)
        self.type_edit.setText(str(type[0]) if type is not None else " ")
        self.type_edit.setHidden(False)

        self.multiply_edit.setHidden(False)
        #TODO: next click must change data

    def get_UI_ready_for_ML(self):
        self.initial_hidden_elements()

        self.main_background_container.setHidden(True)
        self.batch_message_container.setHidden(False)
        self.batch_background_container.setHidden(False)

        self.batch_message_container.setText("choose operation!")
        batch_background = QPixmap(
            r"C:\Users\Golnaz\Desktop\final\UI\images and logos\background.png")

        self.batch_background_container.setScaledContents(True)
        self.batch_background_container.setPixmap(batch_background)

        self.extract_csv_file_button.setHidden(False)
        self.extract_jpg_file_button.setHidden(False)
        self.extract_mp4_file_button.setHidden(False)

    def extract_csv_file(self):
        response = QFileDialog.getExistingDirectory(
            QWidget(),
            caption='Select a folder to extract csv from its data'
        )
        #print(response)
        if not response:
            return
        self.batch_message_container.setText("converting...")
        csv_path = convert_dicom_directory_to_csv(response)
        print(csv_path)
        csv_path = path.realpath(csv_path)
        print(csv_path)
        startfile(csv_path)
        self.batch_message_container.setText("choose operation!")

    def extract_jpg_files(self):
        response = QFileDialog.getExistingDirectory(
            QWidget(),
            caption='Select a folder to extract jpg files from its data'
        )
        # print(response)
        if not response:
            return
        self.batch_message_container.setText("converting...")
        jpg_path = convert_dicom_directory_to_jpg(response)
        print(jpg_path)
        jpg_path = path.realpath(jpg_path)
        print(jpg_path)
        startfile(jpg_path)
        self.batch_message_container.setText("choose operation!")

    def extract_mp4(self):
        response = QFileDialog.getExistingDirectory(
            QWidget(),
            caption='Select a jpg folder to extract video from its data'
        )
        # print(response)
        if not response:
            return
        self.batch_message_container.setText("converting...")
        mp4_path = convert_jpg_directory_to_video(response, frames_per_sec=10, time=1)
        print(mp4_path)
        mp4_path = path.realpath(mp4_path)
        print(mp4_path)
        startfile(mp4_path)
        self.batch_message_container.setText("choose operation!")



