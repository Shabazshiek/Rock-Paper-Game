import random

def  get_user_choice():
    while True:
        user_choices = input("Choose Your move (stone,paper,scissor): ")
        if user_choices in["stone","paper","scissor"]:
            return user_choices
        else:
            print("Invalid choice please enter a valid choice")

# get_user_choice() This is an comment line
    
def get_computer_choice():
    choices=["stone","paper","scissor"]
    return random.choice(choices)

get_computer_choice()

def determine_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return "Its a Tie!!!"
    elif (user_choice == "stone" and computer_choice == "scissor") or \
     (user_choice == "paper" and computer_choice == "stone") or \
     (user_choice == "scissor" and computer_choice == "paper"):
        return "You Win!!!"

    else:
        return "Computer Win!!!"

def play_game():
    while True:
        user_choice=get_user_choice()
        computer_choice=get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"computer chose: {computer_choice}")
        result=determine_winner(user_choice,computer_choice)
        print(result)

        play_again=input("Do you want to play again?(yes/no):").lower()
        if play_again !="yes":
            break

if __name__=="__main__":
    play_game()


    