# Tuple practice
# 1. Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
# 2. Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
# 3. Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
# 4. Создайте кортеж из одного элемента, чтобы при итерировании по этому элементы последовательно выводились значения 1, 2, 3. 
# Убедитесь что len() исходного кортежа возвращает 1.

lst1 =  ['a', 'b', 'c'] 
tpl1 = tuple(lst1)
print('1. ', tpl1)
tpl2 = ('a', 'b', 'c')
lst2 = list(tpl2)
print('2. ', lst2)
a, b, c = 'a', 2, 'python'
print('3. ', a, b, c)
tpl = ('1, 2, 3', )
for element in tpl:
    print('4. ', element)
print('4. ', len(tpl))