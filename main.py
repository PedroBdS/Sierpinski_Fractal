import matplotlib.pyplot as plt
import random

A = [0, 0]
B = [6, 0]
C = [3, 5]

vezes = int(input('Indique o númmero de vezes: '))

def plotL(lado):
    plt.scatter(lado[0], lado[1], c='black', s=15)

def plot(lado, cor):
    plt.scatter(lado[0], lado[1], c=cor, s=2)

def pontoinicial():
    var = 0
    while var == 0:
        pontoy = random.uniform(0, 5)
        pontox = random.uniform(0, 6)
        if pontox < 3:
            if pontoy <= (5 / 3) * pontox:
                ponto = (pontox, pontoy)
                pontovez = [pontox, pontoy]
                var = var + 2
                return pontovez
        if pontox > 3:
            if pontoy <= (pontox - 6) * (-5 / 3):
                ponto = (pontox, pontoy)
                var = var + 2
                pontovez = [pontox, pontoy]
                return pontovez
        if pontox == 3:
            ponto = (pontox, pontoy)
            var = var + 2
            pontovez = [pontox, pontoy]
            return pontovez

def verticealeatorio():
    ver = random.randint(1, 3)
    if ver == 1:
        pontover = [0, 0]
    if ver == 2:
        pontover = [6, 0]
    if ver == 3:
        pontover = [3, 5]
    return pontover

def mediapontos(A, B):
    pontomedio = [(A[0]+B[0])/2, (A[1]+B[1])/2]
    return pontomedio

plotL(A)
plotL(B)
plotL(C)

pponto = pontoinicial()
plot(pponto, 'blue')
pontovez = pponto

p = 0

while p < vezes:
    pontovez = mediapontos(pontovez, verticealeatorio())
    plot(pontovez, 'black')
    p = p + 1


plt.show()
