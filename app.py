#First we import the library to get the random numbers
import random

#This is a counter for the number of guess
guessCounter = 0

#Now we add some lines to interact with the player and a varable to save the name given
print('¡Hola! ¿Cómo te llamas?')
pName = input()

#Lets use the library random in a new variable that receive a random number between 1 and 20
number = random.randint(1, 20)
print('¡Bienvenido ' + pName + '! Estoy pensando un número entre 1 y 20. Tienes seis intentos para acertarlo.')

#And here comes the magic. First let's check how many guesses do we have
while guessCounter < 6:
    print('Di un número.')
    guess=input()
    guess=int(guess)

    guessCounter = guessCounter + 1

#Now we check if the number guessed is bigger or lower than the random one
    if guess < number:
        print('Tu número es más bajo.')
    
    if guess > number:
        print('Tu número es más alto.')

    if guess == number:
        break

#Out of the loop we check if we guess the correct number or not
if guess == number:
    guessCounter = str(guessCounter)
    print('¡Excelente, '+ pName + '! Has adivinado el número que estaba pensando en ' + guessCounter + ' intentos.')

if guess != number:
    number = str(number)
    print('Lo siento, ' + pName + '. El número que estaba pensando es el ' + number + '.')