import random
class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_welcome_message(self):
        print("Welcome to the Quiz Game!")
        print("Answer the following questions to test your knowledge.")
        print("You will receive feedback on each response. Let's get started!\n")

    def present_quiz_questions(self):
        for index, question in enumerate(self.questions, start=1):
            print(f"Question {index}: {question['text']}")
            if 'options' in question:
                for option_index, option in enumerate(question['options'], start=1):
                    print(f"{chr(64+option_index)}. {option}")
                usi = input("Enter your choice: ")
                user_choice=str(ord(usi) - 64)
                if user_choice.isdigit() and 1 <= int(user_choice) <= len(question['options']):
                    user_answer = question['options'][int(user_choice) - 1]
                else:
                    user_answer = None
            else:
                user_answer = input("Your Answer: ")
            self.evaluate_user_response(user_answer, question['answer'])

    def evaluate_user_response(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}\n")

    def display_final_results(self):
        print("Quiz Completed!")
        print(f"Your final score: {self.score}/{len(self.questions)}")

    def play_again(self):
        return input("Do you want to play again? (yes/no): ").lower() == 'yes'

def main():
    quiz_questions = [
        {
            'text': 'What is the capital of France?',
            'options': ['Paris', 'Berlin', 'London'],
            'answer': 'Paris'
        },
        {
            'text': 'Who wrote "Romeo and Juliet"?',
            'options': ['Charles Dickens', 'William Shakespeare', 'Jane Austen'],
            'answer': 'William Shakespeare'
        },
        {
            'text': 'What is the largest planet in our solar system?',
            'options': ['Mars', 'Jupiter', 'Saturn'],
            'answer': 'Jupiter'
        },
        {
            'text': 'In which year did the Titanic sink?',
            'options': ['1912', '1920', '1931'],
            'answer': '1912'
        },
        {
            'text': 'Fill in the blank: "The quick brown fox jumps over the ______."',
            'answer': 'lazy dog'
        }
    ]

    while True:
        quiz = QuizGame(quiz_questions)
        quiz.display_welcome_message()
        quiz.present_quiz_questions()
        quiz.display_final_results()

        if not quiz.play_again():
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()