import pygame
import sys
import string
import random
from words import words_list
from letters import Letter, Menu


def get_word():
    word = random.choice(words_list)
    while " " in word or "-" in word:
        word = random.choice(words_list)
    dash_word = dashify(word)
    return word, dash_word, set(word)


def draw_word(dash_word, game_settings, main_screen):
    word_font = pygame.font.SysFont("couriernew", 40)
    the_dash_word = word_font.render(dash_word, True, (230, 0, 0))
    dash_word_rect = the_dash_word.get_rect(
        center=(int(game_settings.screen_width / 2), int(game_settings.screen_height_third * 1.82)))
    main_screen.blit(the_dash_word, dash_word_rect)


def draw_letters():
    letter_box_height = 40
    letter_box_width = 40
    letter_box_x = 20
    letter_box_y = 400
    spacer = 10

    letter_pile = []
    for count, i in enumerate(string.ascii_lowercase):
        lt = Letter(i, letter_box_x, letter_box_y, letter_box_width, letter_box_height)
        letter_pile.append(lt)
        letter_box_x = letter_box_x + letter_box_width + spacer
        if count == 9 or count == 19:
            letter_box_y = letter_box_y + letter_box_height + spacer
            if count == 9:
                letter_box_x = 20
            elif count == 19:
                letter_box_x = 120
    return letter_pile


def dashify(word):
    dash_word = "".join("-" for char in word)
    return dash_word


def update_word(picked_letters, word, dash_word):
        dwu = list(dash_word)
        for count, c in enumerate(word):
            if c in picked_letters:
                dwu[count] = c
        dw = lambda x: "".join(x)
        dash_word = (dw(dwu))
        print(f" dash word {dash_word}")
        return dash_word


def check_pick(picked_letters, word_set, lives):
    print(f"In check pick: lives {lives}")
    try:
        if picked_letters[-1] not in word_set:
            print("Letter not in word_guess")
            picked_letters.pop()
            print(f"Removed wrong letters, new picked set {picked_letters}")
            lives -= 1
    except IndexError:
        pass
    return lives


def draw_gallow(main_screen, lives):
    gallow = pygame.Rect(150, 50, 5, 250)
    stand = pygame.Rect(100, gallow.bottom,100,5 )
    hanger = pygame.Rect(gallow.x, gallow.y, 100, 5)

    if lives < 7:
        rope = pygame.Rect(hanger.bottomright[0] - 5 , hanger.bottomright[1], 5, 20)
        pygame.draw.rect(main_screen, (120, 20, 10), rope)

    if lives < 6:
        head = pygame.draw.circle(main_screen, (120, 20, 10), (rope.midbottom[0], rope.midbottom[1] + 20), 25, 5)
    if lives < 5:
        torso = pygame.Rect(rope.left, rope.bottom + 40, 5, 80)
        pygame.draw.rect(main_screen, (120, 20, 10), torso)

    if lives < 4:
        left_hand = pygame.draw.line(main_screen, (120, 20, 10), (torso.midtop[0], torso.midtop[1]+20), (227,155), 5)
    if lives < 3:
        right_hand = pygame.draw.line(main_screen, (120, 20, 10), (torso.midtop[0], torso.midtop[1]+20), (267, 155), 5)
    if lives < 2:
        left_foot = pygame.draw.line(main_screen, (120, 20, 10), (torso.midbottom[0], torso.midbottom[1]), (227, 235), 5)
    if lives < 1:
        left_foot = pygame.draw.line(main_screen, (120, 20, 10), (torso.midbottom[0], torso.midbottom[1]), (267, 235), 5)

    pygame.draw.rect(main_screen, (120, 20, 10), gallow)
    pygame.draw.rect(main_screen, (120, 20, 10), stand)
    pygame.draw.rect(main_screen, (120, 20, 10), hanger)


def check_lives(lives):
    print(f"In check lives: lives left = {lives}")
    lives = lives - 1
    print(f"In check lives: lives  - 1 = {lives}")
    return lives


def check_won(picked_letters, word_set):
    # if word_set.issubset(set(picked_letters)):
    if word_set == set(picked_letters):
        return True
    else:
        return False


def check_dead(lives_left):
    if lives_left <= 0:
        return True
    else:
        return False


def update_lives(main_screen, lives):
    lives_font = pygame.font.SysFont("couriernew", 15)
    lives_display = lives_font.render(f"Lives left: {str(lives)}", True, (pygame.Color('red')))
    main_screen_rect = main_screen.get_rect()
    lives_display_rect = lives_display.get_rect(topleft =(main_screen_rect.left + 10, main_screen_rect.top + 10))
    main_screen.blit(lives_display, lives_display_rect)


def update_streak(main_screen, streak):
    streak_font = pygame.font.SysFont("couriernew", 15)
    streak_display = streak_font.render(f"Streak: {str(streak)}", True, (pygame.Color('green')))
    main_screen_rect = main_screen.get_rect()
    streak_display_rect = streak_display.get_rect(topleft=(main_screen_rect.left + 10, main_screen_rect.top + 25))
    main_screen.blit(streak_display, streak_display_rect)

def draw_scene_title(titles, main_screen):
    title_font = pygame.font.SysFont("couriernew", 45)
    y = main_screen.get_rect().centery - (10 * len(titles)) - ((52 * len(titles)))
    # y = main_screen.get_rect().top + 200
    for i, title in enumerate(titles, 1):
        title_display = title_font.render(title, True, (pygame.Color('green')))
        title_rect = title_display.get_rect(center=(main_screen.get_rect().centerx, y))
        main_screen.blit(title_display, title_rect)
        y = y + (52 * i) + (10 * i)
        # print(title_rect.bottom - title_rect.top)









