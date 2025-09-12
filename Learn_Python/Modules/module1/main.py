import modules1
import sys

print('====================================')

print(f'Running main.py - module name:{__name__}')

print(modules1)

modules1.pprint_dict('main.globals',globals())


print('path',sys.path)


print('====================================')

import modules1 # wont run again
print('importing module1 again')
import modules1 # wont run again