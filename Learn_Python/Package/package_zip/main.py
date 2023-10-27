import sys
import pathlib

sys.path.append(f'{pathlib.Path(__file__).parent.absolute()}/common.zip')

import common
import common.validators as validators
import common.models as models

print(validators.json.is_json('{"name":12}'))

print('**********self*************')
for k in dict(globals()).keys():
    print(k)

print('************common***********')
for k in common.__dict__.keys():
    print(k)

print('************validators***********')
for k in validators.__dict__.keys():
    print(k)

print('************models************')
for k in models.__dict__.keys():
    print(k)

print('************posts************')
for k in models.posts.__dict__.keys():
    print(k)

print('************users************')
for k in models.users.__dict__.keys():
    print(k)