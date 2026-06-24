#Word  Scramble Game

import random
max_chance = 5
attempts = 0
#Given list of words for the scramble game
wordsList = ['python','java','javascript','automation','pytest','guvi','selenium']

#choosing a word using random module
picked_word = random.choice(wordsList)
#For testing purpose
#print(picked_word)

scambled_word_list_char = list(picked_word)

#Shuffling the characters in the list
random.shuffle(scambled_word_list_char)

jumbled_word ="".join(scambled_word_list_char)
#print(jumbled_word)
print(f'Welcome to the Word Scramble Game. You have to guess the correct word in {max_chance} attempts')
print(f'Your Scrambled word : {jumbled_word}')

while True:
    guess = input('Guess your scrambled word: ')
    entered_word = guess.lower().strip()
    attempts += 1
    if entered_word == picked_word.lower():
        if attempts == 1:
            print('Congrats!!! You got it right in your first attempt')
        else:
            print(f'Correct Answer.. You answered correctly in {attempts} attempts')

        break
    elif attempts >= max_chance:
        print(f'You exceeded the maximum number of attempts. The correct answer was {picked_word}')
        break
    else:
        print(f'Incorrect Answer.You got only {max_chance - attempts} attempts')
        continue