from turtle import Screen
from wall import Wall
from spaceship import Spaceship
import time
from score import Score

is_finished = False
screen = Screen()
screen.setup(width=350, height=600)
screen.bgcolor('black')
screen.title("Spaceship Game")
screen.tracer(0)
count = 0
speed = 50
value = 260
# Creating the wall
Wall = Wall()
Wall.adding_left_up()
Wall.adding_left_down()
Wall.adding_right_up()
Wall.adding_right_down()

ship = Spaceship()

# creating the user_ship
ship.adding_blocks()
ship.random_ship()

score = Score()
is_ = False
# block = Turtle(shape="square")
# block.color("white")
# block.penup()
# block.setx(11)
# block.sety(-180)

screen.listen()

screen.onkey(ship.left_, "Left")
screen.onkey(ship.right_, "Right")


while not is_finished:
    time.sleep(0.01)
    for j in Wall.blocks:
        screen.update()
        y = j.ycor()
        j.sety(y - 10)

    for k in ship.blocks:
        screen.update()
        x = k.ycor()
        print("yes")
        k.sety(x - speed)
        for t in ship.blocksy:
            difference = t.ycor() - k.ycor()
            differnce_x = t.xcor() - k.xcor()
            print(difference)
            if -21 < difference < 21:
                print("reach")
                if 0 <= differnce_x < 20 or -20 < differnce_x <= 0:
                    is_ = True

    count += 1
    if count % 2 == 0:
        Wall.new_block(value)

    if ship.blocksy[5].ycor() > ship.blocks[0].ycor() + 30:
        score.scoring()
        ship.blocks = []
        ship.random_ship()
        if score.score % 3 == 0:
            speed += 50
    if is_:
        score.reset()
        ship.return_()
        ship.reset()
        is_ = False

screen.exitonclick()
