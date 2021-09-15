import matplotlib.pyplot as plt
from pydicom import dcmread
from cv2 import imwrite
from os import listdir, path, mkdir
import pandas as pd
import csv
from skimage.exposure import equalize_adapthist  # badtaresh kard!


# TODO: handle exceptions when file is broken or non-existent
# TODO: handle image quality improvement: DONE using matplotlib instead
# TODO: iterate through all folders of a directory


def make_ds(file_path):
    ds = dcmread(file_path)  # TODO:transfersyntaxuid
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
    return display_name,ds.PatientID,ds.StudyDate,ds.Rows,ds.Columns,ds.ImageType


def show_image(ds):
    plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
    plt.show()


def make_image_path_based_on_file_path(file_path):
    image_path = file_path.replace('.dcm', '.jpg')
    return image_path


def save_image_as_jpg(ds, image_path):
    #image = ds.pixel_array
    #imwrite(image_path, image)
    #return image
    plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
    x,image_name = path.split(image_path)
    print(image_name,x)
    image = plt.savefig(image_path,bbox_inches="tight",pad_inches = 0)
    print(image)
    return image




def convert_dicom_directory_to_jpg(folder_path):
    images_path = listdir(folder_path)
    first, second = path.split(folder_path)
    second = second + "_JPG"
    jpg_folder_path = path.join(first, second)  # TODO:error handling
    if not path.exists(jpg_folder_path):
        mkdir(jpg_folder_path)
    for n, image in enumerate(images_path):  #TODO: the folder should only contain .dcm else there will be an error
        ds = make_ds(path.join(folder_path, image))
        image = image.replace('.dcm', '.jpg')
        image_path = path.join(jpg_folder_path, image)
        save_image_as_jpg(ds, image_path)
        if n % 50 == 0:
            print('{} image converted'.format(n))


def convert_dicom_directory_to_csv(folder_path):
    csv_path = r"C:\Users\Golnaz\Desktop\system design and analysis\picture-archiving-and-communication-system-PACS-\dicom_manipulator\dicom_image_description.csv"
    dicom_image_description = pd.read_csv(csv_path)
    print("convert")
    first, second = path.split(folder_path)
    second = second + "_CSV"
    dataset_path = path.join(first, second)  # TODO:error handling
    if not path.exists(dataset_path):
        mkdir(dataset_path)
    print(dataset_path)
    dataset_path = dataset_path + r"\dataset.csv"
    with open(dataset_path, 'w', newline='') as csvfile:
        fieldnames = list(dicom_image_description["Description"])
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(fieldnames)
        images_path = listdir(folder_path)
        for n, image in enumerate(images_path):
            ds = make_ds(path.join(folder_path, image))
            rows = []
            for field in fieldnames:
                if ds.get(field, None) is None:  # to avoid error if a file is broken
                    rows.append('')
                else:
                    x = str(ds.data_element(field)).replace("'", "")
                    y = x.find(":")
                    x = x[y + 2:]
                    rows.append(x)
            writer.writerow(rows)


def test1():
    file_path = f"D:\MedicalData\liver\^245652_20210825\FILE10.dcm"
    ds = make_ds(file_path)
    print_patient_image_data(ds, file_path)
    show_image(ds)
    image_path = make_image_path_based_on_file_path(file_path)
    save_image_as_jpg(ds, image_path)


def test2():
    folder_path = f"D:\MedicalData\liver\^245652_20210825"
    convert_dicom_directory_to_jpg(folder_path)
    convert_dicom_directory_to_csv(folder_path)



