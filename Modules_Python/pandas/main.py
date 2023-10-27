# data structure and data analytics

import pandas  # run in jupyter notebook

# ------------list -----------------

df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns = ['price', 'age', 'date'], index = ['one', 'two'])
df2 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]])

# print(df1)
# print()
# print(df2)
# print(df1.price)


df3 = pandas.DataFrame([{'Name':'rabin','age':22, 'salary':2000}, 
{'Name':'sabin', 'age':20, 'salary':3000}])
print(df3)
# print(type(df3))

# print(dir(df3))
# print(df3.mean())