import random


# creeat the display for the world, make lives make a variable for the wrong and right answer 

def play_hangman():
    WORDS = ["python", "java", "kotlin", "javascript"]
    secret = random.choice(WORDS)
    display = ["_"] * len(secret)
    lives = len(secret) + 5
    correct_guesses = set()
    wrong_guesses = set()
    print(f"Your word has {len(secret)} letters: {' '.join(display)}")

    while lives > 0 and "_" in display:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue
        if guess in correct_guesses | wrong_guesses:
            print("You already tried that letter.")
            continue

        if guess in secret:
            correct_guesses.add(guess)
            for i, ch in enumerate(secret):
                if ch == guess:
                    display[i] = guess
        else:
            wrong_guesses.add(guess)
            lives -= 1
            print(f"Wrong! Lives left: {lives}")

        print("Word: " + " ".join(display))
        print("Wrong guesses:", ", ".join(sorted(wrong_guesses)))

    if "_" not in display:
        print("🎉 You won! The word was:", secret)
    else:
        print("😢 You lost. The word was:", secret)

def main():
    play_hangman()
    while input("Play again? (y/n): ").lower().startswith("y"):
        play_hangman()

if __name__ == "__main__":
    main()