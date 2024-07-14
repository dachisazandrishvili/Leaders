def sum_nested_numbers(arr):
    lst = []
    sum = 0
    for i in arr:
        lst.append(str(i))
    for i in lst:
        if i.count("[") == 0:
            sum += int(i)
        else:
            s = 0 
            s += i.count("[")
            i.replace("","[")
            i.replace("","]")     
            sum += int(i) ** s
            
    return sum
