# Memory Game

A classic memory matching game built with Python and Tkinter.

## Overview

This game presents a 4x4 grid of hidden cards. Each card hides an image, and there are 8 pairs of matching images shuffled randomly. The player clicks on two cards at a time to reveal them:

- If the two cards match, they stay revealed.
- If they don’t match, they flip back after a short delay.
- The goal is to match all pairs in the fewest attempts.

## Features

- 4x4 grid layout.
- Custom images for cards and a logo.
- Simple GUI with Tkinter.
- Attempts counter (can be added).

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- Images stored in `/Users/user/Desktop/MemoryGame/images/` folder:
  - `logo.png`
  - `image1.png` through `image8.png` (8 pairs)

Make sure all images are `.png` and sized appropriately (~80x80 pixels).

## How to Run

1. Clone or download the repository.
2. Place your images in the `/images` folder.
3. Run the game with:

   ```bash
   python3 /Users/user/Desktop/MemoryGame/memorygame.py
