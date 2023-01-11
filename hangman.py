import random

# The list of words to choose from
word_list = ["python", "java", "javascript", "c++", "c#", "swift"]

# The word that the player is trying to guess
word = random.choice(word_list)

# The number of incorrect guesses the player has made
incorrect_guesses = 0

# The letters that the player has guessed so far
guessed_letters = []

# The number of allowed incorrect guesses
MAX_INCORRECT_GUESSES = 6

# The letters that make up the word
word_letters = set(word)

# The game loop
while len(word_letters) > 0 and incorrect_guesses < MAX_INCORRECT_GUESSES:
    print("The word: " + " ".join(letter if letter in guessed_letters else "_" for letter in word))
    print("Incorrect guesses: " + str(incorrect_guesses))
    print("Guessed letters: " + " ".join(guessed_letters))
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word_letters:
        word_letters.remove(guess)
        guessed_letters.append(guess)
    else:
        incorrect_guesses += 1
        guessed_letters.append(guess)
    print()

if len(word_letters) == 0:
    print("Congratulations, you won! The word was " + word)
else:
    print("Sorry, you lost. The word was " + word)
