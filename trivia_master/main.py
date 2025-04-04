#---------------------------
#Zach Ignacio
#libraries and modules
#Use libraries to simplify solutions to programming problems
#---------------------------

# main.py
from game_modules.trivia_data import welcome_message
from game_modules.question_utils import get_random_question
from game_modules.game_logic import check_answer, update_score

def main():
    print(welcome_message)
    score = 0

    for _ in range(3):  # Ask 3 questions
        question, answer = get_random_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip().lower()

        # Check if the answer is correct
        is_correct = check_answer(user_answer, answer)

        # Update the score based on correctness
        score = update_score(score, is_correct)

        if is_correct:
            print("Correct!")
        else:
            print(f"Wrong! The correct answer was: {answer}")

    print(f"Game over! Your final score is {score}/3.")

if __name__ == "__main__":
    main()
