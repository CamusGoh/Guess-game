# This will be a guessing game
print("Let's play 3 rounds of guessing game\nDifficulty is in ascending order")
print("You only have 3 guesses for each round")
print("")

# ---------------------------------------------------------------------------------------------------------------
print("Round 1")
print("Clue: It is 3 letter word and a type of vehicle")

secret_word = "car"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True


if out_of_guesses:
    print("Out of guesses, you lose")
else:
    print("You win round 1")

# ---------------------------------------------------------------------------------------------------------------

print("")
print("Round 2")
print("Clue: It is a 5 letter word and a type of drink")

secret_word2 = "coffee"
guess2 = ""
guess_count2 = 0
guess_limit2 = 3
out_of_guesses2 = False

while guess2 != secret_word2 and not(out_of_guesses2):
    if guess_count2 < guess_limit2:
        guess2 = input("Enter guess: ")
        guess_count2 += 1
    else:
        out_of_guesses2 = True


if out_of_guesses2:
    print("Out of guesses, you lose")
else:
    print("You win round 2")

# ---------------------------------------------------------------------------------------------------------------

print("")
print("Round 3")
print("Clue: It is a 7 letter word and a tall mammal")

secret_word3 = "giraffe"
guess3 = ""
guess_count3 = 0
guess_limit3 = 3
out_of_guesses3 = False

while guess3 != secret_word3 and not(out_of_guesses3):
    if guess_count3 < guess_limit3:
        guess3 = input("Enter guess: ")
        guess_count3 += 1
    else:
        out_of_guesses3 = True


if out_of_guesses3:
    print("Out of guesses, you lose")
else:
    print("You win round 3")

