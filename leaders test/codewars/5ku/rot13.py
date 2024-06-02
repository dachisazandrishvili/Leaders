def rot13(message):
    ls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ls2 = []
    ath = []
    for i in ls:
        ls2.append(i.upper())
    for i in message:
        if i in ls:
            m = ls.index(i)
            message.replace(i, ls[m + 1])
        elif i in ls2:
            m = ls2.index(i)
            message.replace(i, ls2[m + 1])
        else:
            ath.append(i)
            message.replace(i,"")
    return message