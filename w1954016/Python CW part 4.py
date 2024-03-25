# w1954016

#05/12/2022

# Part 4

Pass = 0
Defer = 0
Fail = 0

# counts the number of students who obtained progress for the module.
ProgressPrints = 0
TrailerPrints = 0
RetriverPrints = 0
ExcludedPrints = 0

credit_types = [0, 20, 40, 60, 80, 100, 120]
student_ID = 0
uni_dict = {} # dictionery created store the uow id as the key and the credit obtains as values.



def enter_credit(creditinput):
    while True:
        try:
            inputs = int(input(creditinput))
            if (inputs in credit_types):
                return inputs
            else:
                print('Out of range')
                
                
                

        except ValueError: # if the input entered by the user is not an integer handle the error and display the following.
            print("Integer required")

        

while True:
    while True:
        student_ID = input("Enter your student ID : ").lower() # if user input capital letter,it will lower.
        
        try:
            int(student_ID[1:]) #converts the input entered into an integer from the 2nd position onwards
            if student_ID[0] != 'w': # if the student id entered dosent have 'w' displasy the following and continue.
                print('Invalid and try again')
                continue
            else:
                if len(student_ID) < 8 : # if the lenght of the student id exceeds 8 print'invalid' and continue.
                    print('Invalid  ')
                    continue
                else:
                    if student_ID in uni_dict.keys() : # if the student id already exists inth dictionery print the following,if not break the loop.
                        print("University ID already exists")
                    else:
                        break
        except ValueError: # if the input entered by the user doesnt have 'w' and 7 integers handle the error and display the following.
            print('Invalid Student ID')
            continue

        
         
                
     
    
    Pass = enter_credit('Please enter your credits in Pass : ')
    Defer = enter_credit('Please enter your credits in Defer : ')
    Fail = enter_credit('Please enter your credits in Fail : ')

    
     

    total = (Pass + Defer + Fail)

    



    
    if total != 120: # if the total credits not eqal to 120 show this
        print('Total incorrect')

    elif Pass == 120: #Progress
        print("Progress")
        ProgressPrints = +1
        uni_dict[student_ID] = 'Progress - ' + str(Pass) + ', ' + str(Defer) + ', ' + str(Fail)
        
    elif Fail == (80 or 100 or 120):  #Exclude
        print("Exclude")
        ExcludedPrints = +1
        uni_dict[student_ID] = 'Exclude - ' + str(Pass) + ', ' + str(Defer) + ', ' + str(Fail)
        
    elif Pass == 100: #Progress (module trailer)
        print('Progress (module trailer) ')
        TrailerPrints = +1
        uni_dict[student_ID] = 'Progress(Module Trailer - ' + str(Pass) + ', ' + str(Defer) + ', ' + str(Fail)
        
    else: #Do not progress – module retriever
        print("Do not Progress – module retriever ")
        RetriverPrints = +1
        uni_dict[student_ID] = 'Module retriver - ' + str(Pass) + ', ' + str(Defer) + ', ' + str(Fail)
        
    decision = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
    if decision == 'y': # if the user enter 'y' loop will continue.
        continue
    elif decision == 'q': # if the user enter 'q' loop will break.
        break
    else:
        print('Enter a valid decision')
        

print('-------------------------------------------------------------------------------')
print('Histogram')

print("progress", ProgressPrints, ':', '*' * ProgressPrints)
print("Trailer", TrailerPrints, ':', '*' * TrailerPrints)
print("Retriever", RetriverPrints, ':', '*' * RetriverPrints)
print("Excluded", ExcludedPrints, ':', '*' * ExcludedPrints)

outcome_total = ProgressPrints + TrailerPrints + RetriverPrints + ExcludedPrints

print(outcome_total, ' outcome in total')

print('-------------------------------------------------------------------------------')

for student_ID,Value in uni_dict.items():
    print(student_ID,':',Value,end = ' ')

print('\n-------------------------------------------------------------------------------')
