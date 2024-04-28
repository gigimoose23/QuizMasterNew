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
marquee_box = Rect(0, 0, 700, 80)
question_box = Rect(0, 0, 500, 100)
timer = Rect(0, 0, 100, 100)

#Buttons
skip_button = Rect(0, 0, 125, 250)
answer_box_1 = Rect(0, 0, 175, 75)  # Larger width for answer boxes
answer_box_2 = Rect(0, 0, 175, 75) # Larger width for answer boxes
answer_box_3 = Rect(0, 0, 175, 75) # Larger width for answer boxes
answer_box_4 = Rect(0, 0, 175, 75)  # Larger width for answer boxes
answerBoxes = [answer_box_1, answer_box_2, answer_box_3, answer_box_4]

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer.move_ip(550,100)
answer_box_1.move_ip(20,270)
answer_box_2.move_ip(300,270)
answer_box_3.move_ip(20,370)
answer_box_4.move_ip(300,370)
skip_button.move_ip(550,210)
#Drawing
def draw():
    global marquee_message
    screen.clear()
    screen.fill(color="black")
    screen.draw.filled_rect(skip_button, "skyblue")
    screen.draw.filled_rect(timer, "black")
    screen.draw.filled_rect(marquee_box, "black")
    screen.draw.filled_rect(question_box, "blue")
    #Box1
    screen.draw.filled_rect(answer_box_1, "orange")
    screen.draw.filled_rect(answer_box_2, "orange")
    screen.draw.filled_rect(answer_box_3, "orange")
    screen.draw.filled_rect(answer_box_4, "orange")
    screen.draw.filled_rect(timer, "blue")
    marquee_message="Hello and welcome to quiz master game!"
    screen.draw.textbox(marquee_message,marquee_box,color="white")
    screen.draw.textbox(question[0],question_box)
    index = 1
    for box in answerBoxes:
        screen.draw.textbox(question[index],box)
        index+= 1
    screen.draw.textbox(str(timeAmount), timer,color="red",shadow=(0.5,0.5),scolor="darkred")
    screen.draw.textbox("Skip", skip_button,color="black",angle=-90,shadow=(0.5,0.5),scolor="dimgrey")
    
def update():
    move_marquee()


def move_marquee():
    marquee_box.x-=2
    if marquee_box.right<0:
        marquee_box.left = WIDTH

def readQuestionFile():
    global question_file_address
    global questionAmount,questions
    questionFile = open(question_file_address, "r")
    for i in questionFile:
        questions.append(i)
        questionAmount += 1
    print(questions)
    questionFile.close()

def splitQuestion():
    global questionIndex
    questionIndex+=1
    return questions.pop(0).split(",")

def on_mouse_down(pos):
    pass

readQuestionFile()
question=splitQuestion()

pgzrun.go()
