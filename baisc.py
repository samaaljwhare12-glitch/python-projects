 #len تعد عدد الاحرف داخل متغير 
s= 'i love python'
print(len(s))
#len تتعامل مع المسافة كحرف 
d='     i    love   python    '
print(len(d))
#rstrip تحذف المسافات من جهة اليمين
#lstrip تحذف المسافات من جهة اليسار
#strip حذف المسافات من جهة اليمين واليسار
c='      i love python      '
print(c.strip())
print(c.rstrip())
print(c.lstrip())
print('\n')
#جعل اول حرف من كل كلمة كابتل title
j=' i love python so much '
print ( j.title())
#جعل اول حرف من اول كلمة كابتل capitalize
n='i love python so much'
print(n.capitalize())
print('\n')
#zfill وضع اصفار قبل الارقام
k = 1
x = 10
d = 100
z = 1000
print(str(k) .zfill(4))
print(str(x) .zfill(4))
print(str(d) .zfill(4))
print(str(z) .zfill(4))
#upper كل احرف الكلمة كابتل
g='sama'
print(g.upper())
#lower كل احرف الكلمة سمول
o='SAMA'
print(o.lower())