import random
import time

DARTS = 10000 * 10000#测试点数

hits = 0.0 #落在圆内的点数

start = time.perf_counter()
for i in range(1,DARTS+1):
	x,y=random.random(),random.random()
	dist = pow(x ** 2 + y ** 2,0.5)
	if dist <= 1.0:
		hits = hits + 1

pi = 4 * (hits / DARTS)

print(pi)
print(time.perf_counter()-start)