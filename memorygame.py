import tkinter as tk
from tkinter import PhotoImage
import random

# Initialize the main window
root = tk.Tk()
root.title("Memory Game")
root.geometry("650x700")  # Fixed window size for 13-inch laptop
root.resizable(False, False)  # Disable window resizing

# Set up the game board size (4x4 grid)
GRID_SIZE = 4

# Load and resize the logo (resize externally or use subsample for rough sizing)
logo = PhotoImage(file="/Users/kiahvaidya/Desktop/MemoryGame/images/logo.png").subsample(3, 3)

# Create a frame to hold everything, fixed size to prevent resizing
frame = tk.Frame(root, width=650, height=600)
frame.pack(pady=10)
frame.grid_propagate(False)  # Prevent frame from resizing with its content

# Logo at the top
logo_label = tk.Label(frame, image=logo)
logo_label.grid(row=0, column=0, columnspan=GRID_SIZE, pady=10)

# Load 8 images (make sure all images are 100x100 px PNGs)
images = [
    PhotoImage(file=f"/Users/kiahvaidya/Desktop/MemoryGame/images/image{i}.png")
    for i in range(1, 9)
]

# Create 16 cards (8 pairs) and shuffle
cards = images * 2
random.shuffle(cards)

# Track game state
first_card = None
first_button = None
attempts = 0

def flip_card(row, col, button):
    global first_card, first_button, attempts

    # If button already shows image or it's the same button, ignore
    if button["image"] != "" or first_button == button:
        return

    index = row * GRID_SIZE + col
    button.config(image=cards[index])
    button.update()

    if first_card is None:
        first_card = (row, col)
        first_button = button
    else:
        second_card = (row, col)
        second_button = button
        attempts += 1

        i1 = first_card[0] * GRID_SIZE + first_card[1]
        i2 = second_card[0] * GRID_SIZE + second_card[1]

        if cards[i1] == cards[i2]:
            # Matched pair: leave revealed
            first_card, first_button = None, None
        else:
            # Not matched: flip back after 500 ms
            root.after(500, hide_cards, first_button, second_button)
            first_card, first_button = None, None

def hide_cards(btn1, btn2):
    btn1.config(image="")
    btn2.config(image="")

# Create the grid of buttons WITHOUT width/height params so buttons fit image size exactly
buttons = []
for row in range(GRID_SIZE):
    row_buttons = []
    for col in range(GRID_SIZE):
        button = tk.Button(
            frame,
            image="",  # start with no image shown
            command=lambda r=row, c=col: flip_card(r, c, buttons[r][c])
        )
        button.grid(row=row + 1, column=col, padx=10, pady=10)  # padding for spacing
        row_buttons.append(button)
    buttons.append(row_buttons)

root.mainloop()
