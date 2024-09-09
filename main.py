from library import word_library
import random

def random_word():

    max = len(word_library) - 1
    min = 0

    random_num = random.randint(min, max) 
    wordle = []

    for letter in word_library[random_num]:
         wordle.append(letter)

    return wordle

def guess():
        
        guess = str(input("guess a letter: "))
        assert len(guess) == 5, ("Please guess a 5 letter word, or u lose motherfucker")

        letters = []
        for letter in guess:
            letters.append(letter)

        return letters


def matching(lst):

    win_word = lst
    guessed_word = guess()
    print(win_word)

        #(['p', 'e', 'a', 'c', 'e'], ['j', 'a', 'm', 'e', 's']) #output

    for i in win_word:
         for j in guessed_word:
              if j == i:
                print("v nice")

    pass


def main():
    guesses = 0
    matching(random_word())

    while guesses < 2:
        guesses += 1

main()
