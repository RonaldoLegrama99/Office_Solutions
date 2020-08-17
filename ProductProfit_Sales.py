

import pandas as pd
xl = pd.ExcelFile("SalesData.xlsx")
SalesData = xl.parse("Orders")

#Populates the Profit, Sales, and Discount Sub Menu
#Allows users to enter input to see desired data insight
def profit_SubMenu ():
    Decorating = "\n" + "*"*68 + "\n"
    print("\n---------------------------------------------------------------------------")
    print("Summarization Of Profit, Sales, And Discount That Sold In The Past 4 Years: ")
    print("---------------------------------------------------------------------------")
    SalesYear = SalesData
    SalesYear["Year"] = SalesYear["Order Date"].dt.year
    YearlySales = SalesYear [["Year", "Sales", "Profit"]]
    YearlyTotalSales = YearlySales.groupby(by= "Year").sum()
    YearlyTotalSales = YearlyTotalSales.reset_index()
    print(YearlyTotalSales)
    
    print("\n-----------------------")
    print("Yearly Profit and Sales")
    print("------------------------")
    required_input = 1
    while required_input == 1:
        profit_SubMenu = input("Please enter a number from 1-3 below: \n \n [1] The Top 5 Profitable Products And Its Sale Data \n [2] The Least 5 Profitable Products And Its Sales Data \n [3] Main Menu \n \n Please enter here: ")
        if not profit_SubMenu:
            print("\nResponse cannot be blank or space.")
            continue
        if not profit_SubMenu.isdigit():
            print("\nResponse must be a number only.")
            continue
        profit_SubMenu = int(profit_SubMenu)
        if not profit_SubMenu > 0:
            print("\nIncorrect number entered.")
            continue
        if not profit_SubMenu <= 3:
            print("\nIncorrect number entered.")
            continue
   
        if profit_SubMenu == 1:
 
                print("\n------------------------------------------")
                print("Top Profitable Products And Its Sale Data")
                print("------------------------------------------")
                year_profit_discount = SalesData [["Profit", "Sales","Product Name","Year"]]
                years = SalesData.Year.unique()
                years.sort()
               
                required_input_sub = 1
                while required_input_sub == 1:
                    profit_discount = input ("Please enter a number from 1-4 to see detail data: \n \n [1] The Top 5 Profitable Products That Sold The Most \n [2] The Top 5 Profitable Products That Sold The Least \n [3] Main Menu \n [4] Go Back \n \n Please enter here: ")
                    if not profit_discount:
                        print("\nResponse cannot be blank or space.")
                        continue
                    if not profit_discount.isdigit():
                        print("\nResponse must be a number only.")
                        continue
                    profit_discount = int(profit_discount)
                    if not profit_discount > 0:
                        print("\nIncorrect number entered.")
                        continue
                    if not profit_discount <= 4:
                        print("\nIncorrect number entered.")
                        continue
                   
                    if profit_discount == 1:
                        for SalesYear in years:
                            year_profit = year_profit_discount.loc[year_profit_discount["Year"] == SalesYear]
                            year_total_profit = year_profit.groupby(by = ["Product Name","Year"]).sum().sort_values(by = "Profit").sort_values(by = "Sales", ascending = False )
                            print("The top 5 profitable products that sold the most in " + str(SalesYear) + " are: \n \n")
                            year_total_profit = year_total_profit.reset_index()
                            print(year_total_profit.head(5))
                            print(Decorating)
                           
                    if profit_discount == 2:
                        for SalesYear in years:
                            year_profit = year_profit_discount.loc[year_profit_discount["Year"] == SalesYear]
                            year_total_profit = year_profit.groupby(by = ["Product Name", "Year"]).sum().sort_values(by = ["Profit", "Sales"], ascending = False)
                            print("The top 5 profitable products that sold the least in " + str(SalesYear) + " are: \n \n")
                            year_total_profit = year_total_profit.reset_index()
                            print(year_total_profit.head(5))
                            print(Decorating)
                           
                    if profit_discount == 3:
                        required_input_sub = 0
 
                        profit_SubMenu = 3
                        break
                    if profit_discount == 4:
                        required_input_sub = 0
                        break
                    print("Insight Completed. Would you like to look at another data set?")
                   
        if profit_SubMenu ==2:
           
                print("\n-------------------------------------------")
                print("Least Profitbale Products And Its Sale Data")
                print("--------------------------------------------")
                year_profit_wdiscount = SalesData [["Year", "Product Name", "Profit", "Sales"]]
                years = SalesData.Year.unique()
                years.sort()
               
                required_input_sub = 1
                while required_input_sub == 1:
                    profit_noDiscount = input ("Please enter a number from 1-4 to see detail data:  \n \n [1] The Least 5 Profitable Products That Sold The Most \n [2] The Least 5 Profitable Products That Sold The Least \n [3] Main Menu \n [4] Go Back \n \n Please enter here: ")
                    if not profit_noDiscount:
                        print("\n Response cannot be blank or space.")
                        continue
                    if not profit_noDiscount.isdigit():
                        print("\n Response must be a number only.")
                        continue
                    profit_noDiscount = int(profit_noDiscount)
                    if not profit_noDiscount > 0:
                        print("\n Incorrect number entered.")
                        continue
                    if not profit_noDiscount <= 4:
                        print("\n Incorrect number entered.")
                        continue
                   
                    if profit_noDiscount == 1:
                        for SalesYear in years:
                            year_profit = year_profit_wdiscount.loc[year_profit_wdiscount["Year"] == SalesYear]
                            year_total_profit = year_profit.groupby(by = ["Product Name", "Year"]).sum().sort_values(by = ["Profit", "Sales"], ascending = False)
                            print("The least 5 profitable products that sold the most in " + str(SalesYear) + " are: \n \n")
                            year_total_profit = year_total_profit.reset_index()
                            print(year_total_profit.tail(5))
                            print(Decorating)
                           
                    if profit_noDiscount == 2:      
                        for SalesYear in years:
                            year_profit = year_profit_wdiscount.loc[year_profit_wdiscount["Year"] == SalesYear]
                            year_total_profit = year_profit.groupby(by = ["Product Name", "Year"]).sum().sort_values(by = "Profit").sort_values(by = "Sales", ascending = False)
                            print("The least 5 profitable products that sold the least in " + str(SalesYear) + " are: \n \n")
                            year_total_profit = year_total_profit.reset_index()
                            print(year_total_profit.tail(5))
                            print(Decorating)
                           
                    if profit_noDiscount == 3:
                        required_input_sub = 0
 
                        profit_SubMenu = 3
                        break
                    if profit_noDiscount == 4:
                        required_input_sub = 0
                        break
                    print("Insights Completed. Would you like to see another data set?")
        if profit_SubMenu == 3:
            break

