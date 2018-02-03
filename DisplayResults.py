from tkinter import *
from Response import Response


class DisplayResults(Frame):
    # GUI Setup
    def __init__(self, master):
        # Initialise Class
        Frame.__init__(self, master)
        self.pack()


# Main
root = Tk()
root.title("Display Results")
app = DisplayResults(root)
root.mainloop()