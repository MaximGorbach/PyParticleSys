from Particle import *
from ShrinkingParticle import *
import random


class ParticleSystem:
    def __init__(self, gravity):
        self.particles = []
        self.emitters = []
        self.gravity = gravity

    def render(self, surface):
        for particle in self.particles:
            particle.render(surface)

    def step(self):
        for emitter in self.emitters:
            emitter.emit()
        
        self.particles = [p for p in self.particles if p.alive]
        for particle in self.particles:
            # applying gravity to particles
            particle.x_vel += self.gravity[0]
            particle.y_vel += self.gravity[1]
            particle.step() 
        

    def addRandParticles(self, num, pos, radius, colour, lifespan):
        for i in range (0,num):
            self.particles.append(ShrinkParticle(pos, [random.randint(-100,100)/20, random.randint(-100,100)/20], radius, colour, lifespan))

    def addParticle(self, particle):
        self.particles.append(particle)

    def addEmitter(self, emitter):
        self.emitters.append(emitter)