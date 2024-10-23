import random as rnd
import hangman_words as hw

lives = 6
print(hw.logo)
chosen_word = rnd.choice(hw.word_list).upper()
placeholder = "_" * len(chosen_word)

print(" ".join(placeholder))

game_over = False
correct_letters = []

while not game_over:
    print(f"**************{lives}/6 LIVES LEFT**************")
    guess = input("Guess a letter: ").upper()

    if guess in correct_letters:
        print(f"You have already guessed {guess}")
    else:
        correct_letters.append(guess)
    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter + " "
        else:
            display += "_"

    print(display.strip())
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, which is not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"********************IT WAS {chosen_word}! YOU LOSE********************")
    if "_" not in display:
        game_over = True
        print("************************You Win!************************")
    print(hw.stages[lives])
