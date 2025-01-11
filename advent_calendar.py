import tkinter as tk
from tkinter import messagebox

# List of ideas for the advent calendar
ideas = [
    "",
    "Write a holiday card for a friend or loved one.",
    "Watch a classic holiday movie.",
    "Decorate a gingerbread house.",
    "Go for a winter walk and enjoy the decorations.",
    "Have a cozy hot chocolate night.",
    "Make DIY holiday ornaments.",
    "Sing or listen to carols.",
    "Plan a random act of kindness.",
    "Wrap some gifts creatively.",
    "Try a new holiday recipe.",
    "Have a board game night with family or friends.",
    "Write down things you're grateful for this year.",
    "Donate to a local food bank or charity.",
    "Light candles and enjoy the warm glow.",
    "Host a holiday crafting night.",
    "Build a snowman or have a snowball fight (if there's snow).",
    "Make a holiday playlist.",
    "Read a winter-themed book.",
    "Make homemade gift tags.",
    "Create a cozy holiday corner at home.",
    "Host a virtual holiday meetup with distant friends.",
    "Write your New Year's resolutions.",
    "Relax and enjoy a quiet moment."
]

# Create the main window
root = tk.Tk()
root.title("Advent Calendar 🎄")
root.geometry("600x700")
root.configure(bg="#2e3a4d")

# Add a title label
title_label = tk.Label(
    root, text="🎄 Christmas Advent Calendar 🎅",
    font=("Arial", 20, "bold"), bg="#2e3a4d", fg="#ffd700"
)
title_label.pack(pady=10)

# Create a frame for the calendar buttons
calendar_frame = tk.Frame(root, bg="#2e3a4d")
calendar_frame.pack(pady=20)

# Callback function for button click
def show_idea(day):
    idea = ideas[day - 1]
    messagebox.showinfo(f"Day {day}", idea)

# Create calendar buttons (4x6 grid for 24 days)
for day in range(1, 25):
    button = tk.Button(
        calendar_frame, text=f"Day {day}", font=("Arial", 12, "bold"),
        bg="#ffd700", fg="#2e3a4d", width=10, height=2,
        command=lambda d=day: show_idea(d)
    )
    button.grid(row=(day - 1) // 4, column=(day - 1) % 4, padx=5, pady=5)

# Add snow animation (basic simulation)
snow_canvas = tk.Canvas(root, width=600, height=200, bg="#2e3a4d", highlightthickness=0)
snow_canvas.pack()

snowflakes = []

# Create snowflakes
for _ in range(100):
    x = random.randint(0, 600)
    y = random.randint(-200, 0)
    size = random.randint(2, 5)
    snowflake = snow_canvas.create_oval(x, y, x + size, y + size, fill="white")
    snowflakes.append((snowflake, size))

def animate_snow():
    for snowflake, size in snowflakes:
        snow_canvas.move(snowflake, 0, size)
        coords = snow_canvas.coords(snowflake)
        if coords[1] > 200:  # If the snowflake goes below the canvas
            snow_canvas.move(snowflake, 0, -200)
    root.after(50, animate_snow)

animate_snow()

# Run the main event loop
root.mainloop()
