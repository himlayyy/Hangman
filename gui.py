import pygame
import os
import sys
from settings import Settings
import game_functions as gf
from letters import Letter, Menu
import string
from words import words_list

#TO DO:
#1. I-refactor ang pygame events while loop nga mausa siya
#2. I-refactor ang pag update ug events sa screen
#
#


def end_screen(main_screen, streak):

    end_menu = create_menu(["Quit", "Try Again"])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                for menu in end_menu:
                    menu.on_mousemotion(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    for menu in end_menu:
                        choice = menu.menu_select()
                        if choice == "Quit":
                            sys.exit()
                        else:
                            run_game(main_screen, clock, game_settings, streak)

        main_screen.fill(game_settings.bg_color)
        gf.draw_scene_title(["Game over!", f"Streak: {streak}"], main_screen)
        for menu in end_menu:
            menu.update_letters(main_screen)
        pygame.display.flip()



def run_game(main_screen, clock, game_settings):
    streak = 0

    def one_round(main_screen, clock, game_settings, streak):

        letter_pile = gf.draw_letters()


        #Gets and draws word
        word, dash_word, word_set = gf.get_word()
        print(word, dash_word)
        gf.draw_word(dash_word, game_settings, main_screen)


        lives = 7
        gf.draw_gallow(main_screen, lives)

        picked_letters = []
        dead = False
        won = False

        while not won and not dead:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.MOUSEMOTION:
                    for letter in letter_pile:
                        letter.on_mousemotion(event)

                elif event.type == pygame.MOUSEBUTTONUP:

                    if event.button == 1:
                        for letter in letter_pile:
                            letter.on_click(picked_letters)


                    print(f"picked letters {picked_letters}")
                    lives = gf.check_pick(picked_letters, word_set, lives,)
                    print(lives)
                    won = gf.check_won(picked_letters, word_set)
                    dead = gf.check_dead(lives)


                    #Check if midaog na ba ka

                    dash_word = gf.update_word(picked_letters, word, dash_word)


            main_screen.fill(game_settings.bg_color)

            for letter in letter_pile:
                letter.update_letters(main_screen)
            gf.draw_word(dash_word, game_settings, main_screen)
            gf.draw_gallow(main_screen, lives)
            gf.update_lives(main_screen, lives)
            gf.update_streak(main_screen, streak)


            pygame.display.flip()
            clock.tick(20)
        return won

    game_over = False

    while not game_over:
        if one_round(main_screen, clock, game_settings, streak):
            streak += 1
        else:
            game_over = True
            end_screen(main_screen, streak)


def create_menu(options):
    menus = []

    menu_box_height = 75
    menu_box_width = 200
    menu_box_x = 165
    menu_box_y = 300
    spacer = 10

    for count, i in enumerate(options):
        lt = Menu(i, menu_box_x, menu_box_y, menu_box_width, menu_box_height)
        menus.append(lt)
        menu_box_y = menu_box_y + menu_box_height + spacer

    return menus


pygame.init()

clock = pygame.time.Clock()
game_settings = Settings()

main_screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
main_screen.fill(game_settings.bg_color)
pygame.display.set_caption("Hangman")


menus = create_menu(["Start", "Quit"])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            for menu in menus:
                menu.on_mousemotion(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                for menu in menus:
                    choice = menu.menu_select()
                    if choice == "Start":
                        run_game(main_screen, clock, game_settings)
                    else:
                        sys.exit()

    main_screen.fill(game_settings.bg_color)
    gf.draw_scene_title(["HANGMAN"], main_screen)
    for menu in menus:
        menu.update_letters(main_screen)

    pygame.display.flip()
    clock.tick(20)

