from config import config
from PIL import Image
import library


if __name__ == '__main__':
    # 대상 사진 파일 경로 불러오기
    file_path = config["file_path"]
    new_file_path = config["new_file_path"]
    size = config["size"]

    im = Image.open(file_path)
    # im = im.resize(size)
    # im.save(new_file_path)

    # cut_and_histogram 테스트
    image, histogram = library.cut_and_histogram(im, (0, 0, 1920, 1080))
    image.show()
    print(histogram)

    # resize_and_rotation 테스트
    image = library.resize_and_rotation(im, (1920, 1080), 90)
    image.show()

    # getchannel_and_save 테스트
    library.getchannel_and_save(im, 2, 'newjeans_blue.jpg')

    # paste_and_entropy 테스트
    image, entropy = library.paste_and_entropy(im, (1920, 1080))
    image.show()
    print(entropy)

