import openpyxl

wb = openpyxl.load_workbook('')

# Getting sheets from the workbook

print(wb.sheetnames)
