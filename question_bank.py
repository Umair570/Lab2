#--------------------------------------
#  Question Bank
#  Muhammad Talha Zulfiqar
#  Roll No.(271046276)
#--------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("How many hearts does Octopus have?", "Three Hearts"),
        ("What can exist in the three states at a time?", "Water")
        ],
    "Maths": [
        ("What is obtained by adding two numbers and dividing them with two?" , "Average"),
        ("How can we obtain the diameter of Circle?", "Radius * 2 ")
        ],
         
    "Geography" : [
        ("What are vertical imaginary lines on map are called?" ,"Meridians of Longitude"),
        ("The most outer layer of rocks is called?", "Crust")
        ],
    
    "Economics": [
        ("A good used for further production is called?", "Capital Good")
        ("What is a good called which is used for more than 3 years?", "Durable Good")
        ("The satisfaction you get by consuming something is called?", "Utility")
        ],
    
}


hints = {
    "Science": [
        ("Made up of Hydrojen and Oxygen")
        ("More than one")
        ("Essential for life")
    "Maths": 
        ("Middle Value")
        ("Involves Radius")
    "Geography":   
        ("Based on Diameter")
        ("Easily Accessible")
    "Economics" : 
        ("Bussiness Sector")
        ("Long Life")
        ("Luxury")
        
    ],
    
    # Repeat for other categories as needed.
}

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    if not category:
            return "No questions available."

    random_question = random.choice(category)
    return random_question

    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    print("Incorrect. The correct answer is:", correct_answer)

player_answer = input("Pakistan")
correct_answer = "Lahore"
if validate_answer(player_answer, correct_answer):
    print("Correct!")
else:
    display_correct_answer(correct_answer) 
    #------------------------
    
    #------------------------

#--------------------------------------




