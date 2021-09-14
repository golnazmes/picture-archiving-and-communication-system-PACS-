import matplotlib.pyplot as plt
from pydicom import dcmread
from cv2 import imwrite
from os import listdir, path
import pandas as pd
import csv
from skimage.exposure import equalize_adapthist  # badtaresh kard!

# TODO: handle exceptions when file is broken or non-existent
# TODO: handle image quality improvement



folder_path = f"D:\MedicalData\liver\^245652_20210825"
jpg_folder_path = f"D:\MedicalData\jpg"
# csv_folder_path = f"D:\MedicalData\liver\^245652_20210825\csv"


def make_ds(file_path):
    ds = dcmread(file_path) #TODO:transfersyntaxuid
    return ds


def print_patient_image_data(ds, file_path):
    print()
    print(f"File path........: {file_path}")
    print(f"SOP Class........: {ds.SOPClassUID} ({ds.SOPClassUID.name})")
    print()
    pat_name = ds.PatientName
    display_name = pat_name.family_name + ", " + pat_name.given_name
    print(f"Patient's Name...: {display_name}")
    print(f"Patient ID.......: {ds.PatientID}")
    print(f"Modality.........: {ds.Modality}")
    print(f"Study Date.......: {ds.StudyDate}")
    print(f"Image size.......: {ds.Rows} x {ds.Columns}")
    print(f"Pixel Spacing....: {ds.PixelSpacing}")
    print(f"image type.......: {ds.ImageType}")

    # use .get() if not sure the item exists, and want a default value if missing
    print(f"Slice location...: {ds.get('SliceLocation', '(missing)')}")


def show_image(ds):
    plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
    plt.show()


def make_image_path_based_on_file_path(file_path):
    image_path = file_path.replace('.dcm', '.jpg')
    return image_path


def save_image_as_jpg(ds, image_path):
    image = ds.pixel_array
    imwrite(image_path, image)
    return image


def convert_dicom_directory_to_jpg(folder_path, jpg_folder_path):
    images_path = listdir(folder_path)
    for n, image in enumerate(images_path):#the folder should only contain .dcm else there will be an error
        ds = make_ds(path.join(folder_path, image))
        image = image.replace('.dcm', '.jpg')
        image_path = path.join(jpg_folder_path, image)
        save_image_as_jpg(ds, image_path)
        if n % 50 == 0:
            print('{} image converted'.format(n))


def convert_dicom_directory_to_csv(folder_path):
    dicom_image_description = pd.read_csv("dicom_image_description.csv")
    with open('dataset.csv', 'w', newline='') as csvfile:
        fieldnames = list(dicom_image_description["Description"])
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(fieldnames)
        images_path = listdir(folder_path)
        for n, image in enumerate(images_path):
            ds = make_ds(path.join(folder_path, image))
            rows = []
            for field in fieldnames:
                if ds.get(field, None) is None: #to avoid error if a file is broken
                    rows.append('')
                else:
                    x = str(ds.data_element(field)).replace("'", "")
                    y = x.find(":")
                    x = x[y + 2:]
                    rows.append(x)
            writer.writerow(rows)


def test1():
    file_path=f"D:\MedicalData\liver\^245652_20210825\FILE10.dcm"
    ds = make_ds(file_path)
    print_patient_image_data(ds,file_path)
    show_image(ds)
    image_path = make_image_path_based_on_file_path(file_path)
    save_image_as_jpg(ds, image_path)


def test2():
    convert_dicom_directory_to_jpg(folder_path, jpg_folder_path)
    convert_dicom_directory_to_csv(folder_path)


