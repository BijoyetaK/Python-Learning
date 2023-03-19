import os
import csv

csvfile = 'budget_data.csv'
datafolder = 'Resources'
output_filename = 'analysis.txt'
output_folder = 'analysis'
#path to collect the data from the csv file in the csvfile folder
budget_csv = '{0}/{1}/{2}'.format(os.getcwd(),datafolder,csvfile)
output_filepath = '{0}/{1}/{2}'.format(os.getcwd(),output_folder,output_filename)
budgets ={}
budget_analysis =[]
change_values = []

#get the month data from date function
def getmonth_fromdate(datestring):
    month_name = datestring.split('-')[-1]
    return month_name

with open(budget_csv,'r') as csvfilehandle:
     budgetreader = csvfilehandle.readlines()
     i = 0
     for line in budgetreader:
        if i > 0:
            line = line.replace('\n','')
            line_array = line.split(',') #split the string from the list of strings by delimiter and put it into another list
            budget_pf_int = int(line_array[1])
            budgets[line_array[0]] = budget_pf_int #mapping
         
        i = i + 1

budget_dates = list(budgets.keys()) #returning a list of key values aka dates

total_record_cnt = len(budget_dates) #total number of records
i = 0
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
    #calling a function to to get unique months & appending all the calculated values   
    budget_analysis.append([bd,getmonth_fromdate(datestring = bd),current_pf, next_bd_date, next_bd_pf,change_value,change_from_previous])
    change_values.append(change_value)
    i = i + 1

allmonths =[]
change_values.sort(reverse=True)
netprofit = 0
total_change = 0
for ba in budget_analysis:
    netprofit = netprofit + ba[2]
    total_change = total_change + ba[5]
    allmonths.append(ba[1])

    if ba[5] == change_values[0]:
       gr_inc_mon = ba[3]
       gr_inc_chg_value = ba[5]   

    if ba[5] == change_values[-1]:
        gr_dec_mon = ba[3]
        gr_dec_chg_value = ba[5]
        
    
uniquemonths = list(set(allmonths)) #to get all unique months 
avg_change = round((total_change * 1.0) / (total_record_cnt * 1.0),2) #calculating average change
messages = []
messages.append('Financial Analysis\n')
separator = "-" * 50 
separator = separator + '\n'
messages.append(separator)
messages.append('Total Days: {0}\n'.format(str(total_record_cnt)))
messages.append('Total unique months: {0}\n'.format(str(len(uniquemonths))))
messages.append('Total profit/loss : ${0}\n'.format(str(netprofit)))
messages.append('Total change : ${0}\n'.format(str(total_change)))
messages.append('Avg change : ${0}\n'.format(str(avg_change)))
messages.append("Greatest Increase in Profits: {0} (${1})\n" .format(str(gr_inc_mon),str(gr_inc_chg_value)))
messages.append("Greatest Decrease in Profits: {0} (${1})\n" .format(str(gr_dec_mon),str(gr_dec_chg_value)))

print('Total Days: {0}'.format(str(total_record_cnt)))
print('Total unique months: {0}'.format(str(len(uniquemonths))))
print('Total profit/loss : ${0}'.format(str(netprofit)))
print('Total change : ${0}'.format(str(total_change)))
print('Avg change : ${0}'.format(str(avg_change)))
print("Greatest Increase in Profits: {0} (${1})" .format(str(gr_inc_mon),str(gr_inc_chg_value)))
print("Greatest Decrease in Profits: {0} (${1})" .format(str(gr_dec_mon),str(gr_dec_chg_value)))


with open(output_filepath, 'w') as outfilehandler:
    outfilehandler.writelines(messages)
