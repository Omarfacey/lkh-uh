 
#Author:Omar Facey
#Date: Created:
#Course: ITT103
#The whole code is defined as a funtion.




def Commission_calculator():
    #The following varables are used to store the usesr's input.
    try:
        salesperson_id= str(input("Please input the salesperson's ID Number "))
        while not salesperson_id:
            salesperson_id= str(input("Please input the salesperson's ID Number "))

        sales=float(input("Enter the total sales "))
        class_=int(input("Enter the the class number "))
    except ValueError:
        test=str(input("You have entered invalid data, if you wish to start over type 'y' for yes or enter any other input for no")).lower()
        if test== 'y':
            Commission_calculator()
        else:
            exit()    
      

    #The following variables are set to zero to store information later in the code.
    final_commission=0
    rate=0

    #Conditional is be used to check the class entered:
    if class_== 1:
      #A nested if statement is used to check check the amount made in sales the commisssion will also be dont in the nested if statement
      if sales <= 1000:
          rate=6 
          final_commission=sales*(rate/100) 
          
      elif sales <2000:
          rate= 7
          final_commission=sales*(rate/100)
      else:
          rate=10
          final_commission=sales* (rate/100)
      #The result for the calculations and vital informations are printed by the use of the codes below.    
      print("_________________________________________________________")#line are printed to seperate the inofrmaton for a better understanding. 
      print("salseperson ID#:",salesperson_id) 
      print("_________________________________________________________")   
      print("Class number :",class_)
      print("_________________________________________________________")
      print("The commission rate collected is :", rate,"percent")
      print("_________________________________________________________")
      print("The final commission is for sale is:", "$",+(final_commission))
      print("_________________________________________________________")
      print("                                                                   ") 
      
    elif class_ ==2:
      if sales <1000:
          rate=4
          final_commission=sales*(rate/100)
         
      else:
          rate=6
          final_commission=sales*(rate/100)
      #The result for the calculations and vital informations are printed by the use of the codes below.
          
      print("_________________________________________________________")  #lines are printed to seperate the inofrmaton for a better understanding.
      print("salseperson ID#:",salesperson_id)
      print("_________________________________________________________") 
      print("Class number :",class_)
      print("_________________________________________________________")
      print("The commission rate collected is :", rate,"percent")
      print("_________________________________________________________")
      print("The final commission is for sale is:", "$",+(final_commission))
      print("_________________________________________________________")
      print("                                                                   ")

      
    elif class_ == 3:
        rate=4.5
        final_commission=sales*(rate/100)
        #The result for the calculations and vital informations are printed by the use of the codes below.
        print("_________________________________________________________")#lines are printed to seperate the inofrmaton for a better understanding.    
        print("salseperson ID#:",salesperson_id)
        print("_________________________________________________________") 
        print("Class number :",class_)
        print("_________________________________________________________")
        print("The commission rate collected is :", rate,"percent")
        print("_________________________________________________________")
        print("The final commission is for sale is:", "$",+(final_commission))
        print("_________________________________________________________")
        print("                                                                   ")


    #If the class condiftions above aren't me the program would resort to the else statement and print the error message.     
    else:
        print("the class entered is not a vaild class")
        
    #A variable would be used to hold the answer for the for the question asked.      
    question=str(input("Do you wish to do another calculation?, type 'y' for yes and 'n' for no ")).lower()

    #A conditional statement to check the answer that was inputed by th user.
    if question == 'y':
        #If the user inputs 'y' the program is started over by way of a nested fuction.
        Commission_calculator()
    else:
        #If the user entered any other information other than 'y', a message will be printed and the program is ended.
      print("Have a nice day!")
      exit()

#The calling the function above is done which would run the program defined in the function.       
Commission_calculator()     

