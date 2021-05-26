import math

print('he', 'mike', sep=',', end='\n')
print('he', 'mike', sep=',', end='\n')



result = math.sqrt(25)
print(result)

y = math.log2(10)
print(y)

print('hello')
print("hello")
print("I don't know")
print('I don\'t know')
print('hello. \nHello are you?')
print(r'c:\name\name')

print("###################")
print("""\
line
line
line\
""")
print("#######################")

print('hi.' * 3 + 'mike.')
print('py' + 'thon.')
print('py' 'thon')
py = 'py'

print(py + 'thon')

s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')

print(s)

word = 'python'
print(word[2])
print(word[-1])
print(word[0:2])
print(word[2:5])
print('##########################')
print(word[0:2])
print(word[:2])
print('##########################')
print(word[2:])
print('##########################')
word = 'j' + word[1:]
print(word)
print(word[:])
print(len(word))

s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')
print((is_start))
is_start = s.startswith('x')
print((is_start))

print('##########################')

print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))

r = [1, 2, 3, 4, 5, 6, 7, 3 ,3, 3]
print(r.index(5))
print(r.count(3))

if 10 in r:
     print('true')
else:
     print('false')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)

x = ' '.join(to_split)
print(x)

i = [1,2,3,4,5]
j = i
j[0] = 100
print('j =', j)
print('i =', i)

x = [1, 2, 3, 4, 5]
# y = x.copy()
y = x[:]
y[0] = 100
print('y =', y)
print('x =', x)

a = 100
b = 200
print(a, b )
a, b = b, a
print(a, b)

a = dict(a=10, b=20)
type(b)
print(b)

"""
afsajfklasjfksagjahb
fasjfklajs;fja;kjf
jksjflasjf;ajka;

"""