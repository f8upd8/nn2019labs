from random import uniform
import numpy as np

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