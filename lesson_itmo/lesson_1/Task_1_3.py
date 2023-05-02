x = int(input())
y = int(input())
a = x + y
b = x - y
c = x * y
d = int(x / y)
e = int(x // y)

# sum = x + y
# min = x - y
# prod = x * y
# delenie = int(x / y)
# ost = int(x // y)
# if (sum > min):
#     if(sum > prod):
#         if(sum > delenie):
#             if(sum > ost):
#                 if(min > prod):
#                     if(min > delenie):
#                         if(min > ost):
#                             print(min)
#                         else:
#                             print(ost)
#                     elif(delenie > min):
#                         if (delenie > ost):
#                             print(delenie)
#                 elif(prod > min):
#                     if(prod > delenie):
#                         if(prod > ost):
#                             print(prod)
#                         else:
#                             print(ost)
#                     elif(delenie > prod):
#                         if(delenie > ost):
#                             print(delenie)
#                         else:
#                             print(ost)
#             elif(ost > sum):
#                 print(sum)
#         elif(delenie > sum):
#             if(delenie > ost):
#                 if(sum > ost):
#                     print(sum)
#                 else:
#                     print(ost)
#     elif(prod > sum):
#         if(prod > delenie):
#             if(prod > ost):
#                 if(sum > delenie):
#                     if(sum > ost):
#                         print(sum)
#                     else:
#                         print(ost)
#                 elif(delenie > sum):
#                     if(delenie > ost):
#                         print(delenie)
#                     else:
#                         print(ost)
#             else:
#                 print(prod)
#         elif(delenie > prod):
#             if(delenie > ost):
#                 if(prod > ost):
#                     print(prod)
#                 else:
#                     print(ost)
#             elif(delenie > prod):
#                 if(delenie > ost):
#                     if(prod > ost):
#                         print(prod)
#                     else:
#                         print(ost)
#                 else:
#                     print(delenie)
# elif(min > sum):
#     if(min > prod):
#         if(min > delenie):
#             if(min > ost):
#                 if(sum > prod):
#                     if(sum > delenie):
#                         if(sum > ost):
#                             print(sum)
#                         else:
#                             print(ost)
#                     elif(delenie > sum):
#                         if(delenie > prod):
#                             if(delenie > ost):
#                                 print(delenie)
#                             else()



if a > b:
    f = a
    s = b
else:
    f = b
    s = a
if c > f:
    s = f
    f = c
elif c > s:
    s = c
if d > f:
    s = f
    f = d
elif d > s:
    s = d
if e > f:
    s = f
    f = e
elif e > s:
    s = e
print(s)


