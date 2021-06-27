import requests
import json
import random

def get_correct_prompt(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive number")
                continue
            else:
                break
        except ValueError:
            print("Enter correct value")
        
    return value


def get_correct_answer(prompt):
    while True:
        try:
            value = input(prompt).lower()
            if value not in ['a','b','c','d']:
                print("Please enter only one character: a, b, c or d")
                continue
            else:
                break
        except ValueError:
            print("Enter correct value")
        
    return value


number_of_questions = get_correct_prompt("How many questions do want to be asked? \n")
quiz_API_url = 'https://opentdb.com/api.php?amount={number_of_questions}&type=multiple'.format(number_of_questions=number_of_questions)
response = requests.get(quiz_API_url)
json_obj = response.json()["results"]
all_answers = list()
incorrect_answers = list()
correct_answer = list()

def show_question(question):
    print(json_obj[question]['question'])
    print()
    show_answers(question)
    print("correct answer is: ", correct_answer)
    print(all_answers)
    a, b, c, d = all_answers
    print(c)
    answer = get_correct_answer("Choose one of the following: a, b, c or d \n")

def show_answers(question):
    global all_answers
    global incorrect_answers
    global correct_answer
    incorrect_answers = json_obj[question]["incorrect_answers"]
    correct_answer = json_obj[question]["correct_answer"]
    all_answers.append(incorrect_answers)
    all_answers = (incorrect_answers + [correct_answer])
    for _ in range(len(all_answers)):
        print(chr(ord('a') + _), all_answers[_])

for _ in range(number_of_questions):
    show_question(_)