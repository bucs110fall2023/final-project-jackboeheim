import pygame
from src.Controller import Controller

def main():
    pygame.init()
    player = Controller()
    player.run()

if __name__ == '__main__':
    main()

