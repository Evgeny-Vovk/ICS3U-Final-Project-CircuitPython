#!/usr/bin/env python3

# Created by: Evgeny Vovk
# Created on: 2022 Oct
# This file is the splash/first scene for Battle City on PyBadge.

import ugame
import stage
import constants
import time


def splash_scene():
    # this function is the main game game_scene

    # get sound ready
    coin_sound = open("coin.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    background = stage.Grid(
        image_bank_background,
        constants.SCREEN_GRID_X,
        constants.SCREEN_GRID_Y,
    )

    # used this program to split the image into tile:
    # https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [background]
    game.render_block()

    while True:
        # Wait for 2 seconds
        time.sleep(2.0)
        menu_scene()

def menu_scene():
    # this function is the main game game_scene


    # used this program to split the image into tile:
    # https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png

    position_of_tiles_x = 0
    position_of_tiles_y = 0
    tile = 0
    tiles = []
    image_bank_background = stage.Bank.from_bmp16("menu_background_part_one.bmp")
    while tile < 16:
        a_single_tile = stage.Sprite(
            image_bank_background,
            tile,
            position_of_tiles_x,
            position_of_tiles_y,
        )
        position_of_tiles_x += 16
        tile += 1
        if position_of_tiles_x == 160:
            position_of_tiles_y += 16
            position_of_tiles_x = 0
        tiles.append(a_single_tile)
    tile = 0

    image_bank_background = stage.Bank.from_bmp16("menu_background_part_two.bmp")
    while tile < 16:
        a_single_tile = stage.Sprite(
            image_bank_background,
            tile,
            position_of_tiles_x,
            position_of_tiles_y,
        )
        position_of_tiles_x += 16
        tile += 1
        if position_of_tiles_x == 160:
            position_of_tiles_y += 16
            position_of_tiles_x = 0
        tiles.append(a_single_tile)
    tile = 0

    image_bank_backgroundp3 = stage.Bank.from_bmp16("menu_background_part_three.bmp")
    while tile < 16:
        if tile == 10:
            tile += 1
            continue
        elif tile == 11:
            a_single_tile = stage.Sprite(
            image_bank_backgroundp3,
            tile,
            position_of_tiles_x,
            position_of_tiles_y,
            )
            position_of_tiles_x += 16
            if position_of_tiles_x == 160:
                position_of_tiles_y += 16
                position_of_tiles_x = 0
            tiles.append(a_single_tile)
        a_single_tile = stage.Sprite(
            image_bank_backgroundp3,
            tile,
            position_of_tiles_x,
            position_of_tiles_y,
        )
        position_of_tiles_x += 16
        tile += 1
        if position_of_tiles_x == 160:
            position_of_tiles_y += 16
            position_of_tiles_x = 0
        tiles.append(a_single_tile)
    tile = 0

    image_bank_background = stage.Bank.from_bmp16("menu_background_part_four.bmp")
    while tile < 16:
        a_single_tile = stage.Sprite(
            image_bank_background,
            tile,
            position_of_tiles_x,
            position_of_tiles_y,
        )
        position_of_tiles_x += 16
        tile += 1
        if position_of_tiles_x == 160:
            position_of_tiles_y += 16
            position_of_tiles_x = 0
        tiles.append(a_single_tile)
    tile = 0

    image_bank_background = stage.Bank.from_bmp16("menu_background_part_five.bmp")
    while tile < 16:
        a_single_tile = stage.Sprite(
            image_bank_background,
            tile,
            position_of_tiles_x,
            position_of_tiles_y,
        )
        position_of_tiles_x += 16
        tile += 1
        if position_of_tiles_x == 160:
            position_of_tiles_y += 16
            position_of_tiles_x = 0
        tiles.append(a_single_tile)

    tank = stage.Sprite(
            image_bank_backgroundp3,
            10,
            30,
            62,
        )

    text = []
    text1 = stage.Text(
        width=209, height=120, font=None, buffer=None
    )
    text1.move(10, 10)
    text1.text("High score:")
    text.append(text1)

    text2 = stage.Text(
        width=29, height=12, font=None, buffer=None
    )
    text2.move(50, 69)
    text2.text("Play")
    text.append(text2)

    text3 = stage.Text(
        width=29, height=12, font=None, buffer=None
    )
    text3.move(50, 85)
    text3.text("Controls")
    text.append(text3)


    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [tank] + text + tiles
    game.render_block()

    mode = 0
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_UP != 0:
            tank.move(30, 62)
            mode = 0
        if keys & ugame.K_DOWN != 0:
            tank.move(30, 78)
            mode = 1
        if keys & ugame.K_START != 0:
            if mode == 0:
                level_one_scene()
            elif mode == 1:
                controls_scene()

        # redraw Sprites
        game.render_sprites([tank])
        game.tick()

def controls_scene():
    pass

def level_one_scene():
    game_start = open("game_start.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(game_start)

    position_of_tiles_x = 80
    position_of_tiles_y = 32
    tile = 0
    level_tiles = []
    image_level_bank_background = stage.Bank.from_bmp16("level_one_backgroundp1.bmp")
    while tile < 16:
        a_single_tile = stage.Sprite(
            image_level_bank_background,
            tile,
            position_of_tiles_x,
            position_of_tiles_y,
        )
        position_of_tiles_x += 16
        tile += 1
        if position_of_tiles_x == 160:
            position_of_tiles_y += 16
            position_of_tiles_x = 0
        level_tiles.append(a_single_tile)
    tile = 0

    image_level_bank_background = stage.Bank.from_bmp16("level_one_backgroundp2.bmp")
    while tile < 16:
        a_single_tile = stage.Sprite(
            image_level_bank_background,
            tile,
            position_of_tiles_x,
            position_of_tiles_y,
        )
        position_of_tiles_x += 16
        tile += 1
        if position_of_tiles_x == 160:
            position_of_tiles_y += 16
            position_of_tiles_x = 0
        level_tiles.append(a_single_tile)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = level_tiles
    game.render_block()

    while True:
        # Wait for 4 seconds
        time.sleep(4.3)
        level_one_game_scene()

def level_one_game_scene():
    level_start = open("game_sound.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(level_start, loop = True)
    

if __name__ == "__main__":
    splash_scene()
