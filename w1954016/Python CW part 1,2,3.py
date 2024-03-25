# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# 30/11/2022

# student ID : w1954016

Pass  = 0
Defer = 0
Fail  = 0

# counts the number of students who obtained progress for the module.
ProgressPrints = 0
TrailerPrints  = 0
RetriverPrints = 0
ExcludedPrints = 0

#Assigning the list
credit_types = [0,20,40,60,80,100,120]
credit = []

f = open("test.txt","w") #Open the file.

#Functions
def enter_credit(creditinput):
    while True:
        try:
            inputs=int(input(creditinput))
            if( inputs in credit_types):
                return inputs
            else:
                print('Out of range')
                continue
            
        except ValueError: # if the input entered by the user is not an integer handle the error and display the following.
            print("Integer required")

print('If you want Student mode press "s" , If you want Staff mode press "t" ')
mode = input("Select your mode : ")
while True:
    if mode in ['s','t']: #select the mode
        break
    else:
        print('select the correct mode')
        print('If you want Student mode press "s" , If you want Staff mode press "t" ')
        mode = input("Select your mode : ")
if mode == 's':
    while True:
        Pass  = enter_credit('Please enter your credits in Pass : ')
        Defer = enter_credit('Please enter your credits in Defer : ')
        Fail  = enter_credit('Please enter your credits in Fail : ')
  

        inputs = ('Your credits in Pass is ','Your credits in Defer is ','Your credits in Fail is ')
        
        total = Pass + Defer + Fail
        
        if total != 120: # if the total credits not eqal to 120 show this
             print('Total incorrect')
             continue

        else:  #if the total credits are equal 120 continue.
            break
        
    if total>120:
        print("Out of range try again")

       #Progress (student)
    if Pass == 120:
        print("Progress")
      

        #Exclude (student)
    elif Fail == (80 or 100 or 120):
        print("Exclude")
        

        #Progress (module trailer) (student)
    elif Pass == 100:
        print('Progress (module trailer) ')
        
        #Do not progress – module retriever (student)
    else:
        print("Do not Progress – Module retriever ")
        
else:
        
    while True:
        while True:
            Pass  = enter_credit('Please enter your credits in Pass : ')
            Defer = enter_credit('Please enter your credits in Defer : ')
            Fail  = enter_credit('Please enter your credits in Fail : ')
      

            inputs = ('Your credits in Pass is ','Your credits in Defer is ','Your credits in Fail is ')
            
            total = Pass + Defer + Fail
            
            if total != 120: # if the total credits not eqal to 120 show this.
                 print('Total incorrect')
                 continue

            else:    #if the total credits are equal 120 continue.
                break
            
        if total>120:
            print("Out of range try again")

           #Progress 
        if Pass == 120:
            print("Progress")
            ProgressPrints+=1
            credit.append('Progress - '+str(Pass)+', '+str(Defer)+', '+str(Fail))
            f.write('Progress - ' + str(Pass) + ', ' + str(Defer) + ', ' + str(Fail) + '\n')

            #Exclude 
        elif Fail == Fail == 80 or Fail == 100 or Fail == 120:
            print("Exclude")
            ExcludedPrints+=1
            credit.append('Exclude - '+str(Pass)+', '+str(Defer)+', '+str(Fail))
            f.write('Exclude - ' + str(Pass) + ', ' + str(Defer) + ', ' + str(Fail) + '\n')


            #Progress (module trailer)
        elif Pass == 100:
            print('Progress (module trailer) ')
            TrailerPrints+=1
            credit.append('Progress(Module Trailer - '+str(Pass)+', '+str(Defer)+', '+str(Fail))
            f.write('Progress(Module Trailer - ' + str(Pass) + ', ' + str(Defer) + ', ' + str(Fail) + '\n')

            #Do not progress – module retriever
        else:
            print("Do not Progress – module retriever ")
            RetriverPrints+=1
            credit.append('Module retriver - '+str(Pass)+', '+str(Defer)+', '+str(Fail))
            f.write('Module retriver - ' + str(Pass) + ', ' + str(Defer) + ', ' + str(Fail) + '\n')
             
        decision = None
        while True:
            
        
            decision = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
            if decision == 'y' or decision == 'q':    
                break
    #Get the decision.
        if decision == 'y' :
            continue
        elif decision == 'q' : #if the user enter q as the input break with the loop
            break
        else:
            print('Enter a valid decision')
            continue #if the user enter Y as the input continue with the loop 

    f.close()#close the file.
            
    print('-----------------------------------------------------------------------------------------------------------\nHistrogram')

    print("progress" ,ProgressPrints,':', '*'*ProgressPrints)
    print("Trailer", TrailerPrints, ':', '*'*TrailerPrints)
    print("Retriever", RetriverPrints,':', '*'*RetriverPrints)
    print("Excluded", ExcludedPrints,':', '*'*ExcludedPrints)

    outcometotal = ProgressPrints+TrailerPrints+RetriverPrints+ExcludedPrints

    print(outcometotal,' outcome in total')

    print('-----------------------------------------------------------------------------------------------------------')

    print('Part 2 :')#Histrogram

    for i in credit:
        print(i)

    print('part 3 : ')#Part 3 - List/Tuple/Directory

