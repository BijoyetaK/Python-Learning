def get_largest_smallest(input_list):
    #numbers = [4,9,3,1,28]

    largest_num = 0
    smallest_num = 0
    i= 0
    total_numbers = len(input_list)
    
    for num in input_list:
        if i < total_numbers - 1:
            next_number = input_list[i +1]
            if  num > largest_num:
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


num_array = [[8,4,7,1],[3,3,9,2],[51,62,0,5]]
num_list =[]
for num in num_array:
    x,y = get_largest_smallest(input_list= num)
    #print('Smallest is:' + str(x))
    #print('Largest is:' + str(y))
    num_list.append(y)

sml,lrg = get_largest_smallest(input_list = num_list)
print('Largest number is : ' + str(lrg))
    


