import pandas as pd
import xlsxwriter as xl

from revenue import MaxRevenue
from uniqueList import unique

ozon = pd.ExcelFile('wb.xlsx')
wbData = pd.read_excel(ozon, sheet_name='Sheet1')
ozon.close()
# формируем словарь из ogrn
uniqueData = dict.fromkeys(wbData["ogrn"].unique())
# удаляем nan из словаря
uniqueData = {k: v for k, v in uniqueData.items() if k == k}
for row in wbData.index:
    if wbData["ogrn"][row] in uniqueData:  # для каждой строки проверяем наличие ключа в словаре
        if not uniqueData[wbData["ogrn"][row]]:  # если значение по ключу пустое, заполняем его
            clientData = []
            clientData.append(wbData["Официальное название компании (Ozon)"][row])  # 0
            clientData.append(wbData["revenue (год) (Ozon)"][row])  # 1
            clientData.append(wbData["Группа по обороту"][row])  # 2
            clientData.append(str(wbData["domain"][row]))  # 3
            clientData.append(wbData["inn"][row])  # 4
            clientData.append(wbData["ogrn"][row])  # 5
            clientData.append(wbData["clientid"][row])  # 6
            clientData.append(wbData["status"][row])  # 7
            clientData.append(str(wbData["Категории Wildberries"][row]))  # 8
            clientData.append(str(wbData["Рабочий телефон"][row]))  # 9
            uniqueData[wbData["ogrn"][row]] = clientData.copy()
            clientData.clear()
        else:  # если значение по ключу не пустое, дописываем значения
            # выбираем максимальный оборот
            uniqueData[wbData["ogrn"][row]][1] = max(uniqueData[wbData["ogrn"][row]][1],
                                                     wbData["revenue (год) (Ozon)"][row])
            # выбираем максимальную группу по обороту
            uniqueData[wbData["ogrn"][row]][2] = MaxRevenue(uniqueData[wbData["ogrn"][row]][2],
                                                            wbData["Группа по обороту"][row])
            # Добавляем домены из новых строк
            if not wbData["domain"][row]:
                pass
            else:
                uniqueData[wbData["ogrn"][row]][3] = str(uniqueData[wbData["ogrn"][row]][3]) + "," + str(
                    wbData["domain"][row])
            # добавляем категории и телефоны
            uniqueData[wbData["ogrn"][row]][8] = str(uniqueData[wbData["ogrn"][row]][8]) + "," + \
                                                 str(wbData["Категории Wildberries"][row])

            uniqueData[wbData["ogrn"][row]][9] = str(uniqueData[wbData["ogrn"][row]][9]) + "," + \
                                                 str(wbData["Рабочий телефон"][row])

book = xl.Workbook('ClearWB.xlsx')
sheet1 = book.add_worksheet("Sheet1")
k = 0
# выбираем уникальные значения доменов, категорий и телефонов и сразу пишем строку в файл
for i in uniqueData:
    k = k + 1
    if pd.isna(uniqueData[i][0]):
        uniqueData[i][0] = "%%%"
    if pd.isna(uniqueData[i][1]):
        uniqueData[i][1] = "%%%"
    if pd.isna(uniqueData[i][2]):
        uniqueData[i][2] = "%%%"
    uniqueData[i][3] = unique(uniqueData[i][3])
    if pd.isna(uniqueData[i][4]):
        uniqueData[i][4] = "%%%"
    if pd.isna(uniqueData[i][5]):
        uniqueData[i][5] = "%%%"
    if pd.isna(uniqueData[i][6]):
        uniqueData[i][6] = "%%%"
    if pd.isna(uniqueData[i][7]):
        uniqueData[i][7] = "%%%"
    uniqueData[i][8] = unique(uniqueData[i][8])
    uniqueData[i][9] = unique(uniqueData[i][9])
    print(uniqueData[i])
    sheet1.write_row(k, 0, uniqueData[i])
book.close()
