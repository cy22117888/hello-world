'''
    遍历字典
'''

myDict = {'总行数':500,'代码行数':260,'注释行数':180,'空行数':60}
# 1、直接遍历字典，循环变量中储存的是字典中的各个key
for i in myDict:
    print(i,myDict[i])
print()

# 2、对字典的items()函数进行遍历，循环变量中储存的是字典中各个key-value对的元组tuple形式
for i in myDict.items():
    print(i)
print()

# 3、使用两个储存变量对字典的items()函数进行遍历，前一个变量储存各个key,后一个变量储存各个value
for k,v in myDict.items():
    print(k,v)

