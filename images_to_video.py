from cv2 import imread, VideoWriter, VideoWriter_fourcc
from os import listdir, path

def convert_pictures_to_video(jpg_folder_path, video_folder_path, frames_per_sec, time):
    frame_array = []
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


def test_images_to_video():
    directory = f"D:\MedicalData\jpg"
    folder_path = directory + '\\'
    video_path = folder_path + 'test.mp4'
    frames_per_sec = 10
    time = 1
    convert_pictures_to_video(folder_path, video_path, frames_per_sec, time)


#test_images_to_video()