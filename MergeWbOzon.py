import pandas as pd
import xlsxwriter as xl

ozon = pd.ExcelFile("ozon.xlsx")
ozonData = pd.read_excel(ozon, sheet_name="Sheet1")

wb = pd.ExcelFile("wb.xlsx")
wbData = pd.read_excel(wb, sheet_name="Sheet1")

wbData.merge(ozonData, how='left', on="ОГРН")
print(wbData)

book = xl.Workbook('ozonWB.xlsx')
sheet1 = book.add_worksheet("Sheet1")

i = 1
wbData = wbData.fillna("%%%")
print(wbData)
for row in wbData.iterrows():
    sheet1.write_row(i, 0, row[1])
    i = i + 1
book.close()
