# 1. Sort the Monthly_Attendance.csv in descending order according
# to attendance number then find the top 100 students with largest
# attendance and write the sorted information in a new present.csv file

import csv,json

# with open('Monthly_Attendance.csv', 'r') as f:
#     csv_reader = csv.reader(f)
#     title = f.readline()
#     sorted_lists = sorted(csv_reader, key=lambda row: int(row[7]), reverse=True)
#
#
# with open('Present.csv', 'w') as f:
#     f.write(title)
#     csv_writer = csv.writer(f)
#     count = 0
#     for i in sorted_lists:
#         csv_writer.writerow(i)
#         count = count + 1
#         print(count)
#         if count == 100:
#             break


# 2. Convert the sample.csv file to sample.json file without using any external module
# DON'T JUST CHANGE THE FILE EXTENSION
# j = open('sample.json', 'w')
# file = dict()
# with open('sample.csv', 'r') as f:
#     csv_reader = csv.reader(f)
#
#     for i in csv_reader:
#         title = i
#         break
#     f.readline()
#     j.write('[')
#     comma = False
#     for i in csv_reader:
#         if comma:
#             j.write(',')
#         comma = True
#         for li in range(5):
#             file[title[li]] = i[li]
#         json.dump(file, j)
#     j.write(']')

# --------or ------------------- optimized ---------

# with open('sample.csv', 'r') as f:
#     content = list(csv.reader(f))
#     print(content) # in list
#     converted = list()
#     keys = content[0]
#     print(keys) # keys of dictionary
#     for c in content[1:]: # from 1 except keys
#         new = dict()
#         for key, val in zip(keys, c):
#             new[key] = val # one dictionary
#         converted.append(new) # putting that one dictionary to list bcoz json is list of dict
#
# print(converted)


# ----------------------------------------------------------------------------------
# 3. Read the count.txt file and find the freq of every word and then
# write the word with frequency in a new csv file with two columns,
# on with word and other with frequency
# example
# first file: this is an example example
# second file: csv file
# this,1
# is,1
# an,1
# example,1
# ps: don't forget to convert in lowercase


# word = dict()
#
# lineno = 500
# line_length = 8
# with open('count.txt', 'r') as f:
#
#     i = f.readline()
#     for i in f:
#         f.seek(lineno * (line_length + 2))
#         line = i.split(" ")
#
#         for j in line:
#             j = j.lower()
#             if j not in word:
#                 word[j] = 1
#             else:
#                 count = int(word[j])
#                 word[j] = count + 1
#         break
#
# print(word)
# with open('count.csv', 'w') as c:
#     writer = csv.writer(c)
#     for key, value in word.items():
#         writer.writerow([key, value])










