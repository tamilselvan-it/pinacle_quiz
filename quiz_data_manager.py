import json
import os

QUIZ_FOLDER = "quizzes"

def load_quiz(quiz_name):
    path = os.path.join(QUIZ_FOLDER, f"{quiz_name}.json")
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return json.load(f)

def list_quizzes():
    return [f.replace(".json", "") for f in os.listdir(QUIZ_FOLDER) if f.endswith(".json")]

def save_quiz(quiz_name, questions):
    os.makedirs(QUIZ_FOLDER, exist_ok=True)
    path = os.path.join(QUIZ_FOLDER, f"{quiz_name}.json")
    with open(path, "w") as f:
        json.dump(questions, f, indent=2)
