#Pacman in Python with PyGame
#https://github.com/hbokmann/Pacman
  
import pygame
from src.Game import Game

game = Game()

game.initialiseGame(606,606)
game.startGame()

pygame.quit()