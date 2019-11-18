global mpctr #num of patients who may develop pneumonia
global sctr  #num of high risk symptoms one patient has
global hirisk #list of highrisk pneumonia symptoms
hirisk=["pale skin","short breath","weak","nausea","fever"] 
sctr=0      
mpctr=0

def prtspace():
    print("  ")

def displaypatient():
    print("----------------PATIENT DATA------------------")
    print("Name: "+do_diag().pname)
    print("Age: "+do_diag().p_age)
    print("Temperature (degrees in fahrenheit): "+do_diag().fahr)
    print("Status: "+do_diag().pstatus)

def menu():
    print("**************Welcome to MedBot***************")
    print("------------------HOME PAGE-------------------")
    print("Please enter the number that matches the service you want")    
    print("1. Diagnosis")
    print("2. Disease Status Check")
    print("3. Exit")    
    print("----------------------------------------------")
    print("**********************************************")    
    opt=int(input("Enter option "))
    
    if opt != 1 and opt != 2 and opt!=3:
        print("Invalid option")
        prtspace()
        menu()
    elif opt == 1:
        prtspace()
        do_diag()                
    elif opt == 2:
       chk_spike()
    elif opt==3:
        print("Thank you for using MedBot. Have a nice day")
        exit()
    

def do_diag(): 

    pname=input("Enter patient's name:")
    p_age=int(input("Enter patient's age:"))

    #initialise counter for patient symptoms
    #prompt patient for 5 symptoms    
    for i in range(0,5):
        getpsym=input("Please enter a symptom the patient had:")
        #check if fever is a symptom, if true ask for temp in degrees celsius
        if getpsym=="fever":
            temp=float(input("Please enter the temperature in degrees Celsius:"))
            fahr=(temp*(9/5))+32    #convert temp to degrees fahrenheit

        for sym in hirisk:  #for each symptom in the predefined list of highrisk symptoms
            if getpsym==sym:  #count how many of the patient's symptoms match any of the highrisk symptoms
                sctr+=1
                
            
    if sctr>0 and sctr<3: #patients with at least 1 symptom (low risk)
        if (p_age>=1 and p_age<=6) or p_age>65: #infants 
            mpctr+=1 #count how many persons might develop pneumonia               
            pstatus="low risk"

     #if patient has 3 or more high risk symptoms
     # or patient has a high fever then recommend admission  
    if sctr>=3 or fahr>=100.00:
        pstatus="high risk"
        print(pname+", You are at high risk of having pneumonia.")
        print("Recommendation: GO TO HOSPITAL IMMEDIATELY")
      #  print(ctr) #test to see how many matches the patient had
    elif sctr>0 and sctr<3: #patients with at least 1 symptom
        if p_age>=1 and p_age<=6 or p_age>=65: #infants and elderly
            mpctr+=1 #count how many persons might develop pneumonia
        print(pname+", The possibility that you have pneumonia is low.")
        print ("Recommendation: Visit a doctor to get any necessary medication")
    prtspace()
    menu()

def chk_spike():
    if mpctr>=10: #10 as threshold for testing 
        print("ALERT!")
        print("There is an increase in the number of persons prone to pneumonia")
    else:
        print("No alarm at the moment")

def main() :
    prtspace()
    menu()
    

main()