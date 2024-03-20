import string
import random

passordNavn = input(str("Skriv inn hvor passordet tilhører: "))

length = int(input("Skriv inn passord lengde: "))

print('''Velg hvilket tegn i passordet ditt:
        1. Bokstaver
        2. Tall
        3. Special
        4. Generer passord''')

characterList = ""

while(True):
    choice = int(input("Velg hvilket type tegn du vil ha, du kan velge flere: "))
    if(choice == 1):

        characterList += string.ascii_letters
    elif(choice ==2):

        characterList += string.digits
    elif(choice == 3):

        characterList += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Velg mellom 1 - 4")

password = []

for i in range(length):

    randomchar = random.choice(characterList)

    password.append(randomchar)

print(passordNavn + ": " + "".join(password))
