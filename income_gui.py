from Tkinter import *
from Earner import *

class Application(Frame):
    def createWidgets(self):

        topContainer = Frame(root)
        topContainer.pack()

        leftFrame = Frame(topContainer)
        leftFrame.pack( side = LEFT )


        rightFrame = Frame(topContainer)
        rightFrame.pack( side = LEFT )

        rateValue = StringVar()
        rateField = Entry(leftFrame, textvariable=rateValue, justify = LEFT)
        rateField.pack()

        weeklyValue = StringVar()
        weeklyField = Entry(leftFrame, textvariable=weeklyValue)
        weeklyField.pack()


        monthlyValue = StringVar()
        monthlyField = Entry(leftFrame, textvariable=monthlyValue)
        monthlyField.pack()

        annualValue = StringVar()
        annualField = Entry(leftFrame, textvariable=annualValue)
        annualField.pack()

        rateLabel = Label(rightFrame, text="Dollars per Hour")
        rateLabel.pack(  )

        hourLabel = Label(rightFrame, text="Hours per Week")
        hourLabel.pack(  )

        monthlyLabel = Label(rightFrame, text="Monthly")
        monthlyLabel.pack(  )

        annualLabel = Label(rightFrame, text="Annual")
        annualLabel.pack(  )

        def proc():

            e1 = Earner({
            'rate': rateValue.get(),
            'weekly': weeklyValue.get(),
            'monthly': monthlyValue.get(),
            'annual': annualValue.get(),
            })

            e1.controller()
            '''
            print "e1 instance: "
            print e1.rate
            print e1.weekly
            print e1.annual
            print e1.monthly
            '''
            
            rateOut = e1.rate
            weeklyOut = e1.weekly
            annualOut = e1.annual
            monthlyOut = e1.monthly

            rateField.delete(0, END)
            rateField.insert(0,e1.rate)

            weeklyField.delete(0, END)
            weeklyField.insert(0,e1.weekly)

            monthlyField.delete(0, END)
            monthlyField.insert(0,e1.monthly)

            annualField.delete(0, END)
            annualField.insert(0,e1.annual)

        bottomFrame = Frame(root)
        bottomFrame.pack( side = BOTTOM )

        okButton = Button(text="Ok", command=proc)
        okButton.pack( expand = True, fill = X)

        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack( side = LEFT)

        def reset():
            print "deleting"
            rateField.delete(0, END)
            weeklyField.delete(0, END)
            monthlyField.delete(0, END)
            annualField.delete(0, END)

        resetButton = Button(self, text = "RESET", command = reset)
        resetButton.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.master.title("Income Calculator")
app.mainloop()
root.destroy()
