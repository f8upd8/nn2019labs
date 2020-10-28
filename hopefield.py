import random, numpy
from numpy import power
from utility import getRandom2DimArray, getEmpty2DimArray
from dataset import readDataSet
import math
import pickle

def f(x):
  return 1 / (1 + math.exp(-x))

dataSet = readDataSet('data/semeion.data') #Датасет
perfectSet = readDataSet('data/semeion_perfect.data') #Датасет

inputCount = len(dataSet[5][0]) # Количество входов
neuronCount = 3

W = getEmpty2DimArray(inputCount, neuronCount)

def teach(pset):
    for img in pset:
        X = img[0]
        for i in range(inputCount):
            for j in range(neuronCount):
                if i == j:
                    continue
                W[i, j] = W[i, j] + X[i] * X[j]

teach(perfectSet)

sample = dataSet[4][0]



print(W)