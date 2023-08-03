import random
top_range = int(input("Enter a number: "))
if top_range<=0:
    print("Enter a number greater than 0")
    quit()
else:
    print("Please enter a number") 
    quit()

random_number = random.randint(0, top_range)
guesses = 0

while True:
    guesses += 1
    guess = int(input("Enter your guess"))

    if guess == random_number:
        print("You guessed it right!")
        break
    elif guess > random_number:
        print("Your guess is larger than the number")
    else:
        print("Your guess is smaller than the number") 

print("You guessed it in", guesses , "guesses!")