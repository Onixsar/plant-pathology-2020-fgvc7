import cv2
import matplotlib.pyplot as plt


def display_image(path, mode='plt'):
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    if mode == 'plt':
        plt.imshow(image)
    if mode == 'cv2':
        cv2.imshow('image', image)
    return


def read_image(path, color_mode='RGB'):
    assert color_mode in ['RGB', 'GRAY']
    image = cv2.imread(path)
    if color_mode == 'RGB':
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    if color_mode == 'GRAY':
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return image


def calc_clahe(image, cliplimit=5, reset=0):
    clahe = cv2.createCLAHE(clipLimit=cliplimit)
    image = clahe.apply(image) + reset
    return image