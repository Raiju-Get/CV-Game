import pygame
import random
import time
import image
import ui
from settings import *

class Mosquito:
    def __init__(self):
        #size
        random_size_value = random.uniform(MOSQUITO_SIZE_RANDOMIZE[0], MOSQUITO_SIZE_RANDOMIZE[1])
        size = (int(MOSQUITOS_SIZES[0] * random_size_value), int(MOSQUITOS_SIZES[1] * random_size_value))
        # moving
        moving_direction, start_pos = self.define_spawn_pos(size)
        # sprite
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4)
        intNum = random.randint(1,9)
        match intNum:
            case 1:
                self.value = 1
                self.images = [image.load("Assets/mosquito/1.png", size=size, flip=moving_direction == "right")]
            case 2:
                self.value = 2
                self.images = [image.load("Assets/mosquito/2.png", size=size, flip=moving_direction == "right")]
            case 3:
                self.value = 3
                self.images = [image.load("Assets/mosquito/3.png", size=size, flip=moving_direction == "right")]
            case 4:
                self.value = 4
                self.images = [image.load("Assets/mosquito/4.png", size=size, flip=moving_direction == "right")]
            case 5:
                self.value = 5
                self.images = [image.load("Assets/mosquito/5.png", size=size, flip=moving_direction == "right")]
            case 6:
                self.value = 6
                self.images = [image.load("Assets/mosquito/6.png", size=size, flip=moving_direction == "right")]
            case 7:
                self.value = 7
                self.images = [image.load("Assets/mosquito/7.png", size=size, flip=moving_direction == "right")]
            case 8:
                self.value = 8
                self.images = [image.load("Assets/mosquito/8.png", size=size, flip=moving_direction == "right")]
            case 9:
                self.value = 9
                self.images = [image.load("Assets/mosquito/9.png", size=size, flip=moving_direction == "right")]

        self.current_frame = 0
        self.animation_timer = 0


    def define_spawn_pos(self, size): # define the start pos and moving vel of the mosquito
        vel = random.uniform(MOSQUITOS_MOVE_SPEED["min"], MOSQUITOS_MOVE_SPEED["max"])
        moving_direction = random.choice(("left", "right", "up", "down"))
        if moving_direction == "right":
            start_pos = (-size[0], random.randint(size[1], SCREEN_HEIGHT-size[1]))
            self.vel = [vel, 0]
        if moving_direction == "left":
            start_pos = (SCREEN_WIDTH + size[0], random.randint(size[1], SCREEN_HEIGHT-size[1]))
            self.vel = [-vel, 0]
        if moving_direction == "up":
            start_pos = (random.randint(size[0], SCREEN_WIDTH-size[0]), SCREEN_HEIGHT+size[1])
            self.vel = [0, -vel]
        if moving_direction == "down":
            start_pos = (random.randint(size[0], SCREEN_WIDTH-size[0]), -size[1])
            self.vel = [0, vel]
        return moving_direction, start_pos


    def move(self):
        self.rect.move_ip(self.vel)


    def animate(self): # change the frame of the insect when needed
        t = time.time()
        if t > self.animation_timer:
            self.animation_timer = t + ANIMATION_SPEED
            self.current_frame += 1
            if self.current_frame > len(self.images)-1:
                self.current_frame = 0


    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, (200, 60, 0), self.rect)



    def draw(self, surface):
        self.animate()
        image.draw(surface, self.images[self.current_frame], self.rect.center, pos_mode="center")
        if DRAW_HITBOX:
            self.draw_hitbox(surface)


    def kill(self, mosquitos): # remove the mosquito from the list
        mosquitos.remove(self)
        if(self.value % 2 == 0):
            return 1
        else:
            return -BEE_PENALITY
