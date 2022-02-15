import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word




def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('Masz', lives, 'żyć, użyta litera: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Poprawne słowo: ', ' '.join(word_list))

        user_letter = input('Zagnij litere: ').upper()
        if user_letter  in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        
            else:
                lives = lives - 1

        elif user_letter in used_letters:
            print('Już użyłeś tej litery. Spróbuj ponownie. ')
    
        else:
            print('Nieprawidłowa litera. Spróbuj ponownie. ')
    if lives == 0:
        print('Przegrałeś. Słowo to ', word)
    else:
        print('Odgadłeś. Słowo to ', word, '!!')





hangman()

