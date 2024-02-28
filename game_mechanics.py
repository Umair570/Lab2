
#---------------------------------------
#  Game Mechanics
#    M.Umair Ashraf(271047570) (team lead)
#---------------------------------------

def welcome_message():
    """
    Display the game's welcome message to the player.

    Parameters: None
    Returns: None
    """
    #------------------------
    return "Welcome to the game!!!\n"
    #------------------------
    #------------------------ 
#---------------------------------------
    
def choose_category(categories):
    """
    Ask the player to choose a quiz category from a list of categories.

    Parameters:
    - categories (list of str): A list of category names.

    Returns:
    - str: The chosen category.
    """
    #------------------------
    option=input("Choose a category: ")
    if option in categories:
        print("The chosen category:",option)
    else:
        print("Invalid category")
  

    #------------------------

    #------------------------

#---------------------------------------

def display_score(score, round_number):
    """
    Display the current score and round number to the player.

    Parameters:
    - score (int): The player's current score.
    - round_number (int): The current round number.

    Returns: None
    """
    #------------------------
    print("The player's current score: ",int(score))
    print("The current round: ",int(round_number))
    #------------------------
 
    #------------------------

#---------------------------------------
    
def game_over_message(final_score):
    """
    Display a "game over" message along with the player's final score.

    Parameters:
    - final_score (int): The player's final score at the end of the game.

    Returns: None
    """
    #------------------------
    print("\nGame over.\nSee you next time.Bye!!")
    print("\nThe player's final score is: ",int(final_score))

   
    #------------------------
    
    #------------------------

#---------------------------------------
    
def run_game_rounds(categories):
    """
    Implement a basic loop to run the game for 5 rounds.

    Parameters:
    - categories (list of str): A list of quiz categories.

    Returns: None
    """
    #------------------------
    for i in range(5):
        opt=input(f"Chose category for round {i+1}: ")  


    #------------------------
    
    #------------------------

#---------------------------------------
        
def validate_answer(player_answer, correct_answer):
    """
    Validate the player's answer (correct or incorrect).

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the player's answer is correct, False otherwise.
    """
    #------------------------
    print("The answer provided by the player: ",player_answer)
    print("The correct answer to the question is: ",correct_answer)
    if player_answer==correct_answer:
        return True
    else:
        return False

    #------------------------
    
    #------------------------

#---------------------------------------

def update_score(score, correct):
    """
    Implement a scoring system, where each correct answer awards points.

    Parameters:
    - score (int): The current score of the player.
    - correct (bool): Whether the player's answer was correct.

    Returns:
    - int: The updated score.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def next_round(round_number):
    """
    Increase the round number after each question.

    Parameters:
    - round_number (int): The current round number.

    Returns:
    - int: The next round number.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def check_game_over(incorrect_answers):
    """
    Implement a "game over" condition if the player makes 3 incorrect answers.

    Parameters:
    - incorrect_answers (int): The number of incorrect answers given by the player.

    Returns:
    - bool: True if the game should be over, False otherwise.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def restart_or_exit():
    """
    Restart the game or exit after the game is over.

    Parameters: None
    Returns: None
    """
    #------------------------
    while True:
        option=input("Do you want to play again? (yes/no): ")
        
        if option=='yes':
            return True
        elif option=='no':
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    #------------------------
    
    #------------------------

#---------------------------------------
