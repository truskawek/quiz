import requests
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
            if not value in ["a", "b", "c", "d"]:
                print("Please enter only one character: a, b, c or d")
                continue
            else:
                break
        except ValueError:
            print("Enter correct value", ValueError)
        
    return value


number_of_questions = get_correct_prompt("How many questions do want to be asked? \n")
quiz_API_url = 'https://opentdb.com/api.php?amount={number_of_questions}&type=multiple'.format(number_of_questions=number_of_questions)
response = requests.get(quiz_API_url)
json_obj = response.json()["results"]
incorrect_answers = list()
correct_answer = list()
points = 0
possible_answers = list()

def show_question(question):
    print(json_obj[question]['question'])
    print()
    show_answers(question)

def show_answers(question):
    global incorrect_answers
    global possible_answers
    global points
    correct_answer_from_shuffled = list()
    correct_answer = json_obj[question]["correct_answer"]
    incorrect_answers = json_obj[question]["incorrect_answers"]
    possible_answers = [
        [incorrect_answers[0], "a"],
        [incorrect_answers[1], "b"],
        [incorrect_answers[2], "c"],
        [correct_answer, "d"]
    ]
    possible_answers_shuffled = random.sample(possible_answers, len(possible_answers))
    possible_answers_shuffled_list = [
        [possible_answers_shuffled[0][0], "a"],
        [possible_answers_shuffled[1][0], "b"],
        [possible_answers_shuffled[2][0], "c"],
        [possible_answers_shuffled[3][0], "d"]
    ]

    # uncomment the line below to test the quiz and always first show the correct answer
    # print(correct_answer)
    # or just google the right answer :)

    for _ in range(len(possible_answers_shuffled_list)):
        letter = chr(ord("a") + _)
        print('{letter}. {question} '.format(letter = letter, question = possible_answers_shuffled_list[_][0]))
    print()
    answer = get_correct_answer("Choose one of the following: a, b, c or d\n")
    
    for _ in range(len(possible_answers_shuffled_list)):   
        if possible_answers_shuffled_list[_][0] == correct_answer:
            correct_answer_from_shuffled = possible_answers_shuffled_list[_][1]
            if answer == correct_answer_from_shuffled:
                points += 1
                print("This is the correct answer!")
                print()
            else:
                print("Sorry, wrong answer :( The correct answer was:", correct_answer)
                print()

for _ in range(number_of_questions):
    show_question(_)
print("End of the game. You scored", points, "point(s).")