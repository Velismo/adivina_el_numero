import random

n=random.randrange(1,20)
nu=int(input('Adivina el número que he elegido: '))
while nu!=n:
    if nu>n:
        nu=int(input('El numero es más pequeño'))
    elif nu<n:
        nu=int(input('El numero elegido es más grande'))
print('Enhorabuena!! ',n, ' es el número secreto' )