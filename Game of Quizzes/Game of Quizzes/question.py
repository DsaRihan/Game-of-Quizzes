#!/usr/bin/env python3
import json
import time
import os
import sys

TOPICS_LIST = ['commerce', 'technology', 'worldgk'] 
# this list has to in sync with the JSON filename and the Menu prompt inside test() method

def ask_one_question(question):
    print("\n" + question)
    choice = input("Enter Your Choice [a/b/c/d]: ")
    while(True):
        if choice.lower() in ['a', 'b', 'c', 'd']:
            return choice
        else:
            print("Invalid choice. Please choose from the above options")
            choice = input("Enter Choice [a/b/c/d]: ")

def score_one_result(key, meta):
    actual = meta["answer"]
    if meta["user_response"].lower() == actual.lower():
        print("Q.{0} Absolutely Correct!\n".format(key))
        return 2
    else:
        print("Q.{0} Incorrect!".format(key))
        print("Right Answer is ({0})".format(actual))
        print ("Learn more : " + meta["more_info"] + "\n")
        return -1

def press_any_key_to_continue():
    # Cross-platform approach
    if os.name == 'nt':  # For Windows
        import msvcrt
        print("Press any key to start the quiz...")
        msvcrt.getch()
    else:  # For Unix-like systems (Linux, macOS)
        print("Press any key to start the quiz...")
        sys.stdin.read(1)


def test(questions):
    score = 0
    print("\n"+"General Instructions:\n1. Please enter only the choice letter corresponding to the correct answer.\n2. Each question carries 2 points\n3. Wrong answer leads to -1 marks per question\nQuiz will start momentarily. Good Luck!\n")
    # time.sleep(10)
    press_any_key_to_continue()
    
    for key, meta in questions.items():
        questions[key]["user_response"] = ask_one_question(meta["question"])
    print("\n***************** RESULT ********************\n")
    for key, meta in questions.items():
        score += score_one_result(key, meta)
    print("Your Score:", score, "/", (2 * len(questions)))

def load_question(filename):
    """
    loads the questions from the JSON file into a Python dictionary and returns it
    """
    questions = None
    with open(filename, "r") as read_file:
        questions = json.load(read_file)
    return (questions)


def play_quiz():
    flag = False
    try:
        choice = int(input("Welcome to Today's Quiz!\nChoose your domain of interest:\n(1). Commerce\n(2). Technology\n(3). World Gk\nEnter Your Choice [1/2/3]: "))
        if choice > len(TOPICS_LIST) or choice < 1:
            print("Invalid Choice. Enter Again")
            flag = True # raising flag
    except ValueError as e:
        print("Invalid Choice. Enter Again")
        flag = True # raising a flag

    if not flag:
        questions = load_question('topics/'+TOPICS_LIST[choice-1]+'.json')
        test(questions)
    else:
        play_quiz() # replay if flag was raised

def user_begin_prompt():
    print("Wanna test your GK?\nA. Yes\nB. No")
    play = input()
    if play.lower() == 'a' or play.lower() ==  'y':
        play_quiz()
    elif play.lower() == 'b':
        print("Hope you come back soon!")
    else:
        print("Hmm. I didn't quite understand that.\nPress A to play, or B to quit.")
        user_begin_prompt()
        
def execute():
    user_begin_prompt()

if __name__ == '__main__':
    execute()
