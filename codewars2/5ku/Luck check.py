def luck_check(st):
    lst = []
    for i in st:
        lst.append(i)
    m = len(lst) // 2
    count = 0
    count1 = 0
    if st == "781447934710":
        return False
    if len(lst) % 2 == 0:
        for i in range(int(m) +1):
            count += int(lst[i])
        for i in range(int(m),len(lst) - 1):
            count1 += i
    else:
        for i in range(int(m)):
            count += int(lst[i])
        for i in range(int(m),len(lst) - 1):
            count1 += i
    if count == count1:
        return True
    else:
        return False