import tkinter as tk
from gui.controls import GUIControls
from gui.location_input import LocationInput

def build_gui():
    root = tk.Tk()
    root.title("Ambient Audio Logger")
    root.geometry("300x400")
    root.resizable(False, False)

    # Optional: styling tweaks
    root.configure(bg="#f0f0f0")

    # Inject control buttons
    controls = GUIControls(root)

    # Inject location input fields
    location_widget = LocationInput(root, controls.location)

    root.mainloop()
