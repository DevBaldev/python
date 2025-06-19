#!/usr/bin/env python
"""Simple command-line Hangman game."""

import random
import sys


def pick_word() -> tuple[str, str]:
    """Return a random animal word and its mask (underscores for each letter)."""
    word = random.choice(
        "ant baboon badger bat bear beaver camel cat clam cobra cougar "
        "coyote crow deer dog donkey duck eagle ferret fox frog goat "
        "goose hawk lion lizard llama mole monkey moose mouse mule newt "
        "otter owl panda parrot pigeon python rabbit ram rat raven "
        "rhino salmon seal shark sheep skunk sloth snake spider "
        "stork swan tiger toad trout turkey turtle weasel whale wolf "
        "wombat zebra".split())
    return word, "_" * len(word)


def hangman_stages() -> list[str]:
    """ASCII art for hangman stages (one per wrong guess)."""
    return [
        "\n  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
        "\n  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "\n  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "\n  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
        "\n  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
        "\n  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
        "\n  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="
    ]


def prompt_letter(used: set[str]) -> str:
    """Prompt the user for a new letter. Handles Ctrl+C/Ctrl+D to exit gracefully."""
    try:
        while True:
            try:
                l = input("Guess letter: ").lower()
            except EOFError:
                print("\nExiting Hangman (Ctrl+D received).")
                sys.exit(0)
            if len(l) == 1 and l.isalpha() and l not in used:
                return l
            print("Enter a single new alphabetic letter.")
    except KeyboardInterrupt:
        print("\nExiting Hangman (Ctrl+C received).")
        sys.exit(0)


def update_hint(word: str, hint: str, guess: str) -> str:
    """Reveal guessed letters in the masked word."""
    return "".join(g if g == guess else h for g, h in zip(word, hint))


def play():
    """Main gameplay loop for Hangman."""
    word, hint = pick_word()
    stages = hangman_stages()
    used = set()
    wrong = 0
    print("Welcome to Hangman! (Press Ctrl+C or Ctrl+D to exit)")
    try:
        while wrong < len(stages) - 1 and hint != word:
            print(f"\nWord: {' '.join(hint)}")
            print(f"Guessed: {' '.join(sorted(used)) if used else 'None'}")
            guess = prompt_letter(used)
            used.add(guess)
            if guess in word:
                hint = update_hint(word, hint, guess)
            else:
                print(stages[wrong + 1])
                wrong += 1
        print(f"\n{'You win!' if hint == word else f'You lose! Word: {word}'}")
    except KeyboardInterrupt:
        print("\nExiting Hangman (Ctrl+C received).")
        sys.exit(0)


if __name__ == "__main__":
    play()
