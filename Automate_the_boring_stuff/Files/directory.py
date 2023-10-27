import os

# path = os.path.join('folder','pic','home.jpg')
# print(path)
#
# print(os.sep) # the separate
#
# print(os.getcwd()) # get current working directory
#
# print(os.path.abspath('cwd.png')) # absolute path
#
# print(os.path.realpath('cwd.png')) # relative path

# print(os.path.dirname('C:/Users/rabin/PycharmProjects/Automate-the-boring-stuff/Files/cwd.png'))
# directory of the file

# print(os.path.basename('C:/Users/rabin/PycharmProjects/Automate-the-boring-stuff/Files/cwd.png'))
# base directory path

# print(os.path.relpath('C:/Users/rabin/PycharmProjects/Automate-the-boring-stuff/Files/cwd.png','C:/Users/rabin'))
# relative path from a path

# check if file exists
# print(os.path.exists('cwd.png'))
# print(os.path.isfile('cwd.png'))
# print(os.path.isdir('C:/Users/rabin/PycharmProjects/Automate-the-boring-stuff/Files'))

# check the size of the file
# print(os.path.getsize('cwd.png'))

# ------------------------- List Directory Size -------------------------

# ls = os.listdir('C:/Users/rabin/PycharmProjects')
# totalsize = 0
# for filename in ls:
#     if not os.path.isfile(os.path.join('C:/Users/rabin/PycharmProjects', filename)):
#         continue
#     else:
#         totalsize += os.path.getsize(os.path.join('C:/Users/rabin/PycharmProjects', filename))
#
# print(totalsize)

# -------------------- makes dirs ----------
# os.makedirs('hello/ok')














