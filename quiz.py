import json
from operator import itemgetter


def questionDef(message, a, b, c, d, correct):
    answer = 'Enter your answer: '

    # Prints out questions and options from question sets
    print('\n> ' + message)
    print('\na: {} \nb: {} \nc: {} \nd: {}'.format(a, b, c, d))
    response = input(answer)
    if response.lower() == correct:
        return 1
    else:
        return 0


# Defining IDEs for extra question
ides = ['atom', 'vim', 'codeblocks', 'visualstudiocode',
        'codelite', 'dialogblocks', 'eclipse', 'netbeans',
        'komodo', 'aptanastudio', 'geany', 'shiftedit',
        'squad', 'visualstudio', 'monodevelop', 'pycharm',
        'kate', 'gedit', 'sublimetext', 'vscode', 'visualstudio'
        'what am I even doing here ;_;', 'vs']

print('Welcome to quiz about python!')

# Chooses which language to initialize
while True:
    language = input('Choose language [en/pl]: ').lower()
    if language == 'en':
        # (need to be tested) on windows you will probably need to change "/" to "\" in destination path
        with open('question_sets/questions_en.json', 'r') as f:
            questionsets = json.load(f)
            questiondict = []
        break
    elif language == 'pl':
        # (need to be tested) on windows you will probably need to change "/" to "\" in destination path
        with open('question_sets/questions_pl.json', 'r') as f:
            questionsets = json.load(f)
            questiondict = []
        break
    else:
        print('This language isn\'t currently supported. Try again.')
        continue

try:
    with open('data.json') as f:
        data_store = json.load(f)
# If json file doesn't exist or is corrupt/blank, start fresh
except (FileNotFoundError, json.decoder.JSONDecodeError):
    data_store = []

for item in questionsets:
    question = item['Question']
    a = item['a']
    b = item['b']
    c = item['c']
    d = item['d']
    answer = item['answer']
    questiondict.append((question, a, b, c, d, answer))

# Quiz loop
while True:
    name = input('Enter your name: ')
    score = 0

    # For each question in question sets, it calls questionDef,
    # and adds score for correct answer
    for q in questiondict:
        score += questionDef(*q)
    print('\n(-1 point if your answer is wrong)')
    extra = input("Do you want extra question? [y/n] ")
    if extra == 'y':
        ide_extra = input(
            'Enter name of one of popular IDEs. (without spaces,  pure string)\n').lower()
        if ide_extra in ides:
            score += 1
        else:
            score -= 1
    data_store.append({'Name: ': name, 'Score: ': score})
    again = input('Do you want to do next quiz? [y/n] ').lower()
    if again == 'y':
        continue
    else:
        # Saves data into json file
        with open('data.json', 'w') as f:
            json.dump(data_store, f, indent=2)
        break
