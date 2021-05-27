import random
heading = '''


 _   _    __    _  _  ___  __  __    __    _  _
( )_( )  /__\  ( \( )/ __)(  \/  )  /__\  ( \( )
 ) _ (  /(__)\  )  (( (_-. )    (  /(__)\  )  (
(_) (_)(__)(__)(_)\_)\___/(_/\/\_)(__)(__)(_)\_)

'''
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
    print(heading)
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
        self.mistakes_made = 0
        #self.guess_step <= len(self.guess_word) and
        while(self.mistakes_made <=6):
            print(hangman_progress[self.mistakes_made])
            print(self.getCurrentStatus())
            user_guess = input('Please enter your guess letter: ').upper()
            possible_positions = self.checkLetter(user_guess)
            self.updateCurrentGuess(user_guess,possible_positions)
            #we need to update the hangman print progress only if the user enters a wrong letter
            if not possible_positions:
                self.mistakes_made += 1

            self.guess_step +=1 # we update it here so the word is printed right when user wins
            #leverage the fact that if there are no underlines the word is filled correctly
            # we stop the game after six steps with wrong words
            if(self.mistakes_made == 6 and self.current_guess.count('_') != 0):
                print("Game Over!")
            elif(self.current_guess.count('_') == 0):
                print(self.getCurrentStatus())
                print("Congratulations!! You WON!!")
                break


    def addWord(self,word):

        self.word_list.append(word)
        print("{} added".format(word))
        print("Current list: {}".format(self.word_list))

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
        elif(menu_input == 2):
            word = input("Enter the word to be added: ")
            word = word.upper()
            game.addWord(word)
        else:
            pass
