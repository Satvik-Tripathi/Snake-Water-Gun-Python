"""
Snake, Water, Gun Game (Rock, Paper, Scissors)

A simple console-based game where the user plays "Snake, Water, Gun" 
against a random computer opponent. The game includes input validation, 
error handling, and a "play again" loop.
"""

import random
import time as t

# --- Game Setup ---

# Define the mapping of numbers to game choices
choice_map = {1: 'Snake', 2: 'Water', 3: 'Gun'}

# Print the game rules once at the start
print('''Rules of the game are
      1. For Snake enter - 1🐍
      2. For Water enter - 2💧
      3. For Gun enter   - 3🔫
      Lets play!!
      All the best👍''')

# --- Main Game Loop ---

while True: 
    # Get computer's choice for this round
    computer_choice = random.randint(1, 3)

    # --- User Input and Validation ---
    try:
        # Get user's choice and convert to an integer
        user_choice = int(input('\nPlayer play your move :  '))
        
        # Validate if the choice is one of the allowed options
        if user_choice not in [1, 2, 3]:
            print('Invalid Input: Please choose 1, 2, or 3.')
            continue # Restart the loop to ask for input again
            
    except ValueError:
        # Handle cases where user enters text instead of a number
        print('Invalid Input: Please enter a number.')
        continue # Restart the loop

    # --- Process the Round ---
    
    # Reveal the choices
    t.sleep(1) # Add a small delay for suspense
    print(f'''You chose : {choice_map[user_choice]} and Computer chose : {choice_map[computer_choice]}''')

    # --- Determine the Winner ---
    
    # 1. Check for a tie
    if user_choice == computer_choice:
        print('Tied')
    
    # 2. Check for all user "Win" conditions
    elif (user_choice == 1 and computer_choice == 2) or \
         (user_choice == 2 and computer_choice == 3) or \
         (user_choice == 3 and computer_choice == 1):
        print('Congratulations, You Won!!')
        
    # 3. If it's not a tie or a win, it must be a loss
    else:
        print('You lost, Better luck Next time!!')
            
    # --- Play Again Logic ---
    
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    
    # End the game if the user types anything other than "y"
    if play_again != 'y':
        print("\nThanks for playing! Goodbye.")
        break # Exit the 'while True' loop