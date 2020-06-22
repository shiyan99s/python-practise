from random_word_generator import random_word_generator


def play_game():
    # It will contain main logic of my game

    # This will store randomly selected word

    selected_word = random_word_generator()

    # this will store current word state

    current_word_state = ""

    for i in selected_word:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            current_word_state += i
        else:
            current_word_state += "_ "

    


if __name__ == "__main__":
    play_game()



