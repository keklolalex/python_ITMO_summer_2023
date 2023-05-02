


n = list([6,2,35,645,23,2,2,968,74,123,16,867])
nMax = n[0]
nMin = n[0]
for i in range(len(n)):
    if n[i] > nMax :
        nMax = n[i]
    if n[i] < nMin:
        nMin = n[i]
print(nMin)
