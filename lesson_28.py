# Lesson 28 - Building a Multiple Choice Quiz

from Classroom import Question

question_prompts = [
    "What is the color of Apples?\n(a) Green\n(b) Blue\n(c) Red\n\n",
    "What is the color of Bananas?\n(a) Green\n(b) Yellow\n(c) Red\n\n",
    "What is the color of Carrot?\n(a) Orange\n(b) Blue\n(c) Red\n\n",
]

questions = [
    Question(question_prompts[0],"c"),
    Question(question_prompts[1],"b"),
    Question(question_prompts[2],"a"),
]

def run_test():
    score = 0
    for question in questions:
        answer = input("Enter the correct option: \n" + question.prompt)
        if answer == question.answer:
            score += 1
    print("Your Score is: " + str(score) + " out of " + str(len(questions)))

run_test()