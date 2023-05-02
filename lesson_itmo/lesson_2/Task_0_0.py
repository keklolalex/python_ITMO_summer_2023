print(1, 2, 3, sep = ":", end = ";")
print(1, end="?")
print()
print(2)
#help(print)
for i in 'hello world!':
    print(i, end='')
print()
for i in range(-5, 8, 2): # 2 - это шаг, первые два диапазон
    print(i)

for i in range(10):
    print(i, i**2, i**3)

for i in range(10):
    if(i % 2 == 0): # остаток от деления % 0 или 1
        print(i, '- четное')
    else:
        print(i, '- нечетное')


#FizzBazz
# n = int(input())
# for i in range(1, n+1):
#     if(i % 15 == 0):
#         print('FizzBuzz')
#     elif(i%3 == 0):
#         print('Fizz')
#     elif(i%5 == 0):
#         print('Buzz')
#     else:
#         print(i)



# for i in 'hello world!':
#     if i == 'a':
#         break
#     print(i*2, end='')
# else:
#     print()
#     print('Aaaaaaa')



# n = int(input())
# for k in range(n):
#     if k > 10:
#         break
#     elif k%2 == 0:
#         continue
#     else:
#         print(k)
# else:
#     print('Finish')

# hello = 123
# print(hello)
# msg = 'hello world!'
# print(msg[0:5:1])
# print(msg[4::-1])
# print(msg[1:4:2])
# print(msg[6:-1:2])
# msg = 'A' + msg[1:]
# print(msg)
# a = msg.replace('o', 'a')
# print(a)


# n = int(input())
# for i in range(1, n + 1):
#         print('+'*i)


# n = int(input())
# for i in range(1, n + 1):
#     for j in range(i):
#         print('+', end='  ')
#     print()
#     print()


a = [1,2,3,'asdad', True, 1000, [12,25]]
print(*a)
print(a[:])
print(a[6])
b = a #или a[:] // a.copy()
print(id(a), id(b))
b[0] = 111
print(b)
print(a)


print()
a = [1,2,34,5,7]
print(a)
b = list('Copy')
print(len(b))  # len читает кол-во символов
print(len('Vladivostok'))
a = [10,20,30,40]
for i in range(len(a)):
    print(i, a[i])

a = [10, 20, 30, 40]
for k, v in enumerate(a): #получает и индекc и значение элемента списка
    print(k, v)

a = [10, 20, 30, 40]
for i in enumerate(a): #получает и индекc и значение элемента списка
    print(i)

print(list(range(-5, 5, 2)))


input_list = [10, 't', 14, 'as', True]
for i in input_list:
    if type(i) == str:
        print(i * 2)
    elif type(i) == int:
        print(i**2)
    else:
        print(i)


input_list = [10, 't', 14, 'as', True]
for i in enumerate(input_list, 45):
    if type(i) == str:
        print(i * 2)
    elif type(i) == int:
        print(i**2)
    else:
        print(i)


# input_list = [10, 't', 14, 'as', True]
# input_list.append(123)
# print(input_list)
# input_list.insert(2,'sdfg')
# print(input_list)
# input_list.remove('t')
# print(input_list)


# a = []
# for i in range(5):
#     a.append(int(input(a)))
#     print(*a)

a = [1,2,4]
b = ['s',2,"23"]
print( a+ b) #списки можно складывать
# print( a - b) не работает

print()
a = [1,2,3,4,5]
b = []
s = 0
for i in range(len(a)):
    s += i
    print(s)
    b.append(s)
    print(b)


a = [1,2,3,4,5]
b = []
for i in range(len(a)):
    b.append(sum(a[:i+1]))
print(b)


a = [[1,2,3],[5,4,2],[5,8,3]]
s = 0
for i in a:
    for j in i:
        s += j
print(s)














