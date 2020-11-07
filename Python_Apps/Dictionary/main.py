import json
import difflib
from difflib import get_close_matches

with open('data.json', 'r') as f:
    data = json.load(f)

def word_dictionary(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        close_word = get_close_matches(word, data.keys())[0]
        close_ques = input(f'Did you mean {close_word} instead? ' + close_word + ' Y for yes, or N for no ').lower()
        if close_ques == 'y':
            return data[close_word]
    

input_word = input('Enter a word you want to know?').lower()
meaning = word_dictionary(input_word)

if meaning:
        print(input_word + " : " + meaning[0])
        if(len(meaning) > 1):
            print(meaning[1])
else:
    print('Try another question.')