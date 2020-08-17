
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import re

#Populates Sales By Quarter Sub Menu 
#Allows users to enter input to see desired data insight
def SalesByQuarter():
    xl = pd.ExcelFile("SalesData.xlsx")
    SalesData = xl.parse("Orders")
   # Decorating = "\n" + "*"*25 + "\n"
    #Find which quarter had the most sales
    SalesMonth = SalesData
    SalesMonth["Quarter"] = SalesMonth["Order Date"].dt.quarter
    SalesMonth["Year"] = SalesMonth["Order Date"].dt.year
    quarter_sales_columns = SalesData [["Quarter", "Sales"]]
    sns.set(rc = {'figure.figsize' : (11,5)})
   
    print("\n---------------------------------")
    print("Quarterly Sales Data Information")
    print("---------------------------------")
    Seasonal_Data_Input = input("Please enter a number from 1-3 to see the quarterly data: \n \n [1] Identify Product Sales By Quarter Each Year \n [2] Identify Total Sales And Total Profit By Quarter \n [3] Go Back to Main Menu \n \n Please enter here: ")
    while not Seasonal_Data_Input or not Seasonal_Data_Input.isdigit() or Seasonal_Data_Input.isdigit():
        if not Seasonal_Data_Input:
            Seasonal_Data_Input = input("Response cannot be blank. Please enter a number from the given list: \n \n [1] Identify Product Sales By Quarter Each Year \n [2] Identify Total Sales And Total Profit By Quarter \n [3] Go Back to Main Menu \n \n Please enter here: ")
            continue
        if not Seasonal_Data_Input.isdigit():
            Seasonal_Data_Input= input("Response must contain numbers only. Please enter a number from the given list: \n \n [1] Identify Product Sales By Quarter Each Year \n [2] Identify Total Sales And Total Profit By Quarter \n [3] Go Back to Main Menu \n \n Please enter here: ")
            continue
        if Seasonal_Data_Input.isdigit():
            Input_Int = int (Seasonal_Data_Input)
            if Input_Int == 0 or Input_Int >=4:
                Seasonal_Data_Input = input("Incorrect number entered. Please enter a number from the given list: \n \n [1] Identify Product Sales By Quarter Each Year \n [2] Identify Total Sales And Total Profit By Quarter \n [3] Go Back to Main Menu \n \n Please enter here: ")
                continue
            if Input_Int == 1:
                #find product sales by quarter
                    Yearly_Sales_By_Quarter = SalesMonth[["Year", "Quarter", "Sales", "Sub-Category"]]
                    Quarterly_Input = input("Please select the desired year to view:  \n \n [1] 2014 \n [2] 2015 \n [3] 2016 \n [4] 2017 \n \n Please enter here: ")
                    while not Quarterly_Input or not Quarterly_Input.isdigit() or Quarterly_Input.isdigit():
                        if not  Quarterly_Input:
                            Quarterly_Input = input("Response cannot be blank. Please select the desired year to view: \n \n [1] 2014 \n [2] 2015 \n [3] 2016 \n [4] 2017 \n \n Please enter here: ")
                            continue
                        if not  Quarterly_Input.isdigit():
                            Quarterly_Input= input("Response must contain numbers only. Please select the desired year to view: \n \n [1] 2014 \n [2] 2015 \n [3] 2016 \n [4] 2017 \n \n Please enter here: ")
                            continue
                        if Quarterly_Input.isdigit():
                            Quarterly_Input_Int = int (Quarterly_Input)
                            
                            if Quarterly_Input_Int == 0 or Quarterly_Input_Int > 4:
                                Quarterly_Input = input("Incorrect number entered. Please select the desired year to view: \n \n [1] 2014 \n [2] 2015 \n [3] 2016 \n [4] 2017 \n \n Please enter here: ")
                                continue
                            if Quarterly_Input_Int == 1:
                                year_sales = Yearly_Sales_By_Quarter.loc[Yearly_Sales_By_Quarter["Year"] == 2014]
                                Quarter_sales_subCat = year_sales [["Quarter", "Sales", "Sub-Category"]]
                                Quarters = SalesData.Quarter.unique()
                                Quarters.sort()
                                for Quarter in Quarters:
                                    quarters_sales = Quarter_sales_subCat.loc[Quarter_sales_subCat["Quarter"] == Quarter]
                                    noquarters = quarters_sales [["Sales", "Sub-Category"]]
                                    quarter_total_sales = noquarters.groupby(by = "Sub-Category").sum().sort_values(by = "Sales", ascending = False)
                                    quarter_total_sales = quarter_total_sales.reset_index()
                                    barchart3 = sns.barplot(x= "Sub-Category", y = "Sales", data = quarter_total_sales.head(10))
                                    barchart3.set_title("Top 10 Products in Terms of Sales: Quarter " + str(Quarter) + " Year 2014")
                                    plt.rcParams.update({'font.size':3})
                                    plt.ylabel('Sales (Dollar Amount)')
                                    plt.show()
                                    
                            if Quarterly_Input_Int == 2:
                                year_sales = Yearly_Sales_By_Quarter.loc[Yearly_Sales_By_Quarter["Year"] == 2015]
                                Quarter_sales_subCat = year_sales [["Quarter", "Sales", "Sub-Category"]]
                                Quarters = SalesData.Quarter.unique()
                                Quarters.sort()
                                for Quarter in Quarters:
                                    quarters_sales = Quarter_sales_subCat.loc[Quarter_sales_subCat["Quarter"] == Quarter]
                                    noquarters = quarters_sales [["Sales", "Sub-Category"]]
                                    quarter_total_sales = noquarters.groupby(by = "Sub-Category").sum().sort_values(by = "Sales", ascending = False)
                                    quarter_total_sales = quarter_total_sales.reset_index()
                                    barchart4 = sns.barplot(x= "Sub-Category", y = "Sales", data = quarter_total_sales.head(10))
                                    barchart4.set_title("Top 10 Products in Terms of Sales: Quarter " + str(Quarter) + " Year 2015")
                                    plt.rcParams.update({'font.size':3})
                                    plt.ylabel('Sales (Dollar Amount)')
                                    plt.show()
                            if Quarterly_Input_Int == 3:
                                year_sales = Yearly_Sales_By_Quarter.loc[Yearly_Sales_By_Quarter["Year"] == 2016]
                                Quarter_sales_subCat = year_sales [["Quarter", "Sales", "Sub-Category"]]
                                Quarters = SalesData.Quarter.unique()
                                Quarters.sort()
                                for Quarter in Quarters:
                                    quarters_sales = Quarter_sales_subCat.loc[Quarter_sales_subCat["Quarter"] == Quarter]
                                    noquarters = quarters_sales [["Sales", "Sub-Category"]]
                                    quarter_total_sales = noquarters.groupby(by = "Sub-Category").sum().sort_values(by = "Sales", ascending = False)
                                    quarter_total_sales = quarter_total_sales.reset_index()
                                    barchart5 = sns.barplot(x= "Sub-Category", y = "Sales", data = quarter_total_sales.head(10))
                                    barchart5.set_title("Top 10 Products in Terms of Sales: Quarter " + str(Quarter) + " Year 2016")
                                    plt.rcParams.update({'font.size':3})
                                    plt.ylabel('Sales (Dollar Amount)')
                                    plt.show()
                            if Quarterly_Input_Int == 4:
                                year_sales = Yearly_Sales_By_Quarter.loc[Yearly_Sales_By_Quarter["Year"] == 2017]
                                Quarter_sales_subCat = year_sales [["Quarter", "Sales", "Sub-Category"]]
                                Quarters = SalesData.Quarter.unique()
                                Quarters.sort()
                                for Quarter in Quarters:
                                    quarters_sales = Quarter_sales_subCat.loc[Quarter_sales_subCat["Quarter"] == Quarter]
                                    noquarters = quarters_sales [["Sales", "Sub-Category"]]
                                    quarter_total_sales = noquarters.groupby(by = "Sub-Category").sum().sort_values(by = "Sales", ascending = False)
                                    quarter_total_sales = quarter_total_sales.reset_index()
                                    barchart6 = sns.barplot(x= "Sub-Category", y = "Sales", data = quarter_total_sales.head(10))
                                    barchart6.set_title("Top 10 Products in Terms of Sales: Quarter " + str(Quarter) + " Year 2017")
                                    plt.rcParams.update({'font.size':3})
                                    plt.ylabel('Sales (Dollar Amount)')
                                    plt.show()
                            
                            break
                    Seasonal_Data_Input = input("Insight Completed. Would you like to see another data set?: \n \n [1] Identify Product Sales By Quarter Each Year \n [2] Identify Total Sales And Total Profit By Quarter \n [3] Go Back to Main Menu \n \n Please enter here: ") 
    
            if Input_Int == 2:
                quarter_total_sales = quarter_sales_columns.groupby(by = "Quarter").sum().sort_values(by = "Sales")
                quarter_total_sales = quarter_total_sales.reset_index()
                print("The following chart details each quarter based on their total sales: ")
    
                #prints bar graph
                barchart1 = sns.barplot(x= "Quarter", y = "Sales", data = quarter_total_sales)
                barchart1.set_title("Total Sales by Quarter (2014-2017)")
                plt.ylabel('Sales (Dollar Amount)')
                plt.show()
        
                QuarterProfit = SalesMonth[["Quarter" ,"Profit"]]
                quarter_total_profit = QuarterProfit.groupby(by = "Quarter").sum().sort_values(by = "Profit")
                print("\n The following chart details each quarter based on their total profit: ")
              
                quarter_total_profit = quarter_total_profit.reset_index()
                barchart2 = sns.barplot(x = "Quarter", y = "Profit", data = quarter_total_profit)
                barchart2.set_title("Total Profit by Quarter (2014-2017)")
                plt.ylabel('Profit (Dollar Amount)')
                plt.show()
                
                Seasonal_Data_Input = input("Insight Completed. Would you like see another data set?: \n \n [1] Identify Product Sales By Quarter Each Year \n [2] Identify Total Sales And Total Profit By Quarter \n [3] Go Back to Main Menu \n \n Please enter here: ") 
    
            
            if Input_Int == 3:
                break
