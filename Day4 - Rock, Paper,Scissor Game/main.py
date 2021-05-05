import random
random.seed()

# Rock


def printRock():
    print("""
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  """)

# Paper


def printPaper():
    print("""
       _______
  ---'    ____)____
             ______)
            _______)
           _______)
  ---.__________)
  """)

# Scissors


def printScissor():
    print("""
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
  """)

# print the ascii image based on user and computer choice


def printChoices(user_choice, computer_choice):
    print("User chose: ")
    if(user_choice == 'rock'):
        printRock()
    elif(user_choice == 'paper'):
        printPaper()
    elif(user_choice == 'scissors'):
        printScissor()
    else:
        print("Unknown user choice")
    print("Computer chose: ")
    if(computer_choice == 'rock'):
        printRock()
    elif(computer_choice == 'paper'):
        printPaper()
    elif(computer_choice == 'scissors'):
        printScissor()
    else:
        print("Unknown user choice")


game_choices = ['rock', 'paper', 'scissors']
quit = False

# this dictionary contains the rules of the game, the first indicates user and second the pc
lostGames = {('rock', 'paper'): True, ('rock', 'scissors'): False, ('rock', 'rock'): 'draw', ('paper', 'paper'): 'draw',
             ('paper', 'rock'): False, ('paper', 'scissors'): True, ('scissors', 'paper'): False, ('scissors', 'rock'): True,
             ('scissors', 'scissors'): 'draw'}


if __name__ == '__main__':
    while(quit != True):
        print("Welcome to Rock, Paper , Scissors game")
        print("="*50)
        user_choice = input(
            "Please enter your choice (rock / paper / scissors) or 'q' to quit: ")
        if(user_choice == 'q'):
            quit = True
            break
        elif(user_choice == 'rock' or user_choice == 'paper' or user_choice == 'scissors'):
            computer_choice = random.choice(game_choices)
            printChoices(user_choice=user_choice,
                         computer_choice=computer_choice)
            gameLost = lostGames[(user_choice, computer_choice)]
            if(gameLost == 'draw'):
                print("The game is a draw")
            elif(gameLost):
                print("You lose!")
            else:
                print("You Won!")
            #quit = doQuit()
        else:
            print("Unknown choice. Try again")
