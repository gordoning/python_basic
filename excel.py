# 如何使用打开excel文件，获取excel中的数据，处理excel中的信息



#——————————阶段1——————————


import xlrd
from xlrd import open_workbook
from xlutils.copy import copy

#——————————阶段2——————————

xlsx = xlrd.open_workbook('e:/日生产数据2018.09.08.xlsx')

##如果你不想每次都改文件名
# import datetime
# yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y.%m.%d')
#——————————阶段3——————————
table = xlsx.sheet_by_index(0)
# 获取所有sheet名字：xlsx.sheet_names()
# 获取sheet数量：xlsx.nsheets
# 获取所有sheet对象：xlsx.sheets()
# 通过sheet名查找：xlsx.sheet_by_name("test")
# 通过索引查找：xlsx.sheet_by_index(3)
#——————————阶段4——————————
all_data = []
for n in range(1, table.nrows):
    company = table.cell(n, 1).value
    province = table.cell(n, 2).value
    price = table.cell(n, 3).value
    weight = table.cell(n, 4).value
# a) 获取单元格值：
# table.cell_value(1, 2)
# table.cell(1, 2).value
# table.row(1)[2].value
# b) 获取单元格类型：
# table.cell(1, 2).ctype
# table.cell_type(1, 2)
# table.row(1)[2].ctype
    data = {'company': company, 'province': province, 'weight': weight, 'price': price}
    all_data.append(data)
# 以下内容可以用pandas的groupby轻易实现，这里不引入新知识，使用一个笨办法
a_weight = []
a_total_price = []
b_weight = []
b_total_price = []
c_weight = []
c_total_price = []
d_weight = []
d_total_price = []
e_weight = []
e_total_price = []
f_weight = []
f_total_price = []
for i in all_data:
    if i['company'] == '客户A':
        a_weight.append(i['weight'])
        a_total_price.append(i['weight'] * i['price'])
    if i['company'] == '客户B':
        b_weight.append(i['weight'])
        b_total_price.append(i['weight'] * i['price'])
    if i['company'] == '客户C':
        c_weight.append(i['weight'])
        c_total_price.append(i['weight'] * i['price'])
    if i['company'] == '客户D':
        d_weight.append(i['weight'])
        d_total_price.append(i['weight'] * i['price'])
    if i['company'] == '客户E':
        e_weight.append(i['weight'])
        e_total_price.append(i['weight'] * i['price'])
    if i['company'] == '客户F':
        f_weight.append(i['weight'])
        f_total_price.append(i['weight'] * i['price'])
#——————————阶段5——————————
rb = open_workbook('e:/模板2.xlsx')
rs = rb.sheet_by_index(0)
wb = copy(rb)
ws = wb.get_sheet(0)
ws.write(2, 1, str(len(a_weight)))
ws.write(2, 2, str(sum(a_weight)))
ws.write(2, 3, str(sum(a_total_price)))
ws.write(3, 1, str(len(b_weight)))
ws.write(3, 2, str(sum(b_weight)))
ws.write(3, 3, str(sum(b_total_price)))
ws.write(4, 1, str(len(c_weight)))
ws.write(4, 2, str(sum(c_weight)))
ws.write(4, 3, str(sum(c_total_price)))
ws.write(5, 1, str(len(d_weight)))
ws.write(5, 2, str(sum(d_weight)))
ws.write(5, 3, str(sum(d_total_price)))
ws.write(6, 1, str(len(e_weight)))
ws.write(6, 2, str(sum(e_weight)))
ws.write(6, 3, str(sum(e_total_price)))
ws.write(7, 1, str(len(f_weight)))
ws.write(7, 2, str(sum(f_weight)))
ws.write(7, 3, str(sum(f_total_price)))

#——————————阶段6——————————
wb.save('e:/日报.xls')
# import random
# wb.save('e:/日报'+str(random.random())+'.xls')
# wb.save('e:/日报'+str(yesterday)+'.xls')
