import turtle


class Mob(turtle.Turtle):
    _algorythm = 'greedy'

    def __init__(self, coord=(0, 0), name='Frog', img='frog.gif',
                 speed=15):
        super().__init__()
        # self.register_shape(name='frog', shape='frog.gif')
        self.shape('turtle')
        self.penup()
        self.coord = list(coord)
        self.goto(coord)
        self.speed = speed
        self.name = name

    def move(self):
        self.goto(self.coord)

    def step(self, direction='up'):
        if direction == 'up':
            self.coord[1] += self.speed
        if direction == 'down':
            self.coord[1] -= self.speed
        if direction == 'left':
            self.coord[0] -= self.speed
        if direction == 'right':
            self.coord[0] += self.speed
        self.move()
        return self.coord
