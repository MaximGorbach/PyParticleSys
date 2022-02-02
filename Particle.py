import pygame as p

class Particle:
    def __init__(self, pos, velocity, radius, colour, lifespan):
        self.x = pos[0]
        self.y = pos[1]
        self.x_vel = velocity[0]
        self.y_vel = velocity[1]
        self.radius = radius
        self.colour = colour
        self.lifespan = lifespan
        self.age = 0
        self.alive = True

    def render(self, surface):
        p.draw.circle(surface, self.colour, [int(x) for x in self.getPos()], int(self.radius))

    def step(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.change()
        self.age += 1
        if self.age >= self.lifespan:
            self.alive = False
    
    def getPos(self):
        return [self.x, self.y]

    def getVelocity(self):
        return [self.x_vel, self.y_vel]

    # This is a function to be implemented by extended particle classes that need to change size/shape
    def change(self):
        return