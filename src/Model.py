import math
import src.Constants as Constants
import pygame

class Model:
    def __init__(self, player = None):
        """
        Initializes instance of model using an instance of the controller, called player, and defines the screen
        Inputs: player(Controller)
        Outputs N/A
        """
        self.player = player
        self.screen = pygame.display.set_mode(Constants.SCREEN_SIZE)

    def draw_floor_ceiling(self):
        """
        Draws floor and ceiling using colored rectangles
        Inputs: self.screen(Surface)
        Outputs: N/A
        """
        self.screen.fill(Constants.LIGHT_GRAY, pygame.Rect((0,Constants.SCREEN_HEIGHT//2), (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT//2)))
        self.screen.fill(Constants.DARK_GREY, pygame.Rect((0,0), (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT//2)))

    def raycast(self):
        """
        Raycasting algorithm: Uses player's state and effectively draws rays to nearest wall and draws a sliver of wall which is
        inversely proportional in its height to the ray distance. Then uses this distance adn the color and side of the wall hit
        to draw all of the walls
        Inputs: self.player.angle(double)
                self.player.mapX(int)
                self.player.x(double)
                self.player.mapY(int)
                self.player.y(double)
                self.screen(Surface)
        Outputs: N/A
        """
        ray_angle = self.player.angle - Constants.FOV/2 + 1e-6

        x = Constants.LINE_WIDTH/2

        for _ in range(Constants.NUM_RAYS):
            
            ray_x_dir = math.cos(ray_angle)
            ray_y_dir = math.sin(ray_angle)

            delta_x_dist = math.sqrt(((ray_y_dir**2)/(ray_x_dir**2)) + 1) if ray_x_dir != 0 else 1e20
            delta_y_dist = math.sqrt(((ray_x_dir**2)/(ray_y_dir**2)) + 1) if ray_y_dir != 0 else 1e20


            if ray_x_dir > 0:
                x_step = 1
                side_x_dist = (1 + self.player.mapX - self.player.x) * delta_x_dist
            else:
                x_step = -1
                side_x_dist = (self.player.x - self.player.mapX) * delta_x_dist
            if ray_y_dir > 0:
                y_step = 1
                side_y_dist = (1 + self.player.mapY - self.player.y) * delta_y_dist
            else:
                y_step = -1
                side_y_dist = (self.player.y - self.player.mapY) * delta_y_dist

            hit = False

            mapX = self.player.mapX
            mapY = self.player.mapY

            while not hit:
                if side_x_dist < side_y_dist:
                    side_x_dist += delta_x_dist
                    mapX += x_step
                    side = 0

                else:
                    side_y_dist += delta_y_dist
                    mapY += y_step
                    side = 1

                hit = Constants.WOLRD_MAP[mapY][mapX]

            if side:
                wall_dist = side_y_dist - delta_y_dist

            else:
                wall_dist = side_x_dist - delta_x_dist

            ray_angle += Constants.DELTA_THETA

            line_height = int(Constants.SCREEN_HEIGHT / wall_dist)
            margin = (Constants.SCREEN_HEIGHT - line_height)/2

            line_bottom = int(margin) if margin >= 0 else 1
            line_top = Constants.SCREEN_HEIGHT - margin if margin >= 0 else Constants.SCREEN_HEIGHT - 1

            color = Constants.WALL_COLOR[Constants.WOLRD_MAP[mapY][mapX]]

            if side:
                color = color // pygame.Color(2,2,2,1)

            x += Constants.LINE_WIDTH

            pygame.draw.line(self.screen, color, (x,line_bottom), (x,line_top), Constants.LINE_WIDTH)
