import tkinter as tk
from tkinter import messagebox
import pyperclip
import keyboard
from keyboard_dict import keyboard_dict

# Define the function to detect the input language
def detect_input_language(text):
    english_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    hebrew_chars = set("אבגדהוזחטיכלמנסעפצקרשתםןףץ")
    has_english_chars = any((c in english_chars) for c in text)
    has_hebrew_chars = any((c in hebrew_chars) for c in text)
    if has_english_chars and not has_hebrew_chars:
        return "English"
    elif has_hebrew_chars and not has_english_chars:
        return "Hebrew"
    else:
        return "Unknown"

# Define the function to convert the text
def convert_text(original_text):
    converted_text = ""
    for char in original_text:
        if char in keyboard_dict:
            converted_text += keyboard_dict[char]
        else:
            converted_text += char
    return converted_text

# Define the function to copy the transformed text to the clipboard
def copy_transformed_text(converted_text):
    pyperclip.copy(converted_text)

# Define the function to transform the text
def transform_text():
    original_text = pyperclip.paste()
    input_language = detect_input_language(original_text)
    converted_text = convert_text(original_text)
    copy_transformed_text(converted_text)
    instructions_label.config(text=f"Input language: {input_language}, Click the button to transform the highlighted text")
    print("Original text:", original_text)
    print("Transformed text:", converted_text)

# Define the function to run the button function
def run_button_function():
    transform_text()

# Initialize the program with a copied string saying "clip init"
pyperclip.copy("clip init")
messagebox.showinfo(title="How to use", message=f"Run the program with ctrl+shift+i - shift between english and hebrew")


# Create the tkinter window
root = tk.Tk()

# Create a label for the instructions
instructions_label = tk.Label(root, text="Click the button to transform the highlighted text")
instructions_label.pack()

# Create a button to transform the text
transform_button = tk.Button(root, text="Transform", command=run_button_function)
transform_button.pack()

# Register the hotkey Shift+I
keyboard.add_hotkey('ctrl+shift+i', run_button_function, suppress=True)

# Start the tkinter event loop
root.mainloop()


# Stop the hotkey listener when the window is closed
keyboard.unregister_hotkey('ctrl+shift+i')
