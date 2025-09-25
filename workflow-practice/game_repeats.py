import random
import sys

words = [
    "air",
    "boo",
    "cat",
    "cow",
    "dad",
    "dog",
    "elf",
    "fox",
    "hey",
    "mom",
    "oil",
    "pig",
    "rye",
]


def main():
    # guesses remaining (start with 6)
    guesses = 6
    # letters that have been revealed (all empty at first)
    revealed = ["_", "_", "_"]
    # keep track of letters already guessed
    guessed = set()

    # pick a word at random
    word = random.choice(words)
    # print(f"chosen word: {word}")

    # play the game until they win or run out of guesses
    while guesses > 0:
        print("\n-----------------------------")
        print("Word:", " ".join(revealed))
        print("Guessed:", ", ".join(sorted(guessed)))
        print("Guesses Remaining:", guesses)
        print()

        # each round, ask for a letter, then check if it is in the word
        letter = input("Pick a letter: ")

        if letter in guessed:
            # if the letter is already guessed, we tell them that
            # (and let them guess again with no penalty)
            print(f"\nAlready guessed {letter}!")
        else:
            # update guesses and which letters have been seen
            guessed.add(letter)
            guesses -= 1

            # check word one letter at a time
            for index, word_letter in enumerate(word):
                if letter == word_letter:
                    revealed[index] = letter

            # if revealed is only letters, the player has won!
            if "_" not in revealed:
                print(f"{word}! You Win!")
                exit()
    print(f"\nSorry! The word was {word}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        random.seed(sys.argv[1])
    main()
