#!/usr/bin/env python

import json
import string

print('Welcome to quiz about python!')


def question(message, options, correct):
    # message - string
    # options - list
    # correct - int
    answer = 'Enter your answer: '
    optionLetters = string.ascii_lowercase[:len(options)]
    print(message)
    print(' '.join('{}: {}'.format(letter, answer)
                   for letter, answer in zip(optionLetters, options)))
    response = input(answer)
    if response == correct:
        return 1
    else:
        return 0


try:
    with open('data.json') as f:
        data_store = json.load(f)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    # if json file doesn't exist or is corrupt/blank, start fresh
    data_store = []

# ----------- QUESTIONS ----------- #

question_sets = [('\nQuestion 1: Who created python?',
                  ['None of these', 'Guido van Rossum', 'Mark Zuckerberg',
                   'Aliens'], 1),
                 ('\nQuestion 2: What is the lastest version of python?',
                  ['4', '9', '2', '3'], 3),
                 ('\nQuestion 3: Where is creator of python from?',
                  ['USA', 'Mars', 'Netherland', 'Poland'], 2),
                 ('\nQuestion 4: What sites from these are written in python?',
                  ['YouTube', 'All of them', 'Google', 'Reddit'], 1),
                 ('\nQuestion 5: ', ['true', '', '', ''], 0)]

# -------------------------------- #

while True:
    name = input('Enter your name: ')
    score = 0
    for q in question_sets:
        score += question(*q)

    data_store.append({'Name: ': name, 'Score: ': score})
    again = input('Do you want to do next quiz? [y/n] ').lower()
    if again == 'y':
        continue
    else:
        with open('data.json', 'w') as f:
            json.dump(data_store, f)
        break