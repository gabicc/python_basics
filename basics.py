x = 3.2
print(x)

llist = []

for i in range(0, 10):
    llist.append(x)

# for i in llist:
#     print(i)

print(llist)

d = {'a': 51, 'b': 27, 'c': 56, 'a': 34}
d['h'] = 78
d['c'] = 22

e = {'f': 45, 'g': 89, 'c': 123}

e.update(d)

# print(e)

for k in e:
    print(k, ' -> ', e[k])

def suma(a, b):
    return a + b

# r = int(input())
# k = float(input())

my_list = [1, 2, 3, 4, 5]

# import functii
from functii import afis_list
def suma_total(a):
    s = 0
    for i in a:
        s += i
    return s

print(suma_total(my_list))

afis_list(my_list)

#print(suma(r, k))