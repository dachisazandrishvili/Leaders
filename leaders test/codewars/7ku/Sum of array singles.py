def repeats(arr):
    m = []
    sum = 0
    for i in arr:
        if arr.count(i) == 1:
            m.append(i)
    for i in m:
        sum += i
    return sum
            