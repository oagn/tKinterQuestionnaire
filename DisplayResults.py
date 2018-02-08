from tkinter import *
from Response import Response


class DisplayResults(Frame):
    # GUI Setup
    def __init__(self, master):
        # Initialise Class
        Frame.__init__(self, master)
        self.pack()
        self.retrieveResponse()

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
            Ans = db[str(i)]

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

        db.close()

        # Toal number of answers
        self.txtDisplay = Text(self, height=60, width=100)
        self.txtDisplay.tag_configure('boldfont', font=('MS', 13, 'bold'))
        self.txtDisplay.tag_configure('normfont', font=('MS', 13))

        tabResults = ""
        tabResults += ("\t" + "\t" + "\t" + "\t" + "\t")
        self.txtDisplay.insert(END, "Degree Programme" + tabResults + "ALL" + "\t"
                               + "CS" + "\t" + "CS with" + "\t" + "BIS" + "\t"
                               + "SE" + "\t" + "Joints" + '\n', 'boldfont')

        self.txtDisplay.insert(END, "Number of Responses:" + tabResults + str(countAll)
                               + "\t" + str(countCS) + "\t" + str(countCSwith) + "\t" +
                               str(countBIS) + "\t" + str(countSE) + "\t" + str(countJoints)
                               + '\n', 'normfont')

        # Averages and percentages for ALL
        if countAll > 0:
            Q1All = sumQ1All / countAll
            Q2All = sumQ2All / countAll
            Q3All = sumQ3All / countAll
            P1All = sumP1All * 100 / countAll
            P2All = sumP2All * 100 / countAll
            P3All = sumP3All * 100 / countAll
            P4All = sumP4All * 100 / countAll
            P5All = sumP5All * 100 / countAll
            P6All = sumP6All * 100 / countAll

        else:
            Q1All = 0
            Q2All = 0
            Q3All = 0
            P1All = 0
            P2All = 0
            P3All = 0
            P4All = 0
            P5All = 0
            P6All = 0

        # Averages and percentages for CS
        if countCS > 0:
            Q1CS = sumQ1CS / countCS
            Q2CS = sumQ2CS / countCS
            Q3CS = sumQ3CS / countCS
            P1CS = sumP1CS * 100 / countCS
            P2CS = sumP2CS * 100 / countCS
            P3CS = sumP3CS * 100 / countCS
            P4CS = sumP4CS * 100 / countCS
            P5CS = sumP5CS * 100 / countCS
            P6CS = sumP6CS * 100 / countCS

        else:
            Q1CS = 0
            Q2CS = 0
            Q3CS = 0
            P1CS = 0
            P2CS = 0
            P3CS = 0
            P4CS = 0
            P5CS = 0
            P6CS = 0

        # Averages and percentages for CSwith
        if countCSwith > 0:
            Q1CSwith = sumQ1CSwith / countCSwith
            Q2CSwith = sumQ2CSwith / countCSwith
            Q3CSwith = sumQ3CSwith / countCSwith
            P1CSwith = sumP1CSwith * 100 / countCSwith
            P2CSwith = sumP2CSwith * 100 / countCSwith
            P3CSwith = sumP3CSwith * 100 / countCSwith
            P4CSwith = sumP4CSwith * 100 / countCSwith
            P5CSwith = sumP5CSwith * 100 / countCSwith
            P6CSwith = sumP6CSwith * 100 / countCSwith

        else:
            Q1CSwith = 0
            Q2CSwith = 0
            Q3CSwith = 0
            P1CSwith = 0
            P2CSwith = 0
            P3CSwith = 0
            P4CSwith = 0
            P5CSwith = 0
            P6CSwith = 0

        # Averages and percentages for BIS
        if countBIS > 0:
            Q1BIS = sumQ1BIS / countBIS
            Q2BIS = sumQ2BIS / countBIS
            Q3BIS = sumQ3BIS / countBIS
            P1BIS = sumP1BIS * 100 / countBIS
            P2BIS = sumP2BIS * 100 / countBIS
            P3BIS = sumP3BIS * 100 / countBIS
            P4BIS = sumP4BIS * 100 / countBIS
            P5BIS = sumP5BIS * 100 / countBIS
            P6BIS = sumP6BIS * 100 / countBIS

        else:
            Q1BIS = 0
            Q2BIS = 0
            Q3BIS = 0
            P1BIS = 0
            P2BIS = 0
            P3BIS = 0
            P4BIS = 0
            P5BIS = 0
            P6BIS = 0

        # Averages and percentages for SE
        if countSE > 0:
            Q1SE = sumQ1SE / countSE
            Q2SE = sumQ2SE / countSE
            Q3SE = sumQ3SE / countSE
            P1SE = sumP1SE * 100 / countSE
            P2SE = sumP2SE * 100 / countSE
            P3SE = sumP3SE * 100 / countSE
            P4SE = sumP4SE * 100 / countSE
            P5SE = sumP5SE * 100 / countSE
            P6SE = sumP6SE * 100 / countSE

        else:
            Q1SE = 0
            Q2SE = 0
            Q3SE = 0
            P1SE = 0
            P2SE = 0
            P3SE = 0
            P4SE = 0
            P5SE = 0
            P6SE = 0

        # Averages and percentages for Joints
        if countJoints > 0:
            Q1Joints = sumQ1Joints / countJoints
            Q2Joints = sumQ2Joints / countJoints
            Q3Joints = sumQ3Joints / countJoints
            P1Joints = sumP1Joints * 100 / countJoints
            P2Joints = sumP2Joints * 100 / countJoints
            P3Joints = sumP3Joints * 100 / countJoints
            P4Joints = sumP4Joints * 100 / countJoints
            P5Joints = sumP5Joints * 100 / countJoints
            P6Joints = sumP6Joints * 100 / countJoints

        else:
            Q1Joints = 0
            Q2Joints = 0
            Q3Joints = 0
            P1Joints = 0
            P2Joints = 0
            P3Joints = 0
            P4Joints = 0
            P5Joints = 0
            P6Joints = 0

        # Answers for Team Experience Questions
        self.txtDisplay.insert(END, '\n' + "Team Experience:" + '\n', 'boldfont')
        self.txtDisplay.insert(END, "(Score: 4 = Strongly Agree to 1 = Strongly Disagree)" + '\n', 'normfont')

        self.txtDisplay.insert(END, "1. Our team worked together effectively" + tabResults
                               + "%.1f" % Q1All + "\t %.1f" % Q1CS + "\t %.1f" % Q1CSwith
                               + "\t %.1f" % Q1BIS + "\t %.1f" % Q1SE + "\t %.1f" %
                               Q1Joints + '\n', 'normfont')

        self.txtDisplay.insert(END, "2. Our team produced good quality products" + tabResults
                               + "%.1f" % Q2All + "\t %.1f" % Q2CS + "\t %.1f" % Q2CSwith
                               + "\t %.1f" % Q2BIS + "\t %.1f" % Q2SE + "\t %.1f" %
                               Q2Joints + '\n', 'normfont')

        self.txtDisplay.insert(END, "3. I enjoyed working in our team" + tabResults
                               + "%.1f" % Q3All + "\t %.1f" % Q3CS + "\t %.1f" % Q3CSwith
                               + "\t %.1f" % Q3BIS + "\t %.1f" % Q3SE + "\t %.1f" %
                               Q3Joints + '\n', 'normfont')

        # Percentages for Problems Experienced
        self.txtDisplay.insert(END, '\n' + "Problems Experienced:" + '\n', 'boldfont')

        self.txtDisplay.insert(END, "Poor communication" + tabResults
                               + "%.1f" % P1All + "%% \t %.1f" % P1CS + "%% \t %.1f" % P1CSwith
                               + "%% \t %.1f" % P1BIS + "%% \t %.1f" % P1SE + "%% \t %.1f" %
                               P1Joints + '%%\n', 'normfont')

        self.txtDisplay.insert(END, "Members missing meetings" + tabResults
                               + "%.1f" % P2All + "%% \t %.1f" % P2CS + "%% \t %.1f" % P2CSwith
                               + "%% \t %.1f" % P2BIS + "%% \t %.1f" % P2SE + "%% \t %.1f" %
                               P2Joints + '%%\n', 'normfont')

        self.txtDisplay.insert(END, "Members missing meetings" + tabResults
                               + "%.1f" % P3All + "%% \t %.1f" % P3CS + "%% \t %.1f" % P3CSwith
                               + "%% \t %.1f" % P3BIS + "%% \t %.1f" % P3SE + "%% \t %.1f" %
                               P3Joints + '%%\n', 'normfont')

        self.txtDisplay.insert(END, "Members missing meetings" + tabResults
                               + "%.1f" % P4All + "%% \t %.1f" % P4CS + "%% \t %.1f" % P4CSwith
                               + "%% \t %.1f" % P4BIS + "%% \t %.1f" % P4SE + "%% \t %.1f" %
                               P4Joints + '%%\n', 'normfont')

        self.txtDisplay.insert(END, "Members missing meetings" + tabResults
                               + "%.1f" % P5All + "%% \t %.1f" % P5CS + "%% \t %.1f" % P5CSwith
                               + "%% \t %.1f" % P5BIS + "%% \t %.1f" % P5SE + "%% \t %.1f" %
                               P5Joints + '%%\n', 'normfont')

        self.txtDisplay.insert(END, "Members missing meetings" + tabResults
                               + "%.1f" % P6All + "%% \t %.1f" % P6CS + "%% \t %.1f" % P6CSwith
                               + "%% \t %.1f" % P6BIS + "%% \t %.1f" % P6SE + "%% \t %.1f" %
                               P6Joints + '%%\n', 'normfont')

        self.txtDisplay['state'] = DISABLED
        self.txtDisplay.pack()

