# This files generates a sequence of numbers and the player must guess the next number. 
# I did not write this program, chatGPT did. 

import itertools

# Define a sequence of numbers
sequence = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

# Create a sequence of triples of consecutive numbers
triples = list(zip(sequence, sequence[1:], sequence[2:]))

# Loop through the triples, prompting the user to find the next number in the sequence
for (a, b, c) in triples:
    print("Sequence:", a,b,c)
    guess = int(input("What is the next number in the sequence? : "))
    if guess == c + (c-b):
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer was {c + (c-b)} ")
