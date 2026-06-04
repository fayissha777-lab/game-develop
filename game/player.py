"""Player classes for cricket game"""

from enum import Enum
from dataclasses import dataclass


class Role(Enum):
    """Player role in the game"""
    BATSMAN = "Batsman"
    BOWLER = "Bowler"


@dataclass
class Stats:
    """Player statistics"""
    runs: int = 0
    wickets: int = 0
    balls_faced: int = 0
    balls_bowled: int = 0
    sixes: int = 0
    fours: int = 0
    outs: int = 0
    
    def __str__(self):
        return f"Runs: {self.runs}, Wickets: {self.wickets}, Balls: {self.balls_faced}"


class Player:
    """Base Player class"""
    
    def __init__(self, name: str, role: Role):
        self.name = name
        self.role = role
        self.stats = Stats()
        self.is_out = False
        
    def __str__(self):
        return f"{self.name} ({self.role.value})"


class Batsman(Player):
    """Batsman player"""
    
    def __init__(self, name: str):
        super().__init__(name, Role.BATSMAN)
        self.consecutive_failures = 0
        self.current_runs = 0
        
    def reset_failures(self):
        """Reset consecutive failures counter"""
        self.consecutive_failures = 0
        
    def add_failure(self):
        """Add a failure"""
        self.consecutive_failures += 1
        self.stats.balls_faced += 1
        
    def score_runs(self, runs: int):
        """Score runs"""
        self.current_runs += runs
        self.stats.runs += runs
        self.stats.balls_faced += 1
        self.reset_failures()
        
        if runs == 6:
            self.stats.sixes += 1
        elif runs == 4:
            self.stats.fours += 1
            
    def get_out(self):
        """Mark batsman as out"""
        self.is_out = True
        self.stats.outs += 1


class Bowler(Player):
    """Bowler player"""
    
    def __init__(self, name: str):
        super().__init__(name, Role.BOWLER)
        self.consecutive_dots = 0
        self.balls_bowled_count = 0
        
    def bowl_ball(self):
        """Record a bowled ball"""
        self.balls_bowled_count += 1
        self.stats.balls_bowled += 1
        
    def take_wicket(self):
        """Record a wicket"""
        self.stats.wickets += 1
        
    def add_dot(self):
        """Add a dot ball"""
        self.consecutive_dots += 1
