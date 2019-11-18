class Patient:
    def _init_(self, name, age, temperature):
        self.name=name
        self.age=age
        self.temperature=temperature

    def getpname():
        return self.name

    def setpname(name):
        self.name=name

    def getpage():
        return self.age

    def setpage(age)
        self.age=age

    def do_diag():
        pass

class Adult(Patient):
    def _init_(self, name, age, temperature):
        super()._init_(name, age, temperature)

    def do_diag():
        limit=input("Please enter the amount of patients you will be entering data for:")
        ctr=0
        while ctr < limit:
            super().setpname(input("Enter your name:"))
            super().setpage(int(input("Enter your age")))
            hirisk=[""]
            
