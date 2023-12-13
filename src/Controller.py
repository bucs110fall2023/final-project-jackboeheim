import pygame
import math
import src.Constants as Constants

class Controller:

    def __init__(self, player_x = 1.5, player_y = 1.5, player_angle = 0):
        self.x = player_x
        self.y = player_y
        self.angle = player_angle
        self.movement_speed = .06
        self.rot_speed = .12

    @property
    def dir_vec(self):

        return ((math.cos(self.angle), math.sin(self.angle)))
    
    @property
    def mapX(self):

        return int(self.x)
    
    @property
    def mapY(self):

        return int(self.y)

    def run(self, model):
        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()

                    exit()

            self.update_position()

            self.update_save_file()

            model.draw_floor_ceiling()

            model.raycast()

            pygame.display.flip()

            Constants.CLOCK.tick(30)

    def update_position(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:

            if not(Constants.WOLRD_MAP[int(self.y)][int(self.x + self.movement_speed * self.dir_vec[0])]):

                self.x += self.movement_speed * self.dir_vec[0]
            if not(Constants.WOLRD_MAP[int(self.y + self.movement_speed * self.dir_vec[1])][int(self.x)]):

                self.y += self.movement_speed * self.dir_vec[1]

        if keys[pygame.K_s]:

            if not(Constants.WOLRD_MAP[int(self.y)][int(self.x - self.movement_speed * self.dir_vec[0])]):

                self.x -= self.movement_speed * self.dir_vec[0]

            if not(Constants.WOLRD_MAP[int(self.y - self.movement_speed * self.dir_vec[1])][int(self.x)]):

                self.y -= self.movement_speed * self.dir_vec[1]

        if keys[pygame.K_a]:

            while self.angle < 0:

                self.angle += 2 * Constants.pi

            self.angle -= self.rot_speed

        if keys[pygame.K_d]:

            while self.angle > 2 * Constants.pi:

                self.angle -= 2 * Constants.pi

            self.angle += self.rot_speed

    def update_save_file(self):

        pos_ptr = open("etc/player_pos.txt", "w")

        pos_ptr.write(f"{self.x}\n{self.y}\n{self.angle}")

        pos_ptr.close()

        