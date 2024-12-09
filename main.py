import tkinter as tk
from tkinter import messagebox
import random

quotes = [
    "You are amazing just the way you are!",
    "Believe in yourself and all that you are.",
    "Happiness is not by chance, but by choice.",
    "Every day is a new beginning.",
    "Believe you can and you're halfway there."
]

def show_quote():
    quote = random.choice(quotes)
    messagebox.showinfo("Quote of the Day", quote)

def submit_message():
    message = entry_message.get()
    if message:
        messagebox.showinfo("Thank You!", f"Your message: '{message}' has been shared!")
        entry_message.delete(0, tk.END)  
    else:
        messagebox.showwarning("Input Error", "Please write something positive!")

root = tk.Tk()
root.title("Feel Good App")
root.geometry("400x300")
root.config(bg="#FCE4EC")  

label_welcome = tk.Label(root, text="Welcome to the Feel Good App!", font=("Arial", 16), bg="#FCE4EC")
label_welcome.pack(pady=20)

label_message = tk.Label(root, text="Share a positive thought:", font=("Arial", 12), bg="#FCE4EC")
label_message.pack()

entry_message = tk.Entry(root, font=("Arial", 14), width=40)
entry_message.pack(pady=10)

submit_button = tk.Button(root, text="Submit Positive Thought", font=("Arial", 12), command=submit_message)
submit_button.pack(pady=10)

quote_button = tk.Button(root, text="Get a Random Quote", font=("Arial", 12), command=show_quote)
quote_button.pack(pady=10)

root.mainloop()