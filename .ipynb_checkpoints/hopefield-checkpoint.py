import random, numpy
from numpy import power, zeros, e
import numpy as np
from utility import getRandom2DimArray, getEmpty2DimArray, saveMonoImage, imageToData
from dataset import readDataSetNegative
import math
import pickle

eps = 0.05

perfectSet = [imageToData('data/Ideal/0.png', 1, -1), 
              imageToData('data/Ideal/1.png', 1, -1), 
              imageToData('data/Ideal/2.png', 1, -1)]

noiseDetectSet = [imageToData('data/noise/0.png', 1, -1), 
              imageToData('data/noise/1.png', 1, -1), 
              imageToData('data/noise/2.png', 1, -1)]



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
    # for i in range(nc):
    #     for j in range(nc):
    #         W[i, j] = W[i, j] / nc

def run(t):
    Y = list()
    while True:
        Y = zeros((nc))
        for i in range(nc):
            for j in range(nc):
                Y[i] += W[i, j] * t[j]
            Y[i] = 1 if Y[i] > 0 else -1
        impostor = True
        for prot in perfectSet:
            i = 0
            if cmpImages(perfectSet[0], Y) <= 3:
                impostor = False
                print(perfectSet.index(prot))
                break
            i += 1
        if impostor:
            print("Impostor")
            print(f"Difference is: {cmpImages(perfectSet[0], Y)}")
            unteach(Y)
            saveMonoImage('o.png', 1, (16, 16), Y)
        else:
            break
    return Y

def unteach(liar):
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

result = run(noiseDetectSet[1])


saveMonoImage('test.png', 1, (16, 16), result)
