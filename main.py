import random
import hangman_art
import hangman_words
from hangman_art import logo
print(logo)
from hangman_art import skull
print(skull)



from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6






display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    
    if guess in display:
        print("you have already guessed this letter")

    
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    
    if guess not in chosen_word:
        
        print(f"you guessed {guess}, which is not in the chosen word, You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    
    print(f"{' '.join(display)}")

    
    if "_" not in display:
        end_of_game = True
        print("You win.")

    from hangman_art import stages
    print(stages[lives])
    
print(f'Pssst, the solution is {chosen_word}.') 