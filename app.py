#First we import the library to get the random numbers
import random

#This is a counter for the number of guess
guessCounter = 0

#Now we add some lines to interact with the player and a varable to save the name given
print('¡Hola! ¿Cómo te llamas?')
pName = input()

#Lets use the library random in a new variable that receive a random number between 1 and 20
number = random.randint(1, 20)
print('¡Bienvenido ' + pName + '! Estoy pensando un número entre 1 y 20')