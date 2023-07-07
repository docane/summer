from PIL import Image


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
    im = im.getchannel(channel)
    im.save(filepath)


def paste_and_entropy(image: Image.Image, box: tuple) -> (Image.Image, float):
    im = image.copy()
    im.paste(im, box)
    entropy = im.entropy()
    return im, entropy
