import random
def EsPar(num):
    if type(num/2) == int:
        print('Es Par')
    
    else:
        print('Es Impar')

def Randomizar():
    num = random.randint(10, 25)
    num = num - num//2
    return num

num = Randomizar()
EsPar(num)