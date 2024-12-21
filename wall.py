from turtle import Turtle


class Wall:
    def __init__(self):
        self.blocks = []
        self.height = 0
        self.width = 150

    def adding_left_up(self):
        self.width = -150
        for i in range(12):
            block = Turtle(shape="square")
            block.color("white")
            block.penup()
            block.setx(self.width)
            block.sety(self.height)
            self.height += 25
            self.blocks.append(block)
        self.height = 0

    def adding_left_down(self):
        self.width = -150
        for i in range(12):
            block = Turtle(shape="square")
            block.color("white")
            block.penup()
            block.setx(-150)
            block.sety(self.height)
            self.height -= 25
            self.blocks.append(block)

        self.height = 0

    def adding_right_up(self):
        self.width = 140
        for i in range(12):
            block = Turtle(shape="square")
            block.color("white")
            block.penup()
            block.setx(self.width)
            block.sety(self.height)
            self.height += 25
            self.blocks.append(block)
        self.height = 0

    def adding_right_down(self):
        self.width = 140
        for i in range(12):
            block = Turtle(shape="square")
            block.color("white")
            block.penup()
            block.setx(self.width)
            block.sety(self.height)
            self.height -= 25
            self.blocks.append(block)

        self.height = 0

    def new_block(self,value):
        block = Turtle(shape="square")
        block2 = Turtle(shape="square")
        block.color("white")
        block2.color("white")
        block.penup()
        block2.penup()
        block.setx(140)
        block.sety(value + 10)
        block2.setx(-150)
        block2.sety(value)
        self.blocks.append(block)
        self.blocks.append(block2)
