import random
history = []
score = [
    
]
options = [
    "rock",
    "paper",
    "scissor"
]
computer_score = 0
user_score = 0
draws = 0

while True :
    available_options = [
        "Play game",
        "Check Score",
        "Clear Score",
        "History",
        "QUit"
    ] 
    count =0
    for task in available_options:
        count+=1
        print(count,task)
    option_selection = input("Enter the option number : ")
    if option_selection == "1":
        user_choice = input("Enter your choice : ").lower()
        computer_choice = random.choice(options)
        print(computer_choice)
        if user_choice == "rock" and computer_choice == "paper":
            print("Computer Win ")
            history.append("Computer Win")
            computer_score +=1
        elif user_choice == "rock" and computer_choice == "Scissor":
            print("User Win ")
            history.append("User Win")
            user_score +=1
        elif user_choice == "rock" and computer_choice == "rock":
            print("Draw ")
            history.append("Draw")
            draws +=1
        elif user_choice == "paper" and computer_choice == "rock":
            print("User Win ")
            history.append("User Win")
            user_score+=1
        elif user_choice == "paper" and computer_choice == "scissor":
            print("Computer Win ")
            history.append("Computer Win")
            computer_score +=1
        elif user_choice == "paper" and computer_choice == "paper":
            print("Draw ")
            history.append("Draw")
            draws+=1
        elif user_choice == "scissor" and computer_choice == "rock":
            print("Computer Win ")
            history.append("Computer Win")
            computer_choice +=1
        elif user_choice =="scissor" and computer_choice =="paper":
            print("User Win ")
            history.append("User Win")
            user_score +=1
        elif user_choice == "scissor" and computer_choice == "scissor":
            print("Draw ")
            history.append("Draw")
            draws+=1
        else:
            print("Invalid choice, Try again !! ")
    elif option_selection == "2":
        print(f"Computer Score = {computer_score}")
        print(f"User Score = {user_score}")
        print(f"Draws = {draws}")
    elif option_selection == "3":
        computer_score=0
        user_score=0
        draws=0
        print("Scores Cleared Successfully ! ")
    elif option_selection == "4":
        count2=0
        for task in history:
            count2+=1
            print(count2,task)
    elif option_selection == "5":
        print("Thanks for using this game ")
        break
    else :
        print("Invalid Choice, Try again")

        





import random
history = []
score = [
    
]
options = [
    "rock",
    "paper",
    "scissor"
]
computer_score = 0
user_score = 0
draws = 0

while True :
    available_options = [
        "Play game",
        "Check Score",
        "Clear Score",
        "History",
        "QUit"
    ] 
    count =0
    for task in available_options:
        count+=1
        print(count,task)
    option_selection = input("Enter the option number : ")
    if option_selection == "1":
        user_choice = input("Enter your choice :").lower()
        computer_choice = random.choice(options)
        print(computer_choice)
        if user_choice == "rock" and computer_choice == "paper":
            print("Computer Win ")
            history.append("Computer Win")
            computer_score +=1
        elif user_choice == "rock" and computer_choice == "scissor":
            print("User Win ")
            history.append("User Win")
            user_score +=1
        elif user_choice == "rock" and computer_choice == "rock":
            print("Draw ")
            history.append("Draw")
            draws +=1
        elif user_choice == "paper" and computer_choice == "rock":
            print("User Win ")
            history.append("User Win")
            user_score+=1
        elif user_choice == "paper" and computer_choice == "scissor":
            print("Computer Win ")
            history.append("Computer Win")
            computer_score +=1
        elif user_choice == "paper" and computer_choice == "paper":
            print("Draw ")
            history.append("Draw")
            draws+=1
        elif user_choice == "scissor" and computer_choice == "rock":
            print("Computer Win ")
            history.append("Computer Win")
            computer_score +=1
        elif user_choice =="scissor" and computer_choice =="paper":
            print("User Win ")
            history.append("User Win")
            user_score +=1
        elif user_choice == "scissor" and computer_choice == "scissor":
            print("Draw ")
            history.append("Draw")
            draws+=1
        else:
            print("Invalid choice, Try again !! ")
    elif option_selection == "2":
        print(f"Computer Score = {computer_score}")
        print(f"User Score = {user_score}")
        print(f"Draws = {draws}")
    elif option_selection == "3":
        computer_score=0
        user_score=0
        draws=0
        print("Scores Cleared Successfully ! ")
    elif option_selection == "4":
        count2=0
        for task in history:
            count2+=1
            print(count2,task)
    elif option_selection == "5":
        print("Thanks for using this game ")
        break
    else :
        print("Invalid Choice, Try again")

        





