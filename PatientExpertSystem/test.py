from tkinter import *
import tkinter.messagebox

class Patient:
    def __init__(self,name, location, gender, age):
        self.name = name
        self.location = location
        self.gender = gender
        self.age = age
        self.temperature = 0
        self.fever = 0
        self.cough = 0
        self.vomit = 0
        self.lethargic = 0
        self.risk = []

class Infant(Patient):
    def __init__(self, name, location, gender, age):
        super().__init__(name, location, gender, age)
        self.restless = 0
        self.fatigue = 0
        self.feed = 0
        self.crying = 0
        self.pale = 0
        
class Child(Patient):
    def __init__(self, name, location, gender, age):
        super().__init__(name, location, gender, age)
        self.headache = 0
        self.sore_throat = 0
        self.nasal_cong = 0
        self.diah = 0
        self.chill = 0
        self.sweating = 0
        self.flushed = 0
        self.wheeze = 0
        self.blue = 0
        self.diff_breath = 0
        self.flare = 0
        self.musc_breath = 0

class Adult(Patient):
    def __init__(self, name, location, gender, age):
        super().__init__(name, location, gender, age)
        self.cough_blood = 0
        self.chills = 0
        self.diff_breath = 0
        self.chest_pain = 0
        self.sweat = 0
        self.musc_pain = 0
        self.sore_throat = 0
        self.diah = 0
        self.blue = 0
        self.confus = 0

# def createPat(name, location, gender, age):
#     if age < 1 and age < 2:
#         patient = Infant(name, location, gender, age)
#         return diagInfant(patient)
#     elif age > 2 and age < 16:
#         patient = Child(name, location, gender, age)
#     else:
#         patient = Adult(name, location, gender, age)

class RiskWindow:
    def __init__(self, win1):
        self.l1 = Label(win1, text = 'Enter Risk Factor')
        self.l1.grid(row = 0, sticky = E)
        self.riskEnt = Entry(win1)
        self.riskEnt.grid(row = 0,column = 1)
        self.accBut = Button(win1, text = 'Accept', command = self.getVal)
        self.accBut.grid(row = 1, column = 1)
        self.retBut = Button(win1, text = 'Return To Menu', command = win1.destroy)
        self.retBut.grid(row = 2, column = 1)
    def getVal(self):
        #Add code to add risk factor to file
        tkinter.messagebox.showinfo("Information","Entry recorded.")

class DiagIWindow:
    def __init__(self,win3,patient):
        self.frame1 = Frame(win3)
        self.frame1.pack(side = TOP, fill = X)
        self.frame2 = Frame(win3)
        self.frame2.pack(side = BOTTOM, fill = BOTH)

        self.tlabel = Label(self.frame1, text = 'Diagnose Infant', bg = 'grey', fg = 'black')
        self.tlabel.pack(fill = X)

class DiagCWindow:
    def __init__(self,win3,patient):
        pass

class DiagAWindow:
    def __init__(self,win3,patient):
        pass

class DiagWindow:
    def __init__(self, win2):
        self.frame1 = Frame(win2)
        self.frame1.pack(side = TOP, fill = X)
        self.frame2 = Frame(win2)
        self.frame2.pack(side = BOTTOM, fill = BOTH)
        
        self.tlabel = Label(self.frame1, text = 'Add Patient Information', bg = 'grey', fg = 'black')
        self.tlabel.pack(fill = X)
        
        self.nlabel = Label(self.frame2, text = 'Name')
        self.nlabel.grid(row = 0, sticky = E)
        self.nentry = Entry(self.frame2)
        self.nentry.grid(row = 0, column = 1)
        
        self.llabel = Label(self.frame2, text = 'Location')
        self.llabel.grid(row = 1, sticky = E)
        self.lentry = Entry(self.frame2)
        self.lentry.grid(row = 1, column = 1)
        
        self.glabel = Label(self.frame2, text = 'Gender')
        self.glabel.grid(row = 2, sticky = E)
        self.v = IntVar()
        self.gb1 = Radiobutton(self.frame2, text = 'Male', value = 0, variable = self.v)
        self.gb2 = Radiobutton(self.frame2, text = 'Female', value = 1, variable = self.v)
        self.gb1.grid(row = 2, column = 1)
        self.gb2.grid(row = 2, column = 2)
        
        self.alabel = Label(self.frame2, text = 'Age')
        self.alabel.grid(row = 3, sticky = E)
        self.aentry = Entry(self.frame2)
        self.aentry.grid(row = 3, column = 1)
        self.age = 0
        if self.aentry.get() != '':
            age = int(self.aentry.get())
        self.addButton = Button(self.frame2, text = 'Add Patient', command = self.addpat(self.nentry.get(),self.lentry.get(),self.v.get(),self.age))
        self.addButton.grid(row = 4, columnspan = 3)

    def addpat(self,name, location, gender, age):
        if age < 1 and age < 2:
            patient = Infant(name, location, gender, age)
            self.diagIwin(patient)
        elif age > 2 and age < 16:
            patient = Child(name, location, gender, age)
        else:
            patient = Adult(name, location, gender, age)

    def diagIwin(self,patient):  
        subwin3=Tk()
        mywin4=DiagIWindow(subwin3,patient)
        subwin3.title('Diagnose Infant')
        subwin3.geometry("400x200+10+10")
        subwin3.mainloop()  
    
    def diagCwin(self,patient):  
        subwin4=Tk()
        mywin5=DiagCWindow(subwin4,patient)
        subwin4.title('Diagnose Child')
        subwin4.geometry("400x200+10+10")
        subwin4.mainloop()

    def diagAwin(self,patient):  
        subwin5=Tk()
        mywin6=DiagAWindow(subwin5,patient)
        subwin5.title('Diagnose Adult')
        subwin5.geometry("400x200+10+10")
        subwin5.mainloop()

class MainWindow:
    def __init__(self, win):
       self.topframe = Frame(win)
       self.topframe.pack(side = TOP, fill = X)
       self.bottomframe = Frame(win)
       self.bottomframe.pack(side = BOTTOM, fill = X)
       self.titLabel = Label(self.topframe, text = 'Welcome To The Pneumonia Diagnosis Aid System', bg = 'grey', fg = 'black')
       self.titLabel.pack(fill = X, expand = 1)
       self.riskBut = Button(self.bottomframe, text='Add Risk Factor', command= self.riskwin)
       self.diagBut = Button(self.bottomframe, text='Run Diagnosis', command = self.diagwin)
       self.outBut = Button(self.bottomframe, text='Check For Spike In Pneumonia')
       self.riskBut.pack(side = BOTTOM, fill = X)
       self.diagBut.pack(side = BOTTOM, fill = X)
       self.outBut.pack(side = BOTTOM, fill = X)
    
    def riskwin(self):
        subwin=Tk()
        mywin2=RiskWindow(subwin)
        subwin.title('Add Risk Factor')
        subwin.geometry("400x200+10+10")
        subwin.mainloop()  

    def diagwin(self):  
        subwin2=Tk()
        mywin3 = DiagWindow(subwin2)
        subwin2.title('Patient Information')
        subwin2.geometry("400x200+10+10")
        subwin2.mainloop()  

root = Tk()
mywin = MainWindow(root)
root.title('Main Menu')
root.geometry("800x400+10+10")
root.mainloop()