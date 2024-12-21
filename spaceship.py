from turtle import Turtle
import random


class Spaceship:
    def __init__(self):
        self.x = [0, 0, 0, 20, -20, 20, -20]
        self.y = [-200, -220, -240, -220, -220, -260, -260]
        self.blocks = []
        self.blocksy = []

    def adding_blocks(self):
        for i in range(7):
            block = Turtle(shape="square")
            block.color("white")
            block.penup()
            block.setx(self.x[i])
            block.sety(self.y[i])
            self.blocksy.append(block)

    def random_ship(self):
        base_x = random.randint(-100, 100)

        base_y = 360
        modified_x = [base_x, base_x, base_x, base_x + 20, base_x - 20, base_x + 20, base_x - 20]
        modified_y = [base_y, base_y - 20, base_y - 40, base_y - 20, base_y - 20, base_y - 60, base_y - 60]
        for i in range(7):
            block = Turtle(shape="square")
            block.color("white")
            block.penup()
            block.setx(modified_x[i])
            block.sety(modified_y[i])
            self.blocks.append(block)

    def return_(self):
        base_x = random.randint(-100, 100)
        base_y = 360
        modified_x = [base_x, base_x, base_x, base_x + 20, base_x - 20, base_x + 20, base_x - 20]
        modified_y = [base_y, base_y - 20, base_y - 40, base_y - 20, base_y - 20, base_y - 60, base_y - 60]
        for i in range(7):
            self.blocks[i].goto(modified_x[i], modified_y[i])

    def left_(self):

        if self.blocksy[4].xcor() > -120:
            for ship in self.blocksy:
                speed = 20
                ship.setx(ship.xcor() - speed)
        else:
            pass

    def right_(self):
        if self.blocksy[3].xcor() < 100:
            for ship in self.blocksy:
                speed = 20
                ship.setx(ship.xcor() + speed)
        else:
            pass

    def reset(self):

        more_x = [0, 0, 0, 20, -20, 20, -20]
        more_y = [-200, -220, -240, -220, -220, -260, -260]
        for i in range(7):
            self.blocksy[i].goto(more_x[i], more_y[i])

