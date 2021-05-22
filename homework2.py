s = input('Enter String: ')
k = {i:s.count(i) for i in s}
count = 0
n = []
# key = []
for i in k:
    n.append(k[i]) 

if all(n) == any(k):
    print('My string!!')


print(k)
print(n)
