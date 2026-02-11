#snake game using turtle libary

import turtle
import time

delay = 0.2 #secounds

game_win = turtle.Screen()
game_win.title("Game")
game_win.bgcolor("grey")
game_win.setup(width= 480, height=480)
game_win.tracer(0)

#snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"

#move function
def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

    if snake.direction == "left":
        
        snake.setx(snake.xcor() - 20)

def go_up():
    snake.direction ="up"
def go_down():
    snake.direction = "down"
def go_left():
    snake.direction = "left"
def go_right():
    snake.direction = "right"


game_win.listen()
game_win.onkeypress(go_up, "w")
game_win.onkeypress(go_down, "s")
game_win.onkeypress(go_left, "a")
game_win.onkeypress(go_right, "d")



#main game loop
while(True):
    game_win.update()
    
    move()

    time.sleep(delay)

game_win.mainloop()
