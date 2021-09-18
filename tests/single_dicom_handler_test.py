from dicom_manipulator.single_dicom_handler import *


# unit tests
def test_show_and_save_dicom():
    # check showing and saving individual images
    file_path = r"D:\MedicalData\liver\^245652_20210825\FILE10.dcm"
    ds = make_ds(file_path)
    print_patient_image_data(ds, file_path)
    show_image(ds)
    image_path = make_image_path_based_on_file_path(file_path)
    save_image_as_jpg(ds, image_path)


def test_edit_dicom():
    # check edit dicom
    file_path = r"D:\MedicalData\liver\^245652_20210825\FILE10.dcm"
    ds = make_ds(file_path)
    first = print_patient_image_data(ds, file_path)
    edit_dicom(ds, file_path, "golnaz", size=(512, 512))
    second = print_patient_image_data(ds, file_path)
    print(first, second)
    assert first != second, "edit dicom does not work correctly."


# integration test
def single_dicom_integrated_test():
    test_edit_dicom()
    test_show_and_save_dicom()


if __name__ == '__main__':
    single_dicom_integrated_test()
    print("everything for single dicom manipulation works correctly.")
