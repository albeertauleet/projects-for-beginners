import random
number_of_guesses = 0
player_name = input("Hello, what is your name?\n")
print ('Perfect! ' +player_name+ '.')
level = input('Now select the level of the game: easy, regular, difficult or extradifficult and if you guess the number correctly in less than 5 tries you will win.\n')
if (level == 'easy') :
    print('Oky! I am guessing a number between 1 and 10\n')
    number = random.randint(1, 10) 
elif (level == 'regular') :
    print ('Oky! I am guessing a number between 1 and 25\n')
    number = random.randint(1, 25)
elif (level == 'difficult') :
    print ('Oky! I am guessing a number between 1 and 50\n')
    number = random.randint(1, 50)
elif (level == 'extradifficult') :
    print ('Hmm... I am guessing a number between 1 and 1000\n')
    number = random.randint(1, 1000)
else : print ('Try again, you have to select a level between easy, regular, difficult or extradifficult\n')
while number_of_guesses < 5:
        guess = int(input())
        number_of_guesses += 1

        if guess < number:
            print('Your guess is too low.\n')
        elif guess > number:
            print('Your guess is too high.\n')
        else:
            print ('Congratulations! You win :)\n')
            break
if number_of_guesses == 5:
    final = input('Oooh... you lose :(\n Do you want to continue ?\n')
    if final.lower() in ['yes', 'y']:
        final2 = input('Oky! Let continue but I have to advertise you that once you start you cannot stop unless you guess the correct number. Are you sure you want to continue ?\n')
        if final2.lower() in ['yes', 'y']:
            while True:
                guess = int(input())
                number_of_guesses += 1

                if guess < number:
                    print('Your guess is too low.\n')
                elif guess > number:
                    print('Your guess is too high.\n')
                else:
                    print('Congratulations! You have guessed the number but in ' + str(number_of_guesses) + ' tries\n')
                    break
        else:
            print('Goodbye! ' + player_name+'\n')
    else:  
        print('Goodbye! ' + player_name + ' have a good defeat jeje\n')
