word = "Hangman"
lives = 10

underline = "_" * len(word)
print("The word has " + str(len(word)) + " letters")
print(underline)

new_underline = ""

while new_underline != word:
    user_guess = input("Guess a letter: ")
    if user_guess.lower() in word.lower():
        for index, letter in enumerate(word):
            if user_guess == letter:
                letters = list(underline)
                letters[index] = user_guess
                new_underline = "".join(letters)
                underline = new_underline
        print(new_underline)
        print("You have " + str(lives) + " lives.")
        print("Correct!")
    else:
        print("Incorrect, try again")
        lives -= 1
        print("You have " + str(lives) + " lives.")
        if lives == 0:
            print("You ran out of lives")
            print("Game Over")
            break
