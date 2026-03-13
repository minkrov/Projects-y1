## Multiple choice quiz


class questions_answers:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

question1 = questions_answers("What is the capital of France", ["a) Bordeaux", "b) Paris"], "b")
print(question1.question)

question2 = questions_answers("What is the capital of Germany?", ["a) Berlin", "b) Bonn"], "a")

quiz = [question1, question2]

score = 0

for question in quiz:
    print(question.question)
    for choice in question.choices:
        print(choice)
    user_answer = input().lower()
    if user_answer == question.answer:
        score += 1
        print("Correct!")
    else:
        print("Incorrect")


print("You got " + str(score) + " correct!")