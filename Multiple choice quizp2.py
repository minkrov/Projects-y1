import random

class quiz_structure:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

question1 = quiz_structure("What is a soda company that starts with P?", ["a) Pepsi", "b) Coca Cola", "c) Popsicle", "d) Paradisaster"], "a")
question2 = quiz_structure("What is a soda company that starts with C?", ["a) Pepsi", "b) Fanta", "c) 7up", "d) Coca Cola"],"d")
question3 = quiz_structure("What is a soda company that starts with F?", ["a) Coca Cola", "b) Fanta", "c) Pepsi", "d) 7up"], "b")

score = 0

quiz = [question1, question2, question3]

print("We have ", len(quiz), " questions in this quiz")

while True:
    try:
        question_count = int(input("How many questions would you like?: "))
        break
    except ValueError:
        print("That isn't a number!")

while question_count > len(quiz) or question_count < 1:
    if question_count > len(quiz):
        print("That's too many questions!")
    elif question_count < 1:
        print("That's too little questions!")
    else:
        print("Game starting!")
        break
    try:
        question_count = int(input("How many questions would you like?: "))
    except ValueError:
        print("That isn't a number!")

random.shuffle(quiz)

for question in quiz[0:question_count]:
    print(question.question)
    for choice in question.choices:
        print(choice)
    user_answer = input("Answer: ").lower()
    if user_answer == question.answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
        print("The answer was ", question.answer)

print("You got ", str(score), " out of ", str((question_count)))