a = int(input())
tmp = 1
for i in range(1, a-1):
    if a % i == 0:
        tmp = i
print(tmp)
 
