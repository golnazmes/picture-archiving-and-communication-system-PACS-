from dicom_manipulator.batch_dicom_handler import *


# unit tests
def test_convert_directory_to_jpg():
    folder_path = r"D:\MedicalData\LIVER 5\^242908_20210906"
    jpg_folder_path = convert_dicom_directory_to_jpg(folder_path)
    assert path.exists(jpg_folder_path), "JPG folder not generated correctly"


def test_convert_directory_to_csv():
    folder_path = r"D:\MedicalData\LIVER 5\^242908_20210906"
    csv_folder_path = convert_dicom_directory_to_csv(folder_path)
    assert path.exists(csv_folder_path), " CSV folder not generated correctly"


def test_convert_directory_to_mp4():
    folder_path = r"D:\MedicalData\LIVER 5\^242908_20210906_jPG"
    mp4_folder_path = convert_jpg_directory_to_video(folder_path, frames_per_sec=10, time=5)
    assert path.exists(mp4_folder_path), "MP4 folder not generated correctly"


# integration test
def integrated_test_convert_directory_to_jpg_csv_mp4():
    # check converting for ML purposes : works correctly
    test_convert_directory_to_jpg()
    test_convert_directory_to_csv()
    test_convert_directory_to_mp4()


if __name__ == '__main__':
    integrated_test_convert_directory_to_jpg_csv_mp4()
    print("everything for ML purposes works correctly.")
