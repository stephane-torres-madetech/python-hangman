# Hangman Tutorial Reflections 

Following the hangman tutorial found [here](https://realpython.com/python-hangman/#prerequisites), I was able to create a little command line interface game of hangman; reading target words to guess from stored in a .txt file in the same directory, using raw strings to represent different stages of the hangman, and sets to make comparisons between letters present in the target word and those already guessed.

A few things that stuck out to me while going through this tutorial were:
1. How to read other files, did this a bit in the Hard to Heat Homes project, would be interesting to expand on this and maybe try to work with a CSV and what extra steps would be needed to extract the data needed. 
2. Use of a while loop in get_player_input function, and in general while loops over if statements.
3. set() <= set() syntax to check all members/elements in a set are the same, easier than looping through two different lists to check elements.
4. how powerful ``` if __name__ == "__main__": ``` can be, defined logic above and then intialising and defining flow there after.
while going through the tutorial I was wondering when and where the guessed_letters variable was going to be defined as I was passing it around a lot and wasn't quite sure what it was and how it was going to work.

## Playing the game

Clone repo
cd into directory you've cloned into

```
python -m venv .
source bin/activate
python3 hangman.py
```

