import random, numpy
from numpy import power
from utility import getRandom2DimArray, saveMonoImageB
from dataset import readDataSet
import math
import pickle

def f(x):
  return 1 / (1 + math.exp(-x))

dataSet = readDataSet('data/semeion_easy.data') #Датасет

inputCount = len(dataSet[5][0]) # Количество входов
neuronCount = 10 #Количество нейронов

# Шаг 1 - Инициализация Сети
W = getRandom2DimArray(inputCount, neuronCount, -0.3, 0.3)
print(W)
a0 = 0.9
D0 = 10
decD = 0.05
deca = 0.01

NMAX = 1100

N = 0


def vdist(V, W):
    S = 0
    for i in range(len(V)):
        S += (V[i] - W[i]) ** 2
    return math.sqrt(S)

prevWinner = [-1, 0]

while True:
    sumchange = 0
    for data in dataSet[:10]:
        X = data[0]
        D = list()
        for j in range(neuronCount):
            d = 0
            for i in range(inputCount):
                d += (X[i] - W[i, j]) ** 2
            D.append(d)
        minNeuron = D.index(min(D))
        if prevWinner[0] == minNeuron:
            if prevWinner[1] > 3:
                print(f"Too much winning for {minNeuron}")
                minNeuron = random.randint(0, 9)
                prevWinner = [minNeuron, 1]
            else:
                prevWinner[1] += 1
        else:
            prevWinner = [minNeuron, 1]
        DN = round(D0)
        for j in range(neuronCount):
            if vdist(W[:,j], W[:,minNeuron]) > DN and j != minNeuron:
                continue
            for i in range(inputCount):
                change = a0 * (X[i] - W[i, j])
                W[i, j] = W[i, j] + change
                sumchange += abs(change)
    if N >= NMAX or sumchange <= 50:
        with open('weights.txt', 'wb') as file:
            pickle.dump(W, file)
        break
    print(f'Epoch: {N}. \nDN: {D0}.\na0: {a0}\nSummary Change: {sumchange}.')
    N += 1
    if a0 - deca >= 0.1:
        a0 -= deca
    if  D0 - decD   >= 0:
        D0 -= decD  


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

print(classes)