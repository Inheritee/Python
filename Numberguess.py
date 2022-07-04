from random import randint

answer = randint(1, 15)
tries = 5

while True:
    try:
        guess = int(input("guess a random number between 1-15:  "))
        if int(guess) > 0 and int(guess) <= 15:
            if int(guess) == answer:
                print("You guessed the number!")
                break

            elif guess > answer:
                tries -= 1
                print(f"Lower \n Remaining tries: {tries} ")

            elif guess < answer:
                tries -= 1
                print(f"Higher \n Remaining tries: {tries} ")

            if tries == 0:
                print("Game over, try again")
                break
        else:   
            print("Try again, number not within requested range. ")

    except ValueError:
        print("Not a number, please enter a number! ")
        continue

#Run cmd, go current directory (cd) where this .py is located
#type and run: python3 numberguess.py
#example: C:\Users\Username\Desktop\Python>python3 numberguess.py


# added:
# - Attempt counter
# - limited attempts, program ends upon reaching limit
# - Hint as to whether you're below or higher than the randomly generated number
# - Merged lower or higher + attempt update together instead of attempt counter being seperate
# - error to retry on any value that's 1) not a number 2) not within the requested number range

# fixed:
#Operator (-=) reversly typed as: =- 1, reassigning variable tries = 5 to tries = -1 without intent.  Avoided with tries = tries -1 (same as tries -= 1)
#shortened
