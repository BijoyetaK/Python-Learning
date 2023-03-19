import os
import csv

csvfile = 'budget_data.csv'
datafolder = 'csvfile'
#path to collect the data from the csv file in the csvfile folder
budget_csv = '{0}/{1}/{2}'.format(os.getcwd(),datafolder,csvfile)
budgets ={}
budget_analysis =[]
change_values = []

with open(budget_csv,'r') as csvfilehandle:
     budgetreader = csvfilehandle.readlines()
     i = 0
     for line in budgetreader:
        if i > 0:
            line = line.replace('\n','')
            line_array = line.split(',') #split the string from the list of strings by delimiter and put it into another list
            #print(line_array)
            budget_date_int = int(line_array[0].replace('/',''))
            budget_pf_int = int(line_array[1])
            budgets[budget_date_int] = budget_pf_int
         
        i = i + 1

budget_dates = list(budgets.keys()) #returning a datatype dict.keys which needs converted to list before sort
budget_dates.sort() #sorts the date column
print(budget_dates)
i = 0
total_record_cnt = len(budget_dates)
for bd in budget_dates:
    current_pf = budgets[bd]
    if i < total_record_cnt - 1:
       next_bd_date = budget_dates[i+1]
       next_bd_pf = budgets[next_bd_date] 
       change_from_previous = round((next_bd_pf - current_pf) * 1.0 / (1.0 * current_pf),2)
       change_value = next_bd_pf - current_pf
    if i == 0:
        change_from_previous = 0
        change_value = 0
    budget_analysis.append([bd,current_pf, next_bd_date, next_bd_pf,change_value,change_from_previous])
    change_values.append(change_value)
    i = i + 1
print('---------------')
print(budget_analysis)


change_values.sort(reverse=True)
print('-----------------')
print(change_values[0])


