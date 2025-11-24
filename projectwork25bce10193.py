print("PROJECT WORK FOR INTRODUCTION TO PROBLEM SOLVING AND PROGRAMMING")
print('''
''')
print("Name:Abhishek Singh")
print("Registration Number:25BCE10193")
print("Under the guidance of:Dr.G.R.Hemalaxmi")
print("Topic:Station Management System")
print('''
''')
print("***********************************************************************************************************************************************")
print("*                                                        STATION MANAGEMENT SYSTEM                                                            *")
print("***********************************************************************************************************************************************")

print('''
''')

print("                                                              MAIN MENU                                    ")
print('''
''')
print("***********************************************************************************************************************************************")
print("")
record=[]
while True:
  print("What do you want to do?")
  print("1.Register a reservation")
  print("2.Update a record")
  print("3.Search for a reservation")
  print("4.Delete a reservation")
  print("***********************************************************************************************************************************************")
  print("")
  ans=int(input("Please choose an option given above"))
  if ans==1:
    m=int(input("How many people you want to book tickets for?"))
    c=0
    while c<m:
     NAME=input("Enter the name of the passenger")
     BEGINNING=input("Enter the station you want to board train from")
     DESTINATION=input("Enter the destination station")
     PNR=int(input("Enter your PNR number"))
     data=[NAME,BEGINNING,DESTINATION,PNR]
     record.append(data)
     c=c+1
    print("Reservation registered successfully")
  elif ans==2:
     pnr=int(input("Enter your PNR number"))
     if len(str(pnr))==10:
         if data[3]==pnr:
             print("What do you want to update?")
             print("1.Name of the passenger")
             print("2.Boarding station")
             print("3.Destination station")
             ans=int(input('Please enter a choice from the above'))
             if ans==1:
                name=input("Enter the new name to be updated")
                data[0]=name
                print("Name updated successfully")
                print("***********************************************************************************************************************************************")

             elif ans==2:
                board=input("Enter the new boarding station to be updated")
                data[1]=board
                print("Name updated successfully")
                print("***********************************************************************************************************************************************")

             elif ans==3:
                dest=input("Enter the new destination station to be updated")
                data[2]=dest
                print("Name updated successfully")
                print("***********************************************************************************************************************************************")

             else:
                print("Please choose a valid option")
         else:
              print("Sorry no reservation with the given pnr found")
     else:
          print("Invalid PNR,please enter a valid PNR")  
  elif ans==3:
     pnr=int(input("Enter the PNR number"))
     if len(str(pnr))==10:
          for i in record:
             if i[3]==pnr:
               print("The Name of the passenger is:",i[0])
               print("The Boarding station is:",i[1])
               print("The Destiantion station is:",i[2])
               print("***********************************************************************************************************************************************")
               break
             else:
               print("Sorry, no record found")
               print("***********************************************************************************************************************************************")
     else:
          print("Invalid PNR,please enter a valid PNR number")
           
  elif ans==4:
    pnr=int(input("Enter the PNR number"))
    if len(str(pnr))==10:
        for i in record:
           if i[3]==pnr:
               record.remove(i)
        print("Record deleted successfully")
        print("***********************************************************************************************************************************************")
    else:
        print("Invalid PNR,please enter a valid PNR")
    
  else:
      print('Please enter a valid choice')
  print("***************************************************************************************************************************************************")
  choice=input("Want to continue?(y/n)")
  if choice.lower()=="y":
      continue
  elif choice.lower()=="n":
      print("***********************************************************************************************************************************************")
      print("                                                         THANKYOU FOR VISITING                                  ")
      print("                                                            HAVE A NICE DAY                                      ")
      break
  else:
      print("Invalid choice")
          
      
    
    

