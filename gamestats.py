

import json

class GameStats:
    """Track statistics for alien Invasion"""

    def __init__(self, game):
        """Initialize statistics"""
        self.settings = game.setting
        self.reset_stat()
        #self.game_active = False
        # High socre should never be reset.
        #self.high_score = 0
        self.hs_file = "highscore.json"
        
        with open(self.hs_file,'r') as f:
            score = json.load(f)
            if not score:
                self.high_score = 0
            else:
                self.high_score = score
        
    def reset_stat(self):
        """Initialize statistics that can change in the game."""
        self.game_time = self.settings.game_time
        self.score = 0
        self.level = 1