        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #set dimensions and properties of button
        self.width, self.height = 200,50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)
