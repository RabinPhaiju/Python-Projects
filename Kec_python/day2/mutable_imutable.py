# print(dir(list))
# a -> variable
# a location -> which can change value without changing memory address =>mutable
# Mutable = list, dict, set,
# mutable changes in same address dont need to return
a: int = 10
print(id(a))
a = {'a': 2}
print(id(a))
print(a)


eg_list = [1, 2, 3]
print(id(eg_list))
eg_list.append(2)
print(id(eg_list))


# sort vs sorted
a = [1, 5, 7, 4]
a.sort()
print(a)
# sort is a list method and is mutable

sorted_a = sorted(a)
print(sorted_a)
# sorted is builtin function and returns a sorted value


# string is immutable

eg_str1 = 'my name is'
eg_str2 = 'rabin'

#eg_str2[1] = 'a' # not allowed


id_old = id(eg_str1)
eg_str1 += eg_str2
id_new = id(eg_str1)

print(id_old == id_new) # false



