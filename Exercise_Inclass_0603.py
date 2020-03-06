# Python program to count Even
# and Odd numbers in a List

#define function first
def even_function(mylist):
    even_count = 0
    for v in mylist:
        if v % 2 == 0: #modulus 2 = Rest bei einer Divison durch 2 --> # muss 0 sein
            even_count += 1 #take value in even_count and add 1
    return even_count

# create list of numbers
x = [10, 21, 4, 45, 66, 93, 1]

#call function and insert variable

t = even_function(x)

print("Even numbers in the list: ", t)
