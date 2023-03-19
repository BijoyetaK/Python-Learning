#This calculates the largest and smallest in a list
def get_largest_smallest(input_list):
    #numbers = [4,9,3,1,28]

    largest_num = 0
    smallest_num = 0
    i= 0
    total_numbers = len(input_list)
    for num in input_list:
        if i < total_numbers - 1:
            next_number = input_list[i +1]
            if num > next_number:
                largest_num = num
            if num < next_number:
                smallest_num = num
        if i == total_numbers - 1:
            if num > largest_num:
                largest_num = num
            if num < smallest_num:
                smallest_num = num    
                    
        i = i +1 

    return smallest_num, largest_num    

numbers = [4,9,3,1,28]
x,y = get_largest_smallest(input_list= numbers )
msg = "The largest number is : {0}, Smallest number is : {1}".format(str(y),str(x))       
print(msg) 
    
""" numbers = [4,9,3,1,28]

largest_num = 0
smallest_num = 0
i= 0
total_numbers = len(numbers)
for num in numbers:
    if i < total_numbers - 1:
        next_number = numbers[i +1]
        if num > next_number:
            largest_num = num
        if num < next_number:
            smallest_num = num
    if i == total_numbers - 1:
        if num > largest_num:
            largest_num = num
        if num < smallest_num:
            smallest_num = num    
                  
    i = i +1     


msg = "The largest number is : {0}, Smallest number is : {1}".format(str(largest_num),str(smallest_num))       
print(msg)         """


