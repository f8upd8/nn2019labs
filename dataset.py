from PIL import Image , ImageDraw
import random
from utility import arrayLikeGet as arrGet

def readDataSetNegative(path):
    dataSet = list()
    with open(path) as File:
        data = File.readlines()
        for line in data:
            data_list = line.split(' ')
            image_data = list(map(lambda x: (1.0 if x == '1.0000' else -1.0), data_list[:256]))
            neural_image = list(map(lambda x: (-1.0 if x == '1' else 1.0), data_list[256:len(data_list) - 1]))
            dataSet.append((image_data, neural_image))
    return dataSet

def readDataSet(path):
    dataSet = list()
    with open(path) as File:
        data = File.readlines()
        for line in data:
            data_list = line.split(' ')
            image_data = list(map(lambda x: (1.0 if x == '1.0000' else 0.0), data_list[:256]))
            neural_image = list(map(lambda x: (1.0 if x == '1' else 0.0), data_list[256:len(data_list) - 1]))
            dataSet.append((image_data, neural_image))
    return dataSet


def writeImage(path, array):
    size = int(len(array) ** 0.5)
    image = Image.new('1', (size, size), 0xffffff)
    draw = ImageDraw.Draw(image)
    for y in range(size):
        for x in range(size):
            if not arrGet(x, y, array, size):
                continue
            print(arrGet(x, y, array, size))
            draw.point((x, y), fill=0x000000)
    image.save(path, "PNG")