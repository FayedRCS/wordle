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

def guess(wordled, incorrect):
        
        #Making sure it's a 5 letter word
        valid_guess = False
        while valid_guess == False:
            guess = str(input("Guess a 5 letter word: "))
            if len(guess) == 5:
                 valid_guess = True
                 break
            print("Invalid answer dummy")
            
        #Making the guess into a list we can compare to
    
        letters = []
        for letter in guess:
            letters.append(letter)

        right_in_wordle = []

        for i in range(len(letters)):
            compare = letters[i]
            if compare == wordled[i]:
                right_in_wordle.append(compare.upper())
                letters[i] = None # mark this letter as used
            elif compare in wordled:
                right_in_wordle.append(compare)
            else:
                right_in_wordle.append("x")
                incorrect.add(compare)

    
        return right_in_wordle, "".join(wordled), guess.lower()

def main():

    guesses = 0
    wordle = random_word()
    max_guesses = 6
    incorrect = set() #making a set to avoid duplicates easily

    answer = []
    for i in wordle:
        answer.append(i)

    print(wordle)

    while guesses < max_guesses:
        print(f"Guess #{guesses + 1} of {max_guesses}")
        right_in_wordle, wordle, user_guess = guess(wordle, incorrect)

        print(f"incorrect letters: {incorrect}")
        print(right_in_wordle)

        if user_guess.lower() == wordle.lower():
            print(f"You got it, king! The word was {wordle}")
            return
        
        guesses += 1
        
main()
