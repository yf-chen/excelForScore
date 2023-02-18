import openpyxl

workbook = openpyxl.load_workbook('example.xlsx')

# 获取要操作的表格，假设为第一个表格
worksheet = workbook.worksheets[0]

# 遍历每行
for row in worksheet.iter_rows(min_row=2):  # 从第二行开始遍历，跳过标题行
    # 将 A 列的值赋值给 B 列
    # 获取 A 列和 B 列的单元格
    cell_A = row[0]
    cell_B = row[1]
    # 将 A 列的值赋值给 B 列
    cell_B.value = cell_A.value
# 保存更改
workbook.save('example.xlsx')