# mode --read(r), write(w), append(a), binary(b)
# r= --> read-write

file_handler = open('first.txt', 'w')
file_handler.write('hello world')
file_handler.close()


file_handler = open('first.txt', 'r')
print(file_handler.read())

# temp = ['firstline\n', 'secondline\n', 'thirdline']
# file_handler = open('first.txt', 'w')
# file_handler.writelines(temp)
# file_handler.close()


# file_handler = open('first.txt', 'r')
# for i in file_handler:
#     print(i)#to take buffer
# file_handler.close()


# file_handler = open('first.txt', 'r')
# print(file_handler.readline())
# print(file_handler.readline())
# file_handler.close()


# when file is opened , The file need to be closed
# to not worry about closing file,
# WE USE 'with'----------------
# with open('first.txt', 'r') as f:
#     print(f.read())


# with open('first.txt', 'r+') as f:
#     print(f.read())
#     f.write('\nappend')


# with open('first.txt', 'r+') as f:
#     print(f.read(4))
#     print(f.read(4))
#     print(f.read())
#     print('the cursor is in line',f.tell())
#   # if we want to read from beginning
#    f.seek(0)
#    print('the cursor is in line', f.tell())
#    print(f.read())
#   # when we have already read all fine , and again we read then it return --nothing--


# encoding------------------


# with open('first.txt', 'r') as f:
    # print(f.encoding)









