#In this activity, you will create a function that searches a list of students 
#and graduates by state to determine state graduation rates for public, private nonprofit, and private for-profit institutions.

#Analyze the code and CSV provided, looking specifically for what needs to still be added to the application
#Using the starter code provided, create a function called print_percentages which takes in a parameter called state_data and does the following:
#Uses the data stored within state_data to calculate the estimated graduation rates in each category of Title IV 4-year institutions (public, non-profit private, and for-profit private).
#Prints out the graduation rates for each school type for the state to the terminal.
#Note: Some states do not have non-profit or for-profit private schools, so data must be checked for zeros

#Bonus:Still within the print_percentages() function, calculate the overall graduation rate, 
#and create a conditional that checks a state's overall graduation rate and prints 
#either "Graduation success" to the screen if the number was greater than fifty or "State needs improvement" if the number was less than 50.


import os
import csv

csvfile = 'graduation_data.csv'
output_filename = 'Graduation_Analysis.csv'
datafolder = 'csvfile'
#path to collect the data from the csv file in the csvfile folder
graduation_csv = '{0}/{1}/{2}'.format(os.getcwd(),datafolder,csvfile)
output_filepath = '{0}/{1}/{2}'.format(os.getcwd(),datafolder,output_filename)
output_columns = ["State","Public School Graduation Rate","Non-Profit School Graduation Rate", "For-Profit School Graduation Rate", "Overall Graduation Rate", "Status"]

def get_percentages(state_data):
    state = str(state_data[0])
    public_students = int(state_data[1])
    public_graduates = int(state_data[2])
    nonprofit_students = int(state_data[3])
    nonprofit_graduates = int(state_data[4])
    forprofit_students = int(state_data[5])
    forprofit_graduates = int(state_data[6])

    total_students = public_students + nonprofit_students + forprofit_students
    total_graduates = public_graduates + nonprofit_graduates + forprofit_graduates

    if nonprofit_students == 0:
       nonprofit_grad_rate = 0
    else:
        nonprofit_grad_rate = (nonprofit_graduates/nonprofit_students) * 100

    if forprofit_students == 0:
       forprofit_grad_rate = 0
    else:
        forprofit_grad_rate = (forprofit_graduates/forprofit_students) * 100

    public_grad_rate = (public_graduates/public_students) * 100    

    overall_grad_rate = (total_graduates/total_students) * 100

    if overall_grad_rate > 50:
       status = 'Graduation Success'
    else:
       status = "State needs improvement"    

    # print('State: ',state)
    public_grad_rate = round(public_grad_rate,2)
    nonprofit_grad_rate = round(nonprofit_grad_rate,2)
    forprofit_grad_rate = round(forprofit_grad_rate,2)
    overall_grad_rate = round(overall_grad_rate,2)
    
    # print('Public School Graduation Rate: ' + str(round(public_grad_rate,2)) +'%')
    # print('Private Non Profit School Graduation Rate: ' + str(round(nonprofit_grad_rate,2)) +'%')
    # print('Private For Profit School Graduation Rate: ' + str(round(forprofit_grad_rate,2)) +'%')
    # print('Overall Graduation Rate: ' + str(round(overall_grad_rate,2)) +'%')
    # print(message)
    return [state,public_grad_rate, nonprofit_grad_rate, forprofit_grad_rate, overall_grad_rate, status]

#output_columns = ["State","Public School Graduation Rate","Non-Profit School Graduation Rate", "For-Profit School Graduation Rate", "Overall Graduation Rate", "Status"] 
# 
#       
output_list = []
output_list.append(output_columns)
with open(graduation_csv,'r') as csvfilehandle:
     csvreader = csvfilehandle.readlines()
     #print(csvreader)
     i = 0
     for line in csvreader:
        if i > 0:
            line = line.replace('\n','')
            line_array = line.split(',') #split the string from the list of strings by delimiter and put it into another list
            #print(line_array)
            output_row = get_percentages(state_data = line_array)
            output_list.append(output_row)
        i = i + 1
             
with open(output_filepath,'w',newline='') as csvfilehandle:   
    csvwriter = csv.writer(csvfilehandle, delimiter=',')
    csvwriter.writerows(output_list)
    

