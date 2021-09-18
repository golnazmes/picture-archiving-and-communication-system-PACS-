import matplotlib.pyplot as plt
from pydicom import dcmread
from os import path, mkdir


def make_ds(file_path):
    ds = dcmread(file_path, force=True)
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

    print(f"Slice location...: {ds.get('SliceLocation', '(missing)')}")
    return display_name, ds.PatientID, ds.StudyDate, ds.Rows, ds.Columns, ds.ImageType


def show_image(ds):
    plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
    plt.gca().set_axis_on()
    plt.show()


def make_image_path_based_on_file_path(file_path):
    first, dcm_file_name = path.split(file_path)
    first, folder_name = path.split(first)
    image_path = path.join(first, folder_name + dcm_file_name.replace(".dcm", "JPG"))
    if not path.exists(image_path):
        mkdir(image_path)
    image_path = image_path + r"\figure.jpg"
    return image_path


def save_image_as_jpg(ds, image_path):
    plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
    plt.gca().set_axis_off()
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                        hspace=0, wspace=0)
    plt.margins(0, 0)
    plt.savefig(image_path, bbox_inches="tight", pad_inches=0)


def edit_dicom(ds, file_path, name="default", id="default", date="20171017", size=(512, 512),
               type=['ORIGINAL', 'PRIMARY', 'AXIAL', 'CT_SOM5 SPI']):
    ds.PatientName = name
    ds.PatientID = id
    ds.StudyDate = date
    ds.Rows = size[0]
    ds.Columns = size[1]
    ds.ImageType = type
    ds.save_as(file_path)
