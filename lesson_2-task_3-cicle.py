print ()
print ('Создадим список из десяти целых чисел и выведем его на экран!\n')

a = []
b = 1
while b < 11:
    a.append(b)
    b = b + 1 
print (a)

print ()
print ('Теперь увеличим каждое число в списке на 1\n')

for i in a:
    a = i + 1
    print(a)
