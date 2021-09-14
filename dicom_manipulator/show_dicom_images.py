import numpy as np
from dicom_manipulator.dicom_handler import *


class IndexTracker(object):
    def __init__(self, ax, X):
        self.ax = ax
        ax.set_title('Scroll to Navigate through the DICOM Image Slices')

        self.X = X
        rows, cols, self.slices = X.shape
        self.ind = self.slices // 2

        self.im = ax.imshow(self.X[:, :, self.ind])
        self.update()

    def onscroll(self, event):
        print("%s %s" % (event.button, event.step))
        if event.button == 'up':
            self.ind = (self.ind + 1) % self.slices
        else:
            self.ind = (self.ind - 1) % self.slices
        self.update()

    def update(self):
        self.im.set_data(self.X[:, :, self.ind])
        self.ax.set_ylabel('Slice Number: %s' % self.ind)
        self.im.axes.figure.canvas.draw()


def execute(folder_path):
    fig, ax = plt.subplots(1, 1)
    plots = []
    counter = 0
    images_path = listdir(folder_path)
    for n, image in enumerate(images_path):
        if counter > 100:
            break
        else:
            counter += 1
        ds = make_ds(path.join(folder_path, image))
        pix = ds.pixel_array
        pix = pix * 1 + (-1024)
        plots.append(pix)
        print(pix.shape)
    print(type(plots))
    print(plots[0].shape)
    print(plots[1].shape)
    y = np.dstack(plots)
    tracker = IndexTracker(ax, y)
    fig.canvas.mpl_connect('scroll_event', tracker.onscroll)
    plt.show()


execute(folder_path=f"D:\MedicalData\liver\^245652_20210825")
