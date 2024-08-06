immutable_var = (5, 4, False, 6.1, 'saddle')
print('Immutable tuple:',immutable_var)
#immutable_var [0] = 10
#print('Immutable tuple:',immutable_var)
# При попытке изменения элементов программа выдает TypeError: 'tuple' object does not support item assignment
# Так как программа не поддерживает обращение непосредственно к элементам кортежа, кортеж неизменен)
mutable_list = [5, 4, False, 6.1, 'saddle']
mutable_list[4] = ('horse')
mutable_list.append('hat')
print('Mutable list:', mutable_list)