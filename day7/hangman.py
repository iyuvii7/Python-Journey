import random
from words import word_list

# Hangman Game

# Choose a random word
chosen_word = random.choice(word_list)

# Uncomment for testing
print(f"Chosen word: {chosen_word}")

# Number of lives
lives = 6

# Placeholder
display = ["_"] * len(chosen_word)

# Store guessed letters
guessed_letters = []

game_over = False

while not game_over:
    print("\n" + "".join(display))
    print(f"Lives left: {lives}")

    user_guess = input("Guess a letter: ").lower()

    # Validate input
    if len(user_guess) != 1 or not user_guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check repeated guess
    if user_guess in guessed_letters:
        print(f"You've already guessed '{user_guess}'.")
        continue

    guessed_letters.append(user_guess)

    # Correct guess
    if user_guess in chosen_word:
        print(f"Good job! '{user_guess}' is in the word.")

        for position in range(len(chosen_word)):
            if chosen_word[position] == user_guess:
                display[position] = user_guess

        if "_" not in display:
            print("\n" + "".join(display))
            print("🎉 Congratulations! You won!")
            game_over = True

    # Wrong guess
    else:
        lives -= 1
        print(f"'{user_guess}' is not in the word.")
        print(f"You lost a life. Lives remaining: {lives}")

        if lives == 0:
            print("\n💀 Game Over!")
            print(f"The word was: {chosen_word}")
            game_over = True