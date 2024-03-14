# This file was created by: Nate Choi
 
# import necessary modules
# my first source control edit
# test
# test number 2
import pygame as pg 
import sys
from settings import *
from sprites import *
from random import randint
from os import path
from time import sleep

# this is a function!
def draw_text():
    pass

# initializing the class
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        self.running = True
    # we have defined the run method in our game engine
    
    # load save game data
    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)
    
    def new(self):
        # init all variables, set up groups, instantiate classes etc
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = pg.sprite.Group()
        self.coin = pg.sprite.Group()
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

    def run(self): 
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
    def quite(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
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
                            
    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass
# i have instantiated the game class
g = Game()
# g.show_start_screen()
while True:
    g.new()
    g.run()
    # g.show_go_screen()
