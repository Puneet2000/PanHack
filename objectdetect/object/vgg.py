# import torch
# import  torch.nn as nn
# import numpy as np
# # import cv2
# import os
# from torchvision import transforms, utils
# import torchvision.models as models
#
# transforms = transforms.Compose( [transforms.ToTensor(), transforms.ToPILImage(),
#                                    transforms.Resize((224, 224)), transforms.ToTensor()])
#
# classes = {0: 'spam', 1: 'garbage', 2: 'broken_roads', 3: 'fallen_trees'}
#
# def load_model(num_classes=4, path='/home/jatin/codes/PanHack/objectdetect/object/vgg_90.pt'):
#     model = models.vgg13_bn(True)
#     model.classifier = nn.Sequential(
#         nn.Linear(512 * 7 * 7, 4096),
#         nn.ReLU(True),
#         nn.Dropout(),
#         nn.Linear(4096, 4096),
#         nn.ReLU(True),
#         nn.Dropout(),
#         nn.Linear(4096, num_classes)
#     )
#
#     model = torch.load(path)#, map_location='cpu')
#     model.eval()
#     return model
#
# def predict(image):
#     image = transforms(image)
#     image = image.unsqueeze(0)
#     model = load_model()
#     prediction = model(image)
#     a, b = torch.max(prediction, 1)
#     return a, b, classes[b]
#
# def extract_features(image):
#     image = transforms(image)
#     image = image.unsqueeze(0)
#     image_features = model.features(image)
#     image_features = image_features.squeeze(0)
#     return image_features
