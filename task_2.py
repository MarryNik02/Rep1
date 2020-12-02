def my_div(a):
    tmp = 1
    for i in range(1, a-1):
        if a % i == 0:
            tmp = i
    return tmp


a = int(input())
print(my_div(a))
