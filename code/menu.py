#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import pygame as pg
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):

        menu_option = 0
        pg.mixer_music.load('./asset/Menu.mp3')
        pg.mixer_music.play(-1) #-1 music play infinitely

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Moutain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70 ))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2),  120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 1.9), 200 + 25 * i ))

                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i ))



        # Check for all events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                     pg.quit() #close window
                     quit() #end pygame

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN:
                        if menu_option < 4:
                            menu_option += 1

                    if event.key == pg.K_UP:
                        if menu_option > 0:
                            menu_option -= 1

                    if event.key == pg.K_RETURN:
                        return MENU_OPTION[menu_option]

            pg.display.flip()




    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name= 'Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)