import pandas as pd
import numpy as np
from revenue import MaxRevenue
from uniqueList import unique

ozon = pd.ExcelFile('ozon.xlsx')
ozonData = pd.read_excel(ozon, sheet_name='Sheet1')
ozon.close()
uniqueData = np.delete(ozonData["ogrn"].unique(), 0)
data = []
for ogrn in uniqueData:
    clientData = []
    for row in ozonData.iterrows():
        if ogrn == row[1][5]:
            if len(clientData) == 0:
                clientData.append(row[1][0])
                clientData.append(row[1][1])
                clientData.append(row[1][2])
                clientData.append(row[1][3])
                clientData.append(row[1][4])
                clientData.append(str(row[1][5]))
                clientData.append(str(row[1][6]))
                clientData.append(row[1][7])
                clientData.append(row[1][8])
                clientData.append(row[1][9])
                clientData.append(row[1][10])
                clientData.append(str(row[1][11]))
                clientData.append(str(row[1][12]))
            else:
                clientData[1] = max(clientData[1], row[1][1])
                clientData[2] = MaxRevenue(clientData[2], row[1][2])
                if pd.isna(row[1][6]):
                    pass
                else:
                    clientData[6] = clientData[6] + str(row[1][6])
                clientData[11] = clientData[11] + "," + str(row[1][11])
                if pd.isna(row[1][12]):
                    pass
                else:
                    clientData[12] = clientData[12] + "," + str(row[1][12])
                clientData[6] = unique(clientData[6])
                clientData[11] = unique(clientData[11])
                clientData[12] = unique(clientData[12])
    data.append(clientData.copy())
    print(clientData)
    clientData.clear()

df = pd.DataFrame(data)
writer = pd.ExcelWriter('OzonClear.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome', index=False)
writer.save()
