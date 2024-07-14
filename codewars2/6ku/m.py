def sum_nested_numbers(arr):
    tmp = []
    m=0
    ind=1
    while arr:
        for i in arr:
            if isinstance(i, int):
                m+= (i**ind)
            else:
                tmp.extend(i)
        ind+=1
        arr=tmp
        tmp=[]
    return m