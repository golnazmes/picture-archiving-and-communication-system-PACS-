# my code
        # buttons and clicks
        self.convert_project_data_button.clicked.connect(
            self.convert_project_data)  # TODO: age taraf pashimoon she chizi entekhab nakone ro handle konam
        self.view_patient_data_button.clicked.connect(self.view_dcm_data)
        self.extract_video_button.clicked.connect(self.extract_video)
        self.edit_patient_data_button.clicked.connect(self.edit_dcm_data)
        self.apply_edit_button.clicked.connect(self.apply_edit)






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
        if not response[0]:
            return
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
