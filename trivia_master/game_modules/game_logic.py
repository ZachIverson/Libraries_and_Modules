# game_modules/game_logic.py

# Function to check if the player's answer matches the correct answer
def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

# Function to update and display the score
def update_score(score, is_correct):
    if is_correct:
        score += 1
    return score
