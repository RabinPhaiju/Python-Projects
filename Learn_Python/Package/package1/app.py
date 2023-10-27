from me import print_name
import sys
print_name()
print(__name__)

print(sys.path)
# when we import something , it first look in the path you are working
# then to other python packages path
