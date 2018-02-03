from tkinter import *
from Response import Response


class DisplayResults(Frame):
    # GUI Setup
    def __init__(self, master):
        # Initialise Class
        Frame.__init__(self, master)
        self.pack()

    def retrieveResponse(self):
        # retrieve responses from database
        countAll = 0
        sumQ1SE = 0.0
        sumQ2SE = 0.0
        sumQ3SE = 0.0
        sumP1Joints = 0
        sumP2Joints = 0
        sumP3Joints = 0
        sumP4Joints = 0
        sumP5Joints = 0
        sumP6Joints = 0


# Main
root = Tk()
root.title("Display Results")
app = DisplayResults(root)
root.mainloop()