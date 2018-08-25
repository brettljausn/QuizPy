import pickle
import random
import os

dirname = os.path.dirname(__file__)


with open(os.path.join(dirname, 'general.txt'), "rb") as fp:   # Unpickling
    data = pickle.load(fp)

score = 0
i = 0

while True:
    selected_question = random.choice(data)
    print('Question:',selected_question[0] ,"\nA -", selected_question[2],"\nB -", selected_question[3], "\nC -", selected_question[4], "\nD -", selected_question[5])

    while True:
        choice = input('Please enter an answer (A, B, C or D): ').upper()
        if choice == 'A':
            answer = selected_question[2]
            break
        elif choice == 'B':
            answer = selected_question[3]
            break
        elif choice == 'C':
            answer = selected_question[4]
            break
        elif choice == 'D':
            answer = selected_question[5]
            break

    if answer == selected_question[1]:
        print('\nCorrect!\n\n')
        score = score + 10
    else:
        score = score - 5
        print('\nWrong,', selected_question[1], 'would have been correct.\n\n')

    i = i + 1

    if i == 5:
        print("Finished! You got", score, "points!")
        while True:
            replay = input('Play again? (Y/N): ').upper()
            if replay == "Y":
                i = 0
                score = 0
                print("\n")
                break
            elif replay == "N":
                exit()
