import random       # To generate random values
import os          # To use system specific paremeters and functions
import re           # To use Regular Expression


while (1<2): # Creating a continuous loop
    # Define Game
    print("\n")
    print("Piedra, papel, tijeras --- ELIGE!")
    # Taking input from user
    userChoice = input("Elige: [P]iedra, [X]Papel, [T]ijeras, [S]alir: ")

    # Validating the user input
    if(not re.match("[PpXxTtSs]", userChoice)) or (len(userChoice) !=1):
        print("Elige una letra: ")
        print("[P]iedra, [X]Papel, [T]ijeras, [S]alir: ")
        continue

    # Print the user's choice
    print ("Tu elección: " + userChoice)

    #Check if user wants to exit
    if (userChoice =='S' or userChoice == 's'):
        print("Saliendo del juego...")
        break

    #Create a list of possibles choices
    choices = ['P', 'X', 'T']

    #Generationg computer's choice
    opponentChoice = random.choice(choices)

    #Print computer choice
    print('Mi elección: ' + opponentChoice)

    #Check computer's choice and user's choice by applying game logic

    if opponentChoice == str.upper(userChoice):
        print("¡EMPATE! ")
    elif opponentChoice == 'P' and userChoice.upper() == 'T':
        print("Tijeras pierde contra mi piedra, ¡YO GANO!")
    elif opponentChoice == 'T' and userChoice.upper() == 'X':
        print("Mis tijeras cortan tu papel, ¡YO GANO! ")
    elif opponentChoice == 'X' and userChoice.upper() == 'P':
        print("Mi papel envuelve tu piedra, ¡YO GANO!")
    else:
        print("Muy bien esta vez has ganado...")