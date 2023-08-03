print("Welcome to the game!")
playing = input("Do you want to play? ")

if playing != "yes":
    print("See you next time!")  
    quit()  
else:
    print("Let's play!")
    score = 0
    difficulty = input("Choose your difficulty - HARD/MEDIUM/EASY ").lower()
    if difficulty == "hard":
        answer = input("What is the name of prime minister? ")
        if answer.lower() == "narendor modi":
            print("Correct!")
            score +=1
        else: 
            print("You got it wrong loser!")

        print("You got " + str(score) + " questions correct!")    
    

    elif difficulty == "medium":
        answer = input("What is the capital of India? ")
        if answer.lower() == "delhi":
            print("Correct!")
            score +=1
        else: 
            print("You got it wrong loser!")

        print("You got " + str(score) + " questions correct!")    


    else:
        answer = input("What is my birthday month? ")
        if answer.lower() == "august":
            print("Correct!")
            score +=1
        else: 
            print("You got it wrong loser!")

        answer = input("What is my birthday year? ")
        if answer.lower() == "2003":
            print("Correct!")
            score +=1
        else: 
            print("You got it wrong loser!")        

        print("You got " + str(score) + " questions correct!")         