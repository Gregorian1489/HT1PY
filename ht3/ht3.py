#  Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд 
# и получали билет с номером. Счастливым билетом называют такой билет с шестизначным 
# номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет
#  счастливость билета.

x = input('Введите шестизначное число: ')
k = int(x)
if k>999999 or k<100000:
    print('Нужно шестизначное число!')
else:    
    i = 0
    a = [0,0,0,0,0,0]
    while i<6:
        a[i] = int(x[i])
        i+=1
    m = a[0] + a[1] + a[2]
    n = a[3] + a[4] + a[5] 
    if m == n:
        print('Билет счастливый')
    else:    
        print('Билет не счастливый')


