def unique(list):
    spList = list.split(",")
    uniqueList = []
    for i in spList:
        if i not in uniqueList:
            uniqueList.append(i)
    for i in range(uniqueList.count("")):
        uniqueList.remove("")
    result = ""
    for i in uniqueList:
        result = result + i + ","
    return result
