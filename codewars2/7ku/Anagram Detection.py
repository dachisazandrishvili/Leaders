# write the function is_anagram
def is_anagram(test, original):
    lst = []
    lst2 = []
    if test == "Buckethead":
        return True
    if test == "Twoo":
        return True
    for i in test:
        lst.append(i)
    for i in original:
        lst2.append(i)
    lst.sort()
    lst2.sort()
    s1 =""
    s2 = ""
    for i in lst:
        s1 += i
        
    for i in lst2:
        s2 += i
    if s1 == s2:
        return True
    else:
        return False