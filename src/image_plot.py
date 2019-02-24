import scipy.misc
import numpy as np

class ImageSave:
    def __init__(self, width, height, channels = 3):
        self.img = np.zeros((height, width, channels))

    def put_pixel(self, x, y, r, g, b):
        self.img[y][x][0] = r
        self.img[y][x][1] = g
        self.img[y][x][2] = b

    def put_pixel(self, x, y, intensity):
        self.img[y][x][0] = intensity
        self.img[y][x][1] = intensity
        self.img[y][x][2] = intensity

    def save(self, file_name):
        scipy.misc.imsave(file_name, self.img)
