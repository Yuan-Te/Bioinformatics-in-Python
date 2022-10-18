z = '10'
print(type(z))
a = int(z)
print(type(a))
a = float(z)
print(type(a))
a = complex(z)
print(type(a))

b = True
print(type(b))
c = int(b)
print(type(c))
print(c)

b = False
print(type(b))
c = int(b)
print(type(c))
print(c)

list = [1,2,3,4,5,6,7,8,9,10]
print(list[-1])
list[0] = 'fuck'
print(list)
print(list[-2:])
print(list[0:-1:2])
list.append('ur mother')
print(list)

tuple = ('jon', 'va', 'jon')
#turple.append(fuck) -> turple不能change, add, remove item
print(tuple)

set1 = {'cherry', 'mango', 'banana'}
set2 =  {'cherry', 'mango', 'guala'}
union = set1.union(set2) #聯集
inter = set1.intersection(set2) #交集
print(union, '\n', inter)


# Control Flow
x=300
y=33
if x<y:
    print('x is less than y')
elif x==y:
    print('x is equal to y')
else:
    print('x is greater than y')


#Loops
list = ['apple','cereal','beer','milk']
for x in list:
    if x=='beer'or x=='milk':
        print('we want to buy drink')
    else:
        print('we need to buy food')

i=1
while i<=6:
    print(i)
    i+=1


#Reading file
file='lorem_ipsum.txt'
with open(file) as f:
    content = f.read()

print(f.closed)
print(content)
