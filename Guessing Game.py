import random

words = "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "lime", "mango", "nectarine", "orange", "pear", "pineapple", "plum", "raspberry", "strawberry", "tangerine", "watermelon"

word = random.choice(words)

print("These are the words you can guess: ", words)

def word_guess(attempts = 3):
    if attempts == 0:
        print("You didn't guess the word!")
        print("The word is: ", word)
        return
    
    else:
        guess = input("Guess the word: ")
        if guess == word:
            print("You guessed the word!")
            return
        else:
            print("You didn't guess the word!")
            print("Try again!")
            word_guess(attempts - 1)

word_guess()