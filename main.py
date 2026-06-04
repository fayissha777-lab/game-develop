#!/usr/bin/env python3
"""
Cricket Game - Main Entry Point

A simple command-line cricket game where you can play as a batsman or bowler.
"""

from game.match import Match


def get_player_names() -> tuple[str, str]:
    """Get player names from user"""
    print("\n🏏 Welcome to Cricket Game!")
    print("="*50)
    
    batsman_name = input("Enter batsman's name: ").strip() or "Batsman"
    bowler_name = input("Enter bowler's name: ").strip() or "Bowler"
    
    return batsman_name, bowler_name


def get_overs() -> int:
    """Get number of overs for the match"""
    while True:
        try:
            overs = int(input("Enter number of overs (1-5, default 1): ").strip() or "1")
            if 1 <= overs <= 5:
                return overs
            print("Please enter a number between 1 and 5")
        except ValueError:
            print("Please enter a valid number")


def main():
    """Main game loop"""
    play_again = True
    
    while play_again:
        # Get player details
        batsman_name, bowler_name = get_player_names()
        overs = get_overs()
        
        # Create and play match
        match = Match(batsman_name, bowler_name, overs)
        match.play_match()
        
        # Ask to play again
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        play_again = again in ['yes', 'y']
        
        if play_again:
            print("\n" + "="*50)
    
    print("\nThanks for playing! 🏏")


if __name__ == "__main__":
    main()
