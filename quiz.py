import pgzero
import pgzrun
import pygame
from pgzero.builtins import Rect

#Variables
question_file_address = "questions.txt"
currentScore = 0
timeAmount = 10

gameOver = False
marquee_message = ""
questions = []

questionAmount = 0
questionIndex = 0


#Constants
WIDTH = 700
HEIGHT = 500
TITLE = "Quiz Game!"

#Shapes
marquee_box = Rect(50, 400, 500, 80)
question_box = Rect(60, 30, 450, 100)
timer = Rect(575, 370, 100, 100)

#Buttons
skip_button = Rect(550, 50, 125, 300)
answer_box_1 = Rect(50, 300, 175, 75)  # Larger width for answer boxes
answer_box_2 = Rect(250, 300, 175, 75) # Larger width for answer boxes
answer_box_3 = Rect(250, 200, 175, 75) # Larger width for answer boxes
answer_box_4 = Rect(50, 200, 175, 75)  # Larger width for answer boxes
answerBoxes = [answer_box_1, answer_box_2, answer_box_3, answer_box_4]

#Drawing
def draw():
    screen.clear()
    screen.fill(color="black")
    screen.draw.filled_rect(skip_button, "skyblue")
    screen.draw.filled_rect(timer, "black")
    screen.draw.filled_rect(marquee_box, "white")
    screen.draw.filled_rect(question_box, "blue")
    #Box1
    screen.draw.filled_rect(answer_box_1, "orange")
    screen.draw.filled_rect(answer_box_2, "orange")
    screen.draw.filled_rect(answer_box_3, "orange")
    screen.draw.filled_rect(answer_box_4, "orange")
    screen.draw.filled_rect(timer, "blue")

def update():
    pass

def readQuestionFile():
    global question_file_address
    global questionAmount,questions
    questionFile = open(question_file_address, "r")
    for i in questionFile:
        questions.append(i)
        questionAmount += 1
    print(questions)
    questionFile.close()

pgzrun.go()
