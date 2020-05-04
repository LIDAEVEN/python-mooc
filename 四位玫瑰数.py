#玫瑰花数
n = 4
for i in range(1000,9999):
    w = int(i / 1000)
    k = int((i - 1000 * w)/100)
    t = int((i % 100) / 10)
    s = i -w*1000-k*100-t*10
    if i == pow(w,n)+pow(k,n)+pow(t,n)+pow(s,n):
        print(i)
#水仙花数
h = 3
for p in range(100,999):
    w1 = int(p/100)
    k1 = int((p%100)/10)
    t1 = p - w1*100 -k1*10
    if p == pow(w1,h)+pow(k1,h)+pow(t1,h):
        print(p)