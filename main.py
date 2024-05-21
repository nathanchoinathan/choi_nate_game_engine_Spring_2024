# This file was created by: Nate Choi
 
# import necessary modules
# my first source control edit

import pygame as pg 
import sys
from settings import *
from sprites import *
from random import randint
from os import path
from time import sleep
import random
# this is a function!
# initializing the class

# adding level values for each map
LEVEL1 = "level1.txt"
LEVEL2 = "level2.txt"

#adding the levels to the list
levels = [LEVEL1, LEVEL2]

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        self.running = True
        self.current_level = 1
    # we have defined the run method in our game engine
    
    # load save game data
    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, LEVEL1), 'rt') as f:
            for line in f:
                self.map_data.append(line)
    def change_level(self, lvl):
        game_folder = path.dirname(__file__)
        for s in self.all_sprites:
            s.kill()
        self.player.moneybag = 0
        self.map_data = []
        with open(path.join(game_folder, "level" + str(lvl)), 'rt') as f:
            for line in f:
                print(line)
                self.map_data.append(line)
        # repopulate the level with stuff
        for i in range (0,10):
            Coin(self, randint(0,32), randint(0,24))
        for row, tiles in enumerate(self.map_data):
            print(row)
            for col, tile in enumerate(tiles):
                print(col)
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row) 
                if tile == 'E':
                    Enemy(self, col, row)
                if tile == 'C':
                    Coin(self, col, row)
                if tile == 'S':
                    Shield(self, col, row)
           
    
    def new(self):
        # init all variables, set up groups, instantiate classes etc
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.shield = pg.sprite.Group()
        # create player object - top left corner will be (10,10)
        # self.player = Player(self, 10, 10)
        # create 10 unit rectangle
        # for x in range(10, 20):
            # Wall(self, x, 5)
        for row, tiles in enumerate(self.map_data): # function - creates tuples of 2 elements, tuple[0] being the index and tuple[1] being the actual element
            print(tiles)
            for col, tile in enumerate(tiles):
                print(tile)
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row) 
                if tile == 'E':
                    Enemy(self, col, row)
                if tile == 'C':
                    Coin(self, col, row)
                if tile == 'S':
                    Shield(self, col, row)
        self.all_sprites.add(self.player)

    def run(self): 
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
    
    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # updating all sprites
        self.all_sprites.update()
        if self.player.moneybag > 2:
            self.current_level += 1
            self.change_level(levels[self.current_level])

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
    
    def draw_text(self, surface, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        surface.blit(text_surface, text_rect)
    def draw(self):
        self.screen.fill(DARKGREEN)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    # input method
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

            # if event.type == pg.KEYDOWN:
            #     if event.key == pg.K_LEFT:
            #         # moving left
            #         self.player.move(dx=-1)   
            #     if event.key == pg.K_RIGHT:
            #          # moving right
            #         self.player.move(dx=1)
            #     if event.key == pg. K_DOWN:
            #         # moving down
            #         self.player.move(dy=+1) 
            #     if event.key == pg.K_UP:
            #         # moving up
            #         self.player.move(dy=-1)

    # defined the start screen                      
    def show_start_screen(self):
        self.screen.fill(DARKGREY)
        self.draw_text(self.screen, "press any button to start", 24, WHITE, WIDTH/2, HEIGHT/2)
        pg.display.flip()
        self.wait_for_key()
    def show_go_screen(self):
        if not self.running:
            return
        self.screen.fill(DARKGREY)
        self.draw_text(self.screen, "press any button to start", 24, WHITE, WIDTH/2, HEIGHT/2)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pg.KEYUP:
                    waiting = False



# i have instantiated the game class
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
