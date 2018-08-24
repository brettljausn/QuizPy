import pickle
import random
from operator import itemgetter
import os

dirname = os.path.dirname(__file__)


with open(os.path.join(dirname, 'general.txt'), "rb") as fp:   # Unpickling
    data = pickle.load(fp)

score = 0

for i in range(1,11):
    selected_question = random.choice(data)
    print('Question:',selected_question[0] ,"\nA -", selected_question[2],"\nB -", selected_question[3], "\nC -", selected_question[4], "\nD -", selected_question[5])
    choice = input('Please enter an answer (A, B, C or D): ').upper()

    if choice == 'A':
        answer = selected_question[2]
    elif choice == 'B':
        answer = selected_question[3]
    elif choice == 'C':
        answer = selected_question[4]
    elif choice == 'D':
        answer = selected_question[5]
    else:
        choice = input('Please enter an answer (A, B, C or D): ')

    if answer == selected_question[1]:
        print('\nCorrect!\n\n')
        score = score + 1
    else:
        print('\nWrong,', selected_question[1], 'would have been correct.\n\n')

print("Finished! You got", score, "points!")
