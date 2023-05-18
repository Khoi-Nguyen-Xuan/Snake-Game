

from tkinter import *
import random

GAMEWIDTH = 600
GAMEHEIGHT = 600
SPEED = 110
SPACESIZE = 50
BODYPART = 3
SNAKECOLOR = "green"
FOODCOLOR = "red"
BACKGROUND = "black"

class Snake :
    def __init__(self):
        self.bodySize = BODYPART
        self.coordinates = []
        self.squares = []

        for i in range (0,BODYPART):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square = canvas.create_rectangle(x,y,x+SPACESIZE,y+SPACESIZE,fill=SNAKECOLOR, tag ="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, (GAMEWIDTH / SPACESIZE) - 1) * SPACESIZE
        y = random.randint(0, (GAMEHEIGHT / SPACESIZE) - 1) * SPACESIZE

        self.coordinates = [x,y]

        canvas.create_oval(x,y,x+SPACESIZE,y+SPACESIZE, fill =FOODCOLOR, tag ="food")


def nextTurn(snake,food):
    x,y = snake.coordinates[0]
    if direction == "up":
        y -= SPACESIZE
    elif direction == "down":
        y += SPACESIZE
    elif direction == "left":
        x -= SPACESIZE
    elif direction == "right":
        x += SPACESIZE

    snake.coordinates.insert(0,(x,y))

    square = canvas.create_rectangle(x,y, x+SPACESIZE, y+SPACESIZE, fill =SNAKECOLOR)

    snake.squares.insert(0,square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1

        label.config(text ="Score : {}".format(score))

        canvas.delete("food")

        food = Food()

    else :

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if checkCollision(snake):
        gameOver()

    else :
         window.after(SPEED,nextTurn,snake,food)

def changeDirection(newDirection):
    global direction

    if newDirection=="left":
        if direction != "right":
            direction = newDirection

    elif newDirection=="right":
        if direction != "left":
            direction = newDirection\

    elif newDirection=="down":
        if direction != "up":
            direction = newDirection

    elif newDirection =="up":
        if direction != "down":
            direction = newDirection




def checkCollision(snake):
    x,y = snake.coordinates[0]
    if x < 0 or x >= GAMEWIDTH :
        print("Game over")
        return True

    elif y <0 or y>=GAMEHEIGHT:
        print("Game over")
        return True

    for bodyPart in snake.coordinates[1:]:
        if x == bodyPart[0] and y == bodyPart[1]:
            print("Game over")
            return True


    return False

def gameOver():
        canvas.delete(ALL)
        canvas.create_text((canvas.winfo_width()/2, canvas.winfo_height()/2),font =('consolas',70), text ="GAME OVER", fill = "red", tag = "gameover")



window = Tk()
window.title("Snake game")
window.resizable(False,False)
score = 0
direction = "down"

label = Label(window,text="Score:{}".format(score),font= ('consolas',40))
label.pack()

canvas = Canvas(window, bg =BACKGROUND, height=GAMEHEIGHT, width=GAMEWIDTH)
canvas.pack()

window.update()
windowWidth = window.winfo_width()
windowHeight = window.winfo_height()
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

x = int((screenWidth/2 - (windowWidth/2)))
y = int((screenHeight/2 - (windowHeight/2)))

window.geometry(f"{windowWidth}x{windowHeight}+{x}+{y}")

window.bind('<Left>', lambda event : changeDirection('left'))
window.bind('<Right>', lambda event : changeDirection('right'))
window.bind('<Up>', lambda event : changeDirection('up'))
window.bind('<Down>', lambda event : changeDirection('down'))

snake = Snake()
food = Food()

nextTurn(snake,food)

window.mainloop()