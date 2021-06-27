import xlwt
xl = xlwt.Workbook(encoding='UTF-8')
sheet = xl.add_sheet('sheet1', cell_overwrite_ok=True)
for i in range(1,65530):

    sheet.write(i-1,5,xlwt.Formula(f"C{i} * D{i}"))

xl.save("foo.xlsx")
