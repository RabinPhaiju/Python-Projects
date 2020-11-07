# rb to read in binary
# rb+ to read write in binary
with open('file.bin', 'w', encoding='UTF-16') as f:
    num = 'hello'
    f.write(num)


with open('file.bin', 'rb') as f:
    print(f.read())
    f.seek(0)
    print(f.read().decode('cp437'))
    f.seek(0)
    print(f.read().decode('UTF-16'))


