number_list = [1, '2', 3, 'four', 'five']

print('Converting!')
for i in number_list:
    try:
        print(int(i))
    except:
        print("Conversion fail!")
    else:
        print('Conversion successful!')
    finally:
        print('Done!')