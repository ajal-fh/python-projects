""" Python password generator."""
import random


def getAlphaList(n):
    """
    Creates a list of random alphabets

    Parameters:
    n (int): number of aphabets that are to be randomly generated

    Returns:
    list: Random alphabets as list
    """
    alphas = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphas_list = [item for item in alphas]
    if (n > len(alphas_list)):
        alphas_list = alphas_list * n
    random.shuffle(alphas_list)
    return alphas_list[:n]


def getSymbolList(n):
    """
    Create symbols based on user requirement

    Parameters:
    n (int): number of symbols required in the generated password

    Returns:
    list: Random symbol list
    """
    symbols = ['&','%','!','$','^','(',')','@','#']
    if (n > len(symbols)):
        symbols = symbols * n
    random.shuffle(symbols)
    return symbols[:n]


def getNumberList(n):
    """
    Create numbers for the password that is to be generated

    Parameters:
    n (int): number of numbers in the generated password

    Returns:
    list: Random numbers list for the generated password
    """
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    #make sure the list have enough numbers for creation of random numbers
    if (n > len(numbers)):
        numbers = numbers * n
    #shuffle the numbers to obtain randomized numbers
    random.shuffle(numbers)
    return numbers[:n]

def main():
    print("Welcome to the PyPassword Generator")
    letters_in_pass = int(input("How many letters would you like in your password\n"))
    symbols_in_pass = int(input("How many symbols would you like?\n"))
    numbers_in_pass = int(input("How many numbers would you like?\n"))
    generated_pass = getNumberList(numbers_in_pass) + getSymbolList(symbols_in_pass) + getAlphaList(letters_in_pass)
    random.shuffle(generated_pass)
    #create a string out of an iterable using the join() method
    pass_as_str = ''.join(generated_pass)
    print("Here is your password: {}".format(pass_as_str))
if __name__ == '__main__':
    main()


