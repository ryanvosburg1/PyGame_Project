class GameStats:
    '''track stats for alien invasion'''

    def __init__(self,ai_game):
        '''initialze stats'''
        self.settings = ai_game.settings
        self.reset_stats()

        #start alien invasion in inactive state
        self.game_active = False

        #high score never resets in game
        self.high_score = 0

    def reset_stats(self):
        '''initialize stats that can change during game'''
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    