"""Utility functions for cricket game"""

import random
from enum import Enum


class Delivery(Enum):
    """Types of bowling deliveries"""
    FAST_BALL = "Fast Ball"
    SPIN = "Spin"
    YORKER = "Yorker"
    BOUNCER = "Bouncer"


class Shot(Enum):
    """Types of batting shots"""
    DEFENSIVE = "Defensive Shot"
    AGGRESSIVE = "Aggressive Shot"
    DUCK = "Duck (Avoid)"


def get_user_choice(options: dict, prompt: str = "Choose an option") -> str:
    """
    Display options and get user choice
    
    Args:
        options: Dictionary of {key: description}
        prompt: Prompt message
        
    Returns:
        Selected key
    """
    print(f"\n{prompt}:")
    for key, description in options.items():
        print(f"  {key}. {description}")
    
    while True:
        choice = input("\nEnter your choice: ").strip()
        if choice in options:
            return choice
        print("Invalid choice. Please try again.")


def simulate_outcome(success_rate: float) -> bool:
    """
    Simulate outcome based on success rate
    
    Args:
        success_rate: Probability of success (0-1)
        
    Returns:
        True if successful, False otherwise
    """
    return random.random() < success_rate


def get_delivery_effectiveness(delivery: Delivery, shot: Shot) -> tuple[bool, str]:
    """
    Determine if bowler's delivery is effective against batsman's shot
    
    Args:
        delivery: Type of delivery
        shot: Type of shot
        
    Returns:
        Tuple of (is_effective, message)
    """
    # Matrix of delivery vs shot effectiveness
    effectiveness = {
        (Delivery.FAST_BALL, Shot.DEFENSIVE): (0.4, "Blocked safely!"),
        (Delivery.FAST_BALL, Shot.AGGRESSIVE): (0.6, "Good connection!"),
        (Delivery.FAST_BALL, Shot.DUCK): (0.9, "Dodged safely!"),
        
        (Delivery.SPIN, Shot.DEFENSIVE): (0.5, "Managed to defend!"),
        (Delivery.SPIN, Shot.AGGRESSIVE): (0.3, "Tricky delivery!"),
        (Delivery.SPIN, Shot.DUCK): (0.85, "Avoided the spin!"),
        
        (Delivery.YORKER, Shot.DEFENSIVE): (0.2, "Yorker is hard to defend!"),
        (Delivery.YORKER, Shot.AGGRESSIVE): (0.5, "Trying to hit the yorker!"),
        (Delivery.YORKER, Shot.DUCK): (0.7, "Hard to avoid!"),
        
        (Delivery.BOUNCER, Shot.DEFENSIVE): (0.3, "Attempting to block!"),
        (Delivery.BOUNCER, Shot.AGGRESSIVE): (0.7, "Pulling the bouncer!"),
        (Delivery.BOUNCER, Shot.DUCK): (0.9, "Ducked under!"),
    }
    
    success_rate, message = effectiveness.get((delivery, shot), (0.5, "Standard play"))
    is_successful = simulate_outcome(success_rate)
    
    return is_successful, message


def calculate_runs(delivery: Delivery, shot: Shot, is_successful: bool) -> int:
    """
    Calculate runs based on delivery and shot
    
    Args:
        delivery: Type of delivery
        shot: Type of shot
        is_successful: Whether the shot was successful
        
    Returns:
        Number of runs scored
    """
    if not is_successful or shot == Shot.DUCK:
        return 0
    
    # Aggressive shots score more
    if shot == Shot.AGGRESSIVE:
        if delivery == Delivery.FAST_BALL:
            return random.choice([4, 6])
        elif delivery == Delivery.SPIN:
            return random.choice([2, 4])
        else:
            return random.choice([2, 4, 6])
    else:  # Defensive
        return random.choice([1, 2])


def get_out_probability(delivery: Delivery, shot: Shot, is_successful: bool) -> bool:
    """
    Determine if batsman gets out
    
    Args:
        delivery: Type of delivery
        shot: Type of shot
        is_successful: Whether the shot was successful
        
    Returns:
        True if batsman is out
    """
    if is_successful:
        return False
    
    # More likely to get out on aggressive shots
    if shot == Shot.AGGRESSIVE:
        return simulate_outcome(0.5)
    elif shot == Shot.DEFENSIVE:
        return simulate_outcome(0.3)
    else:  # DUCK
        return simulate_outcome(0.1)
