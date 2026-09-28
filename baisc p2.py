 #split
a='i love python'
print(a.split())
b='i-love-python'
print(b.split())
c='i-love-python-and-cpp'
print(c.split('-'))
d='i-love-python-and-cpp'
print(d.split('-',2))
print('\n')
#rsplit
e='i-love-cpp-and-python'
print(e.rsplit('-',2))
#lsplit
f='i-love-cpp-and-python'
print(f.split('-',2))
print('\n')
#center
g='sama'
print(g.center(9))
print(g.center(9,'='))
print('\n')
#count
h='i love python and cpp but python easier'
print(h.count('python'))
i='i love python and i love cpp'
print(i.count('love',0,24))
#swapcase
print('\n')
j='i love python'
k='I LOVE PYTHON'
print(j.swapcase())
print(k.swapcase())
print('\n')
#startswith
l='i love python'
print(l.startswith('i'))
print(l.startswith('g'))
print(l.startswith('l',2))
print('\n')
#endswith
m='i love python'
print(m.endswith('n'))
print(m.endswith('e',0,6))