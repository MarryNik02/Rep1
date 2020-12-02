def my_sum(a, b):
    while b != 1:
        a = my_sum(a, 1)
        b = b-1
    return a + 1

a = int(input())
b = int(input())
print(my_sum(a,b))
