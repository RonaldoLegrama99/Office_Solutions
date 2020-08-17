from SalesByQuarter import SalesByQuarter
from CustomerLoyalty import CustomerLoyaltyMenu
from RegistrationTest import Registration
from ProductProfit_Sales import profit_SubMenu
from Region_Profit import Regional_Insight
from Update import Update_Info

#Populates Main_Menu for users to select what type of data insight they would like to inquire
def Main_Menu():
   
    Main_Menu_input = input("Welcome, please enter a number from 1-7 to see the task you would like to perform: \n \n [1] View Quarterly Sales Data Information \n [2] View Regional Sales Data Information \n [3] View Yearly Profit and Sales \n [4] View Customer Data For Loyalty Program \n [5] Register New User \n [6] Update Employee Information \n [7] Logout \n \n Please enter here: ")
    
    while not Main_Menu_input or not Main_Menu_input.isdigit() or Main_Menu_input.isdigit():
        if not Main_Menu_input:
            Main_Menu_input = input("Response cannot be blank. Please re-enter a number from 1-7 to see the task you would like to perform: \n \n [1] View Quarterly Sales Data Information \n [2] View Regional Sales Data Information \n [3] View Yearly Profit and Sales \n [4] View Customer Data For Loyalty Program \n [5] Register New User \n [6] Update Employee Information \n [7] Logout  \n \n Please enter here: ")
            continue
        if not Main_Menu_input.isdigit():
            Main_Menu_input= input("Response must contain numbers only. Please re-enter a number from 1-7 to see the task you would like to perform: \n \n [1] View Quarterly Sales Data Information \n [2] View Regional Sales Data Information \n [3] View Yearly Profit and Sales \n [4] View Customer Data For Loyalty Program \n [5] Register New User \n [6] Update Employee Information \n [7] Logout \n \n Please enter here: ")
            continue
        if Main_Menu_input.isdigit():
            Main_Menu_input_int = int(Main_Menu_input)
            
            if Main_Menu_input_int <= 0 or Main_Menu_input_int >=8:
                
                Main_Menu_input= input("Incorrect number. Please re-enter a number from 1-7 to see the task you would like to perform: \n \n [1] View Quarterly Sales Data Information \n [2] View Regional Sales Data Information \n [3] View Yearly Profit and Sales \n [4] View Customer Data For Loyalty Program \n [5] Register New User \n [6] Update Employee Information \n [7] Logout \n \n Please enter here: ")

                
            if Main_Menu_input_int == 1:
                
                SalesByQuarter()
                
                Main_Menu_input = input("Welcome, please enter a number from 1-7 to see the task you would like to perform: \n \n [1] View Quarterly Sales Data Information \n [2] View Regional Sales Data Information \n [3] View Yearly Profit and Sales \n [4] View Customer Data For Loyalty Program \n [5] Register New User \n [6] Update Employee Information  \n [7] Logout  \n \n Please enter here: ")
           
            if Main_Menu_input_int == 2:
                
                Regional_Insight()
                
                Main_Menu_input = input("Welcome, please enter a number from 1-7 to see the task you would like to perform: \n \n [1] View Quarterly Sales Data Information \n [2] View Regional Sales Data Information \n [3] View Yearly Profit and Sales \n [4] View Customer Data For Loyalty Program \n [5] Register New User \n [6] Update Employee Information \n [7] Logout \n \n Please enter here: ")

            
            if Main_Menu_input_int == 3:
                
                profit_SubMenu()
                
                Main_Menu_input = input("Welcome, please enter a number from 1-7 to see the task you would like to perform: \n \n [1] View Quarterly Sales Data Information \n [2] View Regional Sales Data Information \n [3] View Yearly Profit and Sales \n [4] View Customer Data For Loyalty Program \n [5] Register New User \n [6] Update Employee Information \n [7] Logout \n \n Please enter here: ")

            
            if Main_Menu_input_int == 4:
               
                CustomerLoyaltyMenu()
                
                Main_Menu_input = input("Welcome, please enter a number from 1-7 to see the task you would like to perform: \n \n [1] View Quarterly Sales Data Information \n [2] View Regional Sales Data Information \n [3] View Yearly Profit and Sales \n [4] View Customer Data For Loyalty Program \n [5] Register New User \n [6] Update Employee Information \n [7] Logout \n \n Please enter here: ")

            if Main_Menu_input_int == 5:
                
                Registration()
                
                Response_input = input("Would you like to register a new user or quit? \n [1] Yes \n [2] Quit \n \n Please enter here: ")
                while not Response_input or not Response_input.isdigit() or Response_input.isdigit():
                    if not Response_input:
                        Response_input = input("Response cannot be blank. Would you like to register a new user or quit? \n \n [1] Yes \n [2] No \n \n Please enter here: ")
                        continue
                    if not Response_input.isdigit():
                        Response_input = input("Response must contain numbers only. Would you like to register a new user or quit? \n \n [1] Yes \n [2] No \n \n Please enter here: ")
                        continue
                    if Response_input.isdigit():
                        Response_input_int = int(Response_input)
                        if  Response_input_int == 0 or Response_input_int > 2:
                            Response_input = input("Incorrect number entered. Would you like to register a new user or quit? \n \n [1] Yes \n [2] No \n \n Please enter here: ")
                            continue
                
                        if Response_input_int == 1:
                            Main_Menu_input_int = 5
                            break
                        if Response_input_int == 2:
                            Main_Menu_input = input("Welcome, please enter a number from 1-7 to see the task you would like to perform: \n \n [1] View Quarterly Sales Data Information \n [2] View Regional Sales Data Information \n [3] View Yearly Profit and Sales \n [4] View Customer Data For Loyalty Program \n [5] Register New User \n [6] Update Employee Information \n [7] Logout \n \n  Please enter here: ")
                            break
                        
                        
            if Main_Menu_input_int == 6:
               
                Update_Info()
               
                Main_Menu_input = input("Welcome, please enter a number from 1-7 to see the task you would like to perform: \n \n [1] View Quarterly Sales Data Information \n [2] View Regional Sales Data Information \n [3] View Yearly Profit and Sales \n [4] View Customer Data For Loyalty Program \n [5] Register New User \n [6] Update Employee Information \n [7] Logout \n \n Please enter here: ")
 
            if Main_Menu_input_int == 7:
                print("\nThank you for using Office Solutions. We hope to see you again soon!")
                break
