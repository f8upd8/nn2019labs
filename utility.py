from random import uniform
import numpy as np
from PIL import Image, ImageDraw

def arrayLikeGet(x, y, array, size):
    return array[y * size + x]

def getRandom2DimArray(rowCount, colCount, bs, be):
    weightsraw = list()
    for i in range(rowCount):
        v0 = list()
        for j in range(colCount):
            v0.append(uniform(bs, be))
        weightsraw.append(v0)
    return np.matrix(weightsraw)

def getEmpty2DimArray(rowCount, colCount):
    weightsraw = list()
    for i in range(rowCount):
        v0 = list()
        for j in range(colCount):
            v0.append(0)
        weightsraw.append(v0)
    return np.matrix(weightsraw)

def saveMonoImage(path, black, res, pixels):
    out = Image.new("1", res, (0))
    d = ImageDraw.Draw(out)
    for i in range(res[0]):
        for j in range(res[1]):
            if arrayLikeGet(i, j, pixels, res[0]) == black:
                d.point((j, i), fill=(255))
    out.save(path)

def saveMonoImageB(path, black, res, pixels):
    out = Image.new("1", res, (0))
    d = ImageDraw.Draw(out)
    for i in range(res[0]):
        for j in range(res[1]):
            if arrayLikeGet(i, j, pixels, res[0]) == black:
                d.point((i, j), fill=(255))
    out.save(path)

def imageToData(path, b, w):
    print(path)
    data = []
    with Image.open(path) as img:
        pixels = img.load()
        for i in range(img.height):
            for j in range(img.width):
                data.append((b if pixels[i,j] == (0, 0, 0) else w))
    return data

def saveClasses(lmao):
    i = 0
    for data in lmao:
        saveMonoImageB(f'result/{i}.png', 0, (16, 16), data[0])
        i += 1