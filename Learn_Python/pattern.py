def mat(n):
    m= n*2-1
    lst= ['1' for _ in range(m)]

    for i in range(m):
        print(' '.join(lst))

        if i<n-1:
            for j in range(abs(-i-1),m-i-1):
                lst[j] = str(i+2)
        else:
            for j in range(abs(m-i-1),i+1):
                lst[j] = str(m-i-1)


mat(6)