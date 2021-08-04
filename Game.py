import random

def fetch_word():
    word = random.choice(open("words_50000.txt").read().split())
    return word.upper()

def game_play(word):
    word_completion = "_"*len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    chances = 6
    print("Lets Begin!")
    print(display_hangman(chances))
    print(word_completion)
    print("\n")
    while not guessed and chances > 0:
        guess = input("Please guess a letter or word:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                chances -= 1
                guessed_letters.append(guess)
            else:
                print("correct guess,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(
                    word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                chances -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("Not a valid guess.")
        print(display_hangman(chances))
        print(word_completion)
        print("\n")
    if guessed:
        print(" 🎉You guessed the word! 🎉")
    else:
        print("sorry you ran out of time. The word was "+word)


def display_hangman(chances):
    stages = [
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]


def main():
    word = fetch_word()
    print("Hint : word length is "+str(len(word)))
    game_play(word)
    while input("Play again? (Y/N)").upper() == "Y":
        word = fetch_word()
        game_play(word)


if __name__ == "__main__":
    main()
