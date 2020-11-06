from random import uniform
import numpy as np
from PIL import Image, ImageDraw

def imageFromArray(array, b):
    rgb_array = list(map((lambda o: (0, 0, 0) if o == b else (255, 255, 255)), array))
    return Image.fromarray(rgb_array, 'RGB')

def arrayLikeGet(x, y, array, size):
    return array[x * size + y]

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

def imageToData(img, b, w):
    data = []
    nparr = np.array(img)
    for i in range(img.height):
        for j in range(img.width):
            data.append(b if nparr[i, j][0] == 0 else w)
    return data
    
def dataToImage(array, b, w, size):
    nparr = np.zeros((size, size, 3))
    for i in range(size):
        for j in range(size):
            nparr[i, j] = [0, 0, 0] if arrayLikeGet(i, j, array, size) == b else [255, 255, 255]
    return nparr
                

def saveClasses(lmao):
    i = 0
    for data in lmao:
        saveMonoImageB(f'result/{i}.png', 0, (16, 16), data[0])
        i += 1