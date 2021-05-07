import random

step_0 = '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
step_1 = '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
'''
step_2 = '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
'''
step_3 = '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
'''
step_4 ='''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
'''

step_5 = '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
'''

step_6 = '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
hangman_progress = [step_0,step_1,step_2,step_3,step_4,step_5,step_6]

class Hangman:

    menu = '''
    1. Play
    2. Add new word
    3. Remove word
    4. Quit

    '''

    def __init__(self,words=None):
        if(words != None):
            self.word_list = words
            self.guess_word = 'BOAT'
            self.current_guess =''
            self.guess_step = 0 # as user makes guess step goes up. The user gets 7 stepsin total


    def checkLetter(self,user_input):
        """
        checkLetter checks if a user input letter is present in the word to be guessed.
        If the letter is present, it returns a list with positions of that particulat letter,
        otherwise it returns an empty list.
        """
        #the positions of user input letter in the guess_word if it exits
        letter_positions = []
        position = 0

        for letter in self.guess_word:
            if(letter == user_input):
                letter_positions.append(position)
            position += 1
        return letter_positions

    def updateCurrentGuess(self,letter, letter_positions):
        """
        Updates the current guess based on the letter and the index of appearance of that letter in the guess word
        """
        temp_list = list(self.current_guess)
        for position in letter_positions:
            temp_list[position] = letter
        self.current_guess = ''.join(temp_list)

    def getCurrentStatus(self):
        return self.current_guess

    def playGame(self):
        self.guess_word = random.choice(self.word_list)
        self.current_guess = '_'*len(self.guess_word)
        self.guess_step = 0
        while(self.guess_step <= 6):
            print(hangman_progress[self.guess_step])
            print(self.getCurrentStatus())
            user_guess = input('Please enter your guess letter: ').upper()
            possible_positions = self.checkLetter(user_guess)
            self.updateCurrentGuess(user_guess,possible_positions)
            self.guess_step += 1
            if(self.guess_step == 6):
                print("Game Over!")

if __name__ == '__main__':
    game = Hangman(['BOAT','APPLE'])
    quit = False
    while not quit:
        print(game.menu)
        menu_input = int(input('Enter command [1-4]:'))
        if(menu_input == 1):
            game.playGame()
        elif(menu_input == 4):
            quit = True
        else:
            pass
