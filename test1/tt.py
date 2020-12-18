TempStr = input("请输入带有符号的温度")

if TempStr[-1] in ['F','f']:
    c=(eval(TempStr[0:-1])- 32)/1.8
    print("转移后的温度{:.2f}c".format(c))
elif TempStr[-1] in ['C','c']:
    F=1.8*eval(TempStr[0:-1])+32
    print("转换后的温度是{:.2}F".format(F))
else:
    print("输入格式错误")