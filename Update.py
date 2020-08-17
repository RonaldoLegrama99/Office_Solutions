#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:30:52 2019
 
@author: cameronlee
"""
 
import sqlite3
import re
 
 
conn = sqlite3.connect("OS_Employee.db")

#Used to check if input has at least one number.       
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
 
#Allows user to update employee password
def Update_Info():
    print("\n----------------------------")
    print("Update Employee Information")
    print("----------------------------")
    Update_Input = input("The following action will update your password, would like to continue? \n [1] Yes \n [2] No  \n \n")
    while not Update_Input or not Update_Input.isdigit() or Update_Input.isdigit():
        if not Update_Input:
            Update_Input = input("Response cannot be blank. The following action will update your password, would like to continue? \n [1] Yes \n [2] No  \n \n")
            continue
        if not Update_Input.isdigit():
            Update_Input = input("Response must contain a number only. The following action will update your password, would like to continue? \n [1] Yes \n [2] No  \n \n")
            continue
        if Update_Input.isdigit():
            Enter_Int =int(Update_Input)
            if Enter_Int == 0 or Enter_Int > 2:
                Update_Input = input("Incorrect number entered. Please enter \n [1] Yes \n [2] No \n \n")
                continue
     
                   
            if Enter_Int == 1:
                employeeIDTest = False
                loopTest = False
                while loopTest == False:
                    while employeeIDTest == False:
                        EmpID = input('Response must contain a number only. Please enter your employee ID: ')
                        EmpID = EmpID.strip()
                        if not EmpID.isdigit():
                            EmpID = input('Please enter your employee ID: ')
                        if EmpID.isdigit():
                            employeeIDTest = True
                            if len(EmpID) < 4:
                               
                                EmpID = input("Incorrect number of digits, please try again: ")
                            if len(EmpID) > 4:
                               
                                EmpID = input("Incorrect number of digits, please try again: ")
             
                    #Checks if inputed employeeID is valid
                    OldPassword = input("Please enter your old password: ")
                    with conn:
                        cur = conn.cursor()
                        cur.execute("SELECT COUNT (*) FROM Employee WHERE(EmployeeID = '" + EmpID +"') AND (Password = '" + OldPassword +"') " )
                        newResults = cur.fetchone()
                #If password does not match employee ID, directs you again to enter old password
                        if newResults [0] ==1:
                            loopTest = True
                        else:
                            employeeIDTest = False
                            print("The employeeid or password provided are incorrect.")
                            continue
                    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
                    NewPassword = input("Please enter your new password. The password should have greater than 8 characters and at least one  number, one capital letter, and a special character: ")
                    while not NewPassword or len(NewPassword) < 8 or NewPassword.isalpha() or not hasNumbers(NewPassword) or regex.search(NewPassword) == None:
                        if not NewPassword: #checks if password is blank
                            NewPassword = input ("Password cannot be blank. Please re-enter an adjusted password: ")
                            continue
                        if len(NewPassword) < 8: #checks if password is less than 8 chracters long
                            NewPassword = input ("Password is not of correct length. Please re-enter an adjusted password: ")
                            continue
                        if not hasNumbers(NewPassword): #checks if password contains at least one number
                            NewPassword = input("Password does not contain any numbers. Please re-enter an adjusted password: ")
                            continue
                        if(regex.search(NewPassword) == None): #checks if password contains at least one special character
                            NewPassword = input("Password does not contain any special characters. Please re-enter an adjusted password: ")
                            continue
                                 #Password Confirmation      
                    Password1 = input("Please verify your new password: ")
                    while (NewPassword != Password1):
                        Password1= input("Passwords do not match. Please try again: ")
                            #Updates New Password
                    with conn:
                        cur = conn.cursor()
                        UpdateValues = "UPDATE Employee SET Password = ('{}') WHERE (EmployeeID = ('{}') AND  Password = ('{}'))"
                        UpdateString = UpdateValues.format( NewPassword, EmpID, OldPassword)
                        cur.execute(UpdateString)
                        cur.execute("SELECT*FROM Employee WHERE(EmployeeID == '{}')".format(EmpID))
                        results = cur.fetchone()
                        print("Your credentials have been updated to: \n ") #prints out the updated employee information which includes new password
                        print(results)
   
                       
                #If user chooses "NO" to update goes back to main menu
            if Enter_Int == 2:
                break
               
            Update_Input = input("Would you like to update another user or quit? \n [1] Yes \n [2] No \n \n")


