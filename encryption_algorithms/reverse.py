str = "Ruhuna"

def reverseStr(str):
    toList = list(str)
    toList.reverse()
    kk = "".join(toList)
    print(kk)


reverseStr(str)