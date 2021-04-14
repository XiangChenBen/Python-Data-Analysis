import xlwings as xw
app = xw.App(visible=True,add_book=False)

'''#新建工作部
workbook = app.books.add()

#保存并关闭
workbook.save(r"D:\pythonProject\venv\自动化\sample.xlsx")
workbook.close()
app.quit()'''

#打开一个已有的workbook（不能是已经open的workbook,否则产生一个只读的复制品）
workbook = app.books.open(r"D:\pythonProject\venv\自动化\sample.xlsx")

#对sheet进行操作
worksheet = workbook.sheets["Sheet1"]
worksheet.range("A1").value = "编号"
worksheet = workbook.sheets.add("产品统计表")
