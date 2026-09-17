#by sama aljwhari
#ادوات مع list
# تبديل عنصر بعنصر آخر
fruits=['apple','banana','orange']
print('befor',fruits)
fruits[0]='kiwi'                                       #تبديلapple 
print('after',fruits)

#زيادة عنصر في آخر القائمة (append.)
fruits=['apple','banana','orange']
print('befor',fruits)
fruits.append('kiwi')
print('after',fruits)

#اضافة عنصر في اي مكان داخل القائمة (insert.)
fruits=['apple','banana','orange']
print('befor',fruits)
fruits.insert(0,'kiwi')                               #اضافة kiwi قبل apple
print('after',fruits)

#حذف عنصر من القائمة(remove.)
fruits=['apple','banana','orange']
print('befor',fruits)
fruits.remove('banana')
print('after',fruits)

#حذف عنصر بكتابة رقمه(del[ ])
fruits=['apple','banana','orange']
print('befor',fruits)
del fruits [2]
print('after',fruits)

#حذف آخر عنصر في القائمة(pop().) اذا تُركت فارغة
fruits=['apple','banana','orange']
print('befor',fruits)
fruits.pop()
print('after',fruits)

#حذف اي عنصر عند كتابة رقمه داخلها ()pop.
fruits=['apple','banana','orange']
print('befor',fruits)
fruits.pop(1)
print('after',fruits)