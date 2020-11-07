import csv

subject = ['name','python','data_structure','physics']
marks = ['rabin', 12, 12, 23]

# with open('marksheet.csv', 'w') as f:
#     csv_writer = csv.writer(f, delimiter=',')
#     csv_writer.writerow(subject)
#     csv_writer.writerow(marks)


marks = [
    ['sabin', 34, 45, 67],
    ['suraj', 12 , 67, 45],
    ['ram', 45, 56, 88]
]
with open('marksheet.csv', 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(subject)
    csv_writer.writerows(marks)
#
#
# # --------- READ -------------
with open('marksheet.csv', 'r') as f:
    csv_reader = csv.reader(f)
    # csv_list = list(csv_reader(f))
    # read row by row -----------
    for i in csv_reader:
        print(i)


# ------- CSV DICTIONARY ---------


with open('mar.csv', 'w') as f:
    csv_writer = csv.DictWriter(f, delimiter=',', fieldnames=['name', 'math'])
    data = {'name': 'rabin', 'math': 23}
    csv_writer.writerow(data)
















