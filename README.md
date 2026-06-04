# Cricket Game 🏏

A simple command-line cricket game where you can play as a batsman or bowler.

## Features

- **Play as Batsman**: Face bowled balls and try to score runs
- **Play as Bowler**: Bowl and try to get the batsman out
- **Score Tracking**: Track runs, wickets, and match statistics
- **Interactive Gameplay**: Real-time decision making during play

## Requirements

- Python 3.6+
- No external dependencies required

## Installation

Clone the repository:
```bash
git clone https://github.com/fayissha777-lab/game-develop.git
cd game-develop
```

## How to Play

Run the main game:
```bash
python main.py
```

### Game Modes

1. **Batsman Mode**: You face bowled balls and decide whether to:
   - Play a defensive shot
   - Play an aggressive shot
   - Duck/Avoid

2. **Bowler Mode**: You bowl to the batsman with different types of deliveries:
   - Fast ball
   - Spin
   - Yorker

## Game Rules

- Batsman gets out on:
  - 3 consecutive failures
  - Bowled by a perfect delivery
  - Caught after aggressive play
  
- Runs are scored based on shot type and delivery type
- Match ends after 6 balls per over

## File Structure

```
game-develop/
├── README.md
├── main.py           # Game entry point
├── game/
│   ├── __init__.py
│   ├── player.py     # Player classes
│   ├── match.py      # Match logic
│   └── utils.py      # Utility functions
└── tests/
    ├── __init__.py
    └── test_game.py  # Test cases
```

## Contributing

Feel free to fork, modify, and enhance the game!

## License

Open source - feel free to use and modify.
