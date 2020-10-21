import random, numpy
from numpy import power
from utility import getRandom2DimArray
from dataset import readDataSet

def F(a, S):
    return 1 / (1 + numpy.e ** (-S * a))

WEIGHTS = (-0.3, 0.3)

class BPNN:
    def __init__(self, input_c, hidden_lc, output_lc, a=0.3, e=0.1, N=10000, bfun=F):
        # Шаг 1 (Инициализация)
        self.whLayer = getRandom2DimArray(hidden_lc, input_c, WEIGHTS[0], WEIGHTS[1])
        self.woLayer = getRandom2DimArray(output_lc, hidden_lc, WEIGHTS[0], WEIGHTS[1])
        self.input_c = input_c
        self.hidden_lc = hidden_lc
        self.output_lc = output_lc
        self.e = e
        self.N = N
        self.bfun = F
        self.a = a

    def afun(self, S):
        return F(self.a, S)

    def generate_output(self, input_vector):
        hidden_out = list()
        for i in range(self.hidden_lc):
            S = 0
            for j in range(self.input_c):
                S += input_vector[j] * self.whLayer[i, j]
            hidden_out.append(self.afun(S))
        output_out = list()
        for i in range(self.output_lc):
            S = 0
            for j in range(self.hidden_lc):
                S += hidden_out[j] * self.woLayer[i, j]
            output_out.append(1 if self.afun(S) > 0.5 else 0)
        return (hidden_out, output_out)

    def teach(self, input_vector, image_vector):
        hOut, Y = self.generate_output(input_vector)
        D = image_vector
        W = self.whLayer
        V = self.woLayer
        dedv = 0
        for j in range(len(hOut)):
            for k in range(self.hidden_lc):
                print(Y[k])
                b = (Y[k] - D[k]) * Y[k] * (1 - Y[k])
                dedv = b * hOut[j]
                V[j, k] = V[j, k] - self.a * dedv
        dedw = 0
        for i in range(self.hidden_lc):
            for j in range(self.input_c):
                S = 0
                for k in range(len(Y)):
                    b = (Y[k] - D[k]) * Y[k] * (1 - Y[k])
                    S += V[j, k] * b
                dedw = S * hOut[j] * (1 - hOut[j]) * input_vector[i]
            W[i, j] = W[i, j] - self.a * dedw
        print(f'{Y} | {D} | {"SUCCESS" if D == Y else "FAILURE"}')


ds = readDataSet('data/semeion.data')

input_size = len(ds[0][0])
output_size = len(ds[0][1])
hidden_size = 5

nn = BPNN(input_size, hidden_size, output_size)

ov = nn.generate_output(ds[0][0])

epoch = 0
while (epoch <= nn.N):
    data_pick = random.choice(ds)
    input_vector = data_pick[0]
    output_vector = data_pick[1]
    nn.teach(input_vector, output_vector)

