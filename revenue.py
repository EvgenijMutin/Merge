def MaxRevenue(group1, group2):
    values = [[1, "менее 10 млн."], [2, "10-100 млн."], [3, "100-200 млн."], [4, "200–500 млн."],
              [5, "500 млн.-1 млрд."], [6, "более 1 млрд."]]
    group1N = 0
    group2N = 0
    for i in values:
        if group1 == i[1]:
            group1N = i[0]
        if group2 == i[1]:
            group2N = i[0]
    resultN = max(group1N, group2N)
    result = ""
    for i in values:
        if resultN == i[0]:
            result = i[1]
    return result



