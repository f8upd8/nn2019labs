import random, numpy
from numpy import power
from utility import getRandom2DimArray
from dataset import readDataSet
import math
import pickle

def f(x):
  return 1 / (1 + math.exp(-x))

dataSet = readDataSet('data/semeion.data') #Датасет

inputCount = len(dataSet[5][0]) # Количество входов
neuronCount = 10 #Количество нейронов

# Шаг 1 - Инициализация Сети
W = getRandom2DimArray(inputCount, neuronCount, -0.3, 0.3)
a0 = 0.3
D0 = neuronCount
decD = 0.0001
deca = 0.0001

NMAX = 50000

N = 0

#with open#

while True:
    N += 1
    X = random.choice(dataSet)[0]
    D = list()
    for j in range(neuronCount):
        d = 0
        for i in range(inputCount):
            d += (X[i] - W[i, j]) ** 2
        D.append(d)
    minNeuron = D.index(min(D))
    print(D)
    DN = round(D0)
    sumchange = 0
    for j in range(neuronCount):
        if abs(minNeuron - j) > DN:
            continue
        for i in range(inputCount):
            change = a0 * (X[i] - W[i, j])
            W[i, j] = W[i, j] + change
            sumchange += abs(change)
    a0 -= deca
    D0 -= decD
    if N >= NMAX or sumchange <= 50:
        with open('weights.txt', 'wb') as file:
            pickle.dump(W, file)
        break
        #print(f'Epoch: {N}. \nSummary Change: {sumchange}.')
    N += 1


classes = list()
for i in range(10):
    classes.append(list())

for data in dataSet:
    dataIndex = dataSet.index(data)
    X = data[0]
    cl = minNeuron = data[1].index(max(data[1]))
    D = list()
    for j in range(neuronCount):
        d = 0
        for i in range(inputCount):
            d += (X[i] - W[i, j]) ** 2
        D.append(d)
    minNeuron = D.index(min(D))
    classes[minNeuron].append(dataIndex)

print(classes[0])