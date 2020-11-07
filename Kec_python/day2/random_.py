import random

print(random.randint(0, 20))

mylist = [1, 2, 3, 4, 5, 7]

print(random.choice(mylist))

# random.shuffle(mylist)
# print(mylist)

new_list = random.sample(mylist, 2)
print(new_list)