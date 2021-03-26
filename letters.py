import pygame
import string

class Button(object):
    bg_color = pygame.Color('white')
    letter_color = pygame.Color('navy')
    picked_letter_color = pygame.Color('red')
    hover_color = pygame.Color('dodgerblue')
    picked_color = pygame.Color("black")

    pygame.font.init()
    letters_font = pygame.font.SysFont("couriernew", 35, bold=True)

    def __init__(self, letter, letter_box_x, letter_box_y, letter_box_width, letter_box_height):
        self.letter_box_width = letter_box_width
        self.letter_box_height = letter_box_height
        self.name = letter

        self.in_word = False
        self.picked = False
        self.mouse_hovering = False
        self.letter_box_color = Button.bg_color

        self.letter_box_x = letter_box_x
        self.letter_box_y = letter_box_y

        self.click_count = 0

        self.letter_box = pygame.Rect((self.letter_box_x, self.letter_box_y, self.letter_box_width,
                                       self.letter_box_height))

    def __str__(self):
        return self.name

    def _draw_letters(self, main_screen):
        if self.picked:
            color = Button.picked_color
        elif not self.picked and self.mouse_hovering:
            color = Button.hover_color
        else:
            color = Button.bg_color
        pygame.draw.rect(main_screen, color, self.letter_box)
        text = self.letters_font.render(self.name, True, Button.letter_color)
        text_rect = text.get_rect(center = self.letter_box.center)
        main_screen.blit(text, text_rect)

    def update_letters(self, main_screen):
        if self.picked:
            self.letter_box_color = Button.picked_color
            self.letter_color = Button.picked_color
        if self.mouse_hovering:
            self.letter_box_color = Button.hover_color
        else:
            self.letter_box_color = Button.bg_color

        self._draw_letters(main_screen)

    def on_mousemotion(self, event):

        self.mouse_hovering = self.letter_box.collidepoint(event.pos)



class Letter(Button):
    def __init__(self, letter, letter_box_x, letter_box_y, letter_box_width, letter_box_height):
        super().__init__(letter, letter_box_x, letter_box_y, letter_box_width, letter_box_height)

    def on_click(self, picked_letters):
        if self.mouse_hovering:
            if not self.picked:
                self.picked = True
                print(self.name)
                picked_letters.append(self.name)
            else:
                print(f"{self.name} has been picked")

class Menu(Button):
    def __init__(self, letter, letter_box_x, letter_box_y, letter_box_width, letter_box_height):
        super().__init__(letter, letter_box_x, letter_box_y, letter_box_width, letter_box_height)

    def menu_select(self, ):
        if self.mouse_hovering:
            if not self.picked:
                self.picked = True
                return self.name
            else:
                print(f"{self.name} has been picked")

