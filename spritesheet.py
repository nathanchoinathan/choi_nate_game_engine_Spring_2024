# This fle was created by: Nate Choi

import pygame as pg

FPS = 30

clock = pg.time.Clock()

frames = ["frame1", "frame2", "frame3", "frame4"]

# print(len(frames))
current_frame = 0

frames_length = len(frames)

then = 0

while True:
    # print("forever...")

    clock.tick(FPS)
    now = pg.time.get_ticks()
    if now - then > 1000:
        print(now)
        then = now
    current_frame += 1
    print(frames[current_frame%frames_length])
