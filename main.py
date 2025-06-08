import tkinter as tk

def get_input():
    # Retrieve the text entered by the user in the Entry field
    user_input = entry.get()
    # Update the Label to display the user's input
    label.config(text=f"You entered: {user_input}")

# Create the main window of the application
root = tk.Tk()
# Create an Entry field for user input
entry = tk.Entry(root)
entry.pack()  # Add the Entry field to the window
# Create a Button to trigger the get_input function
btn = tk.Button(root, text="Submit", command=get_input)
btn.pack()  # Add the Button to the window
# Create a Label to display the user's input
label = tk.Label(root, text="")
label.pack()  # Add the Label to the window
# Start the Tkinter event loop
root.mainloop()