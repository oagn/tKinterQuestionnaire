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

        # Initialise ALL THE COUNTERS!
        countAll = 0
        sumQ1All = 0.0
        sumQ2All = 0.0
        sumQ3All = 0.0
        sumP1All = 0
        sumP2All = 0
        sumP3All = 0
        sumP4All = 0
        sumP5All = 0
        sumP6All = 0

        countCS = 0
        sumQ1CS = 0.0
        sumQ2CS = 0.0
        sumQ3CS = 0.0
        sumP1CS = 0
        sumP2CS = 0
        sumP3CS = 0
        sumP4CS = 0
        sumP5CS = 0
        sumP6CS = 0

        countCSwith = 0
        sumQ1CSwith = 0.0
        sumQ2CSwith = 0.0
        sumQ3CSwith = 0.0
        sumP1CSwith = 0
        sumP2CSwith = 0
        sumP3CSwith = 0
        sumP4CSwith = 0
        sumP5CSwith = 0
        sumP6CSwith = 0

        countBIS = 0
        sumQ1BIS = 0.0
        sumQ2BIS = 0.0
        sumQ3BIS = 0.0
        sumP1BIS = 0
        sumP2BIS = 0
        sumP3BIS = 0
        sumP4BIS = 0
        sumP5BIS = 0
        sumP6BIS = 0

        countSE = 0
        sumQ1SE = 0.0
        sumQ2SE = 0.0
        sumQ3SE = 0.0
        sumP1SE = 0
        sumP2SE = 0
        sumP3SE = 0
        sumP4SE = 0
        sumP5SE = 0
        sumP6SE = 0

        countJoints = 0
        sumQ1Joints = 0.0
        sumQ2Joints = 0.0
        sumQ3Joints = 0.0
        sumP1Joints = 0
        sumP2Joints = 0
        sumP3Joints = 0
        sumP4Joints = 0
        sumP5Joints = 0
        sumP6Joints = 0

        # retrieve responses from database
        import shelve
        db = shelve.open('responsedb')
        respNo = len(db)

        for i in range(1, respNo):
            Ans = get.db(str(i))

            # update counters with values from current response
            countAll += 1
            sumQ1All += Ans.q1
            sumQ2All += Ans.q2
            sumQ3All += Ans.q3
            sumP1All += Ans.pr1
            sumP2All += Ans.pr2
            sumP3All += Ans.pr3
            sumP4All += Ans.pr4
            sumP5All += Ans.pr5
            sumP6All += Ans.pr6

            if Ans.prog == "CS":
                countCS += 1
                sumQ1CS += Ans.q1
                sumQ2CS += Ans.q2
                sumQ3CS += Ans.q3
                sumP1CS += Ans.pr1
                sumP2CS += Ans.pr2
                sumP3CS += Ans.pr3
                sumP4CS += Ans.pr4
                sumP5CS += Ans.pr5
                sumP6CS += Ans.pr6

            if Ans.prog == "CS with":
                countCSwith += 1
                sumQ1CSwith += Ans.q1
                sumQ2CSwith += Ans.q2
                sumQ3CSwith += Ans.q3
                sumP1CSwith += Ans.pr1
                sumP2CSwith += Ans.pr2
                sumP3CSwith += Ans.pr3
                sumP4CSwith += Ans.pr4
                sumP5CSwith += Ans.pr5
                sumP6CSwith += Ans.pr6

            if Ans.prog == "BIS":
                countBIS += 1
                sumQ1BIS += Ans.q1
                sumQ2BIS += Ans.q2
                sumQ3BIS += Ans.q3
                sumP1BIS += Ans.pr1
                sumP2BIS += Ans.pr2
                sumP3BIS += Ans.pr3
                sumP4BIS += Ans.pr4
                sumP5BIS += Ans.pr5
                sumP6BIS += Ans.pr6

            if Ans.prog == "SE":
                countSE += 1
                sumQ1SE += Ans.q1
                sumQ2SE += Ans.q2
                sumQ3SE += Ans.q3
                sumP1SE += Ans.pr1
                sumP2SE += Ans.pr2
                sumP3SE += Ans.pr3
                sumP4SE += Ans.pr4
                sumP5SE += Ans.pr5
                sumP6SE += Ans.pr6

            if Ans.prog == "Joints":
                countJoints += 1
                sumQ1Joints += Ans.q1
                sumQ2Joints += Ans.q2
                sumQ3Joints += Ans.q3
                sumP1Joints += Ans.pr1
                sumP2Joints += Ans.pr2
                sumP3Joints += Ans.pr3
                sumP4Joints += Ans.pr4
                sumP5Joints += Ans.pr5
                sumP6Joints += Ans.pr6


# Main
root = Tk()
root.title("Display Results")
app = DisplayResults(root)
root.mainloop()