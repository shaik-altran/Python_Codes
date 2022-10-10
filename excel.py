import xlrd

my_dict={}
path=r'/home/shaik/Documents/my_sheet.xls'
excel_workbook = xlrd.open_workbook(path)
excel_sheet = excel_workbook.sheet_by_index(0)

"""print(excel_sheet.cell_value(1,0))
print(excel_sheet.cell_value(2,0))
print(excel_sheet.cell_value(3,0))

print(excel_sheet.cell_value(1,1))
print(excel_sheet.cell_value(2,1))
print(excel_sheet.cell_value(3,1))"""
i=0
for i in range(1,7):
    k=excel_sheet.cell_value(i,0)
    v=int(excel_sheet.cell_value(i,1))
    my_dict.update({k:v})
print(my_dict)

print(my_dict["A"])

"""if excel_sheet.cell_value(7,0):
    print("True")
else:
    print("false")"""





