import os
# directory change, path management

print(os.getcwd()) # current dir
print(os.chdir('c:/Users/rabin/PycharmProjects/Learn_Python'))
print(os.getcwd())

# with open('todo.txt', 'r') as f:
#     print(f.read())

# os.mkdir('rabin') # make dir
# os.rmdir('rabin') #remove dir

# os.remove('file_name') # remove file

# os.walk
for i in os.walk('./'):#current dir
    print(i)
