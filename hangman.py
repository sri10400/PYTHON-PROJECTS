# Python Program to illustrate
# Hangman Game
import random
from collections import Counter

someWords = "Himalayas Ganga Thar Brahmaputra Harappa Chola Mughal Shivaji Akbar Lakshmibai Ashoka"

someWords = someWords.split(' ')
# randomly choose a secret word from our "someWords" LIST.
w = random.choice(someWords)
word=w.lower()
if __name__ == '__main__':
    print('Guess the word! HINT: word is related to india')

    for i in word:
        # For printing the empty spaces for letters of the word
        print('_', end=' ')
    print()

    playing = True
    # List for storing the letters guessed by the player
    letterGuessed = ''
    chances = len(word) + 7
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0:  # Flag is updated when the word is correctly guessed
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
                guess=guess.lower()
            except:
                print('Enter only a letter!')
                continue

            # Validation of the guess
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            # If letter is guessed correctly
            if guess in word:
                # k stores the number of times the guessed letter occurs in the word
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess  # The guessed letter is added as many times as it occurs

            # Print the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1
                # If user has guessed all the letters
                # Once the correct word is guessed fully,
                elif (Counter(letterGuessed) == Counter(word)):
                    # the game ends, even if chances remain
                    print("The word is: ", end=' ')
                    print(w)
                    flag = 1
                    print('Congratulations, You won!')
                    break  # To break out of the for loop
                    break  # To break out of the while loop
                else:
                    print('_', end=' ')

        # If user has used all of his chances
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(w))

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()