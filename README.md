# Blackjack Game

This is a simple command line blackjack game implemented in Python.

## Game rules

1. The number of cards in the deck is unlimited.
2. There are no jokers.
3. The Jack, Queen and King all count as 10.
4. The ace can count as 11 or 1.
5. The cards in the list have equal odds of being drawn.
6. Cards are not removed from the deck when they are drawn.

## How to play

1. Run the [`main.py`](main.py) script to start the game.
2. Follow the on-screen instructions to play the game.

## Files

- `main.py`(main.py): Contains the main game logic.
- `art.py`(art.py): Contains the ASCII art for the game logo.
- [`.gitignore`](.gitignore): Specifies files and directories that Git should ignore.

## Functions

### `deal_card()`

Deal a random card from the deck.

### `calculate_score(cards)`

Takes a list of cards and returns the score calculated from the cards.

### `compare(user_score, computer_score)`

Compares the user's score with the computer's score and returns the result.

### `play_game()`

Executes the main game loop.

## Example

```sh
python main.py
```

Enjoy playing Blackjack!
