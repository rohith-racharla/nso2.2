# Import the tkinter library for creating the GUI
import tkinter as tk

# Create the main application window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("400x500") # Set the size of the window
window.resizable(False, False) # Make the window not resizable

# Global variable to store the expression
expression = ""

# --- Function Definitions ---

# Function to update the expression in the entry field
def set_expression(text):
    """Updates the display with the given text."""
    entry_field.delete(0, tk.END)
    entry_field.insert(0, text)

# Function to handle button clicks (numbers and operators)
def button_click(item):
    """Appends the clicked item (number or operator) to the global expression."""
    global expression
    expression += str(item)
    set_expression(expression)

# Function to clear the entire expression
def button_clear():
    """Clears the global expression and the display."""
    global expression
    expression = ""
    set_expression("")

# Function to calculate and display the result
def button_equal():
    """Evaluates the expression and shows the result."""
    global expression
    try:
        # The eval() function evaluates the passed string as a Python expression
        # and returns the result.
        result = str(eval(expression))
        set_expression(result)
        # It's good practice to reset the expression to the result,
        # so the user can use the result in the next calculation.
        expression = result
    except Exception as e:
        # Handle errors like division by zero or syntax errors
        set_expression("Error")
        expression = ""

# --- GUI Layout ---

# Create a frame for the display
display_frame = tk.Frame(window, bg="#222222")
display_frame.pack(expand=True, fill="both")

# Create the entry field for showing the expression/result
entry_field = tk.Entry(
    display_frame,
    font=('Arial', 24, 'bold'),
    textvariable=tk.StringVar(),
    relief=tk.FLAT,
    bg="#222222",
    fg="#FFFFFF",
    justify='right'
)
entry_field.pack(expand=True, fill="both", padx=10, pady=20)

# Create a frame for the buttons
button_frame = tk.Frame(window, bg="#2a2d36")
button_frame.pack(expand=True, fill="both")

# --- Button Creation and Placement ---

# Define the button layout in a list of lists
button_layout = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '.', '+']
]

# Create and place buttons for numbers and operators
for row_index, row_list in enumerate(button_layout):
    button_frame.rowconfigure(row_index, weight=1)
    for col_index, button_text in enumerate(row_list):
        button_frame.columnconfigure(col_index, weight=1)
        if button_text == 'C':
            # Special case for the 'Clear' button
            btn = tk.Button(
                button_frame,
                text=button_text,
                font=('Arial', 18),
                relief=tk.GROOVE,
                border=0,
                command=button_clear
            )
        else:
            # For all other number and operator buttons
            btn = tk.Button(
                button_frame,
                text=button_text,
                font=('Arial', 18),
                relief=tk.GROOVE,
                border=0,
                command=lambda item=button_text: button_click(item)
            )
        btn.grid(row=row_index, column=col_index, sticky="nsew", padx=1, pady=1)

# Create and place the 'equals' button
# It spans all columns in the last row
equal_button = tk.Button(
    button_frame,
    text="=",
    font=('Arial', 18),
    relief=tk.GROOVE,
    border=0,
    command=button_equal
)
equal_button.grid(row=4, column=0, columnspan=4, sticky="nsew", padx=1, pady=1)
button_frame.rowconfigure(4, weight=1)


# --- Start the application's main loop ---
window.mainloop()
