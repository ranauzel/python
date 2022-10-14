

list=[]
for i in range(0,5):
    list.append(eval(input()))
def fonksiyon(n):
    return n*n-20

list.sort(key = fonksiyon)
print(list)



