#snake game using turtle libary

import turtle
import time
import random
import math

delay = 0.15 #secounds

game_win = turtle.Screen()
game_win.title("Game")
game_win.bgcolor("grey")
w = 640
h = 640
game_win.setup(width= w, height=h)
game_win.tracer(0)

#snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("brown")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"

snake_section = []

#
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
#food.goto(0,0)
food.goto(random.randint(-240,240), random.randint(-240,240))


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

def direction_check():
    #if current direction is oposite of wanted direction ignore snake direction change

    return


def go_up():
    snake.direction ="up"
def go_down():
    snake.direction = "down"
def go_left():
    snake.direction = "left"
def go_right():
    snake.direction = "right"




def snake_food_distance():
    cor_x= snake.xcor() - food.xcor()
    cor_y= snake.ycor() - food.ycor()
    distance = math.sqrt(cor_x**2 + cor_y**2)
    if distance <=20:
        
        food.goto(random.randint(-240,240), random.randint(-240,240))
        return True
    return False
def snake_grow():
    #if snake eat food snake grow
    #new snake_section element made
    part = turtle.Turtle()
    part.speed(0)
    part.shape("square")
    part.color("green")
    part.penup()
    
    snake_section.append(part)
    #it follows previous body part

    


game_win.listen()
game_win.onkeypress(go_up, "w")
game_win.onkeypress(go_down, "s")
game_win.onkeypress(go_left, "a")
game_win.onkeypress(go_right, "d")

def restart():
    time.sleep(1)
    for i in snake_section:
        i.hideturtle()
    snake_section.clear()
    snake.goto(0,0)
    snake.direction = "stop"

def move_snake_section():
    if (len(snake_section)==0):
        return
    for i in range (len(snake_section)-1,-1 , -1):
        if i == 0:#follows snake
            #snake_section[i].xcor() = snake.xcor()
            #snake_section[i].ycor() = snake.ycor()
            snake_section[i].goto(snake.xcor(), snake.ycor())

        if i>0:
            #snake_section[i].xcor() = snake_section[i-1].xcor()
            #snake_section[i].ycor() = snake_section[i-1].ycor()

            # section i goes to i-1 coords
            #0 goes to snake coords
            #1 goes to 0 cooeds
            #2 goes to 1 coords
            #everyone goes to snake coords and after loop snake move
            #if 2 goes to 1 
            #1 goes to 0
            #0 to snake
            #
            snake_section[i].goto(snake_section[i-1].xcor(), snake_section[i-1].ycor())

def collison():
    #if snake collides with snake_section game over
    for i in range(len(snake_section)):
        if (snake_section[i].xcor() == snake.xcor()) and (snake_section[i].ycor() == snake.ycor()):
            print("col dect")
            
            restart()

    return False

def border():
    if (snake.xcor()< w/-2 +10 or snake.xcor()>w/2 -10) or (snake.ycor()< h/-2 +10 or snake.ycor()>h/2 -10):
        restart()
    

#main game loop
while(True):
    game_win.update()
    
    if(snake_food_distance()):#if snake eat food, snake grow
        #nothing
        print("ate sum food")
        snake_grow() 
        print(snake_section)

    
    move_snake_section()
    move()

    # collison()
    
    if collison():
       print("Collision detected")
       
       time.sleep(1)   
       restart()
    border()

    time.sleep(delay)

game_win.mainloop()
