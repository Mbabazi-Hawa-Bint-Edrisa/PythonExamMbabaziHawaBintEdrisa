#sum of items in a list
def sum_of_items():

    numbers = [9,2,3,5,8]
    sum = 0

    for number in numbers:
        sum += number
    print("The sum of items in the list is:  " + str(sum))  
    
sum_of_items()   
