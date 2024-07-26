import random
from hangman_words import word_list
from hangman_art import stages 
from hangman_art import logo

print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# print(f'Sssshhh!!, Answer is {chosen_word}')

display = []
for _ in range(word_length):
    display += "_"

print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f'Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}')
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, thats not in the word. you lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose...........")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win!!!")

print(stages[lives])