import tkinter as tk
import pyautogui

# Initialize global variables
x = 0
y = 0
clicks = 0

def save_settings():
    # Save the current settings to a file
    with open('macro_settings.txt', 'w') as f:
        f.write(f'{x},{y},{clicks}')

def load_settings():
    # Load the saved settings from the file
    global x, y, clicks
    with open('macro_settings.txt', 'r') as f:
        data = f.read()
    x, y, clicks = data.split(',')
    x = int(x)
    y = int(y)
    clicks = int(clicks)

def run_macro():
    # Move the mouse to the specified coordinates
    pyautogui.moveTo(x, y)
    
    # Click the left mouse button the specified number of times
    for i in range(clicks):
        pyautogui.click()

def on_click():
    global x, y, clicks
    x = int(x_entry.get())
    y = int(y_entry.get())
    clicks = int(clicks_entry.get())
    run_macro()

# Load the settings if they exist
try:
    load_settings()
except FileNotFoundError:
    pass

root = tk.Tk()

# Create an entry box for the x-coordinate
x_label = tk.Label(root, text='X-coordinate:')
x_label.pack()
x_entry = tk.Entry(root)
x_entry.pack()
x_entry.insert(0, x)

# Create an entry box for the y-coordinate
y_label = tk.Label(root, text='Y-coordinate:')
y_label.pack()
y_entry = tk.Entry(root)
y_entry.pack()
y_entry.insert(0, y)

# Create an entry box for the number of clicks
clicks_label = tk.Label(root, text='Number of clicks:')
clicks_label.pack()
clicks_entry = tk.Entry(root)
clicks_entry.pack()
clicks_entry.insert(0, clicks)

# Create a button to run the macro
run_button = tk.Button(root, text='Run Macro', command=on_click)
run_button.pack()

# Create a button to save the settings
save_button = tk.Button(root, text='Save Settings', command=save_settings)
save_button.pack()

root.mainloop()
