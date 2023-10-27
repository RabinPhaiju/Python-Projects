import csv
import json
import string

'''
1. Sort the Monthly_Attendance.csv in descending order according to attendance number
then find the top 100 students with largest attendace
and write the sorted information in a new present.csv file
'''
# data = []
# with open('Monthly_Attendance.csv', 'r') as f:
#     data = list(csv.reader(f, delimiter=','))
#
# temp = sorted(data[1:], key=lambda x : int(x[7]), reverse=True)
#
# with open('present.csv', 'w', newline='') as f:
#     csv_writer = csv.writer(f)
#     csv_writer.writerow(data[0])
#     csv_writer.writerows(temp)


# 2. Convert the sample.csv file to sample.json file without using any external module
# data = []
# temp = []
# with open('sample.csv', 'r', encoding='UTF-8') as f:
#     data = list(csv.reader(f, delimiter=','))

# creating titles
# titles = data[0]

# converting to dictionary
# for i in  data[1:]:
#     temp.append(dict(zip(titles, i)))

# writing in counted.json file using json.dump
# with open('counted.json', 'w') as f:
#     json.dump(temp, f, indent=2) # dump->write dict to json-file


# 3. Read the count.txt file and find the freq of every word and then
# write the word with frequency in a new csv file with two columns, on with word and other with frequency
data = []
temp = {}

# reading data
with open('count.txt', 'r') as f:
    data = f.readline().lower()

# removing all the punctuations
for i in string.punctuation:
    data = data.replace(i, '')

# counting words
word_list = data.split()
# print(word_list.count('he'))
# print(word_list)
for i in set(word_list):
    temp[i] = word_list.count(i)
    # print(i, word_list.count(i))

# writing in text file
with open('counted.txt', 'w') as f:
    f.write(str(temp))
# writing in json file
with open('couting.json', 'w') as f:
    json.dump(temp, f, indent=2) # write dict to json-file

