import random
def get_choices():
    player_choice = input("Enter your choice(Rock,Paper,Scissors): ")
    options = ["Rock","Paper","Scissors"]
    computer_choice = random.choice(options)
    choices = {"player":player_choice,"computer":computer_choice}
    return choices

def check_win(player,computer):
    print(f"You chose {player},computer chose {computer}")
    if player==computer:
        return "It's a Tie"
    elif player =="Rock":

            if computer=="Scissors" :
                return "Rock smashes Scissors.You Win!!"
            else:
                return "Paper covers rock.You Lose."
    elif player=="Paper":
            if computer=="Rock" :
                return "Paper covers rock.You Win!!"
            else:
                return "Scissors cut paper.You Lose."
    elif player=="Scissors":
            if computer=="Paper" :
                return "Scissors cut paper.You Win!!"
            else:
                return "Rock smashes Scissors.You Lose."

choices= get_choices() 
result = check_win(choices["player"],choices["computer"])
print(result)