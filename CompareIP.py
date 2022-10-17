import xlrd

Path=r'/home/shaik/Documents/Record1.xls'
excel_workbook = xlrd.open_workbook(Path)
excel_sheet = excel_workbook.sheet_by_index(0)

Path1=r'/home/shaik/Documents/Record2.xls'
excel_workbook1 = xlrd.open_workbook(Path1)
excel_sheet1 = excel_workbook1.sheet_by_index(0)


"""print(excel_sheet.cell_value(0,0))
print(excel_sheet.cell_value(2,0))
print(excel_sheet.cell_value(3,0))
print(excel_sheet.cell_value(4,0))
print(excel_sheet.cell_value(5,0))
print(excel_sheet.cell_value(6,0))"""

Common_IP_Addr = []
Diff_IP_Addr = []
for row in range(1,excel_sheet.nrows):
    Common_IP_Addr.append(row)

print(Common_IP_Addr)

"""print(Diff_IP_Addr)"""


