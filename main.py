import pygame as pg

pg.init()
print('Setup Start')
window =  pg.display.set_mode(size = (600, 480))
print('Setup Finish')

print('Loop start')
while True:
    #Check for all events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit() #close window
            print('Loop Finish')
            quit() #end pygame
