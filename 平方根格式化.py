#自己解答
a = int(input())
b = pow(a,0.5)
if (a >= 0):

    s = "%.3f" % b
    c = len(s)
    if (c >= 30):
        print(s)
    else:
        print((30-c)*"+"+s)

else:
    r = "%.3f" % (b.real)
    k = "%.3f" % (b.imag)
    print(18*"+"+str(r)+"+"+str(k)+"j")

#答案

#a = eval(input())
print("{:+>30.3f}".format(pow(a, 0.5)))#左对齐，宽度30，保留3位小数，不足填充+
print("{:+<30.3f}".format(pow(a, 0.5)))#右对齐，宽度30，保留3位小数，不足填充+
print("{:+^30.3f}".format(pow(a, 0.5)))#右对齐，宽度30，保留3位小数，不足填充+

#https://www.runoob.com/python/att-string-format.html
