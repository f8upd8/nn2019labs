import random, numpy
from numpy import power, zeros, e
import numpy as np
from utility import getRandom2DimArray, getEmpty2DimArray, saveMonoImage, imageToData
from dataset import readDataSetNegative
import math
import pickle

eps = 0.00005

perfectSet = [imageToData('data/Ideal/0.png', 1, -1),
              imageToData('data/Ideal/3.png', 1, -1)]

noiseDetectSet = [imageToData('data/noise/0.png', 1, -1), 
              imageToData('data/noise/3.png', 1, -1)]



nc = 256 # Количество входов

W = zeros((nc, nc))

def teach(pset):
    for img in pset:
        print(img)
        X = img
        for i in range(nc):
            for j in range(nc):
                if i == j:
                    continue
                W[i, j] = W[i, j] + X[i] * X[j]
    for i in range(nc):
        for j in range(nc):
            W[i, j] = W[i, j] / nc

def run(t, prot):
    Y = zeros((nc))
    for i in range(nc):
        for j in range(nc):
            Y[i] += W[i, j] * t[j]
        Y[i] = 1 if Y[i] > 0 else -1
    impostor = True
    if cmpImages(prot, Y) <= 0:
        impostor = False
    if impostor:
        print(f"It's not it!")
        print(f"Difference is: {cmpImages(prot, Y)}")
        unteach(Y)
        return run(t, prot)
    return Y


gCounter = 0

def unteach(liar):
    global gCounter
    slipped = True
    gCounter += 1
    for i in range(nc):
        for j in range(nc):
            W[i, j] = W[i, j] - eps* liar[i] * liar[j]


def cmpImages(imga, imgb):
    diff = 0
    for a, b in zip(imga, imgb):
        if a != b:
            diff += 1
    return diff





teach(perfectSet)


run(noiseDetectSet[0], perfectSet[0])
run(noiseDetectSet[1], perfectSet[1])


run(noiseDetectSet[0], perfectSet[0])
run(noiseDetectSet[1], perfectSet[1])