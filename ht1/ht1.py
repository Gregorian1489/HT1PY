# Найдите сумму цифр трехзначного числа.

x = int(input('Введите трехзначное число: '))
if x>999 or x<100:
    print('Нужно трехзначное число!!!')
else:    
    a = x % 10
    b = (x // 10) % 10
    c = x // 100
    print('Сумма чисел = ', a + b + c)