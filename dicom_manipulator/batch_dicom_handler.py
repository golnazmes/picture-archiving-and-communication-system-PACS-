import pandas as pd
from os import listdir
from csv import writer
from cv2 import imread, VideoWriter, VideoWriter_fourcc

from dicom_manipulator.single_dicom_handler import *


def convert_dicom_directory_to_jpg(folder_path):
    images_path = listdir(folder_path)
    first, second = path.split(folder_path)
    second = second + "_JPG"
    jpg_folder_path = path.join(first, second)  # TODO:error handling
    if not path.exists(jpg_folder_path):
        mkdir(jpg_folder_path)
    for n, image in enumerate(images_path):  # TODO: the folder should only contain .dcm else there will be an error
        ds = make_ds(path.join(folder_path, image))
        image = image.replace('.dcm', '.jpg')
        image_path = path.join(jpg_folder_path, image)
        save_image_as_jpg(ds, image_path)
        if n % 50 == 0:
            print('{} image converted'.format(n))
    return jpg_folder_path


def convert_dicom_directory_to_csv(folder_path):
    csv_path = r"C:\Users\Golnaz\Desktop\final\dicom_manipulator\dicom_image_description.csv"
    dicom_image_description = pd.read_csv(csv_path)
    print("convert")
    first, second = path.split(folder_path)
    second = second + "_CSV"
    dataset_path = path.join(first, second)  # TODO:error handling
    if not path.exists(dataset_path):
        mkdir(dataset_path)
    print(dataset_path)
    dataset_folder_path = dataset_path
    dataset_path = path.join(dataset_path, "dataset.csv")
    with open(dataset_path, 'w', newline='') as csvfile:
        fieldnames = list(dicom_image_description["Description"])
        csvwriter = writer(csvfile, delimiter=',')
        csvwriter.writerow(fieldnames)
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
            csvwriter.writerow(rows)
    return dataset_folder_path


def convert_jpg_directory_to_video(jpg_folder_path, frames_per_sec=10, time=1):
    frame_array = []
    first, second = path.split(jpg_folder_path)
    second = second + "_MP4"
    mp4_folder_path = path.join(first, second)  # TODO:error handling
    if not path.exists(mp4_folder_path):
        mkdir(mp4_folder_path)
    folder_path = mp4_folder_path
    video_folder_path = mp4_folder_path + r"\video.mp4"
    images_path = listdir(jpg_folder_path)
    for n, image in enumerate(images_path):
        filename = path.join(jpg_folder_path, image)
        img = imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        for k in range(time):
            frame_array.append(img)
        if n % 50 == 0:
            print('{} image added to frame array'.format(n))
    video = VideoWriter(video_folder_path, VideoWriter_fourcc(*'mp4v'), frames_per_sec, size)
    for i in range(len(frame_array)):
        video.write(frame_array[i])
    video.release()
    print("converted successfully")
    return folder_path
