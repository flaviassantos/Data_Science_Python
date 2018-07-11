"""
Usage: 

python calculator.py

"""

from tkinter import * 
from tkinter import ttk

class Calculator:

    
    initial_value = 0.0  

    # Tack operation clicked
    division_check = False 
    mult_check = False
    add_check = False
    sub_check = False

   # Constructor:
    def __init__(self, app):
        # Stores the values clicked
        self.content = StringVar(app, value="") 

        app.title("Simple Python Calculator by Flavia")
        app.geometry("838x490")
        app.resizable(width=True, height=True)

        # Style for the buttons and screen
        style = ttk.Style()

        style.configure("TButton",
                        font='helvetica 16',
                        padding=30,
                        relief=RAISED,
                        background="blue",
                        disabledbackground="#1E6FBA",
                        foreground='blue',
                        border=2)
                        

        style.configure("TEntry",
                        font="Serif 26 bold",
                        padding=30,
                        relief=SUNKEN,
                        disabledbackground="#1E6FBA",
                        highlightbackground="black",
                        border=2,
                        foreground='blue',
                        background="blue")

        # Create the digit entry box
        self.entry_digit = ttk.Entry(app, 
                                        justify="center",
                                        #disabledbackground="#1E6FBA",
                                        font=("Calibri",25),
                                        textvariable=self.content, 
                                        width=45)
        self.entry_digit.grid(row=0, columnspan=4, pady=5, padx= 5)


            # ----- 1st Row grid -----

        self.btn_4 = ttk.Button(app, text="7", command=lambda: self.btn_click('7')).grid(row=1, column=0)
        self.btn_8 = ttk.Button(app, text="8", command=lambda: self.btn_click('8')).grid(row=1, column=1)
        self.btn_9 = ttk.Button(app, text="9", command=lambda: self.btn_click('9')).grid(row=1, column=2)        
        self.btn_add = ttk.Button(app, text="+", command=lambda: self.math_click('+')).grid(row=1, column=3)

        # ----- 2nd Row grid -----

        self.btn_4 = ttk.Button(app, text="4", command=lambda: self.btn_click('4')).grid(row=2, column=0)
        self.btn_5 = ttk.Button(app, text="5", command=lambda: self.btn_click('5')).grid(row=2, column=1)
        self.btn_6 = ttk.Button(app, text="6", command=lambda: self.btn_click('6')).grid(row=2, column=2)
        self.btn_sub = ttk.Button(app, text="-", command=lambda: self.math_click('-')).grid(row=2, column=3)


        # ----- 3rd Row grid-----

        self.btn_1 = ttk.Button(app, text="1", command=lambda: self.btn_click('1')).grid(row=3, column=0)
        self.btn_2 = ttk.Button(app, text="2", command=lambda: self.btn_click('2')).grid(row=3, column=1)
        self.btn_3 = ttk.Button(app, text="3", command=lambda: self.btn_click('3')).grid(row=3, column=2)
        self.btn_mult = ttk.Button(app, text="x", command=lambda: self.math_click('*')).grid(row=3, column=3)

        # ----- 4th Row grid-----

        self.btn_0 = ttk.Button(app, text="0", command=lambda: self.btn_click('0')).grid(row=4, column=0)
        self.btn_ac = ttk.Button(app, text="AC", command=lambda: self.btn_click('AC')).grid(row=4, column=1)
        #self.btn_ac = ttk.Button(app, text="AC", command=[lambda: self.btn_click('AC') & self.color_change, background="red"]).grid(row=4, column=1)
        self.btn_equal = ttk.Button(app, text="=", command=lambda: self.equal_click()).grid(row=4, column=2)
        self.btn_div = ttk.Button(app, text="/", command=lambda: self.math_click('/')).grid(row=4, column=3)

        """
        Generic function for combining functions:
    
        def combine_funcs(*funcs):
        def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
        return combined_func
        
        self.testButton = Button(self, text = "test", 
                         command = combine_funcs(func1, func2))
            """
    def change_color(self):
        self.button.configure(background='red')
        
    #   Create the UI:
    
    def btn_click(self, value): 
        """Run when a number button is pressed."""
        # 'All Clear' function:
        if value == 'AC':
            self.entry_digit.delete(0, "end")
            self.entry_digit.insert(0, entry_val)
        
        # Get the current value in the entry window
        entry_val = self.entry_digit.get()

        # Concatenate the new value to the right of it
        entry_val += value

        # Clear the entry box
        self.entry_digit.delete(0, "end")

        # Insert the new value going from left to right
        self.entry_digit.insert(0, entry_val)

   
    def isfloat(self, str_value):
        try:

            float(str_value)
            return True
        except ValueError:
            return False

    
    def math_click(self, value): 
        """
        Handles the mathematic expressions when respectives buttons are pressed
        """
        if self.isfloat(str(self.entry_digit.get())):

            self.add_check = False
            self.sub_check = False
            self.mult_check = False
            self.division_check = False
            self.initial_value = float(self.content.get())

            if value == "/":
                self.division_check = True
            elif value == "*":
                self.mult_check = True
            elif value == "+":
                self.add_check = True
            else:
                self.sub_check = True

            self.entry_digit.delete(0, "end")

    def equal_click(self):

        # Make sure a math button was clicked
        if self.add_check or self.sub_check or self.mult_check or self.division_check:

            if self.add_check:
                result = self.initial_value + float(self.content.get())
            elif self.sub_check:
                result = self.initial_value - float(self.content.get())
            elif self.mult_check:
                result = self.initial_value * float(self.content.get())
            else:
                result = self.initial_value / float(self.content.get())

            self.entry_digit.delete(0, "end")
            self.entry_digit.insert(0, result)


# Get the app window
app = Tk()

# Create the calculator
calc = Calculator(app)

# Run the app until exited 
app.mainloop()