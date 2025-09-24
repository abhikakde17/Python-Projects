

import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move Rock, Paper or Scissor: ")
computer_choice = random.choice(item_list)

print(f"Your Choice: {user_choice}")
print(f"Computer Choice: {computer_choice}")


if user_choice == computer_choice:
    print("--- MATCH TIE !!! ---")
    
elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("Paper Covers Rock.") 
        print("--- COMPUTER WIN !!! ---")
        
    else:
        print("Rock Smashes Scissor.")
        print("--- YOU WIN !!! ---")
        
elif user_choice == "Paper":
    if computer_choice == "Rock":
        print("Paper Covers Rock.")
        print("--- YOU WIN !!! ---")
    
    else:
        print("Scissor Cuts Paper.")
        print("--- COMPUTER WIN !!! ---")
    
elif user_choice == "Scissor":
    if computer_choice == "Rock":
        print("Rock Smashes Scissor.")
        print("--- COMPUTER WIN !!!")
    
    else:
        print("Scissor Cuts Paper.")
        print("--- YOU WIN !!! ---")