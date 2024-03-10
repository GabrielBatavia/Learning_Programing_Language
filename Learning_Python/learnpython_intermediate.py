def get_root(a,b,c):
  r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
  r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
  r3 = (a + b + c)
  return r1,r2,23

result1, result2, result3 = get_root(a=1,c=-8,b=2)
print('Hasil akar-akarnya adalah', result1, 'atau', result2, 'dan pertambahan nya adalah', result3)

add = lambda x, y : x + y
print("total dari 100 dan 200 adalah:",add(100,200))

list_umur = [34,39,20,18,13,54]
print("Umur yang dewasa: ")
for a in filter(lambda x: x >= 19, list_umur): # filter umur menggunakan fungsi filter
    print(a,end = ' ')
    
print()

a = [1,2,3,4,5,6,7]

a_kuadrat = list(map(lambda x: x **2, a))
print(a_kuadrat)

from functools import reduce
# Returns the sum of two elements
def sumTwo(a,b):
    return a+b

result = reduce(sumTwo, [1, 2, 3, 4, 10, 12])
print(result)


a = [1,2,3,4]
n = reduce(lambda x,y : x + y, a)
print(n)
