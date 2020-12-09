"""
-------------------------------------------------------
[file name]
[program description]
-------------------------------------------------------
Author:  your name
ID:      your ID
Email:   your Laurier email address
__updated__ = "2020-12-09"
-------------------------------------------------------
"""
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename


class APP(Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createButtons()
        self.mainloop()
        
    def reporting(self):
        filename = asksaveasfilename(title="save as...", initialfile="tax.txt", filetypes=[("text File", "*.txt")])
        f = open(filename, "w")
        f.write("Hello " + self.FirstName.get() + " " + self.LastName.get() + '\n')
        f.write("Your tax preview for year " + self.year.get() + " will look like this" + '\n')
        f.write("Your income tax: $" + "   "*3 + str(self.incometax) + '\n')
        f.write("Your free parking benefit is: $" + "   "*3 + str(self.fp) + '\n')
        f.write("Your allowance benefit is: $" + "   "*3 + str(self.a) + '\n')
        f.write("Your incurred meal deductive is: $" + "   "*3 + str(self.meal) + '\n')
        f.write("Your Automobile deductive is: $" + "   "*3 + str(self.abT) + '\n')
        f.write("Your total is: $" + "   "*3 + str(self.incometax + self.fp + self.a - self.meal - self.abT) + '\n')
        f.close
    
    def donate(self):
        messagebox.showinfo("Support us", "EzTax is solely ran by university students, if you enjoying using our work, help us get better through EMT EZtax@gmail.com")
        
    def cra(self):
        messagebox.showinfo("CRA", "Please contact CRA for further infomation, through\n" + "https://www.canada.ca/en/revenue-agency.html")
    
    def callback(self):
        self.abA, self.abB, self.abC, self.abD, self.abE, self.abF = float(self.abTA.get()), float(self.abTB.get()), float(self.abTC.get()), float(self.abTD.get()), float(self.abTE.get()), float(self.abTF.get())
    
    def taxpre(self):
        top1 = Toplevel()
        top1.title("Tax preview")
        top1.geometry("700x700")
        Label(top1, text=("Hello " + self.FirstName.get() + " " + self.LastName.get())).pack()
        Label(top1, text=("Your tax preview for year " + self.year.get() + " will look like this")).pack()
        Label(top1, text=" ").pack()
        
        self.incometax = 0
        if (float(self.income.get()) > 220000):
            self.incometax = float(self.income.get()) * 0.1316
        elif(float(self.income.get()) > 150000):
            self.incometax = float(self.income.get()) * 0.1216
        elif(float(self.income.get()) > 89482):
            self.incometax = float(self.income.get()) * 0.1116
        elif(float(self.income.get()) > 44740):
            self.incometax = float(self.income.get()) * 0.0915
        elif(float(self.income.get()) > 0):
            self.incometax = float(self.income.get()) * 0.0505
        Label(top1, text=("Your income tax: $" + "   "*3 + str(self.incometax))).pack()
        Label(top1, text=" ").pack()
        
        if self.FreeParking.get():
            self.fp = float(self.fp.get())
            Label(top1, text=("Your free parking benefit is: $" + "   "*3 + str(self.fp))).pack()
            Label(top1, text=" ").pack()
            
        if  self.a.get() != "":
            self.a = float(self.a.get())
            Label(top1, text=("Your allowance benefit is: $" + "   "*3 + str(self.a))).pack()
            Label(top1, text=" ").pack()
        
        if self.meal.get() != "":
            self.meal = float(self.meal.get()) * 0.5
            Label(top1, text=("Your incurred meal deductive is: $" + "   "*3 + str(self.meal))).pack()
            Label(top1, text=" ").pack()
            
        if self.ab.get():
            if self.abF != 0:
                self.abT = (self.abA / self.abB * (0.02 * (self.abC)) + 2 / 3 * (self.abE / self.abF))
            else:
                self.abT = self.abA / self.abB * (0.02 * (self.abC))
            Label(top1, text=("Your Automobile deductive is: $" + "   "*3 + str(self.abT))).pack()
            Label(top1, text=" ").pack()
        
        Label(top1, text=("Your total is: $" + "   "*3 + str(self.incometax + self.fp + self.a - self.meal - self.abT))).pack()
        Label(top1, text="Thank you for using EzTax").pack()
        
        Button(top1, text="generate report", command=self.reporting).pack()

    def AutoMobile(self):
        self.ab.set(True)
        top = Toplevel()
        top.title("Automobile")
        top.geometry("700x700")
        Label(top, text="What's your total personal-use km driven during the time period?").pack()
        self.abTA = Entry(top)
        self.abTA.pack()
        Label(top, text="What is the total days you use this automobile?").pack()
        self.abTB = Entry(top)
        self.abTB.pack()
        Label(top, text="What is the full original cost of an employer-owned vehicle, including HST?").pack()
        self.abTC = Entry(top)
        self.abTC.pack()
        Label(top, text="What is the total available days when you owned the vehicle?").pack()
        self.abTD = Entry(top)
        self.abTD.pack()
        Label(top, text="What is the lease payment made, including HST, by the employer?(if vehicle is leased)").pack()
        self.abTE = Entry(top)
        self.abTE.pack()
        self.abTE.insert(END, 0)
        Label(top, text="What is the portion of the lease payments which pertains to insurance for loss or damages?(if vehicle is leased, otherwise 0)").pack()
        self.abTF = Entry(top)
        self.abTF.pack()
        self.abTF.insert(END, 0)
        
        Button(top, text="submit", command=self.callback).pack()
        
    def createButtons(self):
        """first name entry"""
        Label(self, text="Your first Name:").grid(row=0, column=0, sticky="W")
        self.FirstName = Entry(self)
        self.FirstName.grid(row=0, column=1)
        
        """the Donation button"""       
        self.Donate = Button(self, command=self.donate)
        self.Donate["text"] = "Support us"      
        self.Donate.grid(row=0, column=3)
        
        """last name entry"""
        Label(self, text="Your last Name:").grid(row=1, column=0, sticky="W")
        self.LastName = Entry(self)
        self.LastName.grid(row=1, column=1)
        
        """SIN"""
        Label(self, text="Your Social insurance number:").grid(row=2, column=0, sticky="W")
        self.SIN = Entry(self)
        self.SIN.grid(row=2, column=1)
        
        """CRA"""
        Button(self, text="Contact CRA", command=self.cra).grid(row=2, column=3)
        
        """Address"""
        Label(self, text="Your Address:").grid(row=3, column=0, sticky="W")
        self.Address = Entry(self)
        self.Address.grid(row=3, column=1)
        
        """year"""
        Label(self, text="Year applied:").grid(row=4, column=0, sticky="W")
        self.year = Entry(self)
        self.year.grid(row=4, column=1)
        
        """student"""
        Label(self, text="Are you a student:").grid(row=5, column=0, sticky="W")
        self.student = BooleanVar()
        Radiobutton(self, text="Yes", value=True, variable=self.student).grid(row=5, column=2)
        Radiobutton(self, text="No", value=False, variable=self.student).grid(row=5, column=1)
         
        """tutition(if applied)"""
        Label(self, text="Tutition fee:").grid(row=5, column=3)
        self.tutition = Entry(self)
        self.tutition.grid(row=5, column=4)
        
        """Income"""
        Label(self, text="What is your income for this year? ").grid(row=6, column=0, sticky="W")
        self.income = Entry(self)
        self.income.grid(row=6, column=1)
        
        """Free Parking"""
        Label(self, text="Do you have free parking spaces at work?").grid(row=7, column=0, sticky="W")
        self.FreeParking = BooleanVar(self)
        Radiobutton(self, text="Yes", value=True, variable=self.FreeParking).grid(row=7, column=2)
        Radiobutton(self, text="No", value=False, variable=self.FreeParking).grid(row=7, column=1)
        Label(self, text="Parking Fee").grid(row=7, column=3, sticky="W")
        self.fp = Entry(self)
        self.fp.grid(row=7, column=4)
        
        """Allowances"""
        Label(self, text="How much is your allowance(if no, 0)?").grid(row=8, column=0, sticky="W")
        self.a = Entry(self)
        self.a.grid(row=8, column=1)
        
        """Automobile benefits"""
        self.ab = BooleanVar(self)
        Label(self, text="Do you use an automobile provided by employer?").grid(row=9, column=0, sticky="W")
        Button(self, text="Yes", command=self.AutoMobile).grid(row=9, column=1)

        """meals incurred"""
        Label(self, text="How much did you pay on meals incurred").grid(row=10, column=0, sticky="W")
        self.meal = Entry(self)
        self.meal.grid(row=10, column=1)
        
        Button(self, text="tax calculating", command=self.taxpre).grid(row=11, column=1)
        
        
root = Tk()
root.title("EzTax")
root.geometry("1000x700")

Eztax = APP(master=root)

