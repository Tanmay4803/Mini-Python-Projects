import random
user_wins = 0
computer_wins = 0
tied_games = 0
options = ["rock" , "paper" , "scissor"]

while True:
    user_chance = input("Enter your go or press Q to quit").lower()
    if user_chance == "q":
        break
    if user_chance not in options:
        print("Choose from rock/paper/scissor")
        continue

    random_number = random.randint(0,2)
    random_go = options[random_number]
    print("Computer picked " + random_go + ".")
    if user_chance == "rock":
        if random_go == "rock":
            print("Its a tie go again")
            tied_games += 1
        elif random_go == "scissor":
            print("You win!")
            user_wins += 1
        elif random_go == "paper":
            print("You lose and you are trash!")   
            computer_wins += 1     
    
    if user_chance == "paper":
        if random_go == "paper":
            print("Its a tie go again")
            tied_games += 1
        elif random_go == "rock":
            print("You win!")
            user_wins += 1
        elif random_go == "scissor":
            print("You lose and you are trash!")
            computer_wins += 1

    if user_chance == "scissor":
        if random_go == "scissor":
            print("Its a tie go again")
            tied_games += 1
        elif random_go == "paper":
            print("You win!")
            user_wins += 1
        elif random_go == "rock":
            print("You lose and you are trash!") 
            computer_wins += 1  


print("You won", user_wins , "times.")
print("Computer won", computer_wins , "times." )
print("Total number of tied games are " + str(tied_games) + ".")