from quiz_data_manager import load_quiz, list_quizzes, save_quiz

def take_quiz(quiz_name):
    quiz = load_quiz(quiz_name)
    if not quiz:
        print("Quiz not found!")
        return
    
    score = 0
    for i, q in enumerate(quiz):
        print(f"\nQ{i+1}: {q['question']}")
        for opt in q['options']:
            print(f"  {opt}")
        answer = input("Your answer: ").strip().upper()
        if answer == q['answer'].upper():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")
    
    print(f"\n🎯 Final Score: {score} / {len(quiz)}")

def add_question_to_quiz():
    quiz_name = input("Enter quiz name to add questions: ").strip()
    questions = load_quiz(quiz_name) or []

    while True:
        question = input("Enter question (or 'q' to quit): ")
        if question.lower() == 'q':
            break
        options = []
        for opt in ['A', 'B', 'C', 'D']:
            options.append(f"{opt}) {input(f'Option {opt}: ')}")
        answer = input("Correct answer (A/B/C/D): ").upper()
        questions.append({
            "question": question,
            "options": options,
            "answer": answer
        })
    save_quiz(quiz_name, questions)
    print("✅ Questions added successfully.")

def main_menu():
    while True:
        print("\n==== Online Quiz Platform ====")
        print("1. Take a quiz")
        print("2. Add questions")
        print("3. View available quizzes")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            print("\nAvailable quizzes:", list_quizzes())
            quiz_name = input("Enter quiz name: ")
            take_quiz(quiz_name)
        elif choice == '2':
            add_question_to_quiz()
        elif choice == '3':
            print("Available Quizzes:", list_quizzes())
        elif choice == '4':
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main_menu()
