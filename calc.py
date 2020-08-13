
from tkinter import *



class Calculator:

    def __init__(self):
        self.root = Tk()
        self.root.title("My Calc")
        self.root.maxsize(500,800)

        self.result = Label(self.root,width=10   ,height=3,bg="White")
        self.result.grid(row=0,column=0)



        num9 = Button(self.root, width=5,height=2,text="9",bg="SkyBlue",command=lambda:self.getnum("9")).grid(row=1,column=1)

        num8 = Button(self.root, width=5, height=2, text="8", bg="SkyBlue", command=lambda: self.getnum("8")).grid(
            row=1, column=2)
        num7 = Button(self.root, width=5, height=2, text="7", bg="SkyBlue", command=lambda: self.getnum("7")).grid(
            row=1, column=3)
        num6 = Button(self.root, width=5, height=2, text="6", bg="SkyBlue", command=lambda: self.getnum("6")).grid(
            row=2, column=1)


        num5= Button(self.root, width=5, height=2, text="5", bg="SkyBlue", command=lambda: self.getnum("5")).grid(
            row=2, column=2)
        num4 = Button(self.root, width=5, height=2, text="4", bg="SkyBlue", command=lambda: self.getnum("4")).grid(
            row=2, column=3)
        num3 = Button(self.root, width=5, height=2, text="3", bg="SkyBlue", command=lambda: self.getnum("3")).grid(
            row=3, column=1)

        num2 = Button(self.root, width=5, height=2, text="2", bg="SkyBlue", command=lambda: self.getnum("2")).grid(
            row=3, column=2)



        num1 = Button(self.root, width=5, height=2, text="1", bg="SkyBlue", command=lambda: self.getnum("1")).grid(
            row=3, column=3)
        num0 = Button(self.root, width=5, height=2, text="0", bg="SkyBlue", command=lambda: self.getnum("0")).grid(
            row=4, column=2)
        clr = Button(self.root, width=5, height=2, text="CLr", bg="SkyBlue", command=lambda: self.clear()).grid(
            row=4, column=1)
        equal = Button(self.root, width=5, height=2, text="=", bg="SkyBlue", command=lambda: self.getresult()).grid(
            row=4, column=3)


        add = Button(self.root, width=10, height=2, text="+", bg="SkyBlue", command=lambda: self.fetchsign("+")).grid(
            row=1, column=0)
        subtract = Button(self.root, width=10, height=2, text="-", bg="SkyBlue", command=lambda: self.fetchsign("_")).grid(
            row=2, column=0)
        multiply = Button(self.root, width=10, height=2, text="*", bg="SkyBlue", command=lambda: self.fetchsign("*")).grid(
            row=3, column=0)
        divide = Button(self.root, width=10, height=2, text="/", bg="SkyBlue", command=lambda: self.fetchsign("/")).grid(
            row=4, column=0)

        self.root.mainloop()

    def getnum(self,num):
        newtext=self.result['text']+num
        self.result.configure(text=newtext)

    def clear(self):
        self.result.configure(text="")

    def fetchsign(self,str):
        self.firstnum =int( self.result['text'])
        self.sign = str
        self.clear()

    def getresult(self):
        secondnum = int(self.result['text'])

        if self.sign == "+":
            res = self.firstnum+secondnum
        elif self.sign == "-":
            res = self.firstnum-secondnum
        elif self.sign == "*":
                res = self.firstnum * secondnum
        elif self.sign == "/":
            res = self.firstnum / secondnum


        self.result.configure(text=str(res))



ob = Calculator()