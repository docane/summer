from PIL import Image
import numpy as np


def cut_and_histogram(image: Image.Image, box: tuple) -> (Image.Image, list):
    im = image.copy()
    im = im.crop(box)
    histogram = im.histogram()
    return im, histogram


def resize_and_rotation(image: Image.Image, size: tuple, angle: int) -> Image.Image:
    im = image.copy()
    im = im.resize(size)
    im = im.rotate(angle)
    return im


def getchannel_and_save(image: Image.Image, channel: int, filepath: str):
    assert (3 > channel) or (channel < 0), 'channel is 0 ~ 3'
    im = image.copy()
    r, g, b = im.split()
    if channel == 0:
        temp = r
    elif channel == 1:
        temp = g
    elif channel == 2:
        temp = b
    array = np.asarray(temp)
    empty_array = np.zeros((2160, 3840, 3))
    empty_array[:, :, channel] = array
    im = Image.fromarray(np.uint8(empty_array))
    im.save(filepath)


def paste_and_entropy(image: Image.Image, box: tuple) -> (Image.Image, float):
    im = image.copy()
    im.paste(im, box)
    entropy = im.entropy()
    return im, entropy
