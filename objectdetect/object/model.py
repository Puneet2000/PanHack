from PIL import Image
import cv2
import numpy as np
from .image_models.vggnet import vgg19_bn
import os


class Finder(object):
    def __init__(self, image_path):
        self.image_path = image_path

    def predict(self):
        image = process(self.image_path)
        model = vgg19_bn(pretrained=True)
        ans = model(image)
        with open("/home/jatin/codes/projects/objectdetect/object/imagenet_classes.txt") as f:
            for i, line in enumerate(f):
                if i == ans:
                    return line[9:]
                    break
        return ans


def process(path):
    image = Image.open(path)
    # image.show()
    image = np.array(image)
    image = cv2.resize(image, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)
    image = image.reshape((1, 224, 224, 3))
    image = np.transpose(image, (0, 3, 1, 2))
    #print(image.shape)
    return image


#image_path = "/home/jatin/download.jpeg"
#object_detector = Finder(image_path)
#ans = object_detector.predict()
#print(ans)
#print(np.argmax(ans))
