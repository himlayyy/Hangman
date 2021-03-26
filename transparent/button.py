import pygame

class Button(object):
    def __init__(self, rect, command, **kwargs):
        self.rect = pygame.Rect(rect)
        self.command = False
        self.hovered = False
        self.hover_text = None
        self.clicked_text = None
        self.process_kwargs(kwargs)
        self.render_text()

    def process_kwargs(self, kwargs):
        settings = {
            "color" : pygame.Color(120, 20, 10),
            "text" : None,
            "font" : None,
            "call_on_release" : True,
            "clicked_color" : None,
            "font_color" : pygame.Color(255, 255, 255),
            "hover_font_color" : None,
            "clicked_font_color" : None,
            "border_color" : pygame.Color(3,56,178),
            "border_hover_color" : pygame.Color(250, 34, 56),
            "disabled" : False,
            "disabled_color" : pygame.Color(255, 3, 119)
            "radius" : 3,
        }

        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError(f"{self.__class__.__name__} has no keyword {kwarg}")
        self.__dict__.update(settings)

        def render_text(self):
            if self.text:
                #Text color if hovered
                if self.hover_font_color:
                    color = self.hover_font_color
                    self.hover_text = self.font.render(self.text, True, color)
                #Text color if clicked
                if self.clicked_font_color:
                    color = self.clicked_font_color
                    self.clicked_text = self.font.render(self.text, True, color)
            #Text color if not clicked or hovered
            self.text = self.font.render(self.text, True, self.fon_color)

        def get_event(self, event):
            #Left click down
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.on_click(event)

            #Left click up
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.on_release(event)

        #Aha man dapita ming click?
        def on_click(self, event):
            #Sa button ba ni click?
            if self.rect.collidepoint(event.pos):
                self.clicked = True
                #If button is still clicked (?)
                if not self.call_on_release:
                    self.function()

        def on_release(self, event):
            #Sa button ming click, so call the button command
            if self.clicked and self.call_on_release::
            #If user is still within button rect upon mouse release
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.command()
            self.clicked = False

        #Check if sa button ba ang hover
        def check_hover(self):
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                if not self.hovered:
                    self.hovered = True
            else:
                self.hovered = False

        def draw(self, surface):
            color = self.color
            text = self.clicked_text
            border = self.border_color
            self.check_hover()

            #Ani i-draw ang button based sa event HOVERED OR PICKED
            if not self.disabled:
                if self.clicked and self.clicked_color:
                    color = self.clicked_color
                    if self.clicked_font_color:
                        text = self.clicked_text
                elif self.hovered and self.hover_color:
                    color = self.hover_colo
                    if self.hover_font_color:
                        text - self.hover_text

                if self.hovered and not self.clicked:
                    border - self.border_hover_color
            else:
                color = self.disabled_color

            if self.radius:
                rad = self.radius
            else:
                rad = 0
            self.round_rect(surface, self.rect, border, rad, 1, color)
            if self.text:
                text_rect = text.get_rect(center=self.rect.center)
                surface.blit(text, text_rect)

        def round_rect(self, surface, rect, color, rad=20, border=0, inside=(0, 0, 0)):
            rect = pygame.Rect(rect)
            zeroed_rect = rect.copy()
            zeroed_rect = rect.copy()
            #Ani usbon para sa coords sa letters, start with a
            zeroed_rect.topletf = 0, 0
            image = pygame.Surface(rect.size).convert_alpha()
            image.fill((0, 0, 0, 0))
            self._render_region(image, zeroed_rect, color, rad)
            if border:
                zeroed_rect.inflate_ip(-2 * border, -2 * border)
                self._render_region(image, zeroed_rect, inside, rad)
            surface.blit(image, rect)

        def _render_region(self, image, rect, color, rad):
            corners = rect.inflate(-2 * rad, 0)
            for attribute in ("topleft", "topright", "bottomleft", "bottomright"):
                pygame.draw.circle(image,color, getattr(corners, attribute), rad)

            image.fill(color, rect.inflate(-2 * rad, 0))
            image.fill((color, rect.inflate(0, -2 *rad))

        def update(self):
            #for completeness
            pass


