list_ = [1, 2,3,4,5]
list2 = list(list_)
x = list_[3]
y = list2[3]

print(x is y)

d = {'a': 0, 'b':1, 'c':0}

if d['a'] > 0:
    print ('ok')
elif d['b'] > 0:
     print('ok')
elif d['c'] > 0:
     print('ok')
elif d['d'] > 0:
     print('ok')
else:
    print("not ok")

file = open("freq.txt")
result = file.readline()
print(type(result))

d = {"name": "Joseph Kovba", "role": "instructor", "years": 4}
list_ = ["name", "role"]

for s in list_:
    if s in d.keys():
        print(d[s])

string = "Hello, world!"

print(string[-6:-(len(string[2:10])-4)])