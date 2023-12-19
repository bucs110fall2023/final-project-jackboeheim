import pygame
import math
import src.Constants as Constants
from src.Model import Model

class Controller:

    def __init__(self, player_x = 1.5, player_y = 1.5, player_angle = 0):
        """
        Initializes player status vars and uses constants for rotation speed and movment speed
        Inputs: player_x (double)
                player_y(double)
                player_angle(double)
        Outputs: N/A
        """
        self.x = player_x
        self.y = player_y
        self.angle = player_angle
        self.movement_speed = Constants.MOVEMENT_SPEED
        self.rot_speed = Constants.ROT_SPEED

    @property
    def dir_vec(self):
        """
        Creates dir_vec as a member of class based on angle for current direction player faces
        Inputs: self.angle (double)
        Outputs: dir_vec(tuple)
        """
        return ((math.cos(self.angle), math.sin(self.angle)))
    
    @property
    def mapX(self):
        """
        Created mapX to signify current map x coord of player
        Inputs: self.x(double)
        Outputs: mapX(int)
        """
        return int(self.x)
    
    @property
    def mapY(self):
        """
        Created mapY to signify current map y coord of player
        Inputs: self.y(double)
        Outputs: mapY(int)
        """
        return int(self.y)

    def run(self):
        """
        Runs game and starts by updating player position and angle based on save file, then starts main and event loop. Creates model class,
        calls update_position update_save_file model.draw_floor_ceiling and model.raycast on each loop iteration
        Inputs: N/A
        Outputs: N/A
        """
        pos_ptr = open("etc/player_pos.txt", "r")

        self.x = float(pos_ptr.readline())

        self.y = float(pos_ptr.readline())

        self.angle = float(pos_ptr.readline())

        pos_ptr.close()

        model = Model(self)

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
        """
        Update player angle and position based on keys pressed, if walking results in collision, dont allow it
        Inputs: N/A
        Outputs N/A
        """
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
        """
        Updates the save file to store the players current position and angle
        Inputs: self.x(double)
                self.y(double)
                self.angle(double)
        Outputs: N/A
        """
        pos_ptr = open("etc/player_pos.txt", "w")

        pos_ptr.write(f"{self.x}\n{self.y}\n{self.angle}")

        pos_ptr.close()

        
