#find
a='i love python '
print(a.find('p'))
b='i love java'
print(b.find('j',0,8))
c='i love cpp'
print(c.find('c',0,3))#-1 
print('\n')
#rjust
d='sama'
print(d.rjust(10))
print(d.rjust(10,'d'))
print(d.rjust(10,'*'))
#ljust
print(d.ljust(10))
print(d.ljust(10,'e'))
print(d.ljust(10,'#'))
print('\n')
#splitlines
e='''one
two
three'''
print(e.splitlines())
f='one\ntwo\nthree'
print(f.splitlines())
print('\n')
#expandtabs
g='i\tlove\tpython'
print(g.expandtabs())
print(g.expandtabs(2))
print('\n')
#istitle
one ='I Love Python'
print(one.istitle())
two= 'I Love Cpp'
print(two.istitle())
print('\n')
#isspace
three='      '
print(three.isspace())
four=''
print(four.isspace())
print('\n')
#islower
five='i love python'
print(five.islower())
six='I Love Python'
print(six.islower())
print('\n')
#isidentifier
seven='sama_py'
eight='samapy'
nine='sama--py'
print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())
print('\n')
#isalpha
i='A'
print(i.isalpha())
j='A1'
print(j.isalpha())
print('\n')
#isalnum
k='A'
print(k.isalnum())
l='A1'
print(l.isalnum())
m='11*11a1'
print(m.isalnum())
