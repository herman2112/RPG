import pygame
import sys

from game import Game

def main():
    game = Game()
    while game.running:
        game.playing = True
        game.game_loop()

if __name__ == "__main__":
    main()