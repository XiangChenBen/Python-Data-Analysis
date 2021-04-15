import pandas as pd
import numpy as np

"""numpy基本操作，数组介绍"""
#the difference between list and array
a = [1,2,3,4]
b = np.array(a)
print(a)
print(b)
print(type(a))
print(type(b))
print(a[:2])
print(b[:2])
a = a*2
b = b*2
print(a)
print(b)

c = np.arange(5,20,2) #类似range()的作用
print(c)

d = np.random.randn(12) #标准正态随机选取
print(d)

d = d.reshape(3,4) #reshape可以重组成2维数组
e = np.random.randint(0,10,(4,4)) #在0 和10之间随机取数生成4*4数组
print(d)
print(e)


"""pandas基本操作"""
s = pd.Series(["Jack","Luke","Anna"]) #优势在带有索引
print(s)

a = pd.DataFrame([[1,2],[3,4],[5,6]])
print(a)

#赋予行索引和列索引
a = pd.DataFrame([[1,2],[3,4],[5,6]],
                 columns=["date","score"],index=["A","B","C"])
print(a)

b = pd.DataFrame()
date = [1,3,5]
score = [2,4,6]
b["date"] = date #确保 date 和 score 一样长
b["score"] = score
print(b)

c = pd.DataFrame({"date":[1,3,5],"score":[2,4,6]},index=["x","y","z"])
print(c)


# from_dict  将orient 定向到index 将会使列定向到index
d = pd.DataFrame.from_dict({"date":[1,3,5],"socre":[2,4,6]},orient="index")
print(d)

# 从numpy 到 pandas
a = np.arange(12).reshape(3,4)
b = pd.DataFrame(a,columns={0,1,2,3} , index=["a","b","c"])
print(b)

#添加索引总称和修改索引
a = pd.DataFrame([[1,2],[3,4],[5,6]],
                 columns=["date","score"],index=["A","B","C"])
a.index.name = "Company"
#a.rename 必须要重新赋值
a = a.rename(index = {"A":"Alibaba","B":"Baidu","C":"Tencent"},
             columns={"date":"日期","score":"成绩"})
'''
#可以用inplace 永久性修改，无需重新赋值
a.rename(index = {"A":"Alibaba","B":"Baidu","C":"Tencent"},
         columns={"date":"日期","score":"成绩"},inplace=True) #inplace可以永久性修改
'''
print(a)

#把常规列变成行索引
a.reset_index(inplace=True) #用 [0,1,2] 变成索引，并且将原行索引变成新的一列
print(a)
a.set_index("日期",inplace=True) #将某一列调出变成行索引
print(a)





"""pandas库调用excel"""

#excel读取
#data = pd.read_excel(r"D:\pythonProject\venv\自动化\sample.xlsx",
#                     sheet_name=0) #读取excel第一页sheet
#pd.read_csv("sample.csv",delimiter=",",encoding="utf-8") 可以读取csv格式,逗号分隔


#excel写入 （csv有相同操作）
data1 = pd.DataFrame([[1,2],[3,4],[5,6]],columns=["A列","B列"])
#创建新表并填入信息，如有会相同的workbook，会覆盖
data1.to_excel("sample1.xlsx",sheet_name="This sheet")
#只填1列并且不添加行索引
data1.to_excel("sample2.xlsx",columns=["A列"],index=False)


"""数据选取和处理"""
#创建数据
data = pd.DataFrame(np.arange(1,10).reshape(3,3),
       columns=["c1","c2","c3"],index=["r1","r2","r3"])

#提取列
c1_part1 = data["c1"] #第一列的一维序列
print(c1_part1)
c1_part2 = data[["c1"]]#第一列的二维数据
print(c1_part2)
c1_c3_part = data[["c1","c3"]] #第一列第三列
print(c1_c3_part)

#提取行 [1:3] 左闭右开
r2_r3_part = data.iloc[1:3] #iloc 数字类第二行第三行
print(r2_r3_part)
r1_r2_part = data.loc[["r1","r2"]] #loc 字符类第一行第二行
print(r1_r2_part)
r3_part = data.iloc[-1] #最后一行
print(r3_part)
head_2_row = data.head(2) # 头2行的数据
print(head_2_row)
part_data1 = data.iloc[0:2][["c1","c3"]] #前两行的c1 c3，先选行再选列！！
print(part_data1)


"""数据筛选"""
raw_data = pd.DataFrame(np.arange(1,10).reshape(3,3),
       columns=["c1","c2","c3"],index=["r1","r2","r3"])

#筛选出c1中数字大于1的行
filtered_data = raw_data[raw_data["c1"]>1]
print(filtered_data)

# & --> 且    | --> 或
filtered_data = raw_data[(raw_data["c1"]>1) & (raw_data["c2"]==5)]
print(filtered_data)


"""数据排序"""
#sort_value--> 按列排序  将c2进行降序排列
filtered_data = raw_data.sort_values(by="c2",ascending=False) #不上升-》下降
print(filtered_data)

#sort_index--> 按行排序  将行索引降序排列成 c3 > c2 > c1
filtered_data = raw_data.sort_index(ascending=False)
print(filtered_data)


"""数据的运算"""
raw_data["c4"] = raw_data["c3"] * raw_data["c1"]
print(raw_data)


"""数据的删除"""
#drop()删除
computed_data = raw_data.drop(columns="c1",index="r1")
#raw_data.drop(columns="c1",inplace=True)  inplace永久修改
print(computed_data)

#删除多列多行，行索引得是名称而不是数字，除非本来就是数字序号
computed_data = raw_data.drop(columns=["c1","c3"],index=["r1","r3"])
print(computed_data)


"""数据表的拼接"""
company_info1 = pd.DataFrame(
        {"companies":["Baidu","Alibaba","Tencent"],
         "scores":[90,95,85]}
)

company_info2 = pd.DataFrame(
        {"companies":["Baidu","Alibaba","Huawei"],
        "share price":[213.5,239.93,81.081]}
)

print(company_info1)
print(company_info2)

#merge()根据一个或多个同名的列将不同数据表连接起来,不一样的就会被删掉，可以用on来设置连接点
company_merged = pd.merge(company_info1,company_info2)
#company_merged = pd.merge(company_info1,company_info2,on="companies")
print(company_merged)

#默认为 inner交集，  可以设成outer并集,空值为NaN
company_merged = pd.merge(company_info1,company_info2,how="outer")
print(company_merged)

#对左表在意，而对右表不在意，可用left
company_merged = pd.merge(company_info1,company_info2,how="left")
print(company_merged)

#按照行索引进行合并
company_merged = pd.merge(company_info1,company_info2,
                          left_index=True,right_index=True)
print(company_merged)


#append的用法
company_merged = company_info1.append(
            {"companies":"Huawei","scores":90},ignore_index=True
)
print(company_merged)