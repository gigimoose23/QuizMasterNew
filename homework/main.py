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
TITLE = "Marquee"

#Shapes
marquee_box = Rect(0, 0, 700, 80)
question_box = Rect(0, 0, 500, 100)
timer = Rect(0, 0, 100, 100)

marquee_box.move_ip(0,250)
    
def update():
    move_marquee()

def draw():
    screen.clear()
    marquee_message="Happy Birthday Sami!"
    screen.draw.textbox(marquee_message,marquee_box,color="white")

def move_marquee():
    marquee_box.x-=2
    if marquee_box.right<0:
        marquee_box.left = WIDTH



pgzrun.go()
