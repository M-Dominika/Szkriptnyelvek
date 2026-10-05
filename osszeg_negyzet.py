import math

def main(lista):
    ossz_negy=math.pow(sum(lista), 2)
    for i in range(len(lista)):
        lista[i] *= lista[i]
    print(ossz_negy-sum(lista))


if __name__ == '__main__':
    lista=list(range(1,101))
    main(lista)
