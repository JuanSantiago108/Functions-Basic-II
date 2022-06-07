# 1.Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]





def count_down (num): # after def is what ever you call it (changing varible (parameter))
    new_list=[] #This is an array but called LIST

    for x in range(num, -1, -1): # range(start, end, + or -) range (end)
        new_list.append(x) # This is the same as push
    return new_list # To get the result of the function


print(count_down(10)) 

print("============================================================================")


#2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return (my_list):
    print(my_list[0])# This is printing first index
    return my_list[1]# This is returns second index

# print_and_return([1,2])
print(print_and_return([1,2]))

print("============================================================================")

# 3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def first_plus_length (my_list):
    return my_list[0] + len(my_list)


print(first_plus_length([6,2,10,15,70]))


print("============================================================================")
# 4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

def values_greater_than_second(my_list):
    new_list = []
    if (len(my_list)<2):
        return False
    else:
        for x in range (len(my_list)):
            if (my_list[1]<my_list[x]):
                new_list.append(my_list[x])
    
    print(len(new_list))

    return new_list

list_one=[10,50,40,100,95,200]
list_two=[54]
print(values_greater_than_second(list_one))
print(values_greater_than_second(list_two))
print("============================================================================")
# 5. This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]


def length_and_value (size,value):
    new_list=[]
    for x in range(size):
        new_list.append(value)
    return new_list
    


print(length_and_value(4,7))