import pygame as p
import random
from Particle import *
from ShrinkingParticle import *
from ParticleSystem import *
from Emitter import *

GRAVITY_CONST = (0, 0.5)

# initialising pygame
p.init()
screenWidth = 1500
screenHeight = 1000
screen = p.display.set_mode((screenWidth,screenHeight))
clock = p.time.Clock()
running = True

particleSys = ParticleSystem(GRAVITY_CONST)

# Test Rocket
rocket = [[700, 1000], [0,-5]]
rocketEmitter = Emitter(rocket[0], (255,100,0), particleSys)


# Main Loop ================================================================================
while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
    
    if p.mouse.get_pressed()[0]:
            particleSys.addRandParticles(5, p.mouse.get_pos(), 10, (0, 0, 255), 60)
    
    screen.fill((255, 255, 255))

    # render particles
    particleSys.step()
    particleSys.render(screen)

    # handle test rocket
    p.draw.rect(screen, (0,0,0), p.Rect(rocket[0], (20, 40)))
    rocket[0][0] += rocket[1][0]
    rocket[0][1] += rocket[1][1]
    rocketEmitter.x = rocket[0][0] + 10
    rocketEmitter.y = rocket[0][1] + 40

    p.display.flip()
    clock.tick(80)

p.quit()