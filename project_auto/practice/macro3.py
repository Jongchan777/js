import tkinter as tk
import pyautogui

class Macro:
    def __init__(self):
        # Initialize global variables
        self.x = 0
        self.y = 0
        self.clicks = 0

        # Load the saved settings if they exist
        self.load_settings()

        # Create the GUI
        self.create_gui()

    def create_gui(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Macro")

        # Create an entry box for the x-coordinate
        x_label = tk.Label(self.root, text="X-coordinate:")
        x_label.pack()
        self.x_entry = tk.Entry(self.root)
        self.x_entry.pack()
        self.x_entry.insert(0, self.x)

        # Create an entry box for the y-coordinate
        y_label = tk.Label(self.root, text="Y-coordinate:")
        y_label.pack()
        self.y_entry = tk.Entry(self.root)
        self.y_entry.pack()
        self.y_entry.insert(0, self.y)

        # Create an entry box for the number of clicks
        clicks_label = tk.Label(self.root, text="Number of clicks:")
        clicks_label.pack()
        self.clicks_entry = tk.Entry(self.root)
        self.clicks_entry.pack()
        self.clicks_entry.insert(0, self.clicks)

        # Create a button to run the macro
        run_button = tk.Button(self.root, text="Run Macro", command=self.run_macro)
        run_button.pack()

        # Create a button to save the settings
        save_button = tk.Button(self.root, text="Save Settings", command=self.save_settings)
        save_button.pack()

        # Create a button to load the settings
        load_button = tk.Button(self.root, text="Load Settings", command=self.load_settings)
        load_button.pack()

    def save_settings(self):
        # Save the current settings to a file
        self.x = int(self.x_entry.get())
        self.y = int(self.y_entry.get())
        self.clicks = int(self.clicks_entry.get())
        with open("macro_settings.txt", "w") as f:
            f.write(f"{self.x},{self.y},{self.clicks}")

    def load_settings(self):
        # Load the saved settings from a file
        try:
            with open("macro_settings.txt", "r") as f:
                data = f.read()
                self.x, self.y, self.clicks = map(int, data.split(","))
                self.x_entry.delete(0, tk.END)
                self.x_entry.insert(0, self.x)
                self.y_entry.delete(0, tk.END)
                self.y_entry.insert(0, self.y)
                self.clicks_entry.delete(0, tk.END)
                self.clicks_entry.insert(0, self.clicks)
        except FileNotFoundError:
            pass

    def run_macro(self):
        # Move the mouse to the specified coordinates
        pyautogui.moveTo(self.x, self.y)

        # Click the left mouse button the specified number of times
        for i in range(self.clicks):
            pyautogui.click()

    def start(self):
        # Start the GUI
        self.root.mainloop()

# Create an instance of the Macro class and start the GUI
macro = Macro()
macro.start()
