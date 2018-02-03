from tkinter import *
from tkinter import messagebox
from Response import Response
from DisplayResults import *


class Questionnaire(Frame):
    # GUI Setup
    def __init__(self, master):
        # Initialise Questionnaire Class
        Frame.__init__(self, master)
        self.grid()
        self.createProgSelect()
        self.createTeamExpQuest()
        self.createProblems()
        self.createComments()
        self.createButtons()

    def createProgSelect(self):
        # Create widgets to select a degree programme from a list
        lblProg = Label(self, text='Degree Programme:', font=('MS',13,'bold'))
        lblProg.grid(row=0, column=0, columnspan=2, sticky=NW)

        self.listProg = Listbox(self, height=3)
        scroll = Scrollbar(self, command=self.listProg.yview)
        self.listProg.configure(yscrollcommand=scroll.set)

        self.listProg.grid(row=0, column=2, columnspan=2, sticky=NE)
        scroll.grid(row=0, column=4, columnspan=2, sticky=W)

        for item in ["CS", "CS with", "BIS", "SE", "Joints", ""]:
            self.listProg.insert(END, item)

        self.listProg.selection_set(END)

    def createTeamExpQuest(self):
        # Create widgets to ask Team Experience Questions

        # Create labels for radio button question titles
        lblQuestions = Label(self, text='Team Experience: ', font=('MS',13,'bold'))
        lblQuestions.grid(row=3, column=0, rowspan=2, columnspan=4, sticky=SW)

        lblStrAgr = Label(self, text='Strongly \n Agree', font=('MS',13,'bold'))
        lblStrAgr.grid(row=3, column=4, rowspan=2)

        lblAgr = Label(self, text='Agree', font=('MS',13,'bold'))
        lblAgr.grid(row=3, column=5, rowspan=2)

        lblDisAgr = Label(self, text='Disgree', font=('MS',13,'bold'))
        lblDisAgr.grid(row=3, column=6, rowspan=2)

        lblStrDisAgr = Label(self, text='Strongly \n Disgree', font=('MS',13,'bold'))
        lblStrDisAgr.grid(row=3, column=7, rowspan=2)

        # Add Question text and radio buttons
        lblQ1 = Label(self, text='1. Our team worked together effectively')
        lblQ1.grid(row=5, column=0, columnspan=4, sticky=NW)

        self.varQ1 = IntVar()
        R1Q1 = Radiobutton(self, variable=self.varQ1, value=4)
        R1Q1.grid(row=5, column=4)
        R2Q1 = Radiobutton(self, variable=self.varQ1, value=3)
        R2Q1.grid(row=5, column=5)
        R3Q1 = Radiobutton(self, variable=self.varQ1, value=2)
        R3Q1.grid(row=5, column=6)
        R4Q1 = Radiobutton(self, variable=self.varQ1, value=1)
        R4Q1.grid(row=5, column=7)

        lblQ2 = Label(self, text='2. Our team produced good quality products')
        lblQ2.grid(row=6, column=0, columnspan=4, sticky=NW)

        self.varQ2 = IntVar()
        R1Q2 = Radiobutton(self, variable=self.varQ2, value=4)
        R1Q2.grid(row=6, column=4)
        R2Q2 = Radiobutton(self, variable=self.varQ2, value=3)
        R2Q2.grid(row=6, column=5)
        R3Q2 = Radiobutton(self, variable=self.varQ2, value=2)
        R3Q2.grid(row=6, column=6)
        R4Q2 = Radiobutton(self, variable=self.varQ2, value=1)
        R4Q2.grid(row=6, column=7)

        lblQ3 = Label(self, text='3. I enjoyed working in our team')
        lblQ3.grid(row=7, column=0, columnspan=4, sticky=NW)

        self.varQ3 = IntVar()
        R1Q3 = Radiobutton(self, variable=self.varQ3, value=4)
        R1Q3.grid(row=7, column=4)
        R2Q3 = Radiobutton(self, variable=self.varQ3, value=3)
        R2Q3.grid(row=7, column=5)
        R3Q3 = Radiobutton(self, variable=self.varQ3, value=2)
        R3Q3.grid(row=7, column=6)
        R4Q3 = Radiobutton(self, variable=self.varQ3, value=1)
        R4Q3.grid(row=7, column=7)

    def createProblems(self):
        # Create Widgets to show Problems experienced
        lblProb1 = Label(self, text='Problems:', font=('MS',13,'bold'))
        lblProb1.grid(row=9, column=0)
        lblProb2 = Label(self, text='Our team often experienced the ' +
                                'following problems (choose all that apply):')
        lblProb2.grid(row=9, column=1, columnspan=6, sticky=SW)

        self.varCB1 = IntVar()
        CB1 = Checkbutton(self, text=" Poor Communication", variable=self.varCB1)
        CB1.grid(row=9, column=0, columnspan=4, sticky=W)

        self.varCB2 = IntVar()
        CB2 = Checkbutton(self, text=" Members missing meetings", variable=self.varCB2)
        CB2.grid(row=9, column=4, columnspan=4, sticky=W)

        self.varCB3 = IntVar()
        CB3 = Checkbutton(self, text=" Lack of direction", variable=self.varCB3)
        CB3.grid(row=10, column=0, columnspan=4, sticky=W)

        self.varCB4 = IntVar()
        CB4 = Checkbutton(self, text=" Members not contributing", variable=self.varCB4)
        CB4.grid(row=10, column=4, columnspan=4, sticky=W)

        self.varCB5 = IntVar()
        CB5 = Checkbutton(self, text=" Disagreements amongst team", variable=self.varCB5)
        CB5.grid(row=11, column=0, columnspan=4, sticky=W)

        self.varCB6 = IntVar()
        CB6 = Checkbutton(self, text=" Members not motivated", variable=self.varCB6)
        CB6.grid(row=11, column=4, columnspan=4, sticky=W)

    def createComments(self):
        # Free text
        lbltxtComment = Label(self, text='Comments about \n teamwork:', font=('MS',13,'bold'))
        lbltxtComment.grid(row=12, column=0, columnspan=2, rowspan=3)

        self.txtComment = Text(self, height=3, width=60)
        scroll = Scrollbar(self, command=self.txtComment.yview)
        self.txtComment.configure(yscrollcommand=scroll.set)
        self.txtComment.grid(row=12, column=2, columnspan=5, sticky=E)
        scroll.grid(row=12, column=7, sticky=W)

        lblName = Label(self, text='Name (optional):', font=('MS',13,'bold'))
        lblName.grid(row=15, column=2)
        self.entName = Entry(self)
        self.entName.grid(row=15, column=4, columnspan=2, sticky=E)

    def createButtons(self):
        # Submit responses to the questionnaire
        butSubmit = Button(self, text='Submit', font=('MS', 13, 'bold'))
        butSubmit['command'] = self.storeResponse  # Note: no () after the method
        butSubmit.grid(row=16, column=2, columnspan=2)

        butClear = Button(self, text='Clear', font=('MS', 13, 'bold'))
        butClear['command'] = self.clearResponse  # Note: no () after the method
        butClear.grid(row=16, column=4, columnspan=2)

        butResults = Button(self, text='Show esults', font=('MS', 13, 'bold'))
        butResults['command'] = self.openResultsWindow  # Note: no () after the method
        butResults.grid(row=16, column=6, columnspan=2)

    def clearResponse(self):
        # Clear the Questionnaire
        # Clear the program selection
        self.listProg.selection_clear(0, END)
        self.listProg.selection_set(END)

        # Clear radio buttons
        self.varQ1.set(0)
        self.varQ2.set(0)
        self.varQ3.set(0)

        # Clear tick boxes
        self.varCB1.set(0)
        self.varCB2.set(0)
        self.varCB3.set(0)
        self.varCB4.set(0)
        self.varCB5.set(0)
        self.varCB6.set(0)

        # Clear entries into text boxes
        self.entName.delete(0, END)
        self.txtComment.delete(1.0, END)

    def storeResponse(self):
        # Store the results of the Questionnaire
        # Check that degree program has ben selected
        index = self.listProg.curselection()[0]
        strProg = str(self.listProg.get(index))
        strMsg = ""

        if strProg == "":
            strMsg = "You need to select a Degree Programme. "

        # Check that Team Experience questions have been answered
        if (self.varQ1.get() == 0) or (self.varQ2.get() == 0) or (self.varQ3.get() == 0):
            strMsg = strMsg + "You need to answer all Team Experience Questions"

        # If all is OK, use shelve to open a database
        if strMsg == "":
            import shelve
            db = shelve.open('responsedb')

            # Generate unique key
            responseCount = len(db)
            Ans = Response(str(responseCount + 1), strProg,
                           self.varQ1.get(), self.varQ2.get(), self.varQ3.get(),
                           self.varCB1.get(), self.varCB2.get(), self.varCB3.get(),
                           self.varCB4.get(), self.varCB5.get(), self.varCB6.get(),
                           self.txtComment.get(1.0, END), self.entName.get())
            db[Ans.respNo] = Ans
            db.close

            messagebox.showinfo("Questionnaire", "Questionnaire Submitted")
            self.clearResponse()

        else:
            messagebox.showwarning("Entry Error", strMsg)

    def openResultsWindow(self):
        t1 = Toplevel(root)

        DisplayResults(t1)


 # Main
root = Tk()
root.title("Teamwork Questionnaire")
app = Questionnaire(root)
root.mainloop()
