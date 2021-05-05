n = 10000000


""" prove 
1 + 1/2 + ... + 1/n + .. is infinity """

sum = 0
for i in range(1, n+1):
    sum += 1/i
print(sum)