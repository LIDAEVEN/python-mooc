import time
start = time.perf_counter()
h= 0

def isprime(t):
    k=0
    g=0
    for i in range(2,t+1):
        if t%i == 0:
            g=g+1
            if g > 1:
                break#如果大于1就不用往下算了，时间效率有提升
    if g>1:
        k=1#no
    else:
        k=2#yes
    return k

for i in range(2,101):
    if isprime(i)==2:
        h=h+i
print(h)
print(time.perf_counter()-start)
'''
while i<=100:
    for t in range(2,i):
        if i % t == 0:
            g = g + 1
    if g==1:
        h = h + i

    i = i + 1
print(h)
'''
'''
for i in range(2,101):

    for k in range(2,i+1):
        if i % k == 0:
            g = g + 1
            if g == 1:
                h = h + i
print(h)
'''
