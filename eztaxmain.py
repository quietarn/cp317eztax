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
    
    def donate(self):
        messagebox.showinfo("Support us", "EzTax is solely ran by university students, if you enjoying using our work, help us get better through xxxxxxxx@email.com")
    
    def savepdf(self):
        filename = asksaveasfilename(title="save as...", initialfile="tax.pdf", filetypes=[("PDF File", "*.pdf")])
    
    def callback(self):
        self.abA, self.abB, self.abC, self.abD, self.abE, self.abF = float(self.abTA.get()), float(self.abTB.get()), float(self.abTC.get()), float(self.abTD.get()), float(self.abTE.get()), float(self.abTF.get())
        print(self.abA, self.abB, self.abC, self.abD, self.abE, self.abF)
    
    def taxpre(self):
        pass
        
    def AutoMobile(self):
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
        top.mainloop()
        
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
        
        """Address"""
        Label(self, text="Your Address:").grid(row=3, column=0, sticky="W")
        self.Address = Entry(self)
        self.Address.grid(row=3, column=1)
        
        """year"""
        Label(self, text="Year applied:").grid(row=4, column=0, sticky="W")
        self.Address = Entry(self)
        self.Address.grid(row=4, column=1)
        
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
        
        Button(self, text="generate report", command=self.taxpre).grid(row=11, column=1)
        
        self.mainloop()
        
        
root = Tk()
root.title("EzTax")
root.geometry("1000x700")

Eztax = APP(master=root)

