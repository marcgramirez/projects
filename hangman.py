import random
players_input = []
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

##play_input = players_input(input("what do you want your word to be ?"))

display = []
for _ in range(word_length):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("can you guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"current position: {position} \n Current letter: {letter}\n Guess letter: {guess}")
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game = True
        print("you win")


## guessing lives left 

lives = 6 

if guess not in chosen_word:
    lives -= 1
    if lives == 0:
        end_of_game = True