import random
from Hangman_words import word_list 
chosen_word = random.choice(word_list)
lives = 6
end = False
from Hangman_art import logo
print(logo)
display = []
for i in chosen_word:
    display.append("_")
print(f"{' '.join(display)}")
while not end:
    guess = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if (letter == guess):
            display[i] = letter
    print(f"{' '.join(display)}") 

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end = True
            print("You lose")

    if "_" not in display:
        end = True
        print("You win")
    from Hangman_art import stages
    print(stages[lives]) 

print("The word was " + chosen_word)   