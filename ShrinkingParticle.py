from Particle import *

class ShrinkParticle(Particle):
    def __init__(self, pos, velocity, radius, colour, lifespan):
        super().__init__(pos, velocity, radius, colour, lifespan)
        self.radReduction = (self.radius - 1)/self.lifespan

    def change(self):
        self.radius -= self.radReduction
