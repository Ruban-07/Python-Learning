# Lesson 17 - Building a Guessing Game

secret_name = "Ruban"
guess_name = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess_name != secret_name and not(out_of_guesses):
    if guess_count < guess_limit:
        guess_name = input("Enter your guess name: ")
        guess_count +=1
    else:
        out_of_guesses = True
        
if out_of_guesses:
    print("Oops, you Lost the game!")
else:
    print("Wow, you won the game!")