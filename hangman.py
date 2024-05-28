from random import choice
import string


MAX_INCORRECT_GUESSES = 6

def select_word():
    # how to read a text file in the same dir
    with open("words.txt", mode="r") as words:
        # create a list from text file 
        word_list = words.readlines()
        # pick a random word from list and remove any blank spaces.
        return choice(word_list).strip()
    
""" Now, you need a way to get the player’s guesses at the command line. After all, 
a game isn’t much of a game if there isn’t some way for the player to influence the outcome.

In your hangman game, you have to get the player’s input and make sure that it’s valid. 
Remember when you created your list of words? All the words were in lowercase, 
so you should turn the player’s guesses into lowercase letters as well.

Additionally, the player shouldn’t be able to guess the same letter twice. 
It’d also be good to avoid numbers, special characters, and complete words as well.

So you need a two-part solution. The first part will gather the player’s input, and the second part will validate it. 
You can get the player’s input for the command line using the built-in input() function: """

def get_player_input(guessed_letters):
    # why are we using a while loop here? while what's true? game state?
    while True:
        # take input and make lower case.
        player_input = input("Guess a letter: ").lower()
        if validate_input(player_input, guessed_letters):
            return player_input
        

# check player input is only one letter, is a lowercase letter, and not already guessed. 
def validate_input(player_input, guessed_letters):
    return(
        len(player_input) == 1
        and player_input in string.ascii_lowercase
        and player_input not in guessed_letters
    )

# add guess to other guessed letters, tutorial suggests using a set to store guesses.
def join_guessed_letters(guessed_letters):
    return " ".join(sorted(guessed_letters))

def build_guessed_word(target_word, guessed_letters):
    current_letters = []
    for letter in target_word:
        if letter in guessed_letters:
            current_letters.append(letter)
        else:
            current_letters.append("_")
    return " ".join(current_letters)


# copied this one, as would be long otherwise, using rare strings, r""" """
# holding the different stages of hangman in an array/list.
def draw_hanged_man(wrong_guesses):
    hanged_man = [
        r"""
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
  |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
    ]

    print(hanged_man[wrong_guesses])

def game_over(wrong_guesses, target_word, guessed_letters):
    if wrong_guesses == MAX_INCORRECT_GUESSES:
        return True
    # don't quite get this syntax, both are sets, <= checks if every item in the left set is a member in the right
    if set(target_word) <= guessed_letters:
        return True
    return False


# remember this is funky python business, checks if the file is one being executed or if code is being executed from 
# another file or module in which case it's name won't be main.
if __name__ == "__main__":
    # also cool that you can setup in this if statement otherwise would have to do in the top of file.
    # initial setup
    target_word = select_word()
    guessed_letters = set()
    guessed_word = build_guessed_word(target_word, guessed_letters)
    wrong_guesses = 0
    print("Welome to hangman")

    # game loop
    while not game_over(wrong_guesses, target_word, guessed_letters):
        draw_hanged_man(wrong_guesses)
        print(f"Your word is: {guessed_word}")
        print("Current guessed letters: "
              f"{join_guessed_letters(guessed_letters)}\n")
        
        player_guess = get_player_input(guessed_letters)
        if player_guess in target_word:
            print("Great guess!")
        else:
            print("Sorry, it's not there.")
            wrong_guesses += 1

        guessed_letters.add(player_guess)
        guessed_word = build_guessed_word(target_word, guessed_letters)

    draw_hanged_man(wrong_guesses)
    if wrong_guesses == MAX_INCORRECT_GUESSES:
        print("Sorry, you lost!")
    else:
        print("Congrats! You did it!")
    print(f"Your word was: {target_word}")
