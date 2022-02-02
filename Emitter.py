from ParticleSystem import *
from Particle import *
from ShrinkingParticle import *
import random

class Emitter:
    def __init__(self, pos, colour, particleSys):
        self.x = pos[0]
        self.y = pos[1]
        self.x_vel = 0
        self.y_vel = 0
        self.colour = colour
        self.enabled = True
        self.particleSys = particleSys
        particleSys.addEmitter(self)

    # varying emitter functionality can be implemented by extending this class and overriding this function
    def emit(self):
        if self.enabled:
            for i in range(0,8):
                p = ShrinkParticle(self.getPos(), [random.randint(-80,80)/20, random.randint(-100,0)/20], 5, self.colour, 25) 
                self.particleSys.addParticle(p)
            self.move()

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def getPos(self):
        return [self.x, self.y]

    def getVelocity(self):
        return [self.x_vel, self.y_vel]

    def setVelocity(self, velocity):
        self.x_vel = velocity[0]
        self.y_vel = velocity[1]

    def setPos(self, pos):
        self.x = pos[0]
        self.y = pos[1]