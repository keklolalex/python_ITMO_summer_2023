x = int(input())
y = int(input())
sum = x + y
min = x - y
prod = x * y
delenie = int(x / y)
ost = int(x // y)
if (sum > min and sum > prod and sum > delenie and sum > ost):
    print(sum)
elif (min > sum and min > prod and  min > delenie and min > ost):
    print(min)
elif (prod > sum and prod > min and prod > delenie and prod > ost):
    print(prod)
elif (delenie > sum and delenie > min and delenie > prod and delenie > ost):
    print(delenie)
else:
    print(ost)
