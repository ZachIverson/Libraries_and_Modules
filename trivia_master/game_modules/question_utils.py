# game_modules/question_utils.py
import random
from game_modules.trivia_data import trivia_questions

# Function to get a random question and its correct answer
def get_random_question():
    question = random.choice(list(trivia_questions.keys()))
    return question, trivia_questions[question]
