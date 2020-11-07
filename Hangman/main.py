import random
from hangman_word_list import hangman_word_list
# Hangman

game_is_running = True
display_game_name = True
hang_level = 6
dash_word = ''
entered_word = []


def display_game_name():
    print('H', end='')
    print('a', end='')
    print('n', end='')
    print('g', end='')
    print('M', end='')
    print('a', end='')
    print('n :', end=' ')


def display_hangman():
    print('')
    print('__________')
    if hang_level > 0:
        print(' |/     |')
    else:
        print(' |/')
    if hang_level > 0:
        print(' |      O')
    else:
        print(' |')
    if hang_level > 1:
        print(' |      |')
    else:
        print(' |')
    if hang_level > 2:
        print(' |     /.\\')
    else:
        print(' | ')
    if hang_level > 3:
        print(' |      |')
    else:
        print(' |')
    if hang_level > 4:
        print(' |     / \\')
    else:
        print(' |')
    print(' |')
    print('/|\\_________')
    if display_game_name:
        display_game_name()


def choose_word():
    return random.choice(hangman_word_list)


def new_word(word):
    global dash_word
    word_length = len(word)
    for i in range(word_length):
        if i % 2 == 1:
            dash_word += word[i]
        else:
            dash_word += '-'
    return dash_word


def guess_word(word):
    global hang_level, entered_word, game_is_running, dash_word
    same_list = ''
    print(dash_word)
    if len(entered_word) > 0:
        print('Wrong letters:', end=' ')
        for i in entered_word:
            print(i, end=' ')
    print('')
    guess = input('Enter a letter: ')
    if len(guess) > 1:
        if int(guess) == 11:
            game_is_running = False
            start_game()
        print(f'Enter a single letter. Not "{guess}"')
        guess_word(word)
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                same_list += word[i]
            else:
                same_list += dash_word[i]
        dash_word = same_list
    else:
        hang_level += 1
        entered_word.append(guess)


def check_game_finish(word):
    check_win(word)
    check_finish(word)


def check_finish(word):
    global game_is_running
    if hang_level > 4:
        print(f'Try again! The word is "{word}')
        game_is_running = False


def check_win(word):
    global game_is_running
    if dash_word == word:
        print(f'You got the word "{word}"')
        game_is_running = False


def play_again():
    again = input('Press y/n to play again!').lower()
    if again == 'y':
        return True
    return False


def play():
    global hang_level, game_is_running, entered_word, dash_word
    display_hangman()
    hang_level = 0
    display_hangman()
    word = choose_word()
    new_word(word)
    while game_is_running:
        guess_word(word)
        display_hangman()
        check_game_finish(word)
    if play_again():
        game_is_running = True
        entered_word = []
        dash_word = ''
        play()


def start_game():
    option = int(input('--- HANG MAN ---\n1. Start Game\n2. How to play.\n3. Hangman words.\n4. About game.\n5. Exit'))
    if option == 1:
        play()
    elif option == 2:
        print("How to play hangman.\nHangman is a simple word guessing game. Players try to figure out an unknown "
              "word by guessing letters. If too many letters which do not appear in the word are guessed, the player "
              "is hanged (and loses).")
        start_game()
    elif option == 3:
        for i in hangman_word_list:
            print(i)
        start_game()
    elif option == 4:
        print('To stop playing during game.\ntype 11 in letters.')
        start_game()
    elif option == 5:
        exit()
    else:
        print('Wrong input!\nEnter again')
        start_game()


start_game()

