from cv2 import imread, VideoWriter, VideoWriter_fourcc
from os import listdir, path, mkdir


def convert_pictures_to_video(jpg_folder_path, frames_per_sec=10, time=1):
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



def test_images_to_video():
    directory = f"D:\MedicalData\jpg"
    folder_path = directory + '\\'
    video_path = folder_path + 'test.mp4'
    frames_per_sec = 10
    time = 1
    convert_pictures_to_video(folder_path, frames_per_sec, time)


#test_images_to_video()