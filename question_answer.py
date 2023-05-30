import json

with open("question_answer.json", "r") as f:
    content = f.read()

data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(f"{index + 1}. {alternative}")
    user_choice = int(input("Enter your choice: "))
    if user_choice <= len(question["alternatives"]):
        question["user_choice"] = user_choice
    else:
        print("You entered wrong alternative")
        break

score = 0

for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Correct answer"
    else:
        result = "Wrong answer"

    print(f"{index + 1}. Your answer: {question['user_choice']}, Correct answer: {question['correct_answer']}")


print("Your score is: ", score, "/", len(data))