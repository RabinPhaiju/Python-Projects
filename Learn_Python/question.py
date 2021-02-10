# Write a program that accepts a sequence of whitespace separated 
# words as input and prints the words after removing all duplicate
#  words and sorting them alphanumerically.

# x = input('Enter a sequence of white space words')
# x = x.split(" ")
# x = list(set(x))
# for x in sorted(x):
#     print(x,end=" ")

# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print
#  the first half values in one line and the last half values in one line.

# t1 = (1,2,3,4,5,6,7,8,9,10)
# print(t1[0:len(t1)//2])
# print(t1[5:len(t1)])

# Given five positive integers, find the minimum and maximum values that can be 
# calculated by summing exactly four of the five integers. Then print the respective
#  minimum and maximum values as a single line of two space-separated long integers.

# mylist = [2,1,3,4,5]
# mylist.sort()
# print(f"{sum(mylist[1:])} {sum(mylist[:-1])}")