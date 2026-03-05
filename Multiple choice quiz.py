## Multiple choice quiz

# ─── ADD OR EDIT QUESTIONS HERE ───────────────────────────────────────────────
questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
    },
    {
        "question": "What is 12 x 12?",
        "choices": ["A) 124", "B) 132", "C) 144", "D) 148"],
        "answer": "C"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "choices": ["A) Charles Dickens", "B) Jane Austen", "C) Mark Twain", "D) William Shakespeare"],
        "answer": "D"
    },
    {
        "question": "What is the chemical symbol for water?",
        "choices": ["A) O2", "B) H2O", "C) CO2", "D) NaCl"],
        "answer": "B"
    },
]
# ──────────────────────────────────────────────────────────────────────────────


def run_quiz(questions):
    score = 0

    print("\n=== Multiple Choice Quiz ===\n")

    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for choice in q["choices"]:
            print(f"  {choice}")

        while True:
            answer = input("Your answer (A/B/C/D): ").strip().upper()
            if answer in ("A", "B", "C", "D"):
                break
            print("  Please enter A, B, C, or D.")

        if answer == q["answer"]:
            print("  Correct!\n")
            score += 1
        else:
            print(f"  Wrong. The correct answer was {q['answer']}.\n")

    print(f"Quiz complete! You scored {score}/{len(questions)}.")


if __name__ == "__main__":
    run_quiz(questions)
